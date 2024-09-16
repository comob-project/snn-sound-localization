(basic-model)=
## A minimal trainable model of IPD processing

```{list-table}
* - Section authors
  <!-- - Dan Goodman -->
* - Notebooks
  - [](../research/time-constant-solutions.ipynb)
```

This section describes the initial model developed for the [Cosyne tutorial that served as the starting point for this project](https://neural-reckoning.github.io/cosyne-tutorial-2022/) {cite:p}`10.5281/zenodo.7044500`. It also describes some small variants of this basic model produced in the course of the project, which can be seen in the notebook [](../research/time-constant-solutions.ipynb).

The aim of the model was to address a long standing question about how and why the brain localises sounds in the way it does, restricted specifically in this case to interaural phase differences (IPDs) cues used at low frequencies. A common strand in this research is to consider a population of binaurally responsive neurons, each with a different frequency and IPD tuning, summarised by their best frequency (BF) and best delay (BD), i.e. the frequency and delay/phase at which they give their strongest response. From this spatial-temporal *encoding* of the sound, a second network attempts to *decode* the sound location. In the place theory of {cite:t}`Jeffress1948`, the encoding is done by coincidence detection neurons arrayed so that each neuron receives a sound from the left and right ear with different conduction delays. Decoding proceeds as follows. When the conduction delays match the acoustic delays induced by the arrival time difference of the sound at the two ears, the neuron fires at a maximal rate because of the coincidence detection. Doubt was cast on this theory by {cite:t}`10.1038/86049`, who argued that it was not robust to neural noise, and proposed instead a "hemispheric code" that encodes the sound in the difference in the average firing rates of neurons whose best delay is positive versus negative. While this optimises robustness to neural noise, {cite:t}`goodman_decoding_2013` showed that it was not efficient at integrating across frequencies, was biased in the presence of acoustic noise, and generalised poorly to sounds outside of the training set.

In this project, we asked what strategies would be found when jointly optimising for both encoding and decoding using modern machine learning methods to train a network end-to-end.

(basic-methods)=
### Methods

The model consists of the following pathway, illustrated in {ref}`basic-arch`: IPD $\rightarrow$ stimulus $\rightarrow$ input neurons $\rightarrow$ hidden layer neurons $\rightarrow$ readout neurons.

```{figure} ./sections/_figures/model-diagram.png
:label: basic-arch
:width: 100%

Overall model architecture. Sinusoidal audio signals are passed through two populations of units, with a range of preassigned delays, representing the left and right ears. These units generate Poisson spike trains which pass forward to a layer of leaky-integrate and fire (LIF) units, then a layer of leaky-integrator output units from which we readout the networks estimate of the interaural phase difference (IPD). 
```

The IPD is an angle uniformly randomly selected in $\alpha\in[-\pi/2,\pi/2]$ (frontal plane only).

The stimulus is a sine wave, and we model interaural phase differences (IPDs) by adding the IPD $\alpha$ as a phase delay to the right ear. Enumerating the ears with index $i\in\{0,1\}$ so that $i=0$ is the left ear, we get that the stimulus in ear $i$ is:

$$S_i(t)=\sin(2\pi f t+i\alpha)$$

To model a population of spiking neurons with different lags, we associate each input layer neuron with an ear and an additional phase delay $\psi$ uniformly spaced in the range $(0, \pi/2)$. This ensures that by comparing a left and right ear you can generate any phase difference in the range $(-\pi/2,\pi/2)$ as required. Specifically, we set neuron $j$ connected to ear $i$ to receive the stimulus:

$$S_{ij}(t)=\sin(\theta_{ij})$$

where

$$\theta_{ij}(t)=2\pi f t+i\alpha+\psi_j$$

$$\psi_j = j\pi/2(N_\psi-1)$$

and $N_\psi$ is the number of input neurons per ear.

Next, we make these neurons spiking by giving them a time varying firing rate:

$$R_{ij}(t)=R_\mathrm{max}((1+\sin\theta_{ij}(t))/2)^2$$

where $R_\mathrm{max}$ is the maximum firing rate. Spikes are then generated via an inhomogeneous Poisson process with intensity $R_{ij}(t)$. Some example raster plots are shown in {ref}`example-stimuli`.

```{figure} sections/basicmodel/stimuli-examples.png
:label: example-stimuli
:width: 100%

Examples of generated input spike trains.
```

The $2N_\psi$ input neurons are connected all-to-all to a "hidden layer" of $N_h$ spiking neurons. These are standard leaky integrate-and-fire neurons with a membrane potential $v$ that in the absence of spikes evolves over time according to the differential equation:

$$\tau \frac{\mathrm{d}v}{\mathrm{d}t}=-v$$

where $\tau$ is the membrane time constant. An incoming spike on a synapse with weight $w$ causes an instantaneous increase $v\leftarrow v+w$. These weights are stored in a matrix $W_{ih}$ of size $(2N_\psi,N_h)$. If $v$ crosses the spike threshold of 1, the neuron emits a spike and instantaneously resets to $v\leftarrow 0$.

The hidden layer is all-to-all connected to a readout layer of $N_c$ neurons via a weight matrix $W_{ho}$. The aim is to divide the set of possible IPDs into $N_c$ intervals $I_k=[-\pi/2+k\pi/N_c,-\pi/2+(k+1)\pi/N_c]$ and then, if neuron $k$ is the most active, guess that the IPD must be in interval $I_k$. These hidden layer neurons follow the same differential equation but do not spike. Instead, to guess the IPD we compute their mean membrane potential over the duration of the stimulus, $\bar v_k$, and then compute an output vector that is the log softmax function of these mean membrane potentials:

$$x_k = \log \frac{\exp\bar v_k}{\sum_\ell \exp \bar v_\ell}$$

We then interpret $x_k$ as the estimated probability that $\alpha\in I_k$. Our estimate of the IPD $\hat\alpha$ will be the midpoint of the interval corresponding to the most active neuron $\hat k=\argmax_k x_k$. Note that the softmax function and probability interpretation are important for training the network, but once the network is trained you can equally well compute $\hat k=\argmax_k \bar v_k$.

The network is trained by defining a loss function that increases the further away the network behaviour is from what we would like (defined in detail below), and then using the surrogate gradient descent method [@Zenke2018;@10.1109/MSP.2019.2931595]. Full details on training parameters can be found in the notebook [](../research/3-Starting-Notebook.ipynb).

The loss function we use is composed of two terms. The first is the cross entropy or negative log likelihood loss that measures how far our predicted probability distribution $x_k$ is from the true probability distribution (which has value 1 for the correct $k$ and 0 for all other $k$). The second term, which is not used in all the notebooks in this project, is an optional regularisation term. In [](../research/time-constant-solutions.ipynb) we regularise based on the firing rates of the hidden layer neurons. We compute the firing rate for each hidden neuron $r_m$. If this is below a mimimum threshold $r_-$ it contributes nothing to the loss, otherwise we compute $L_m=((r_m-r_-)/(r_+-r_-))^2$ for each neuron for a constant $r_+$ explained below. We now compute the average and multiply a constant $L=c\sum_m L_m/N_h$. The constant $r_+$ is the maximum firing rate we would like to see in the network, so that $L_m=1$ if $r_m=r_+$. The constant $c$ is chosen to be the expected initial cross-entropy loss of the network before training. This makes sure that a firing rate of $r_m=r_+$ is heavily penalised relative to the cross-entropy loss, but that any firing rate below $r_-$ is fine. We chose $r_-=100$ sp/s and $r_+=200$ sp/s.

### Results

This approach is able to train a network that can perform the task well, using very few neurons ($N_\psi=100$ input neurons per ear, $N_h=8$ hidden neurons and $N_c=12$ output neurons). Mean absolute error in IPD is $\sim 2.6$ deg ({ref}`confusion-matrix`). Hidden neuron firing rates are between 110 and 150 sp/s ({ref}`hidden-firing-rates`).

```{figure} sections/basicmodel/confusion.png
:label: confusion-matrix
:width: 60%
Confusion matrix. Results of training the network with $f=50$ Hz, $\tau=2$ ms, $N_\psi=100$, $N_h=8$, $N_c=12$. Mean absolute IPD errors are $\sim 2.6$ deg.
```

```{figure} sections/basicmodel/hidden-firing-rates.png
:label: hidden-firing-rates
:width: 60%
Hidden neuron firing rates. Results of training the network with $f=50$ Hz, $\tau=2$ ms, $N_\psi=100$, $N_h=8$, $N_c=12$. Mean absolute IPD errors are $\sim 2.6$ deg.
```

Analysis of the trained networks show that it uses an unexpected strategy. Firstly, the hidden layer neurons might have been expected to behave like the encoded neurons in Jeffress' place theory, and like recordings of neurons in the auditory system, with a low baseline response and an increase for a preferred phase difference (best phase). However, very reliably they find an inverse strategy of having a high baseline response with a reduced response at a least preferred phase difference ({ref}`tuning-curves-hidden`). Note that the hidden layer neurons have been reordered in order of their least preferred delay to highlight this structure. These shapes are consistently learned, but the ordering is random. By contrast, the output neurons have the expected shape ({ref}`tuning-curves-output`). Interestingly, the tuning curves are much flatter at the extremes close to an IPD of $\pm \pi/2$. We can get further insight into the strategy found by plotting the weight matrices $W_{ih}$ from input to hidden layer, and $W_{ho}$ from hidden layer to output, as well as the product $W_{io}=W_{ih}\cdot W_{ho}$ which would give the input-output matrix for a linearised version of the network ({ref}`basic-weights`).

```{figure} sections/basicmodel/tuning-hidden.png
:label: tuning-curves-hidden 
:width: 100%
Tuning curves of hidden neurons. Strategy found by trained network with $f=50$ Hz, $\tau=2$ ms, $N_\psi=100$, $N_h=8$, $N_c=12$.
```

```{figure} sections/basicmodel/tuning-output.png
:label: tuning-curves-output
:width: 100%
Tuning curves of hidden neurons. The dashed red lines indicate the estimated IPD if that neuron is the most active.Strategy found by trained network with $f=50$ Hz, $\tau=2$ ms, $N_\psi=100$, $N_h=8$, $N_c=12$.
```

```{figure} sections/basicmodel/weights.png
:label: basic-weights
:width: 100%
Weight matrices, with hidden neurons reordered by best delay. Strategy found by trained network with $f=50$ Hz, $\tau=2$ ms, $N_\psi=100$, $N_h=8$, $N_c=12$.
```

A number of features emerge from this analysis. The first is that the tuning curves of the hidden neurons have a very regular structure of having a high baseline firing rate with a dip around a "least preferred" delay that varies uniformly in the range $-\pi/2$ to $\pi/2$. Indeed, the tuning curves $i$ can be very well fit with the function $a+be^{-(\alpha-\alpha_i)^2/2\sigma_\alpha^2}$ where $\alpha$ is the IPD, $\alpha_i=-\pi/2+i\pi/N_h$ is the "least preferred" IPD, and $a, b, \sigma_\alpha$ are parameters to fit ({ref}`tuning-curves-hidden`, orange lines). This would look likely to be consistent with some form of optimal coding theory that minimises the effect of the Poisson noise in the spike counts, although we did not pursue this explanation.

The second feature is that spike timing does not appear to play a significant role in this network. This may initially appear suprising but in fact it is inevitable because of the coding scheme we have used where the initial layer of neurons fire Poisson spikes, and there is only one spiking layer, meaning there is no scope for spike times to be used (a limitation of this model realised late in the process). Indeed, if we predict the output of the network purely using the firing rates of the input stimulus passed through the weight matrices $W_{ih}$ and $W_{ho}$ plus a static nonlinearity for the input to hidden layer, we get an excellent approximation for the hidden neurons ({ref}`tuning-curves-hidden`, blue lines) and a qualitatively good fit for the output neurons ({ref}`tuning-curves-output`, blue lines). Specifically, if $r_i(t)$ is the instantaneous time-varying firing rate of input neuron $i$ we approximate the instantaneous hidden units firing rates by the function:

$$r_h(t)=\begin{cases}
0 & \mbox{if } r_i(t)\leq 1 \\
\frac{1}{t_\mathrm{refrac}+\tau\log\frac{r_i(t)}{r_i(t)-1}} & \mbox{if } r_i(t)>1 \\
\end{cases}$$

This function is the firing rate of a leaky integrate-and-fire neuron $\tau v^\prime=r_i(t)-v$ with a refractory period $t_\mathrm{refrac}$ (which is $\mathrm{d}t$ in our case because of the way it is simulated) if the function $r_i(t)$ were constant over time, but it fits well even with a time-varying $r_i(t)$. From this we can take an average over time to get the mean firing rate. The output units do not spike so their activity is simply approximated by $r_o(t)=\sum_h W_{ho}r_h(t)$.

Finally, we note that the weight matrix $W_{ho}$ visible in {ref}`basic-weights` seems to have a very regular structure of weights that have a broad excitation and a narrowly tuned inhibition (an unusual pattern). Indeed, we can fit this well with a Ricker wavelet (or "Mexican hat") function:

$$W_ho\approx a(1-(\delta/\sigma_\delta)^2) e^{-\delta^2/2\sigma_\delta^2}+b$$

where $\delta=o-N_c h / N_h$, $h$ and $o$ are the indices of the hidden and output neurons, $N_h$ is the number of hidden neurons, $N_c$ the number of output neurons, and $a$, $b$ and $\sigma_\delta$ are parameters to estimate. Using this approximation and the rate-based approximation from before, we get the orange curves in {ref}`tuning-curves-output`. If we use both the Ricker wavelet approximation of $W_{ho}$ and the idealised tuning curves, we get the green curves. All in all, this gives us a 6 parameter model that fits the data extremely well, a significant reduction on the 896 parameters for the full model ($N_\psi N_h+N_h N_c$).

(basic-discussion)=
### Discussion

This subproject was an extension of the original notebook [](../research/3-Starting-Notebook.ipynb) with the aim of understanding the solutions found in more detail. We successfully found a 6-parameter reduced model that behaves extremely similarly to the full model, and we can therefore say that we have largely understood the nature of this solution. We did not look in detail for a deep mathematical reason why this is the solution that is found, and this would make for an interesting follow-up. Are these tuning curves and weights Bayes optimal to reduce the effect of the Poisson spiking noise, for example?

The solution that was found gives tuning curves that are unlike those found in natural auditory systems, with an inverted "least preferred phase" structure instead of the typical "preferred phase". In addition, the weight matrix from the hidden to output layer has broadly tuned excitation and narrowly tuned inhibition, which is an unusual pattern.

The solution found does not appear to use coincidence detection properties of spiking neurons, and indeed can be well approximated by a purely rate-based approximation. It appears to find a solution similar to that suggested by the equalisation-cancellation theory {cite:p}`durlach_equalization_1963;culling_equalization_cancellation_2020`. This seems initially surprising, but in fact because of the nature of the input stimulus (Poisson spike trains) and the fact that there is only one spiking layer of neurons, there is no temporal structure for coincidence detection to make use of, so it was inevitable that it would not find a solution that uses this strategy. An interesting follow-up would be to use a more detailed model of neuronal firing in the cochlear nucleus for example, or a multi-layer structure, and see if different solutions are found.