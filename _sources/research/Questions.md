
# Questions & challenges


## Modelling questions / aims

Starting point:

* What are the best strategies for localising sounds with a spiking neural network?
* Can we train networks end-to-end to perform as well or better than hand-crafted solutions?
* Can we understand what these trained networks are doing in a high level way?
  - _Dan_: I'm going to try out a few ideas for this.
* Do these networks do something similar to what has been proposed in the literature (labelled line models, hemispheric models, pattern match decoders) or something completely different?
  - _Lavinia_: I'm interested into looking at this (how spiking neural networks can be used to model observed neural representations).
* Do different optimal models emerge in different parameter regimes (head size, signal to noise ratio, multiple sound sources)?
* How do the results depend on the neuron model and available dynamics? For example, does adaptation matter and in which conditions?
  - _Alberto_: I'm interested into looking at this (neuron and synapse model, plasticity). 


## Technical challenges

* Delay learning: can we train delays with surrogate gradient descent?
* Alternatives to surrogate gradient descent?
* Add a more realistic auditory periphery (cochlear filtering and more realistic spiking model).
* Number of time steps might be an issue for a more realistic model. May want to use dt=0.1ms and duration>=100ms so more than 1000 time steps.
* Add a more realistic sound localisation task (natural sounds, background noise, multiple sound sources).
  - _Tomas_: experiment with this, starting with multi-frequency sounds
* Consider multiple architectures, potentially matching the auditory system.
* Consider more complicated neuron models and perhaps make some of these neuron model parameters trainable; for what situations can that help?
* How to understand what the learned network does?
* Use regression instead of classification
* Which level of biological realisms does the learning need to comply to? Which observables are available at the synapse as input to a learning rule?
