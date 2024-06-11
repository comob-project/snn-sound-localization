(basic-model)=
## A minimal trainable model of IPD processing

This section describes the initial model developed for the [Cosyne tutorial that served as the starting point for this project](https://neural-reckoning.github.io/cosyne-tutorial-2022/) {cite:p}`10.5281/zenodo.7044500`. It also describes some small variants of this basic model produced in the course of the project.

The aim of the model was to address a long standing question about how and why the brain localises sounds in the way it does, restricted specifically in this case to interaural phase differences (IPDs) cues used at low frequencies. A common strand in this research is to consider a population of binaurally responsive neurons, each with a different frequency and IPD tuning, summarised by their best frequency (BF) and best delay (BD), i.e. the frequency and delay/phase at which they give their strongest response. From this spatial-temporal *encoding* of the sound, a second network attempts to *decode* the sound location. In the place theory of {cite:t}`10.1037/h0061495`, the encoding is done by coincidence detection neurons arrayed so that each neuron receives a sound from the left and right ear with different conduction delays. Decoding proceeds as follows. When the conduction delays match the acoustic delays induced by the arrival time difference of the sound at the two ears, the neuron fires at a maximal rate because of the coincidence detection. Doubt was cast on this theory by {cite:t}`10.1038/86049`, who argued that it was not robust to neural noise, and proposed instead a "hemispheric code" that encodes the sound in the difference in the average firing rates of neurons whose best delay is positive versus negative. While this optimises robustness to neural noise, {cite:t}`10.7554/eLife.01312` showed that it was not efficient at integrating across frequencies, was biased in the presence of acoustic noise, and generalised poorly to sounds outside of the training set.

In this project, we asked what strategies would be found when jointly optimising for both encoding and decoding using modern machine learning methods to train a network end-to-end.

### Methods

The model consists of the following pathway, illustrated in {ref}`basic-arch`: IPD $\rightarrow$ stimulus $\rightarrow$ input neurons $\rightarrow$ hidden layer neurons $\rightarrow$ readout neurons.

```{figure} ../research/diagrams/arch-stimuli.png
:label: basic-arch

Overall model architecture.
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

This approach is able to train a network that can perform the task well ({ref}`basic-results`), using very few neurons ($N_\psi=100$ input neurons per ear, $N_h=8$ hidden neurons and $N_c=12$ output neurons). Mean absolute error in IPD is $\sim 2.6$ deg ({ref}`confusion-matrix`). Hidden neuron firing rates are between 110 and 150 sp/s ({ref}`hidden-firing-rates`).

```{figure}
:label: basic-results

(confusion-matrix)=
![Confusion matrix.](sections/basicmodel/confusion.png)

(hidden-firing-rates)=
![Hidden neuron firing rates.](sections/basicmodel/hidden-firing-rates.png)

Results of training the network with $f=50$ Hz, $\tau=2$ ms, $N_\psi=100$, $N_h=8$, $N_c=12$. Mean absolute IPD errors are $\sim 2.6$ deg.
```

Analysis of the trained networks show that it uses an unexpected strategy ({ref}`basic-strategy`). Firstly, the hidden layer neurons might have been expected to behave like the encoded neurons in Jeffress' place theory, and like recordings of neurons in the auditory system, with a low baseline response and an increase for a preferred phase difference (best phase). However, very reliably they find an inverse strategy of having a high baseline response with a reduced response at a least preferred phase difference ({ref}`tuning-curves-hidden`). Note that the hidden layer neurons have been reordered in order of their least preferred delay to highlight this structure. These shapes are consistently learned, but the ordering is random. By contrast, the output neurons have the expected shape ({ref}`tuning-curves-output`). Interestingly, the tuning curves are much flatter at the extremes close to an IPD of $\pm \pi/2$. We can get further insight into the strategy found by plotting the weight matrices $W_{ih}$ from input to hidden layer, and $W_{ho}$ from hidden layer to output, as well as the product $W_{io}=W_{ih}\cdot W_{ho}$ which would give the input-output matrix for a linearised version of the network ({ref}`basic-weights`).

```{figure}
:label: basic-strategy

(tuning-curves-hidden)=
![Tuning curves of hidden neurons.](sections/basicmodel/tuning-hidden.png)

(tuning-curves-output)=
![Tuning curves of hidden neurons. The dashed red lines indicate the estimated IPD if that neuron is the most active.](sections/basicmodel/tuning-output.png)

(basic-weights)=
![Weight matrices, with hidden neurons reordered by best delay.](sections/basicmodel/weights.png)

Strategy found by trained network with $f=50$ Hz, $\tau=2$ ms, $N_\psi=100$, $N_h=8$, $N_c=12$.
```

TODO: EXPLAIN THE STRATEGY.

* Hidden unit tuning curves are behaving as rate-based neurons (rate approx)
* Hidden unit tuning curves follow an idealised reversed Gaussian shape (idealised)
* $W_{ho}$ has a very clear Ricker / mexican hat structure. If we fit this, we get a good approximation of the output firing rates.
* Overall, the network appears to have learned a strategy of finding tuning curves that minimise the effect of Poisson noise, using the overcomplete basis set of input spike trains to achieve the right hidden neuron firing rates. There is no strong evidence of spike-based processing.

TODO: DEPENDENCE ON TAU.

TODO: DEPENDENCE ON F?

TODO: DEPENDENCE ON $N_h$?

### Discussion

* Hidden neurons are unlike real MSO neurons, but these tuning curves are very reliable. Excitation-only notebook gives hints that it could work, but why would we do it that way evolutionarily speaking if it's less efficient?
* Small time constants better, but not for coincidence detection!
* Learned strategy might be something like equalisation-cancellation theory.
* Hard to draw a strong conclusion about biology given hidden neurons are unlike MSO, but raises interesting questions as to why.