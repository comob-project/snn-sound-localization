(delay-section)=
## Learning delays

```{list-table}
* - Section authors
  - Karim G. Habashy, Balázs Mészáros
* - Notebooks
  - [](../research/Learning_delays.ipynb), [](../research/Learning_delays_major_edit2.ipynb), [](../research/Solving_problem_with_delay_learning.ipynb), [](../research/Quick_Start_Delay_DCLS.ipynb)
```

We introduce a simple method to solve the sound localization problem with only learnable delays, and discuss a method that learns both weights and delays, introduced in {cite:p}`hammouamri2024learning`.

### Introduction

Following the classic work by {cite:t}`Jeffress1948` on axonal delays, {cite:t}`KLWH2001` investigated the question of how ITD computation maps can arise ontogenetically in the laminar nucleus of the barn owl. They showed that interaural time differences (ITD) computational maps emerge from the combined effect of a Hebbian spike-based learning rule and its transmission along the presynaptic axon. In other words, axonal delays shape network structure when coupled with temporal learning rules. Based on this insight, several studies investigated the combined effect of spike timing-dependent plasticity (STDP), axonal conduction delays and oscillatory activity on recurrent connections in spiking networks. {cite:t}`KBTG2013` demonstrated the selective potentiation of recurrent connections in this scenario, while {cite:t}`HKTI2016` showed that neural selection for memory formation depends on neural competition and, in turn, for neural competition to emerge in recurrent networks, spontaneously induced neural oscillation coupled with STDP and axonal delays are a prerequisite. 

We can use this to develop an intuition behind coupling neuronal delays with STDP. The sign of the STDP rule depends on the order of post- and pre-synaptic spiking, and axonal delays can effectively reverse this. For example, the arrival of presynaptic spikes at the synapse before the backpropagated action potential leads to a synaptic depression. However, reducing the axonal transmission speed would lead to potentiation. In this line of thought, {cite:t}`MAVT2017` studied the combined role of delays and STDP on the emergent synaptic structure in neural networks. It was shown that, qualitatively different connectivity patterns arise due to the interplay between axonal and dendritic delays, as the synapse and cell body can have different temporal spike order. 

Aside from their role in modeling cortical functions or shaping a network's synaptic structure, another line of research emerged from the seminal work by {cite:t}`EMI2006`. They showed that when including conduction delays and STDP into their simulation of realistic neural models, polychronous groups of neurons emerge (although {cite:t}`pauli_reproducing_2018` suggests that some of these results may be implementation-specific artifacts). These groups show time-locked spiking patterns with millisecond precision. Subsequent studies investigated the properties and functions of such neuronal groups. For example, {cite:t}`BSEI2010` demonstrated the natural emergence of large memory content and working memory when the neuronal model exploits temporal codes. Specifically, short term plasticity can briefly strengthen the synapses of specific polychronous neuronal groups (PNG) resulting in an enhancement of their spontaneous reactivation rates.  In a qualitatively different study, {cite:t}`EIAS2018` showed that networks that exhibit PNG possess potential capabilities that might solve the dynamic binding problem. These networks respond with stable spatio-temporal spike trains when presented with input images in the form of randomized Poisson spike trains. The functionality of these kind of networks emerged due to the interplay of various factors including: i) random distribution of axonal delays ,ii) STDP and iii) lateral, bottom-up and top-down synaptic connections. 

Finally, it should be noted that most of the studies that incorporate axonal and/or dendritic delays, include them as a non-learnable parameter. Few studies investigated the possibility of training transmission delays in order to enhance the computational capabilities of spiking neural networks (SNN). {cite:t}`TM2017` proposed an algorithm that modifies the axonal delays and synaptic efficacy in both supervised and unsupervised approaches.  The learning method involved approximates the Expectation-Maximization (EM) algorithm and, after training, the network learns to map spatio-temporal input-output spike patterns. Thus, EM is one way to train SNNs that are cast as probabilistic models. Another approach that exploits recent developments in deep learning is {cite:t}`hammouamri2024learning`. In this work, delays are represented as 1D convolutions through time, where the kernels include a single per-synapse non-zero weight. The temporal position of these non-zero weights corresponds to the desired delays. The proposed method co-trains weights and delays and is based on the Dilated Convolution with Learnable Spacings (DCLS) algorithm {cite:p}`ITT2023`.

