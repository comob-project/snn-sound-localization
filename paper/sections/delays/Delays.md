(delay-section)=
## Learning delays

```{list-table}
* - Section authors
  - Karim G. Habashy
  - Balázs Mészáros
* - Notebooks
  - [](../research/Learning_delays.ipynb), [](../research/Learning_delays_major_edit2.ipynb), [](../research/Solving_problem_with_delay_learning.ipynb)
- [](../research/Quick_Start_Delay_DCLS.ipynb)
```

This section introduces a simple method to solve the sound localization problem with only learnable delays. Additionally, it discusses a method that learns both weights and delays, introduced in {cite:p}`hammouamri2024learning`.

### Introduction

:::{warning}
Karim here: I have checked the main intro and the intro here and I see no common passages. Thus, I recommend moving all to main intro after the first paragraph. However, if done so, the main intro of delays would be visibly larger than the other sections. In this regard, I leave to you guys to remove any passages you guys deem not necessary as both of you will have the bigger picture. I have made some small edits to improve it, I hope that helps. 
:::

Studying the computational properties of axonal transmissions goes as far back as in {cite:p}`Jeffress1948`. In this study, it was shown that with the right network setup, axonal delays can be utilized to transform a temporal cue to a spatial one for sound localization. This study was a leading study in terms of using delays explicitly to explain a neuronal function. It paved the way for others to follow, like the study by {cite:p}`KLWH2001`, where they investigated the question of how ITD computation maps can arise ontogenetically in the laminar nucleus of the barn owl. They showed that interaural time differences (ITD) computational maps emerge from the combined effect of a Hebbian spike-based learning rule and its transmission along the presynaptic axon. Thus, from this study, another role of axonal delays can be inferred. They shape network structure when coupled with temporal learning rules. Based on this insight, several studies investigated the combined effect of spike timing-dependent plasticity (STDP), axonal conduction delays and oscillatory activity on recurrent connections in spiking networks. In one of the studies, {cite:p}`KBTG2013` demonstrated the selective potentiation of recurrent connections when the beforementioned computational considerations are taken into account. Also, {cite:p}`HKTI2016` showed that neural selection for memory formation depends on neural competition. In turn, for neural competition to emerge in recurrent networks, spontaneously induced neural oscillation coupled with STDP and axonal delays are a perquisite. 

From the above, the intuition behind coupling neuronal delays with STDP can be reasoned about. The sign of the STDP rule depends on the order of post- and pre-synpatic spiking, which axonal delays can effectively reverse. For example, the arrival of presynaptic spikes at the synapse before the backpropagated action potential leads to a synaptic depression. However, reducing the axonal transmission speed would lead to potentiation. In this line of thought, {cite:p}`MAVT2017` studied the combined role of delays and STDP on the emergent synaptic structure in neural networks. It was shown that, qualitatively different connectivity patterns arise due to the interplay between axonal and dendritic delays, as the synapse and cell body can have different temporal spike order. 

Aside from their role in modeling cortical functions or shaping a network's synaptic structure, another line of research emerged from the seminal work by {cite:p}`EMI2006`. They showed that when including conduction delays and spike-timing dependent plasticity (STDP) into their simulation of realistic neural models, polychronous groups of neurons emerge. These groups show time-locked spiking pattern with millisecond precision. Subsequent studies investigated the properties and functions of such neuronal groups. For example, {cite:p}`BSEI2010` demonstrated the natural emergence of large memory content and working memory when the neuronal model exploits temporal codes. Specifically, short term plasticity can briefly strengthen the synapses of specific polychronous neuronal groups (PNG) resulting in an enchantment in their spontaneous reactivation rates.  In a qualitatively different study, {cite:p}`EIAS2018` showed that networks that exhibit PNG possess potential capabilities that might solve the dynamic binding problem. These networks respond with stable spatio-temporal spike trains when presented with input images in the form of randomized Poisson spike trains. The functionality of these kind of networks emerged due to the interplay of various factors including: i) random distribution of axonal delays ,ii) STDP and iii) lateral, bottom-up and top-down synaptic connections. 

