
# Questions & challenges


## Modelling questions / aims

Starting point:

* What are the best strategies for localising sounds with a spiking neural network?
* Can we train networks end-to-end to perform as well or better than hand-crafted solutions?
  - _Zachary_: I'm going to try a few things to improve performance
* Can we understand what these trained networks are doing in a high level way?
  - _Dan_: I'm going to try out a few ideas for this.
* Do these networks do something similar to what has been proposed in the literature (labelled line models, hemispheric models, pattern match decoders) or something completely different?
  - _Lavinia_: I'm interested into looking at this (how spiking neural networks can be used to model observed neural representations).
* Do different optimal models emerge in different parameter regimes (head size, signal to noise ratio, multiple sound sources)?
  - _Danish_:  I have some previous work on head size scaling which could be relevant here.
* How do the results depend on the neuron model and available dynamics? For example, does adaptation matter and in which conditions?
  - _Alberto_: I'm interested into looking at this (neuron and synapse model, plasticity).
  - _Danish_: I'm also interested in looking at this from the perspective of synaptic plasticity and auditory spatial working memory models. 
  - _Dilay_: I'm interested in using/adapting the filter-and-fire neuron model (recently proposed by Beniaguev et al., 2022) in the SNN. 


## Technical challenges

* Delay learning: can we train delays with surrogate gradient descent?
  - _Jakub_: I'm interested in looking into this.
  - _Balázs_: I'm looking into this using DCLS as in https://arxiv.org/pdf/2306.17670.pdf
* Alternatives to surrogate gradient descent?
  - _Danish_:  I use a correlation learning model of synaptic plasticity which could in principle capture timing delays.
* Add a more realistic auditory periphery (cochlear filtering and more realistic spiking model).
  - _Danish_:  I have a simple vertebrate biophysical model of filtering in the auditory periphery which I could quickly test here.
* Number of time steps might be an issue for a more realistic model. May want to use dt=0.1ms and duration>=100ms so more than 1000 time steps.
* Add a more realistic sound localisation task (natural sounds, background noise, multiple sound sources, different frequencies).
  - _Tomas_: experiment with this, starting with multi-frequency sounds
  - _Danish_: I have looked into multi-frequency cochlear filtering for speech localization. It may be useful here.
  - _Divyansh_: How well does the model perform at different frequencies (even if still just pure tones)
* Consider multiple architectures, potentially matching the auditory system.
  - _Alicja_: I'll look into that, beginning with checking the effect of adding more hidden layers.
  - _Mingxuan_: I'll experiment with this starting with altering the output neurons.
* Consider more complicated neuron models and perhaps make some of these neuron model parameters trainable; for what situations can that help?
  - _Danish_:  I use a correlation learning model of synaptic plasticity which could in principle learn timing and ITD information.
  - _Ido_: Might be interesting to consider multi compartment biophysical neuron models. For starters, I'd be interested to try to add dendrites to the individual units (for example by using https://github.com/Poirazi-Lab/dendrify).
* How to understand what the learned network does?
  - _Helena_:  This is just a warm up, and I am starting with a simple thresholding on the W1W2 plot to improve the contrast. I am going to push file named as SNN_sound_W1W2_threshold_plot.ipynb. I will probably come back to this later. 
* Use regression instead of classification
  - _Mingxuan_: I'd like to experiment with this idea.
* Which level of biological realisms does the learning need to comply to? Which observables are available at the synapse as input to a learning rule?
  - _Danish_:  Very interesting question that I would like to explore.
* Level of biological realism and impact on performance - Dale law.
  - _Jose_: Looking into this
* Distribution of inhibitory and excitatory neurons using Dale's law
  - _Sara_: First exploratory and interesting results, warrant further investigation
