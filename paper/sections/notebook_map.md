The following lists the notebooks, authors, summary and related notebooks in this project.

% this will only appear on the online version, not in the printed version

```{mermaid}
flowchart LR
    SN[Starting Notebook] --> FF[Filter-and-Fire Neuron Model]
    Dale --> QS[Quick Start Notebook]
    Tau --> QS
    SN --> AON[Altering Output Neurons]
    ATN --> AW[Analysing trained networks - workshop edition]
    SN --> Dale[Sound localisation following Dale's law]
    SN --> DThr[Dynamic threshold]
    SN --> Exc[Sound localisation using excitatory-only inputs]
    SN --> DDL[Learning delays]
    SN --> DCLS[Dilated Convolution with Learnable Spacings]
    SN --> Rob[Robustness to Noise and Dropout]
    SN --> V250[Version with 250 Hz Input]
    SN --> ATN[Analysing trained networks]
    SN --> Tau[Optimizing the membrane time constant]
    subgraph Minimal trainable model
        Tau --> AnTau[Analysing solutions for different time constants]
        V250 --> AnTau
        ATN --> AnTau
    end
    subgraph Learning delays
        DDL
        DCLS
    end
    subgraph Alternative neuron models
        FF
        Dale
        DThr
    end
```

## Introductory notebooks

[](../research/1-Background.md)
    : Explanation of the background. (Author: Dan Goodman.)

[](../research/2-Questions.md)
    : List of research questions and challenges. (Author: everyone.)

## Templates / starting points

[](../research/3-Starting-Notebook.ipynb)
    : The template notebook suggested as a starting point, based on the [Cosyne tutorial](https://neural-reckoning.github.io/cosyne-tutorial-2022/) that kicked off this project. (Author: Dan Goodman.)

[](../research/4-Quick_Start.ipynb)
    : Condensed version of [](../research/3-Starting-Notebook.ipynb) using the shorter membrane time constants from [](../research/Optimizing-Membrane-Time-Constant.ipynb) and Dale's law from [](../research/Dales_law.ipynb). (Author: Dilay Fidan Erçelik, Karim Habashy, Marcus Ghosh.)  

## Individual notebooks

[](../research/Alt-Filter-and-Fire_Neuron_Model_SNN.ipynb)
    : Using an alternative neuron model. (Author: Ido Aizenbud based on work from Dilay Fidan Erçelik.)

[](../research/Altering_output_neurons.ipynb)
    : Comparison of three different ways of reading out the network's decision (average membrane potential, maximum membrane potential, spiking outputs) with short and long time constants. (Author: Mingxuan Hong.)

[](../research/Analysing-Trained-Networks-Part2.ipynb)
    : Group project from an early workshop looking at hidden unit spiking activity and single unit ablations. Found that some hidden neurons don't spike, and ablating those does not harm performance. Builds on [](../research/Analysing-Trained-Networks.ipynb). (Author: Gabriel Béna, Josh Bourne, Tomas Fiers, Tanushri Kabra, Zekai Xu.)

[](../research/Dales_law.ipynb)
    : Investigation into the results of imposing Dale's law. Incorporated into [](../research/4-Quick_Start.ipynb). Uses a fix from [](../research/IE-neuron-distribution.ipynb). (Author: Marcus Ghosh, Gabriel Béna, Jose Gomes.)

[](../research/Dynamic_threshold.ipynb)
    : Adds an adaptive threshold to the neuron model and compares results. Conclusion is that the dynamic threshold does not help in this case. (Author: Mingxuan Hong.)

[](../research/Excitatory-only-localisation.ipynb)
    : Results of imposing an excitatory only constraint on the neurons. Appears to find solutions that are more like what would be expected from the Jeffress model. (Author: TODO who is luis-rr???.)

[](../research/Learning_delays.ipynb), [](../research/Learning_delays_major_edit2.ipynb) and [](../research/Solving_problem_with_delay_learning.ipynb)
    : Delay learning using differentiable delay layer, written up in [](#learning-delays) (Author: Karim Habashy.)

[](../research/Quick_Start_Delay_DCLS.ipynb)
    : Delay learning using Dilated Convolution with Learnable Spacings, written up in [](#learning-delays). (Author: Balázs Mészáros.)

[](../research/Noise_robustness.ipynb)
    : Test effects of adding Gaussian noise and/or dropout during training phase. Conclusion is that dropout does not help and adding noise decreases performance. (Author: TODO: Who is a-dtk???.)

[](../research/Quick_Start_250HzClassification.ipynb), [](../research/Quick_Start_250HzClassification_CleanVersion.ipynb)
    : Analysis of results with a higher frequency input stimulus and different membrane time constants for hidden and output layers. Conclusion is that smaller time constant matters for hidden layer but not for output layer. (Author: Dilay Fidan Erçelik.)

[](../research/time-constant-solutions.ipynb)
    : Deeper analysis of strategies found by trained networks as time constants vary. Added firing rate regularisation. Extends [](../research/Optimizing-Membrane-Time-Constant.ipynb). Written up in more detail in [](#basic-model). (Author: Dan Goodman.)

[](../research/Workshop_1_Write_Up.md)
    : Write-up of what happened at the first workshop. (Author: Marcus Ghosh.)

## Inconclusive

The following notebooks did not reach a solid conclusion.

[](../research/Compute-hessians-jax-version.ipynb)
    : An unfinished attempt to perform sensitivity analysis using Hessian matrices computed via autodifferentiation with the Jax library. (Author: Adam Haber.)

[](../research/Quick_Start_random.ipynb)
    : Analysis of an alternative way of handling noise. (Author: Balázs Mészáros.)

[](../research/SNN_sound_W1W2_threshold_plot.ipynb)
    : Unfinished attempt to improve analysis code. (Author: Helena Yuhan Liu.)

## Historical

This subsection includes notebooks whose content got merged into an updated notebook later.

[](../research/Analysing-Trained-Networks.ipynb)
    : Early work on analysing the strategies learned by trained networks. Folded into [](../research/Analysing-Trained-Networks-Part2.ipynb). (Author: Dan Goodman.)

[](../research/Optimizing-Membrane-Time-Constant.ipynb)
    : Analyses how performance depends on membrane time constant. Folded into [](../research/time-constant-solutions.ipynb). (Author: Zach Friedenberger, Chen Li, Peter Crowe.)

[](../research/IE-neuron-distribution.ipynb)
    : Fixed a mistake in an earlier version of [](../research/Dales_law.ipynb). (Author: Sara Evers.)
