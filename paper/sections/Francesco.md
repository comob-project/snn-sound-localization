# Contralateral glycinergic inhibition as key factor in creating ITD sensitivity

# Intro
Why a more biological inspired model? 
- Existance of both ITDs and ILDs for azimuthal sounds localization
- Jeffress model existance in mammals is not plausible: 3 main critical issues
  - axonal delay lines absence in mammalian MSO
  - contralateral inhibition role not considered in Jeffress
  - peaks of MSO responses outside physiological range: slopes as the encoding part of the curves
- Evolutionary history reasons explaining why inhibition strategy for ITDs-coding in MSO could be more plausible

<details>
  <summary>Introduction Text (from which to draw in writing the overall Introduction paragraph)</summary>
For the vast majority of animals, sound localization is realized through two classes of hidden acoustic cues: binaural cues and spectral cues. In humans, binaural cues alone are sufficient to discriminate azimuth angle between 0-180 degrees, whereas psychoacoustic evidence has showed how spectral cues have a role in the solution of front-back ambiguities and in angle recognition along the vertical plane (i.e. elevation angles).
Focusing on binaural cues, the two main signals exploited by different animals in creating an acoustic spatiality are interaural time and level differences (ITDs and ILDs). Their role and their dominance over each other depend mainly on animal head size and hearing range in terms of frequencies. 
It is clear at first glance how ITDs assume significant values for species with large head sizes while being much smaller, and so much harder to neuronally encode, for smaller animals. ILDs on the other hand occur when the wavelength of the sound stimulus is shorter than the size of the animal's head, which then generates a significant attenuation at the contralateral ear. For this reason, ILDs significance with respect to ITDs is greater in smaller animals with a middle ear specialised for the transmission of high frequencies. 
These data soon led to the conclusion that in humans, whose audible range is centred on lower frequencies than in other mammals, the ITD was the main binaural cue in discriminating different azimuth angles. For this reason, the most important model that attempts to explain human sound localization, namely the Jeffress Model [1. Jeffress], only takes ITDs into account and proposes a theoretical circuit consisting of axonal delay lines at the level of the brainstem that can create this type of sensitivity. For many years, Jeffress's remained the most accepted proposal, given the discovery of axonal lines potentially similar to those theorised by Jeffress in the Nucleo Laminaris (NL) of different bird species [Yin 2019]. However, the presence of similar delay lines in the mammalian nucleus called the medial superior olive (MSO), within the superior olivary complex and analogous to the avian NL, has never been demonstrated [Groethe 2010]. Furthermore, there are other critical issues in the Jeffress model: several recent studies suggested that synaptic inhibition coming from the contralateral ear could have a main role in processing ITDs in the MSO, as it does for the sensitivity to ILDs in the contiguous nucleus of the lateral superior olive (LSO). Experiments have also highligted how the characteristic delay (CD) values (the peaks in the ITD function) in mammalian MSO are placed beyond the physiological range in many species, that coincides with the potential range of interaural time differences dictated by the subject head size [Groethe 2010]. Positioning the CDs at long ITD values increases the sensitive slope of the function centered on 0 μs ITDs, where the greatest ITD discrimination is required. This factor would then lead to the assumption that the encoding of different positions in space does not happen with the peaks, but exploits instead different slopes of the firing rate curves. This coding strategy stands in contrast to the Jeffress labeled line arrangement, in which spatial positions are encoded by the peak activity of only a few identified units within an array of heterogeneously (in terms of CD) neurons. Eventually, another study also shown how the values of the ITD peaks did not vary according to the different head size as might be expected. 
In the pivotal study of our work [Groethe 2014], Groethe et al. support the thesis that the neuronal structures of sound localization depend on the evolutionary history of the specific species in question. The original binaural cue used by the ancestor of that species at the time of inner ear development is in fact a key factor in determining the neural strategy currently applied in coding the binaural cues. For this reason, humans and all other large mammals may have very different structures than birds for encoding ITDs, because whereas the latter derive from large archosaurs with low-frequency hearing, in which ITD was already the main binaural cue, the former derive from early mammals, which had smaller dimensions and ILDs as a central cue in shaping acoustic spatiality.
Thus, the strategy we tried to validate in our computational model stands as an alternative to the Jeffress model with regard to the analysis of ITDs. It is more grounded in the neural circuits actually observed in the mammalian brainstem and it has glycinergic inhibition from the contralateral ear as its main actor, in a  way similar to the creation of ILD sensitivity in the lateral superior olive (LSO).
</details>

# Methods
The network was mainly developed in Python using the NEST Simulator framework. Inspired by the neurophysiological data, we implemented a complex spiking neural network composed of more than 170,000 spiking units. The different neuronal populations composing the brainstem circuit and their interconnections are depicted in Figure 1. 

