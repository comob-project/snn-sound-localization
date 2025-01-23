(tca-section)=
## Tensor component analysis

```{list-table}
* - Section authors
  - Umar Abubacar
* - Notebooks
  - [](../research/TCA-analysis.ipynb)
```

To explore the spiking activity of the hidden units in our simple, neural network model, we used tensor component analysis (TCA) {cite:p}`Williams2018`. Conceptually, this method identifies groups / ensembles of neurons with similar activity patterns, termed components. More specifically, each component, identified by the algorithm, is composed of three factors:
* A neuron factor - describing how strongly associated each neuron is with each component.
* A time factor - indicating how the activity of each component changes within a trial. 
* A trial factor - denoting how active each component is on each trial.  
Notably the number of components, termed the rank, is a hyperparameter which requires some consideration. 

### Methods
To acquire the necessary data we trained the basic model, and recorded the spiking activity of it's hidden layer. We then smoothed each unit's activity over time using a Gaussian kernel. Then applied nonnegative tensor component analysis using the [Tensortools library](https://github.com/neurostatslab/tensortools).

### Results
As a first pass, we began by recording the spikes from a model during training and running TCA with a single rank [](#rank1). This single component contained a subset of the hidden units (middle panel), which were more active during trials with high IPDs (left panel) and tended to have sinusoidal-like patterns of activity (right panel).      

```{figure} sections/TCA/rank-1.png
:label: rank1
:width: 100%
Applying TCA, with a single rank, to the spikes collected from a single neural network's hidden layer during training. Left: this component's activation (y-axis) across a subset of training trials (x-axis), each trial is coloured by it's IPD from low (blue) to high (yellow). Middle: of the network's 30 hidden units (x-axis) only a subset are strongly associated (y-axis) with this component. Right: the activity of this component (y-axis) over time (x-axis) within trials resembles a sinusoid. 
```

Next, we took a trained network, recorded it's spikes in response to a range of IPDs and then used TCA to identify 6 components [](#rank6). While some units were associated with multiple components (middle column) and all of the component's temporal factors were generally sinusoid-like (right column), each components activity was strongly modulated by the trial's IPD (left column). For example, component 4 was strongly active on trials with a low IPD and virtually inactive on trials with a high IPD. While, component 5 showed the opposite behaviour. Taken together, this suggests that some of network's hidden units are selectively responsive to low/high IPD input signals. 

Finally, we experimented with training multiple networks, analysing their spiking activity with TCA and comparing the results. Our preliminary analysis of these data can be found [here](../../../research/TCA-analysis.ipynb). 

```{figure} sections/TCA/rank-6.png
:label: rank6
:width: 100%
TCA analysis, with 6 ranks, of a trained network's spiking in response to a range of IPDs. Each row shows one of six identified components. Left column: each components trial factor - i.e. it's activation (y-axis) across a set of test trials (x-axis). Each test trial is coloured by it's IPD from low (blue) to high (yellow). Middle column: of the network's 30 hidden units (x-axis) slightly different subsets are associated with each component. Right: the activity of each component (y-axis) over time (x-axis) within trials.
```