Finally, it should be noted that most of the studies that incorporate axonal and/or dendritic delays, include them as a non-learnable parameter. Few studies investigated the possibility of training transmission delays in order to enhance the computational capabilities of spiking neural networks (SNN). {cite:p}`TM2017` proposed an algorithm that modifies the axonal delays and synaptic efficacy in both supervised and unsupervised approaches.  The learning method involbed used approximates of the Expectation-Maximization (EM) algorithm and after training, the network learns to map spatio-temporal input-output spike patterns. Thus, EM is one way to train SNNs that are cast as probabilistic models. Another approach that exploits the massive infrastructure that is laid out the deep learning literature is the work by {cite:p}`hammouamri2024learning`. In this work, delays are represented as 1D convolutions through time, where the kernels include a single per-synapse non-zero weight. The temporal position of these non-zero weights corresponds to the desired delays. The proposed method co-trains weights and delays and is based on the Dilated Convolution with Learnable Spacings (DCLS) algorithm ({cite:p}`ITT2023`).  

In this work we propose a delay learning algorithm that is simple and efficient. The delay learning is mediated by a differentiable delay layer (DDL). This layer can be inserted between any two layers in an SNN in order to learn the appropriate delay to solve a machine learning task. This DDL is architecture agnostic. Also, the method is designed to learn delays separately from synaptic weights. 

### Methods

The DDL is, mainly, based on a 1D version of the spatial transformer (STN) network {cite:p}`JSZK2015`. The STN is a differentiable module that can be added into convolutional neural networks (CNNs) architectures to empower them with the ability to spatially transform feature maps in a differentiable way. This addition leads to CNN models that are invariant to various spatial transformations like translation, scaling and rotation. Image manipulations are inherently  not differentiable, because pixels are a discrete. However, this problem is overcome by the application of an interpolation  (for example bi-linear) after the spatial transformation. 

The DDL is a 1D version of the spatial transformer where the only transformation done is translation. Translation of a spike along the time dimension can be thought of as a translation of a pixel along the spatial coordinates. The general affine transformation matrix for the 2D case takes the form in the following equation:
	
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
		