![model_map1](https://github.com/francescodesantis/snn-sound-localization/assets/96658597/2a9a3283-e92b-4e37-95f7-3f1d3a88dc28)
**Figure 1** - The end-to-end system with the network diagram

The principal inputs to the network are the spectrogram of a sound stimulus arriving at both ears and the azimuth angle from which univocal values of ITD and ILD are computed. With regards to the spectrogram, we covered the whole human audible range of sound between a minimum frequency of 20 Hz and a maximum of 20 kHz. We subdivided it into 3500 channels since this value is the most likely estimate of the number of inner hair cells (IHCs) present in the human cochlea. With the intent to mimic the physiological distribution of IHCs along the basilar membrane, the width of each frequency channel was not constant throughout the range but grew exponentially. Once an azimuth angle was set, the value of ITD was calculated considering the interaural path difference, which is the difference between the paths traveled by the sound starting from the source and arriving at the two ears, and dividing it by the speed of sound in air (i.e., 330 m/s). For ILDs, a maximum attenuation of 2 dB was provided to the ear contralateral to the origin of the sound for azimuth angles of ±90°. 

Two different strategies were used to model the principal cells of LSO and MSO. Regarding the LSO, the number of cells was kept equal to that of GBCs. For the MSO, on the other hand, a battery of ten neurons was created for each frequency channel. These neurons have the same physiological characteristics and inputs, i.e., an excitation from the ipsi and contralateral SBCs and a dominant inhibition from the contralateral GBCs. The parameter that has been differentiated between the units of a battery is only the synaptic weight of inhibition, which takes values ranging from -2 to -24 nS. The aim is, in fact, to have different slopes and distinct values in the responses of MSO neurons for different azimuth angles so that each neuron can code for the entire physiological range of ITD, as described by the two-channels model. 
All neuronal populations just described, with the exception of ANFs, were modeled with the iaf_cond_alpha, an implementation of a spiking neuron in NEST using integrate-and-fire dynamics with conductance-based synapses.

For the validation of the complete brainstem network, comprising both LSO and MSO of both sides, sound stimuli with a frequency of 100 Hz and 1 s duration from different spatial positions were tested. Specifically, we gave the model azimuth angles ranging from -90° to +90° with an interval of 10°. Once the data about the firing rate response of the four nuclei had been obtained, we proceeded to interpolate them with quadratic polynomials. Then, the actual test was carried out by stimulating the network at different azimuth angles and saving the firing rate values of the two LSOs (left and right) and of the ten neurons comprising the two batteries of neurons of both MSOs. These responses were then used with the interpolations to obtain sound source angle predictions.
Finally, six different configurations were tested, consisting in:
1. the predictions obtained using the information given by the value of the response averaged over both LSOs;
2. the predictions obtained using only the LSO contralateral to the stimulus, e.g., the right LSO for azimuth angles in [-90°, 0°];
3. the prediction obtained by mediating the result of the two MSOs. The prediction of each MSO was obtained in turn by averaging the predictions made by each neuron in the battery;
4. the predictions obtained using only the response of the MSO contralateral to the stimulation;
5. the predictions obtained by considering both LSOs and both MSOs;
6. the predictions mediated only on the LSOs and MSOs contralateral to the stimulus.
   
The results of each of these six configurations were then quantified by calculating the root mean square error (RMSE) expressed in degrees and the Pearson correlation coefficient R between the real and predicted angles.

# Results

As the first result concerning the spiking activity of brainstem neural populations, a refinement of phase locking was obtained at the level of the spherical and globular bushy cells, which then exhibited a behavior faithful to their biological counterparts. 

With regard to the LSO, the responses in terms of firing rate following stimulation with different pure tones (i.e., with different CFs) presented the desired subtraction process described, regardless of the stimulation CF, as depicted in Figure 2. 

![LSO1](https://github.com/francescodesantis/snn-sound-localization/assets/96658597/428de33c-d5fb-405f-b44e-949f701374fa)
**Figure 2** - Firing rates and spike trains of left and right LSO populations after different stimoulus frequencies.

Indeed, the nuclei on both sides show low response values for stimuli from contralateral azimuth angles, with a minimum at +90° for the left LSO and at -90° for the right LSO. This is due to the greater strength and speed of inhibition compared to ipsilateral excitation.

Considering the right LSO, for sake of simplicity, when the sound arrives from a source placed at -90°, the contralateral ear (left) receives sounds earlier and more intensely than the ipsilateral ear (right). As the azimuth angle proceeds toward 0° (frontal position), the firing rate increases while maintaining a constant slope. This steep segment is the most informative part of the right LSO response curve, as a high sensitivity to changing input azimuth angles is guaranteed. Once past 0°, the firing rate ceases to increase steadily, and the response flattens out to high rate values. Here, the ipsilateral (right) excitation dominates due to positive ITD and ILD with respect to the contralateral ear.

Regarding the MSO, at the microscopic level, inhibition of increasing strength leads to an increasing reduction of the membrane potential in the principal cells. In detail, small inhibitory weights delay the spike instant of the cell and then altogether abolish the potential spike when they take larger values, keeping the membrane potential below the threshold, as depicted in Figure 3.


![inhibition7](https://github.com/francescodesantis/snn-sound-localization/assets/96658597/43aa94a4-1848-4320-8477-3cc709f00af0)\
**Figure 3** - Trend of the membrane potential of two cells belonging to the same battery (same CF) showed on a single period during a pure tone stimulation at 100 Hz at 0° and duration of 100 ms. The inhibitory post-synaptic potential (IPSP) leads to a shift and then, for larger weights, to the cancellation of the neuron spike. As in [2], the contralateral IPSP is fast and anticipates both the ipsilateral and the contralateral excitatory post-synaptic potentials.

On the other hand, on a global level, by evaluating the firing rate of an entire battery of principal cells for different locations we first noticed that only five neurons out of the ten that made up a battery had a significant firing rate, while in the five that received stronger inhibitory synapses from the contralateral side (i.e., weight from -12 to -24 nS) the number of spikes during the entire simulation was too low or even null. The trend in the responses of the first five neurons is similar to that of the LSO, with a steeper and more informative positive slope for contralateral stimuli (Figure 4). 

![mso5](https://github.com/francescodesantis/snn-sound-localization/assets/96658597/4900480c-eba9-4d56-b5ae-9adafa29c43d)\
**Figure 4** - Normalised responses of the first five neurons of the MSO batteries of both sides. Normalisation was obtained by dividing the firing rate of each neuron composing the battery by the maximum attained by spanning all the different azimuth angles. The shaded area corresponds approximately to the physiological range of ITD in the human context.

On the other hand, for ipsilateral angles, we can observe a second (negative) slope, less steep than the previous one but still potentially more informative than the plateau found in the same region for LSO curves (\ref(Figure 2)).

The predictions of the entire brainstem network for the different azimuth angles and for the different configurations tested are described by the RMSE, R, and its pvalue presented in Table 1. 

| Configuration: | 1           | 2           | 3           | 4           | 5           | **6**            |
|----------------|-------------|-------------|-------------|-------------|-------------|--------------|
| RMSE           | 19.297 deg  | 11.527 deg  | 21.397 deg  | 18.072 deg  | 15.777 deg  | **11.06 deg**    |
| R              | 0.947       | 0.979       | 0.948       | 0.961       | 0.961       | **0.983**        |
| p value        | 9.578*10<sup>-7</sup> | 5.891*10<sup>-9</sup> | 8.782*10<sup>-7</sup> | 1.695*10<sup>-7</sup> | 1.944*10<sup>-7</sup> | **1.658*10<sup>-9</sup>** |\

**Table 1** - Comparison of performance between the six configurations. In bold, the best performance.

The first important result that can be deduced from these data concerns the improvement in the overall network performance when integration is made between the LSO and the MSO. Both in the case of configuration "5" compared to "3" and "1", and in the case of "6" compared with "4" and "2", a meaningful improvement in performance was found. This result, therefore, validates the existence of a dual pathway in the mammalian brainstem, in which both binaural cues (ITD and ILD) play an essential role in the accurate recognition of the position in the horizontal plane of a sound stimulus. A second observation can be made about using information from both ipsilateral and contralateral nuclei (configurations "1", "3", and "5") compared to the exploitation of the contralateral nucleus only (configurations "2", "4", and "6"). The information given only by the LSO and MSO contralateral to the input sound stimulus, without integrating the one coming from the ipsilateral ones, improves the model’s performance (Figure 5).

![6](https://github.com/francescodesantis/snn-sound-localization/assets/96658597/c12ccd0e-9bd8-4d6c-8463-009a52da1a16)\
**Figure 5** - Model’s results for configuration "6", in which predictions are obtained by considering only LSO and MSO contralateral to
the stimulus. The results were obtained with an input tone of 100 Hz and a duration of 1 s for different azimuth angles.

The results obtained show how the role of fast and dominant inhibitory inputs to the LSO and MSO can be crucial in distinguishing between different azimuth angles.
The spiking neural network implementation of the brainstem also demonstrated how the encodings of different ITDs do not necessarily have to be generated by the activity peaks of different cells in the MSO but, on the contrary, they can be coded by the slope in the response firing rates within the range of physiological ITDs. Furthermore, this work has shown how the integration of information from LSO and MSO allows for more accurate localizations than the responses of the two nuclei taken individually, at least for pure tones of 100 Hz frequency.
