---
title: Spiking neural network models of sound localisation via a massively collaborative process
authors:
  - name: Marcus Ghosh
    affiliations:
      - Imperial College London
    orcid: 0000-0002-2428-4605
    email: mghosh@imperial.ac.uk

  - name: Karim Habashy
    affiliations: 
      - University of Bristol

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
      - University College London

  - name: Balázs Mészáros
    affiliations: 
      - School of Engineering and Informatics, University of Sussex, Falmer, Brighton, United Kingdom
    orcid: 0000-0002-1261-4523

  - name: Zachary Friedenberger
    affiliations:
      - University of Ottawa
    orcid: 0000-0002-2205-3387

  - name: Gabriel Béna
    affiliations:
      - Imperial College London

  - name: Jose Gomes
    affiliations:
      - University of

  - name: Mingxuan Hong
    affiliations: 
      - University of

  - name: Rory Byrne
    affiliations: 
      - Imperial College London

  - name: Helena Yuhan Liu
    affiliations: 
      - University of Washington       

  - name: Sara Evers 
    affiliations:
      - Sorbonne University

  - name: Ido Aizenbud
    affiliations:
      - Edmond and Lily Safra Center for Brain Sciences (ELSC), The Hebrew University of Jerusalem, Jerusalem 91904, Israel
    orcid: 0009-0006-6855-567X

  - name: Brendan Bicknell  
    affiliations: 
      - University College London

  - name: Volker Bormuth
    affiliations: 
      - Sorbonne University

  - name: Alberto Antonietti
    affiliations:
      - Department of Electronics, Information and Bioengineering, Politecnico di Milano, Milano, Italy
    orcid: 0000-0003-0388-6321

  - name: Dan F. M. Goodman
    affiliations:
      - Imperial College London
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
Neuroscientists are increasingly initiating large-scale collaborations which bring together tens to hundreds of researchers. However, while these projects represent a step-change in scale, they retain a traditional structure with centralised funding, participating laboratories and data sharing on publication. Inspired by an open-source project in pure mathematics, we set out to test the feasibility of an alternative structure by running a grassroots, massively collaborative project in computational neuroscience. To do so, we launched a public Git repository, with code for training spiking neural networks to solve a sound localisation task via surrogate gradient descent. We then invited anyone, anywhere to use this code as a springboard for exploring questions of interest to them, and encouraged participants to share their work both asynchronously through Git and synchronously at monthly online workshops. At a scientific level, our work demonstrates how a range of biologically-relevant parameters, from time delays to membrane decays and levels of inhibition, impact sound localisation in networks of leaky-integrate-and-fire units. At a more macro-level, our project brought together 35 researchers from multiple countries, and provided hands-on research experience to early career participants and opportunities for supervision and leadership development to later career participants. Looking ahead, our project provides a glimpse of what open, collaborative science could look like and provides a necessary, tentative step towards it.  
+++

# Introduction

```{include} sections/intro.md
```

# Towards open collaborative science 

```{include} sections/meta_science.md
```

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

# Appendices

In this section, each subsection is the detailed results as written up by the author of those results.

```{include} sections/basicmodel/basicmodel.md
```

```{include} sections/new_inh_model/inhibition_model.md
```

```{include} sections/delays/Delays.md
```

# Funding and Acknowledgements

* FS and AA work is fully funded by the project “EBRAINS-Italy (European Brain ReseArch INfrastructureS-Italy),” granted by the Italian National Recovery and Resilience Plan (NRRP), M4C2, funded by the European Union –NextGenerationEU (Project IR0000011, CUP B51E22000150006, “EBRAINS-Italy”).
* BM is funded by the be.AI Leverhulme Doctoral Scholarships (Leverhulme Trust).
