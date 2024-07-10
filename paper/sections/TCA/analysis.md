(tca-section)=
## TCA Analysis
### Introduction

In the analysis of neural networks through TCA, we've explored the representation and learning dynamics of multiple models by examining their neuron, trial, and temporal factors. TCA helps decompose multidimensional data into core components that capture the essential structure and relationships inherent in the neural activities across different dimensions. This analysis provides a clear insight into how models encode and process information over multiple trials, revealing the underlying mechanisms that drive their performance and behaviour. By employing hierarchical clustering with Ward's method, we've specifically focused on assessing the similarity in neuron factor representations across models, which has elucidated the consistency and diversity of neural encoding across different training instances.

### Results

We use nonnegative tensor component analysis (TCA) to examine spiking activity from the hidden layer of a neural network. Gaussian smoothing is applied to the spike events, and trials are stacked into a single tensor. The rank-1 decomposition in [](#rank1) during training illustrates the model's learning process, characterised by increased activity across all IPD bins through a subset of hidden neurons. The analysis highlights predominant firing within two critical intervals in the time domain: 0-25ms and 50-75ms, which aligns with periods of active input signals.

```{figure} sections/TCA/rank-1.png
:label: rank1
Rank 1 decomposition of spiking during training of the simple model
```

To capture the categorical dynamics within the model, the optimal number of components was determined by minimising reconstruction error and maximising component similarity. An optimal count of six ranks was identified for the model and are shown in [](#rank6). The factors derived from tensor component analysis reveal distinct patterns of neural activation across time, highlighting the dynamic nature of responses to stimuli. Specifically when looking at trail factors, Factor 5 is responsive to the extreme IPDs of +π/2 and -π/2, while Factors 1 and 4 focus on more central IPDs. Factors 2 and 3 indicate neuron assemblies responsive to IPDs towards -π/2 as is Factor 6 to +π/2. 

```{figure} sections/TCA/rank-6.png
:label: rank6
Rank 6 decomposition of spiking during training of the simple model
```

### Model variability

To test variability between different instances of the simple model we trained 50 models on the same training data and compared the neuron and temporal factors of the rank 1 decomposition. Neuron factors were sorted by activation strength to align the most significant neurons across models and factors were normalised. Performing clustering analysis of the neuron factors between models helps to elucidate the ensembles responsible for learning the task. The dendrogram from the clustering provided a visual representation of these relationships, with models grouped together showcasing more similar model dynamics compared to those further apart. Here we can see grouping of models into 2 major categories in [](#clustering). 

Sampling models from each cluster shows that clusters with a higher number of active neurons tend to have better training accuracy but do not consistently achieve better test accuracy. In fact, clusters with fewer active neurons sometimes demonstrate better generalisation which had a slightly higher test accuracy despite fewer active neurons. This suggests that models with a moderate number of active neurons can achieve a balance between training effectiveness and test generalisation, potentially leading to more robust solutions. This discrepency in accuracies can be seen in [](#cluster_acc) where cluster 1-4 are increase in average active neurons. 

Comparing the activation of neural assemblies with more ranks as in [](#clustering) shows similar tuning across trails and models suggesting the models learn the same task but are able to do so with a range of subsets of neurons at the cost of accuracy. 

<!-- Split figure of clustering and temporal_av -->
```{figure} sections/TCA/clustering.png
:label: clustering
Hierarchical clustering of neuron factors across models
```

```{figure} sections/TCA/cluster_acc.png
:label: cluster_acc
Training and test accuracy of models in each cluster
```

```{figure} sections/TCA/temporal_av.png
:label: temporal_av
Temporal factors across models
```

Visualising the mean and standard deviation of temporal factors across models shows a common pattern of activation within the hidden layer neurons. The representation in [](#temporal_av) highlights periods of peak neuronal activity. The shifts in peak timings across different models suggest variability in how these models prioritise processing delays related to inputs. Such differences likely stem from the weights learned by each model, reflecting the phase differences prioritised.

Overall the analysis employing TCA and hierarchical clustering provided insights into the learning dynamics and neuron behaviour of the simple model trained under identical conditions. Our study identified the variability and consistency in neuron activation across different models, showcasing how the architecture can learn identical tasks using different neuronal assemblies. This research highlights the balance between neuron activity and model accuracy, suggesting that optimal learning may be achieved with a moderate number of highly active neurons, balancing robust training performance with effective generalisation. These findings allow for further explorations into model optimisation, adjustments and further analysis of similar spiking models.

<!-- ## Analysis of simple model 
We focused on exploring the behaviour of neurons across trials and temporal factors across multiple initialisations of the simple model. Analyzing the hidden layer's spiking activity during training using Tensor Component Analysis (TCA) [@Williams2018] revealed a distinct learning phase. A rank-1 decomposition highlighted a progressive amplification of neuronal responses across the entire range of labels. When decomposed to more ranks the trial factors showcased the tuning of the hidden layer for each IPD category. To test the temporal activity of the neurons, the simple model was trained on a standardised data generation process, then repeated ten times and analysed to reveal how consistently the model learned to represent the data. This reveals a highly active period of broad peaks where input neurons are most active. 

Hierarchical clustering, through Ward's method [@Ward1963], was applied to sorted and normalised neuron factors, revealing clusters of models with similar neuron activation patterns. This clustering indicated how similarly different models processed the same input data, based on the structural similarities in their learned neuron factors. This in conjunction with the recovered tuning of neural assemblies shows the model learns the same function with different subsets of neurons. 

Overall, the TCA and clustering revealed both consistencies and divergences in how different models learned from identical datasets. This insight is important for understanding model behaviour in predicting how variations in initial conditions or training protocols might impact the learning outcomes. The approach adopted here helps in identifying key neurons that drive model behaviour, which could be critical for further tuning and optimisation of the simple model. -->