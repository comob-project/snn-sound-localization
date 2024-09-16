---
title: Spiking neural network models of sound localisation via a massively collaborative process
authors:
  - name: Anonymous Anonymous
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
Neuroscientists are increasingly initiating large-scale collaborations which bring together tens to hundreds of researchers. However, while these projects represent a step-change in scale, they retain a traditional structure with centralised funding, participating laboratories and data sharing on publication. Inspired by an open-source project in pure mathematics, we set out to test the feasibility of an alternative structure by running a grassroots, massively collaborative project in computational neuroscience. To do so, we launched a public Git repository, with code for training spiking neural networks to solve a sound localisation task via surrogate gradient descent. We then invited anyone, anywhere to use this code as a springboard for exploring questions of interest to them, and encouraged participants to share their work both asynchronously through Git and synchronously at monthly online workshops. At a scientific level, our work investigated how a range of biologically-relevant parameters, from time delays to membrane time constants and levels of inhibition, could impact sound localisation in networks of spiking units. At a more macro-level, our project brought together 31 researchers from multiple countries, provided hands-on research experience to early career participants, and opportunities for supervision and teaching to later career participants. Looking ahead, our project provides a glimpse of what open, collaborative science could look like and provides a necessary, tentative step towards it.  
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

(contributors)=
# Contributors

Removed for double blind.

# Notebook map

```{include} sections/notebook_map.md
```

(appendices)=
# Appendices

In this section, we provide detailed write-ups of our scientific results.

```{include} sections/basicmodel/basicmodel.md
```

```{include} sections/TCA/analysis.md
```

```{include} sections/delays/Delays.md
```

%```{include} sections/filter_and_fire_model/filter_and_fire.md
%```

```{include} sections/new_inh_model/inhibition_model.md
```

# Funding and Acknowledgements

