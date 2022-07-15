
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


## Technical challenges

* Delay learning: can we train delays with surrogate gradient descent?
  - _Jakub_: I'm interested in looking into this.
* Alternatives to surrogate gradient descent?
- _Danish_:  I use a correlation learning model of synaptic plasticity which could in principle capture timing delays.
* Add a more realistic auditory periphery (cochlear filtering and more realistic spiking model).
  - _Danish_:  I have a simple vertebrate biophysical model of filtering in the auditory periphery which I could quickly test here.
* Number of time steps might be an issue for a more realistic model. May want to use dt=0.1ms and duration>=100ms so more than 1000 time steps.
* Add a more realistic sound localisation task (natural sounds, background noise, multiple sound sources).
  - _Tomas_: experiment with this, starting with multi-frequency sounds
  - _Danish_: I have looked into multi-frequency cochlear filtering for speech localization. It may be useful here.
* Consider multiple architectures, potentially matching the auditory system.
* Consider more complicated neuron models and perhaps make some of these neuron model parameters trainable; for what situations can that help?
  - _Danish_:  I use a correlation learning model of synaptic plasticity which could in principle learn timing and ITD information.
* How to understand what the learned network does?
  - _Helena_:  This is just a warm up, and I am starting with a simple thresholding on the W1W2 plot to improve the contrast. I am going to push file named as SNN_sound_W1W2_threshold_plot.ipynb. I will probably come back to this later. 
* Use regression instead of classification
* Which level of biological realisms does the learning need to comply to? Which observables are available at the synapse as input to a learning rule?
  - _Danish_:  Very interesting question that I would like to explore.