In this work, we propose a delay learning algorithm that is simple and efficient. The delay learning is mediated by a differentiable delay layer (DDL). This layer can be inserted between any two layers in an SNN in order to learn the appropriate delay to solve a machine learning task. This DDL is architecture agnostic. Also, the method is designed to learn delays separately from synaptic weights. 

### Methods

The DDL is, mainly, based on a 1D version of the spatial transformer (STN) network {cite:p}`JSZK2015`. The STN is a differentiable module that can be added into convolutional neural networks (CNNs) architectures to empower them with the ability to spatially transform feature maps in a differentiable way. This addition leads to CNN models that are invariant to various spatial transformations like translation, scaling and rotation. Image manipulations are inherently  not differentiable, because pixels are discrete. However, this problem is overcome by the application of an interpolation  (for example bi-linear) after the spatial transformation. 

The DDL is a 1D version of the spatial transformer where the only transformation used is translation. Translation of a spike along the time dimension can be thought of as a translation of a pixel along the spatial coordinates. The general affine transformation matrix for the 2D case takes the form in the following equation:
	
$$ \begin{bmatrix} 
	sr_1 & sr_2 & t_x\\
	sr_3 & sr_4 & t_y\\
	0 & 0 & 1
\end{bmatrix} \begin{bmatrix} 
    x_t\\
	y_t\\
	1
\end{bmatrix} = \begin{bmatrix} 
    x_s\\
	y_s\\
	1
\end{bmatrix}
$$ 
		
In the above equation, ${sr_1,~sr_2,~sr_3,~sr_4}$ are the elements responsible for the linear transformations of scaling, rotation and shear. $t_x$ and $t_y$ are the translations in the x-axis and y-axis respectively. $x_t$ and $y_t$ are the location of a spike/pixel (in case of spikes $y = 0$) in the target/output grid, while $x_s$ and $y_s$ are the location of the source grid. A grid can be an image or a 2D array of spike trains. For the case of only translation along the x-axis, the affine transformation matrix becomes: 
	
$$ \begin{bmatrix} 
	1 & 0 & t_x\\
	0 & 1 & 0\\
	0 & 0 & 1
\end{bmatrix}
$$
	