In the above equation, ${sr_1,~sr_2,~sr_3,~sr_4}$ are the elements responsible for the linear transformations of scaling and rotation. ${t_x~and~t_y}$ are the translations in the x-axis and y-axis respectively. ${x_t~and~y_t}$ are the location of a spike/pixel (in case of spikes y = 0) in the target/output grid, while ${x_s~and~y_s}$ are the location of the source grid. A grid can be an image or a 2D array of spike trains. For the case of only translation along the x-axis, the affine transformation matrix becomes: 
	
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
Structure of the DDL. The DDL shifts an input spike train by applying translation then interpolation.
```

Only the DDL is needed to solve the sound localization problem, where the output classes are the target IPD. As shown in [](#DelayNetwork), the DDL inserted between the input and output nodes is sufficient to solve the sound localization problem. In this cases, the weights are set to one and the biases to zero.

```{figure} sections/delays/Network.png
:label:DelayNetwork
:width: 60%
The model architecture. The DLL inserted between the input and out nodes is sufficient to solve the sound localization problem. The output nodes are IPD classes spanning the range ${[-90^o,~85^o]~in~5^o}$ steps.
```

Though the DLL shifts the spike trains in a differentiable way, this shift has a meaningful impact through a multiplicative synapse. Also, to facilitate learning, a non-spiking output was utilized. Thus, these two points taken together, the voltage at the output takes the form:

$$v_i = -\sum_{t=0}^{T}(u_{1i}(t) - u_{2i}(t))^2$$
$$\tau_m*\frac{du_{xi}}{dt} = -u_{xi} + S_x(t)  \;\;\;\;  x \in \{1,2\}
S_x(t) = \sum_{z=1}^{n} \delta(t-t_x^z)$$

${v_i}$ is the voltage at output node ${i.~u_{xi}}$ is the dendritic potential. $\tau_m$ is the time constant of a dendritic branch. $S_x(t)$ is the input spike train. The form $(u_{1i}(t) - u_{2i}(t))^2$ looks like a squared error and might, at first glance, seem not biological, but the expanded term (as seen from the following equation) is a from of multi-synaptic multiplicative-additive interaction.

$$
(u_{1i}(t) - u_{2i}(t))^2 = u_{1i}(t)^2 -2*u_{1i}(t)*u_{2i}(t) + u_{2i}(t)^2
$$

The synaptic delay learning method, employing Dilated Convolutions with Learnable Spacings, operates by delaying spike trains through a 1D convolution featuring a single non-zero element, equivalent to the synaptic weight, positioned at the appropriate delay value. This method also uses interpolation to identify the optimal delay, facilitating the learning of delays with weights through backpropagation through time in arbitrarily deep SNNs. As we have implemented the method precisely as described in the original paper (with the exception of hyperparameters), we direct the reader to the original paper for a comprehensive understanding{cite:p}`hammouamri2024learning`.

### Results and discussion

In this section, the problem complexity is increased up to 36 output units spanning an IPD range of ${[-90,~85]}$ with a step of ${5^o}$. Employing the DDL to solve such a task leads to the spike raster plots shown in [](#DelaySpikeHistograms).

```{figure} sections/delays/Results_1.png
:label: DelaySpikeHistograms
:width: 100%
Spike histograms for IPDs before and after training.
```

To facilitate the search for a solution while using the DDL, we assume that the delay lines coming from one ear is fixed, while the delay lines from the other ear is adaptable starting from an initial default value. Thus, the learned delays can be thought of as the change in delays, which is added to the default delays. This approach leads to the results shown in [](#DelaySpikeHistograms)B, where the top of the spike histograms is fixed, while the bottom half has a graded shift in its spike plots. Such results were achieved with the application of time constant decay that leads to a decrease in loss as shown in [](#DelayLossDist)A. 

```{figure} sections/delays/loss-and-dist.png
:label: DelayLossDist
:width: 100%
Performance metrics one. A) Loss as a function of the epochs. B) The difference between the True and predicted IPDs in a test batch.
```

Further analysis of such solutions warrants testing them in different forms. In this regards, we start by displaying the distribution of the errors between the true IPDs and predicted IPDs in a test batch as shown in [](#DelayLossDist)B, which shows an almost log-normal distribution. In addition, we show the confusion matrix for both the training and testing batches on the right images of [](#DelayConfuse), and the difference between the true and predicted IPDs on the left images of [](#DelayConfuse).


```{figure} sections/delays/Confuse.png
:label: DelayConfuse
:width: 100%
Performance metrics two. Here is shown the distribution and confusion matrix between true IPD values and A) training batch IPD estimates, B) testing batch IPD estimates.
```

Similar to the other cases, the DCLS architecture is trained for classification across 12 classes, as shown in [](#DelaySpikeHistograms2). While delays were manually added to the data in other cases, it is not feasible to ascertain if the method learns identical delay values due to the implementation of varied conduction delays for each synapse. However, in terms of performance, similar accuracy is achieved.


```{figure} sections/delays/Confuse_dcls.png
:label: DelaySpikeHistograms2
:width: 100%
Distributions of true and estimated IPD values, along with their corresponding confusion matrices for the training and test sets, obtained using the DCLS algorithm.
```
Learning synaptic delays with weights enables the visualization of the 'receptive field' of postsynaptic neurons, as illustrated in [](#rf). Five randomly chosen neurons from the hidden layer are plotted, revealing clear spatiotemporal separation of excitation and inhibition.

```{figure} sections/delays/0-5.png
:label: rf
:width: 100%
Receptive fields of 5 randomly chosen neurons in the hidden layer. The x-axis represents the presynaptic neuron index, while the y-axis displays the learned delay value. Colors indicate the sign of the weight (excitation or inhibition), with transparency denoting magnitude. Excitation and inhibition appear to be spatiotemporally separated.
```
