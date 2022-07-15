# Workshop 1 Write-up 

08.07.2022   
Organised by Marcus Ghosh (France, Postdoc)

## Introduction 
Our first workshop brought together 16 researchers (undergraduates, doctoral students and postdocs) from 7 countries! We started the day by discussing ideas for the project and what work people had already commited to the repository. Our ideas fell into roughly four themes: time constants, Dale's law, learning delays and analysing trained networks, so we created these breakout rooms and allowed everyone to join their team of interest. In most teams one person shared their screen and wrote code, while the rest of team provided ideas / input and read relevant literature.Below are some notes on each teams work, and our cross-team discussion at the end of the day.  

## Teams 
### Time Constants 
#### Members 
Chen Li (UK, Manchester)  
Rory Byrne (UK, Masters)    
Zachary Friedenberger (Canada, PhD)   

#### Questions
1. How do membrane time constants affect network performance? 
2. If we train the membrane time constants - what distribution emerges?   
3. Do heterogenous time constants improve performance?   
4. What happens if we allow seperate time constant per layer?  

#### Results
1. Model performance decreases as the membrane time constant increases 
2. Performance seemed to increase with small output unit time constants too  
3. Code to train the membrane time constants seemed to be working   

#### References 
https://www.nature.com/articles/s41467-021-26022-3 

### Dale's Law  
#### Members 
Bena Gabriel (UK, PhD)   
Jose Gomes (Portugal, PhD)  
Peter Crowe (Germany, Undergraduate)  

#### Questions 
1. Can networks with only positive weights learn the task? 
2. If we implement Dale's law (i.e. units can only have positive or negative output connections weights) - how does performance change as a function of the ratio of excitatory:inhibitory units? 

#### Results
1. Wrote code to enforce Dale's law and change the ratio of excitatory:inhibitory units 
2. Preliminary results suggest this is a promising direction to explore! 

#### References 
https://www.biorxiv.org/content/10.1101/2020.11.02.364968v2 

### Learning delays 
#### Members 
Karim Habashy (Germany, PhD)  
Leonidas Richter (Germany, PhD)  

#### Questions
1. With a random weight matrix - can you solve the task by just learning input delays?
2. With a bit of weight pretraining - can you improve performance by learning input delays?

#### Results
1. Learning the input delays didn't seem to improve performance, but we discussed how a surrogate gradient-esq trick could help with this in future. 
    
### Analysing trained networks 
#### Members 
Gabryel Mason-Williams (UK, Undergraduate)  
Josh Bourne (UK, Masters)  
Tanushri Kabra (India, Masters)  
Tomas Fiers (UK, PhD)  
Zekai Xu (UK, Undergraduate)      

#### Questions
1. How can we interpret the spiking activity of trained networks? 
2. Is it helpful to rank unit's importance (by the impact of ablation on task performance)?  

#### Results
1. Only some hidden units spike - ablating those degrades performance, while ablating the others does not  
2. Hidden units seem continuously tuned to the input angles 
3. Smaller networks (2 or 7 hidden units, as opposed to 30) worked significantly better than chance, but not as well as the larger networks 

#### Next steps
Train networks until convergence   
Test the impact of dropout (drop units or connections)  
Regularize network spiking (e.g. using a lower and upper bound)  

#### Discussion 
Before lunch and at the end of the day we regrouped to share our progress. For the latter discussion we were joined by Alessandro Galloni (USA, Postdoc) and Boris Marin (Brazil, Assistant Professor).  

Based on results from the time constants team, we agreed that we should all use a shorter time constant when training the networks and there was a general consensus that we should base our analysis on networks trained until convergence. We agreed that the breakout room format worked well (though 5 may be a resonable limit on team size), and were pleased to hear that those not coding themselves learnt a lot from following along. Looking ahead we decided that we should meet on a monthly basis (starting in September) and agreed that a local meetup format would be great. Ideas for future work included: conductance-based synpases, heterogeneity (e.g. activation functions) and work on a reinforcement learning version of the task. 

