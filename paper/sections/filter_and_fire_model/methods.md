# Methods [WIP]

We followed an incremental methodology to introduce our adaptation of the F&F neuron model in the baseline SNN: we devised three Experiments, with increasing complexity introduced to the baseline SNN. In all Experiments, we endowed single neurons in the hidden layer of the SNN with synaptic dynamics (rise and decay time constants), in order to obtain synaptic currents from the input spike trains that were originally fed into the baseline SNN.

The synaptic current to a single hidden neuron (e.g., the $j_{th}$ hidden neuron) receiving inputs from $N$ presynaptic (input) neurons with $M$ connections between each input neuron and the $j_{th}$ hidden neuron, at timestep $t$ of the simulation, is described in Equation (1):

$$g_{j}(t) = \sum_{i=1}^{N} \sum_{k=1}^{M}(x_{i} \ast kernel_{i,k,j})^{T} \cdot {W_{i,k,j}}$$

where:

- $M = 1$ in **Experiment 1** and **Experiment 2**; $M$ took discrete values in $[2, 5]$ in **Experiment 3**.
- $kernel_{i,k,j}$ is the synaptic kernel of the synapse from the $k_{th}$ connection of the $i_{th}$ input neuron to the $j_{th}$ hidden neuron.
- Implementation note: the kernels were computed and stored for each synapse before the filtering, and the weight matrix between the input and hidden layers was a $(N \cdot M \cdot H, H)$ matrix, where $(N \cdot M \cdot H)$ is the total number of synapses across $N$ input neurons and $H$ hidden neurons.

The synaptic kernel for a synapse $syn$ is defined as the difference of two exponentials (adapted from Roth & Rossum, 2009):

$$kernel_{syn} = e^{-(window\_size)/\tau_{decay}} - e^{-(window\_size)/\tau_{rise}}$$

where the window size $window\_size$ was the entire simulation size ($1000$ ms).

In **Experiment 1**, $tau_{decay}$ and $tau_{rise}$ were fixed across all synapses (the same kernel is used for all synapses), with $tau_{decay}$ ranging from 0.4 to 2 ms and $tau_{rise}$ ranging from 0.2 to 1.8 ms. These ranges were empirically motivated from a diverse literature on auditory modelling and experimental research in animals (e.g., see review in Trussell, 1997). In **Experiments 2** and **3**, $tau_{decay}$ and $tau_{rise}$ were randomly sampled for each synapse such that the kernel peak times are roughly uniformly distributed in a fixed real-valued range of $[0, 1]$ ms: this approximative range is motivated by the physiological human range of interaural time differences (ITDs) observed for a single frequency of $250$ Hz. The peak time of a synaptic kernel (i.e., when the synaptic conductance peaks) is given by Equation (3) (Roth & Rossum, 2009):

$$t_{peak} = t_{0} + \frac{\tau_{decay}\tau_{rise}}{\tau_{decay} - \tau_{rise}} + \ln(\frac{\tau_{decay}}{\tau_{rise}})$$

**Experiment 2** acts, therefore, as an extension to **Experiment 1**, and implements dendritic filtering with heterogeneous synaptic dynamics across synapses. Importantly, **Experiment 3** extends the dendritic filtering implemented in **Experiment 2** by allowing each hidden F&F neuron to be contacted multiple ($M > 1$) times by each input neuron.

The operations above assume a batch size of 1 (i.e., only one simulation training sample is considered). During training, we used minibatch stochastic gradient descent ($batch\_size = 64$), so these computations were vectorised across all examples of a given batch.

The main hyperparameters are reported in Table 1.

| **Hyperparameter** | **Name** | **Value** |
|---------------------|----------|-----------|
| sound stimulus duration | duration | 100 (ms) |
| sound stimulus frequency | F | 250 Hz |
| timestep | DT | 0.1 (ms) |
| number of input neurons | input\_size | 200 (100 neurons per "ear") |
| number of hidden neurons | num\_hidden | 5 |
| number of output neurons (bins of IPDs) | num\_classes | 6 |
| membrane time constant (hidden neuron) | tau\_hidden | 2 (ms) |
| membrane time constant (output neuron) | tau\_output | 20 (ms) |
| connection drop probability (Exp 3 only) | drop\_probability | [0, 0.2, 0.5, 0.8] |
| connections per axon between each input neuron and hidden neuron | connections\_per\_axon | 1 for Exps 1-2, [2,3,4,5] for Exp 3 |
| batch size | batch\_size | 64 |
| number of training batches | n\_training\_batches | 64 |
| number of testing batches | n\_testing\_batches | 64 |
| number of training epochs | num\_epochs | 50 |
| learning rate | lr | [0.0001, 0.0004, 0.0007, 0.001, 0.004, 0.007, 0.01, 0.04, 0.07, 0.1] for Exps 1-2, [0.1, 0.01, 0.001, 0.0001] for Exp 3 |
| hyperparameter for surrogate gradient descent | BETA | 5 (ms) |

**Table 1:** Main Hyperparameters
