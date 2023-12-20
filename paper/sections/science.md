# Collective intro 
* Introduce problem. 
* Explain Jeffries model. 
* Outline general questions - e.g. the role of inhibition and how networks encode temporal information. 

# A simple spiking neural network model
* To explore how networks of spiking neurons can localise sound, we used surrogate gradient descent (ref) to train a simple model.
* Our model consisted of a single layer of leaky integrate-and-fire (LIF) units with inputs from two populations (representing the left and right ears) and feed-forward connections to a layer of non-spiking output units (Fig.x).
* As inputs we generated Poisson spike trains representing a sine wave signals which arrive with an inter-aural phase difference (IPD) between the two ears (Fig.x).  
* We discretised these IPDs into classes and used surrogate gradient descent (ref) to train networks to report the most likely IPD range.
* Using this setup we succesfully trained SNNs on this task, and found that performance increased with shorter membrane time constants (Zach's notebook).
* [Notably membrane only version can't solve the task].    
* Building on this base result, we explored two main questions: how changing the neuron model, alters the networks behaviour and how the phase delays (within each ear) can be learned.    
    
## Alternative neuron models  
* Here we explore how changing the hidden unit's neuron model impacts the network. 

### Dale's law 
* In biological networks most neurons release a single neurotransmitter and so can be considered as being either excitatory or inhibitory. 
* Constraining our units this way lead to...       

### Filter-and-fire 
* Unlike most point neuron models, in which pairs are connected by a single weight, many biological neurons make multiple contacts with their partners at different points along their dendritic tree. 
* This leads to different dynamics - which can be represented using the filter-and-fire neuron model. 
* Using this setup we conducted three experiments. 
* First, convolve input_spikes with one single filter, with fixed tau hyperparameters. 
* Second, convolve input_spikes with different, random filters (try with, and without delay ranges = a random fixed delay value or just 0); here, we don't use fixed tau hyperparameters and instead randomly sample them from predefined ranges.
* Third, use filter-and-fire neurons (e.g. M = 3 connections per axon). 

## Learning delays 
Here we explore how the phase delays can be learned in the network through two methods. 

### With dilated convolutions with learnable spacings (DCLS)
First, with DCLS. Needs to train weights and delays. 

### With a differentiable delay layer (DDL)
Second, with differentiable delays. Can train weights and delays independently. 
Comparisons between DCLS, single-layer, related methods. 

# A more biologically plausible model
Finally, we developed a more detailed model in which... (new_inh_model)