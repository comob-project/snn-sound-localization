
# How to contribute

Follow these steps to get started.



## 1. Join the community

[**Join the Discord**][1], to chat about the project and follow announcements. 
If you have a question, use [our Q&A forum on GitHub][2].
Participation in the community is subject to our [](Code-of-Conduct.md).

You can check out where others are located in the world, and add yourself, on [this map 🗺][3].

[1]: https://discord.gg/GtdS9tQyU7
<!-- (This discord invite link is never-expiring) -->
[2]: https://github.com/comob-project/snn-sound-localization/discussions/categories/q-a
[3]: https://getethermap.org/m/comob



## 2. Learn about the subject

[**Watch the two videos**][vids] of Dan Goodman's tutorial on spiking neural network (SNN) models.

<!-- The following is MyST syntax to create a collapsible container
    ("Click to show more"). → https://jupyterbook.org/en/stable/interactive/hiding.html
-->
```{admonition} Topics covered in the videos
:class: dropdown

- [**Video 1**][vid1]
  - Spiking neuron models (LIF and more)
  - Intro to the sound localization problem
  - The classic delay line / **coincidence detection** model of sound localization
      - The notebook explained in this part — from 32:40 on — uses a package ([Brian](https://brian2.readthedocs.io/)) that we do not use here.
      This part is still relevant insofar that the introduced concepts are used in the next video and in our project.

- [**Video 2**][vid2]
  - Learning in neural networks, and **surrogate gradient descent** for SNNs.
  - Training an SNN for sound localization using PyTorch.
      - **This part — [from 18:36 on][vid2-nb] — explains our [Starting Notebook](research/Starting-Notebook.ipynb)**.
```
The slides, and links for learning more, are available at the [tutorial website](https://neural-reckoning.github.io/cosyne-tutorial-2022/).

Then, read [](research/Background.md) for a brief introduction to the auditory system and sound localization, and for links to previous modelling work in sound localization.

[vids]: https://www.youtube.com/playlist?list=PL09WqqDbQWHGJd7Il3yVxiBts5nRSxvJ4
[vid1]: https://www.youtube.com/watch?v=GTXTQ_sOxak&list=PL09WqqDbQWHGJd7Il3yVxiBts5nRSxvJ4&index=1
[vid2]: https://www.youtube.com/watch?v=rfck_p0JrIc&list=PL09WqqDbQWHGJd7Il3yVxiBts5nRSxvJ4&index=2
[vid2-nb]: https://youtu.be/rfck_p0JrIc?list=PL09WqqDbQWHGJd7Il3yVxiBts5nRSxvJ4&t=1116



## 3. Pick a research question

Visit [](research/Questions.md) to find inspiration for something you'd like to try out or investigate.

```{margin}
It is hard to say beforehand where research will lead you, so you can of course change this at any time.
```

Edit that page and **add your name to an item**, or add a new item:

```{admonition} How to edit the Questions page
:class: dropdown

On the [](research/Questions.md) page, **via the GitHub logo at the top, click "suggest edit"** (or go there directly using [this link][edit-questions]).
Sign up / log in to GitHub if needed, and edit the markdown text there to add your name / research question.

If you are not already a member of our GitHub organization, GitHub will warn you that "You’re making changes in a project you don’t have write access to."
Make your edit anyway and click the green "Propose changes" button.
This will make a Pull Request to our project. We will merge it, and add you to our GitHub organization.

If you are already a member, you can simply choose "Commit directly to the `main` branch".
```

[edit-questions]: https://github.com/comob-project/snn-sound-localization/edit/main/research/Questions.md



## 4. Work in a notebook

The [](research/Starting-Notebook) contains a basic analysis pipeline.

```{dropdown} Overview of the Starting notebook

- A simple sound localization task is defined, and input/output data for it are generated.
    - The task: given a pure tone that arrives with a delay in one ear, calculate the interaural phase difference (IPD).
- An SNN model is defined, and trained on this data, using surrogate gradient descent.
- The model's performance is analyzed, and its learned weights are visualized.
```

This notebook is a good starting point for your own experiments.
**Duplicate the Starting notebook** and work on your experiment in this copy. You can do this using either Google Colab or a local setup:


```{admonition} How to work with Google Colab ☁
:class: dropdown
On the [](research/Starting-Notebook) page, **via the rocket icon at the top, click "Colab"** (or go there directly via [this link][colab-start-nb]).

For an intro to the Colab interface and its keyboard shortcuts, see [here][colab-help].

To save your changes, use one of the **"Save a copy …"** options in the File menu.
(You can choose either your personal GitHub / GitHub Gists, or your Google Drive).

When you have something ready to share, **'Download' the notebook as an .ipynb file** via the File menu. See the next step for how to share this file and have it appear on this website.

[colab-start-nb]: https://colab.research.google.com/github/comob-project/snn-sound-localization/blob/main/research/Starting-Notebook.ipynb
[colab-help]: https://colab.research.google.com/notebooks/basic_features_overview.ipynb
```


````{admonition} How to work locally 💻
:class: dropdown
<!-- ↑ Four backticks, to handle the nested three-tick code fences. -->

Below are detailed instructions to get set up locally.  
If you are already familiar with such instructions however, the summary is:

1. Install `conda` if it is not already installed.
    - <small>The recommended installer is [miniforge](https://github.com/conda-forge/miniforge#download): it is lean, and is generally faster than installers like Miniconda, as it only uses the `conda-forge` channel by default.</small>
2. Download [the repository](https://github.com/comob-project/snn-sound-localization).
3. Run, in the repo root:
   ```
   $ conda env create -f environment.yml
   $ conda activate spikeloc
   $ jupyter notebook
   ```
4. Make a copy of `research/Starting-Notebook.ipynb` and work in that notebook.

Detailed steps (click to expand):

<!-- Factoring out to external file, as it's quite long -->
```{include} web/content/detailed-installation-steps.md
```
````

Duplicating the starting notebook is a suggestion. You could also do one of the following:

```{dropdown} Other ways to work

- Duplicate another notebook than the 'Starting' one, if you want to build on someone else's work.
- Start from scratch in a new notebook.
- If no code is needed, write a simple markdown file. ('[](research/Background.md)' is an example of this).
- If you prefer scripts to Jupyter Notebooks, upload 1) the script (`.py` file), 2) the generated plots (image files), and 3) a `.md` file that describes the analysis and includes the plots (preferably placed in a subdirectory).
```



## 5. Share your work

When you have some finished work to share: 

1. Rename your notebook file to something reflective of its contents.
    - The notebook's filename (e.g. `Learning-delays.ipynb`) is used to create the URL for your notebook on this website
    - The notebook's title (the markdown in the first cell, e.g. `# Learning delays`)
2. Upload the notebook file to our GitHub repository





## 6. Check out others' work

All our notebooks and research notes appear under the 'Research' rubric to the left.

You can **comment** on notebooks and other pages of this website (even this one, try it out!). Select some text and click 'Annotate'. You'll be prompted to login or sign up for a _Hypothesis_ account, after which you can comment and reply.

Instead of commenting on some specific part ("Annotations"), you can also comment on the entire page ("Page notes"). To do so, click the little sticky note icon in the gray sidebar on the far right of the page. In this sidebar you can also see others' comments.


## 7. Help write the paper

Once the story is clearer, we'll start an Overleaf document and start writing up the paper. If you can, please join in on this! Write the paragraph for your subproject. Comment on the overall flow of the text and improve it, etc.


## ...


<!-- If you are already a member of the [COMOB github organization][1]: simply drag and drop your notebook file into the [`notebooks` directory on github][2].
Choose 'commit directly to the `main` branch' and press the 'Commit changes' button.
The website will be rebuilt automatically, and your notebook should appear on the website when this is done (the website build status can be checked [here][3])

If not, [fork the project, make PR], we'll merge and add you as org member so you can do as above.


pieter test → fork, then upload in your repo (it'll prompt to PR)

what about changes. drag and drop overwrite? yes :)

can colab edit? no. so: File > Download .ipynb > [upload as before]

[1]: https://github.com/comob-project
[2]: https://github.com/comob-project/snn-sound-localization/tree/main/notebooks
[3]: https://github.com/comob-project/snn-sound-localization/actions/workflows/deploy-web.yml -->
