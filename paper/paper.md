---
title: Spiking neural network models of sound localisation via a massively collaborative process
authors:
  - name: Marcus Ghosh
    affiliations:
      - Laboratoire Jean Perrin, Institut de Biologie Paris-Seine, CNRS, Sorbonne Université, Paris, France
      - Department of Electrical and Electronic Engineering, Imperial College London, United Kingdom
    orcid: 0000-0002-2428-4605
    email: mghosh@imperial.ac.uk

  - name: Karim Habashy
    affiliations: 
      - School of Psychological Science, University of Bristol, United Kingdom
    orcid: 0009-0006-2635-129X

  - name: Francesco De Santis
    affiliations:
      - Department of Electronics, Information and Bioengineering, Politecnico di Milano, Milano, Italy
    orcid: 0009-0005-8393-9658
    
  - name: Tomas Fiers
    affiliations: 
      - Department of Data Analysis, Ghent University, Ghent, Belgium
    orcid: 0000-0002-1938-6025

  - name: Dilay Fidan Erçelik 
    affiliations: 
      - Faculty of Brain Sciences, University College London, United Kingdom
    orcid: 0000-0002-9550-5161 

  - name: Balázs Mészáros
    affiliations: 
      - School of Engineering and Informatics, University of Sussex, Falmer, Brighton, United Kingdom
    orcid: 0000-0002-1261-4523

  - name: Zachary Friedenberger
    affiliations:
      - Centre for Neural Dynamics and Artificial Intelligence, University of Ottawa, Ottawa, Ontario, Canada
      - Department of Physics, University of Ottawa, Ottawa, Ontario, Canada
    orcid: 0000-0002-2205-3387

  - name: Gabriel Béna
    affiliations:
      - Department of Electrical and Electronic Engineering, Imperial College London, United Kingdom

  - name: Mingxuan Hong
    affiliations: 
      - Department of Computer Science and Engineering, The Chinese University of Hong Kong, Hong Kong SAR, China
    orcid: 0009-0004-7311-8656 

  - name: Umar Abubacar
    affiliations:
      - COMBYNE lab, University of Surrey, Guildford, United Kingdom
    orcid: 0009-0006-3128-9005 

  - name: Rory T. Byrne
    affiliations: 
      - Department of Electrical and Electronic Engineering, Imperial College London, United Kingdom
      - Department of Engineering, University of Cambridge, United Kingdom
    orcid: 0009-0000-6236-1125 

  - name: Juan Luis Riquelme  
    affiliations:
      - Max Planck Institute for Brain Research, Frankfurt, Germany
      - School of Life Sciences, Technical University of Munich, Freising, Germany
    orcid: 0000-0003-4604-7405

  - name: Yuhan Helena Liu
    affiliations: 
      - Princeton Neuroscience Institute, Princeton University, Princeton, NJ, USA
      - Department of Applied Mathematics, University of Washington, Seattle, WA, USA
    orcid: 0000-0001-7269-8338         

  - name: Ido Aizenbud
    affiliations:
      - Edmond and Lily Safra Center for Brain Sciences (ELSC), The Hebrew University of Jerusalem, Jerusalem 91904, Israel
    orcid: 0009-0006-6855-567X

  - name: Brendan A. Bicknell  
    affiliations: 
      - Gatsby Computational Neuroscience Unit, University College London, London, UK 
    orcid: 0000-0002-2307-2109

  - name: Volker Bormuth
    affiliations: 
      - Laboratoire Jean Perrin, Institut de Biologie Paris-Seine, CNRS, Sorbonne Université, Paris, France

  - name: Alberto Antonietti
    affiliations:
      - Department of Electronics, Information and Bioengineering, Politecnico di Milano, Milano, Italy
    orcid: 0000-0003-0388-6321

  - name: Dan F. M. Goodman
    affiliations:
      - Department of Electrical and Electronic Engineering, Imperial College London, United Kingdom
    orcid: 0000-0003-1007-6474

license: CC-BY-4.0
export:
  - format: docx
  - format: tex
    template: lapreprint
  - format: pdf
    id: paper
    template: lapreprint-typst
downloads:
  - id: paper
    title: Download Paper
---

% Add your name, affiliations, etc. at the top of the authors list


+++ {"part": "abstract"}
Neuroscientists are increasingly initiating large-scale collaborations which bring together tens to hundreds of researchers. However, while these projects represent a step-change in scale, they retain a traditional structure with centralised funding, participating laboratories and data sharing on publication. Inspired by an open-source project in pure mathematics, we set out to test the feasibility of an alternative structure by running a grassroots, massively collaborative project in computational neuroscience. To do so, we launched a public Git repository, with code for training spiking neural networks to solve a sound localisation task via surrogate gradient descent. We then invited anyone, anywhere to use this code as a springboard for exploring questions of interest to them, and encouraged participants to share their work both asynchronously through Git and synchronously at monthly online workshops. At a scientific level, our work demonstrates how a range of biologically-relevant parameters, from time delays to membrane decays and levels of inhibition, impact sound localisation in networks of spiking units. At a more macro-level, our project brought together 35 researchers from multiple countries, provided hands-on research experience to early career participants, and opportunities for supervision and teaching to later career participants. Looking ahead, our project provides a glimpse of what open, collaborative science could look like and provides a necessary, tentative step towards it.  
+++

# Introduction

```{include} sections/intro.md
```

(metascience)=
# Towards open collaborative science 

```{include} sections/meta_science.md
```

(science)=
# Training SNNs for sound localisation

```{include} sections/science.md
```

(discussion)=
# Discussion

```{include} sections/discussion.md
```

# Contributors

```{include} sections/contributor_table.md
```

# Notebook map

```{include} sections/notebook_map.md
```

(appendices)=
# Appendices

In this section, each subsection is the detailed results as written up by the author of those results.

```{include} sections/basicmodel/basicmodel.md
```

```{include} sections/TCA/analysis.md
```

```{include} sections/new_inh_model/inhibition_model.md
```

```{include} sections/delays/Delays.md
```

# Funding and Acknowledgements

* MG is supported by Schmidt Sciences, LLC. Previously, MG was a Fellow of Paris Region Fellowship Program - supported by the Paris Region, and funding from the European Union's Horizon 2020 research and innovation program under the Marie Skłodowska-Curie grant agreement No 945298-ParisRegionFP.  
* FS and AA work is fully funded by the project “EBRAINS-Italy (European Brain ReseArch INfrastructureS-Italy),” granted by the Italian National Recovery and Resilience Plan (NRRP), M4C2, funded by the European Union –NextGenerationEU (Project IR0000011, CUP B51E22000150006, “EBRAINS-Italy”).
* DFE is funded by the SURF programme (undergraduate research fellowship) from the Simons Foundation (SCGB). 
* DFE and BAB acknowledge the use of the UCL Myriad High Performance Computing Facility (Myriad@UCL), and associated support services, in the completion of this work.
* ZF is funded by a NSERC PGS-D Scholarship. 
* BM is funded by the be.AI Leverhulme Doctoral Scholarships (Leverhulme Trust).
* UA is supported by the UK Engineering and Physical Sciences Research Council (EPSRC) DTP Studentship 2753922 for the University of Surrey.
* JLR was funded by the Max Plank Society. 
* YHL is supported by NSERC PGS-D, FRQNT B2X, and Pearson Fellowship.
* VB is supported by the European Research Council (ERC) under the European Union's Horizon 2020 research innovation program, grant agreement number 715980.