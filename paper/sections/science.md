## Introduction 

We chose sound localisation using interaural time differences as the topic of the original [Cosyne tutorial that kicked off this project](https://neural-reckoning.github.io/cosyne-tutorial-2022/) {cite:p}`10.5281/zenodo.7044500`. The reasoning was that the tutorial was about spiking neural networks, and their unique distinguishing feature is the way that time is processed, something that is particularly important in the sound localisation circuit.

We are able to localise sound by detecting location- or direction-specific cues in the signals that arrive at our ears. One of the most important source of cues (although not the only one) come from differences in the signal between two ears, including both timing and level differences (interaural timing difference or ITD, and interaural level difference or ILD). Humans are able to detect arrival time differences in some cases as small as 20 $\mu$s.

The classic model of ITD sensitivity is the delay line model of {cite:t}`Jeffress1948` in which an array of binaural coincidence detector neurons receive inputs from the two ears with different delays. When the neural delays exactly match the acoustic delays induced by the sound location, the neuron is most active, and therefore the identity of the most active neuron can tell you the direction of the sound. This model was shown to be inefficient with respect to neural noise by {cite:t}`McAlpine2003`, who proposed an alternative model based on average firing rates of the two binaural hemispheres. This model was shown to be optimally robust to neural noise. {cite:t}`goodman_decoding_2013` showed that this model performed too poorly to account for behavioural data, especially in situations where sounds had complex and unknown spectral properties, or in the presence of background noise, and proposed an alternative based on a perceptron-like neural network that was both robust to neural noise and performed well across a range of conditions.

The starting point of this project was to ask: what solutions would you find if you directly optimised a spiking neural network to localise sounds? How would those solutions depend on the available neural mechanisms and statistics of the sound? Could we understand the solutions found in a simple way? What properties would the solution have in terms of robustness to noise, generalisation, and so forth? Could the solutions found by optimisation throw light on features found in the auditory systems of different animals? 

## A simple spiking neural network model
* To explore how networks of spiking neurons can localise sound, we first considered a simple model, akin to the Jeffress model (ref).
* Our model consisted of a single layer of leaky integrate-and-fire (LIF) units with inputs from two populations (representing the left and right ears) and feed-forward connections to a layer of non-spiking output units (Fig.x).
* As inputs we used sine wave signals which arrived at each ear with an inter-aural phase difference (IPD).
* Each ear contained a population of units with uniform phase delays, which generated independent Poisson spike trains (Methods).
* We discretised the range of IPDs into classes and trained networks, using supervised surrogate gradient descent (ref), to report the most likely IPD range for a given input.
* Using this setup we successfully trained SNNs on this task, and found that accuracy increased as we reduced the membrane time constant of the units in the hidden layer (Zach's notebook); emphasising the role of coincidence detection in this task. 
* Building on this base model, we explored two main questions: how changing the neuron model, alters the networks behaviour and how the phase delays (within each ear) can be learned. 
    
## Alternative neuron models  
* Here we explore how changing the hidden unit's neuron model impacts the network. 

### Dale's principal 
* In biological networks most neurons release the same set of transmitters from all of their synapses, and so can be broadly be considered to be excitatory or inhibitory to their post-synaptic partners; a phenomenon known as Dale's principal (ref), 
* and the Jeffress model uses all excitatory neurons.  
* In contrast, most artificial neural networks, including our base model, allow single units to have both positive and negative output weights.
* To test the impact of restricting units to being either excitatory or inhibitory, we trained our base model across a range of inhibitory:excitatory unit ratios, and tested it's performance on unseen, test data. 
* We found that networks which balanced excitation and inhibition performed significantly better than both inhibition-only networks - which perform at chance level as no spikes propagate from the hidden to output layer, and excitation-only networks - which were roughly 30% less accurate than balanced networks; 
* highlighting the importance of inhibition in this model.  
* To understand where in the network inhibition is required, we then trained a second set of networks in which we forced either the input or hidden units to be all excitatory, and set the remaining units to be half inhibitory and half excitatory.
* Networks with all excitatory hidden units performed as well as networks with balanced units, while networks with purely excitatory inputs performed significantly worse (Fig. x), demonstrating a role for inhibition in the input-hidden connections / delay lines.    

### Filter-and-fire 
* Unlike most point neuron models, in which pairs are connected by a single weight, many biological neurons make multiple contacts with their post-synaptic partners at different points along their dendritic tree.
* These contacts evoke post-synaptic potentials (PSPs) with distinct temporal dynamics, depending on their distance from the soma, with distal/proximal contacts inducing prolonged/brief PSPs (ref).
* These features are captured by the filter-and-fire neuron model (F&F) (ref), in which units make multiple contacts with their partners and each input is convolved with a distance-from-soma dependent synaptic filter.  
* While networks of F&F units outperform networks of LIF units on a temporal version of MNIST (ref), we hypothesised that this difference would be magnified in our sound localisation task, given it's natural temporal structure. 

* To test this, we conducted three experiments. 
* First, convolve input_spikes with one single filter, with fixed tau hyperparameters. 
* Second, convolve input_spikes with different, random filters (try with, and without delay ranges = a random fixed delay value or just 0); here, we don't use fixed tau hyperparameters and instead randomly sample them from predefined ranges.
* Third, use filter-and-fire neurons (e.g. M = 3 connections per axon). 

## Learning delays 
Many studies which incorporate axonal and/or dendritic delays include them as non-learnable parameters (refs) like our base model. Here we explore how these phase delays can be learned through two approaches.

### With dilated convolutions with learnable spacings (DCLS)
First, with DCLS (Hammouamri et al., 2023; Khalfaoui-Hassani et al., 2023).
Key points: 
* Use 1D convolutions through time to simulate delays between consecutive layers.
* Where the kernels include a single non-zero weight per-synapse, which corresponds to the desired delay.  
* Learns both weights and delays. 
* Visualisation of results: 
    * x - learned delay, y - learned weight.
    * Hidden units separate data spatio-temporally. 

### With a differentiable delay layer (DDL)
Second, by introducing a differentiable delay layer.
Key points: 
* Can be placed between any two layers in an SNN.  
* Can train weights and delays independently. 
* It would be great to include experimental or conceptual comparisons between DCLS and DDL. 

## A more biologically plausible model (new_inh_model)
* Finally, we developed a more detailed model in which we used over 170,000 units, with conductance-based synapses, to approximate the structure of the mammalian brainstem circuit (Methods).
* In short, input spectrograms representing sounds at azimuth angles from -90° to +90° were converted into spikes,
* then passed forward to populations representing the globular and spherical bushy cells, and subsequently the lateral and medial superior olivary nuclei, from which we readout sound source angle predictions (Fig. x). 
* Note that, unlike the work with our simple model, we used no learnable parameters in this model, and instead based parameters on neurophysiological data. 
* For example, the MSO units had excitatory inputs from both the ipsi and contralateral SBCs and dominant inhibition from contralateral GBCs (Fig. x).  

Results: 
* 

