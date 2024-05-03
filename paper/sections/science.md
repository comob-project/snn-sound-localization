## Collective introduction 

* (Based on new_inh_model.md)
* For most animals, sound localization is realised through two classes of acoustic signals: binaural and spectral cues. 
* In humans, binaural cues are sufficient to discriminate sounds in the azimuth plane, while spectral cues help to discriminate vertical angles and resolve font-back ambiguities (ref). 
* Focussing on binaural cues, animals exploit two differences in the signals arriving at each ear: their interaural time and level difference (ITD and ILD).
* Though the relative importance of these two cues for a given animal, depends on it's head size and range of audible frequencies (ref). 
* As our audible range is centred on lower frequencies than other mammals (ref) and y (ref), it has long been assumed that we mainly use ITDs when discriminating between different azimuth angles, 
* and, the predominant model of human sound localisation, known as the Jeffress model, relies solely on ITDs (ref).
* In this model, the acoustic signals arriving at each ear are converted into spike trains, and then passed along monoaural delay lines to a bank of binaural coincidence detectors, via excitatory synapses.
* As each detector receives each monoaural signal with some delay, each is sensitive to a particular range of ITDs. For example, a sound heard from the left, will proceed through the left delays ahead of the right, until they converge at a coincidence detector tuned to that temporal offset.  
* Finally, the outputs of these coincidence detectors are summed over time and used to estimate the sounds location (Fig. x). 
* However, while such delay lines were found in the avian Nucleus Laminaris (ref) equivalent structures are yet to be found in mammals, and experiments suggest a role for inhibition, as well as excitation in sound localisation (refs).  
* With these caveats in mind, we set out to explore sound localisation through both simple, and more biologically plausible spiking neural network models.  

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