Conventionally, for the spatial transformer, after the projection of the target grid onto the source grid comes the process of interpolation as the transformed pixel might not coincide with a representative one in the source grid/image. Hence, interpolation is performed to estimate the value of the transformed pixel from the surrounding ones. However, applying this process to spike trains can lead to a distortion of the spikes as the allowed values are only 1s and 0s. To avoid this, the translation element ${t_x}$ should be multiples of the minimum delay. Thus, any transformed spike location from the target grid will find a matching spike location in the source grid. Interpolation (for example bi-linear) will pick the coincident source spike with a weighting of one and provide zero weighting for any other nearby spikes.  This process is summarized visually in [](#DDL). The input spike trains to the DDL should be padded by zeros so as to not lose information after translation. 

```{figure} sections/delays/DDL.png
:label: DDL
:width: 100%
Structure of the differentiable delay layer (DDL). The DDL shifts an input spike train by applying translation then interpolation.
```

We will see below that only the DDL is needed to solve the sound localization problem, where the output classes are the target IPD. This network architecture is shown in [](#DelayNetwork), with the DDL inserted between the input and output nodes. In this cases, the weights are set to one and the biases to zero.

```{figure} sections/delays/Network.png
:label:DelayNetwork
:width: 60%
Differentiable delay layer (DDL) model architecture. The DDL is inserted between the input and output nodes. The output nodes are IPD classes spanning the range $[-90^\circ, +85^\circ]$ in $5^\circ$ steps.
```

The DDL shifts the spike trains in a differentiable way, which modifies the output membrane potential via a multiplicative synapse, described below. Also, to facilitate learning, a non-spiking output was utilized (i.e. the output membrane potential is used and the output neuron does not fire spikes, as in [](#basic-methods)).

$$\begin{aligned}
v_i &= -\sum_{t=0}^{T}(u_{1i}(t) - u_{2i}(t))^2 \\
\tau_m\frac{\ud u_{xi}}{\ud t} &= -u_{xi} + S_x(t) \\
S_x(t) &= \sum_{z=1}^{n} \delta(t-t_x^z)
\end{aligned}$$

Here ${v_i}$ is the voltage at output node $i$, $u_{xi}$ is the dendritic potential from input $x\in\{1,2\}$ and output node $i$, $\tau_m$ is the time constant of a dendritic branch, $S_x(t)$ is the spike train of input $x$. The form $(u_{1i}(t) - u_{2i}(t))^2$ looks like a squared error and might, at first glance, seem biologically implausible, but by expanding it as follows we see it is a form of multi-synaptic multiplicative-additive interaction:

$$
(u_{1i}(t) - u_{2i}(t))^2 = u_{1i}(t)^2 -2u_{1i}(t)u_{2i}(t) + u_{2i}(t)^2
$$

In addition to the DDL, we also use the dilated convolutions with learnable spacings {cite:p}`hammouamri2024learning` algorithm, which operates by delaying spike trains through a 1D convolution featuring a single non-zero element, equivalent to the synaptic weight, positioned at the appropriate delay value. This method also uses interpolation to identify the optimal delay, facilitating the learning of delays with weights through backpropagation through time in arbitrarily deep SNNs (see {cite:t}`hammouamri2024learning` for details).

### Results and discussion

For the DDL we discretised IPDs into 36 classes from $-90^\circ$ to $+85^\circ$ in $5^\circ$ increments. To simplify learning, we fix delays from one ear and only allow delays from the other ear to be learned. This can be seen in switch from the vertical bands of blue spikes in [](#DelaySpikeHistograms)A before learning, to the diagonal bands in [](#DelaySpikeHistograms)B after learning.

```{figure} sections/delays/Results_1.png
:label: DelaySpikeHistograms
:width: 100%
Spike histograms for IPDs before (A) and after (B) training. Each panel shows the delayed input spikes for a sample sound at a particular inteaural phase difference (IPD). Note that the first half of the spikes (coloured in red) have fixed delays, while the second half (blue) are learnable. The shift from a fixed delay to a set of delays can be seen in the transition from vertical to diagonal blue bands of spikes after training.
```

Loss curves and the histogram of errors after training are shown in [](#DelayLossDist). Overall errors correspond to a classification accuracy of 11.8% (compared to a chance level of 2.8%), or a mean absolute error of $19.1^\circ$. Confusion matrices are shown in [](#DelayConfuse).

```{figure} sections/delays/loss-and-dist.png
:label: DelayLossDist
:width: 100%
Left: Evolution of training loss of the differential delay layer model as a function of the number of training epochs. Right: Histogram of absolute errors (in degrees) after training.
```

```{figure} sections/delays/Confuse.png
:label: DelayConfuse
:width: 100%
Analysis of classifications by the trained differential delay layer model. Data are shown for errors made on the training data set (A) and test data set (B). Left shows a histogram of the true IPDs (blue) and estimated IPDs (orange). Right shows the confusion matrices on a blue-yellow colour scale (so perfect prediction would correspond to a blue image with a yellow diagonal).
```

Next we show results for the dilated convolutions with learnable spacings (DCLS) algorithm, in this case using 12 IPD classes instead of 36, in [](#DelaySpikeHistograms2). Performance of this algorithm for this task was better, with a mean absolute error on the test dataset of $4.2^\circ$.

```{figure} sections/delays/Confuse_dcls.png
:label: DelaySpikeHistograms2
:width: 100%
Analysis of classifications by the trained dilated convolutions with learnable spacings (DCLS) model. Data are shown for errors made on the training data set (A) and test data set (B). Left shows a histogram of the true IPDs (blue) and estimated IPDs (orange). Right shows the confusion matrices on a blue-yellow colour scale (so perfect prediction would correspond to a blue image with a yellow diagonal).
```

Learning synaptic delays with weights enables the visualization of the 'receptive field' of postsynaptic neurons, as illustrated in [](#rf). Five randomly chosen neurons from the hidden layer are plotted, revealing clear spatiotemporal separation of excitation and inhibition.

```{figure} sections/delays/0-5.png
:label: rf
:width: 100%
Receptive fields of 5 randomly chosen neurons in the hidden layer of the dilated convolutions with learnable spacings model. The x-axis represents the presynaptic neuron index, while the y-axis displays the learned delay value. Colors indicate the sign of the weight (blue=excitation, red=inhibition), with transparency denoting magnitude. Excitation and inhibition appear to be spatiotemporally separated.
```
