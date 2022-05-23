
# How to contribute

Follow these steps to get started.


## 1. Join the community

[**Join the Discord**][1], to chat about the project and follow announcements. 
If you have any questions, ask them on [our GitHub Discussions page][2].
Participation in the community is subject to our [](Code-of-Conduct.md).

You can check out where others are located in the world, and add yourself, on [this map 🗺][3].


[1]: https://discord.gg/GtdS9tQyU7
<!-- (This discord invite link is never-expiring) -->
[2]: https://github.com/comob-project/snn-sound-localization/discussions
[3]: https://getethermap.org/m/comob



## 2. Get acquainted with the subject

[**Watch the two videos**][vids] of Dan Goodman's tutorial on spiking neural network (SNN) models.

<!-- The following is MyST syntax to create a collapsible container
    ("Click to show more"). → https://jupyterbook.org/en/stable/interactive/hiding.html
-->
```{admonition} Topics covered in the videos
:class: dropdown

[**Video 1**][vid1]
- Spiking neuron models (LIF and more)
- Intro to the sound localization problem
- The classic delay line / **coincidence detection** model of sound localization
    - The notebook explained in this part — from 32:40 on — uses a package ([Brian](https://brian2.readthedocs.io/)) that we do not use here.
    This part is still relevant insofar that the introduced concepts are used in the next video and in our project.

[**Video 2**][vid2]
- Learning in neural networks, and **surrogate gradient descent** for SNNs.
- Training an SNN for sound localization using PyTorch.
    - **This part — [from 18:36 on][vid2-nb] — explains our [Starting Notebook](research/Starting-Notebook.ipynb)**.
```
The slides, and links for learning more, are available at the [tutorial website](https://neural-reckoning.github.io/cosyne-tutorial-2022/).

Then, read [](research/Background.md) for a brief introduction to the auditory system and sound localization, and for links to previous modelling work on sound localization.


[vids]: https://www.youtube.com/playlist?list=PL09WqqDbQWHGJd7Il3yVxiBts5nRSxvJ4
[vid1]: https://www.youtube.com/watch?v=GTXTQ_sOxak&list=PL09WqqDbQWHGJd7Il3yVxiBts5nRSxvJ4&index=1
[vid2]: https://www.youtube.com/watch?v=rfck_p0JrIc&list=PL09WqqDbQWHGJd7Il3yVxiBts5nRSxvJ4&index=2
[vid2-nb]: https://youtu.be/rfck_p0JrIc?list=PL09WqqDbQWHGJd7Il3yVxiBts5nRSxvJ4&t=1116



## 3. Pick a research question

Visit [](research/Questions.md) to find inspiration for something you'd like to try out or investigate.

Edit that page and **add your name to an item**, or add a new item.

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

[colab or local]


## 5. Share your notebook

[drag and drop]


## 6. Check out others' work

All our notebooks and research notes appear under the 'Research' rubric to the left.

You can **comment** in-situ on notebooks and other pages of this website (even this one, try it out!). Select some text and click 'Annotate'. You'll be prompted to login or sign up for a _Hypothesis_ account, after which you can comment and reply.

You can see others' comments using the far right sidebar.


## 7. Help write the paper


# ...


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
