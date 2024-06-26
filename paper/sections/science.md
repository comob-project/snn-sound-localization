## Introduction 

In the [Cosyne tutorial](https://neural-reckoning.github.io/cosyne-tutorial-2022/) {cite:p}`10.5281/zenodo.7044500` on spiking neural networks (SNNs) that launched this project, we used a sound localisation task. Reasoning that sound localisation requires the precise temporal processing of spikes at which these networks would excel.  

Animals localise sounds by detecting location- or direction-specific cues in the signals that arrive at their ears. Some of the most important sources of cues (although not the only ones) come from differences in the signals between two ears, including both level and timing differences. Respectively, termed interaural level difference (ILD) and interaural timing difference (ITD). In some cases humans are able to detect arrival time differences as small as 20 $\mu$s.

The classic model of ITD sensitivity is the delay line model of {cite:t}`Jeffress1948` in which an array of binaural coincidence detector neurons receive inputs from the two ears with different delays. When a neurons' delays exactly match the acoustic delays induced by the sound location, it will be maximally active. Therefore, the identity of the most active neuron indicates the direction of the sound. This model is widely accepted, though was shown to be inefficient with respect to neural noise by {cite:t}`McAlpine2003`, who proposed an alternative model based on the two binaural hemispheres average firing rates - which is optimally robust to neural noise. However, {cite:t}`goodman_decoding_2013` showed that these model's perform too poorly to account for behavioural data, especially in situations where sounds had complex and unknown spectral properties, or in the presence of background noise, and proposed an alternative based on a perceptron-like neural network - which is both robust to neural noise and performed well across a range of conditions. 

Building on this literature, and our Cosyne tutorial, the starting point of this project was to ask: what solutions would you find if you directly optimised a spiking neural network to localise sounds? How would those solutions depend on the available neural mechanisms and statistics of the sound? Could we understand the solutions found in a simple way? What properties would the solution have in terms of robustness to noise, generalisation, and so forth? Could the solutions found by optimisation throw light on features found in the auditory systems of different animals? 

## A simple spiking neural network model

We started with a simple, spiking neural network model (described in more detail in [](#basic-methods)) trained to solve a highly abstracted sound localisation task. 

The task is to estimate the ITD of a pure tone (sine wave) at a fixed frequency. This is equivalent to estimating the interaural phase difference (IPD) since the ITD is ambiguous for a sine wave. The model consists of three layers. First, a layer of spiking input neurons which fire spikes according to a Poisson process with a time-varying rate determined by the input stimulus. This layer is divided into two subpopulations corresponding to the two ears, with signals to one ear delayed with respect to the other. Each neuron within a subpopulation has a different phase delay. Next, comes a single hidden layer of leaky integrate-and-fire (LIF) neurons, and an output layer of leaky, non-spiking neurons. Each output neuron is associated to a particular IPD, and the estimated IPD of the model is the identity of the most active output neuron. 

The input neurons are all-to-all connected to the layer of hidden neurons via a trainable weight matrix. In this way, during training the model is free to *select* the neurons with the appropriate phase delays to generate the desired properties for the hidden layer neurons. This lets the model learn to make use of delays without having to directly implement trainable delays, as this is a challenging problem (which we tackled later in [](#overview-delays)).

Using this setup, we successfully trained SNNs on this task, and found that accuracy increased as we reduced the membrane time constant of the units in the hidden layer ([](../research/Optimizing-Membrane-Time-Constant.ipynb)). This initially suggested that coincidence detection played an important role. However, further analysis in [](../../research/time-constant-solutions.ipynb) (described in more detail in [](#basic-model)) showed that in fact, the network was not using a coincidence detection strategy, or indeed a spike timing strategy. Rather, it appears to be using an approach similar to the equalisation-cancellation theory {cite:p}`durlach_equalization_1963;culling_equalization-cancellation_2020` by subtracting various pairs of signals to find the point where they approximately cancel. Careful analysis of the trained model showed that it could be extremely well approximated by a 6-parameter model that is quite easy to describe, but does not obviously correspond to any known features of the auditory system.

Building on this base model, we explored two main questions: how changing the neuron model alters the network's behaviour and how the phase delays (within each ear) can be learned.
    
## Alternative neuron models  

### Dale's principle 

In biological networks most neurons release the same set of transmitters from all of their synapses, and so can be broadly be considered to be excitatory or inhibitory to their post-synaptic partners; a phenomenon known as Dale's principle [@10.1177/003591573502800330;@10.1001/jama.1954.02940400080039;@DalesPrinciple]. In contrast, most neural network models, including our base model, allow single units to have both positive and negative output weights.

To test the impact of restricting units to being either excitatory or inhibitory, we trained our base model across a range of inhibitory:excitatory unit ratios, and tested it's performance on unseen, test data ([](../research/Dales_law.ipynb)). We found that networks which balanced excitation and inhibition performed significantly better than both inhibition-only networks - which perform at chance level as no spikes propagate forward, and excitation-only networks - which were roughly 30% less accurate than balanced networks.

To understand where in the network inhibition is required, we then trained a second set of networks in which we forced either the input or hidden units to be all excitatory, and set the remaining units to be half inhibitory and half excitatory. Networks with all excitatory hidden units performed as well as networks with balanced units, while networks with purely excitatory inputs performed significantly worse, demonstrating a role for inhibition in the input-hidden connections / delay lines.

Inhibition therefore plays an important role in this model, in line with experimental data that shows that blocking inhibition eliminates ITD-sensitivity in the medial superior olive [@Brand2002;@Pecka2008].

### Filter-and-fire

Unlike most point neuron models, in which pairs are connected by a single weight, many biological neurons make multiple contacts with their post-synaptic partners at different points along their dendritic tree. These contacts evoke post-synaptic potentials (PSPs) with distinct temporal dynamics, depending on their distance from the soma, with distal/proximal contacts inducing prolonged/brief PSPs. These features are captured by the filter-and-fire neuron model (F&F) [@beniaguev_dendro_plexing_2024], in which units make multiple contacts with their partners and each input is convolved with a distance-from-soma dependent synaptic filter. While networks of F&F units outperform networks of LIF units on a temporal version of MNIST, we hypothesised that this difference would be magnified in our sound localisation task, given it's natural temporal structure. We found that while training performance was increased using the F&F model, test performance was much worse, suggesting overfitting. 

(overview-delays)=
## Learning delays 
As in our base model, many studies incorporate axonal and/or dendritic delays as non-learnable parameters. Here, we explore how these phase delays, as well as synaptic delays, can be learned through two approaches.

The first method was to develop a differentiable delay layer (DDL). This method uses a combination of translation and interpolation, where the interpolation allows the delays to be differentiable even though time steps are discrete. This can be placed between any two layers in a spiking neural network, and is capable of solving the task without weight training. This work is described in more detail in [](#delay-section).

While we were developing our DDL-based method, a paper introducing synaptic delays using dilated convolutions with learnable spacings (DCLS) was published [@hassani2023dilated;@hammouamri2024learning], prompting us to explore this approach as well. This method also relies on interpolation and is very similar to the DDL method, serving as a generalization for synaptic delays. It uses a 1D convolution through time to simulate delays between consecutive layers. The kernels include a single non-zero weight per synapse, which corresponds to the desired delay. This method co-trains weights and delays.

We found that both methods performed well and eliminated the artificial phase delays introduced in the basic model.

## Detailed inhibition-based model

Finally, we developed a more detailed model in which we used over 170,000 units, with conductance-based synapses, to approximate the structure of the mammalian brainstem circuit (see more details in [](#inhib-model)). 

In short, input spectrograms representing sounds at azimuth angles from -90° to +90° were converted into spikes, then passed forward to populations representing the globular and spherical bushy cells, and subsequently the lateral and medial superior olivary nuclei, from which we readout sound source angle predictions. Note that, unlike the work with our base model, we used no learnable parameters in this model, and instead based parameters on neurophysiological data. For example, the MSO units had excitatory inputs from both the ipsi and contralateral SBCs and dominant inhibition from contralateral GBCs.

The model generated realistic tuning curves for lateral and medial superior olive (LSO and MSO) neurons. Moreover, removing inhibition shifted ITD sensitivity to the midline, as in [@Brand2002;@Pecka2008].
