
# How to contribute

Follow these steps to get started.



# 1. Join the community

[**Join the Discord**][1], to chat about the project and follow announcements. 
If you have any questions, ask them on [our GitHub Discussions page][2].
Participation in the community is subject to our [](Code-of-Conduct.md).

You can check out where others are located in the world, and add yourself, on [this map 🗺][3].

[1]: https://discord.gg/GtdS9tQyU7
<!-- (This discord invite link is never-expiring) -->
[2]: https://github.com/comob-project/snn-sound-localization/discussions
[3]: https://getethermap.org/m/comob



# 2. Get acquainted with the subject

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

Then, read [](research/Background.md) for a brief introduction to the auditory system and sound localization, and for links to previous modelling work in sound localization.

[vids]: https://www.youtube.com/playlist?list=PL09WqqDbQWHGJd7Il3yVxiBts5nRSxvJ4
[vid1]: https://www.youtube.com/watch?v=GTXTQ_sOxak&list=PL09WqqDbQWHGJd7Il3yVxiBts5nRSxvJ4&index=1
[vid2]: https://www.youtube.com/watch?v=rfck_p0JrIc&list=PL09WqqDbQWHGJd7Il3yVxiBts5nRSxvJ4&index=2
[vid2-nb]: https://youtu.be/rfck_p0JrIc?list=PL09WqqDbQWHGJd7Il3yVxiBts5nRSxvJ4&t=1116



# 3. Pick a research question

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



# 4. Work in a notebook

The [](research/Starting-Notebook) contains a basic analysis pipeline.

<details><summary>Overview of the starting notebook</summary>

- A simple sound localization task is defined, and input/output data for it are generated.
    - The task: given a pure tone that arrives with a delay in one ear, calculate the interaural phase difference (IPD).
- An SNN model is defined, and trained on this data, using surrogate gradient descent.
- The model's performance is analyzed, and its learned weights are visualized.
</details><br>

This notebook is a good starting point for you own experiments.

**Duplicate the [](research/Starting-Notebook)** and work on your experiment in this copy, using either Google Colab or a local setup:

```{admonition} How to work with Google Colab ☁
:class: dropdown
On the [](research/Starting-Notebook) page, **via the rocket icon at the top, click "Colab"** (or go there directly via [this link][colab-start-nb]).

For an intro to the Colab interface and its keyboard shortcuts, see [here][colab-help].

To save your changes, use one of the "Save a copy …" options in the File menu.
(You can choose either your personal GitHub / GitHub Gists, or your Google Drive).

When you have something ready to share, **'Download' the notebook as an .ipynb file** via the File menu. See the next step for how to share this file and have it appear on this website.
```

[colab-start-nb]: https://colab.research.google.com/github/comob-project/snn-sound-localization/blob/main/research/Starting-Notebook.ipynb
[colab-help]: https://colab.research.google.com/notebooks/basic_features_overview.ipynb

<!-- _four_ backticks, to handle the nested three-tick code fences. -->
````{admonition} How to work locally 💻
:class: dropdown

Below are detailed instructions to get set up locally.  
If you are already familiar with such instructions however, the summary is:

1. Install `conda` if it is not already installed.
    - <small>The recommended installer is [miniforge](https://github.com/conda-forge/miniforge#download): it is lean, and is generally faster than installers like Miniconda, as it only uses the `conda-forge` channel by default.</small>
2. Download [the repository](https://github.com/comob-project/snn-sound-localization).
3. Run, in the repo root:
   ```
   conda env create -f environment.yml
   conda activate spikeloc
   jupyter notebook
   ```

Detailed steps (click to expand):


<details>
<summary>1. <b>Install Conda</b></summary>

- If you do not have `conda` already installed, download and run 
  the _Miniforge3_ conda installer for your OS over at
  https://github.com/conda-forge/miniforge#download.

- On Windows: in step 5 of the installer ("Advanced Installation Options"),
  tick the checkbox next to "Add Miniforge3 to my PATH environment variable".
  
- On MacOS, Ubuntu, etc, go to 'Terminal' and run `chmod +x` on the downloaded `.sh` file, then run it
  with `./Miniforge3-{os}-{arch}.sh`.

  For Mac, there is also a `.pkg` installer available: a file to download and to install by just double-clicking it.
  Find it [here](https://docs.conda.io/en/latest/miniconda.html#latest-miniconda-installer-links) (_Miniconda_ is similar to Miniforge: they are both lean installers for `conda`).
</details>


<details>
<summary>2. <b>Download the repository</b></summary>

- On [our GitHub](https://github.com/comob-project/snn-sound-localization), at the top of the page, click the green "Code" button, then "Download ZIP".
  Uncompress the downloaded `.zip` to a location of your choosing.

- Alternatively, if you use Git, you can `git clone` the repository
</details>


<details>
<summary>3. <b>Open a terminal in the repository directory</b></summary>

- On Windows, either search the Start menu for the built-in 'Command Prompt', 
  or install the more modern [Windows Terminal](https://github.com/microsoft/terminal#readme)
  from the Microsoft Store ([link](https://www.microsoft.com/store/productId/9N0DX20HK701)).
  
- On MacOS or e.g. Ubuntu, run 'Terminal'.

- To run the commands in the following steps, either type or copy-paste them
  into the terminal, and hit `Enter`.

- After starting the terminal, you can use the `cd` command to point it
  to the exercise directory. For example, if you extracted the `.zip` contents
  to `C:\Users\jane\Desktop`, run
  ```
  cd C:\Users\jane\Desktop\snn-sound-localization-main\`
  ```
  (If you `git clone`d the repository, the directory is just called
  `snn-sound-localization`, without the branch name `-main`).
  
- Alternatively, you can directly open a terminal in the right directory
  using your OS's file explorer (Explorer on Windows, GNOME on Ubuntu, …),
  by right clicking in the directory.
  - If you've installed Windows Terminal or are e.g. on Ubuntu,
    simply select "Open in (Windows) Terminal" from the right-click menu.
  - This is not applicable to vanilla Windows. (You could hold `Shift`
    while right clicking, and then select "Open PowerShell window here",
    but the `jupyter notebook` command below does not work
    by default in PowerShell).
  
- Your final directory should be the one where the `research/` subdirectory and an
  `environment.yml` file are located. Use `ls` (or `dir` in Windows' Command Prompt) to
  see a list of the files in the current directory.
</details>


<details>
<summary>4. <b>Install dependencies</b></summary>

- With your Terminal pointing to the exercise directory, run the following command:
  ```
  conda env create -f environment.yml
  ```
  This will download and install all dependencies.
  It will take a while.
  
- If any errors pop up, retry the command with elevated privileges.
  - On Windows, close the terminal and reopen it with "Run as Administrator".
  - On most other OSes (including MacOS), prepend `sudo` to the command;
    i.e. `sudo conda env create …`, and enter the password when prompted.

- When the installation was succesful, run
  ```
  conda activate spikeloc
  ```
  This makes sure that all future commands ran in this terminal
  will use the installed software.
</details>


<details>
<summary>5. <b>Run the notebook server</b></summary>

- Still in this terminal in the exercise directory,
  with the `spikeloc` conda environment activated, run
  ```
  jupyter notebook
  ```
  After a short while, this should open your browser,
  showing a list of the files in the current directory. 

- Click on the `research/` directory and then on `Starting-Notebook.ipynb` to open it.
  Try running some of the cells using `Shift`-`Enter`.
  If no errors apear below these cells: congratulations! The installation was succesful.

- Some more information on how to work with a Jupyter Notebook can be found
  e.g. [here](https://realpython.com/jupyter-notebook-introduction/#running-cells).

- When you are done with the notebooks, you can exit the notebook server application
  that is still running in your terminal with `Ctrl`-`C`
</details>

````

Duplicating the starting notebook is a suggestion. You could also do one of the following:

<details><summary>Other ways to work</summary>

- Start from scratch in a new notebook
- Duplicate another notebook than the 'Starting' one, if you want to build on someone else's work
- If no code is needed, write a simple markdown file ('[](research/Background.md)' is an example of this).
- If you prefer scripts to Jupyter Notebooks, upload 1) the script (`.py` file), 2) the generated plots (image files), and 3) a `.md` file that describes the analysis and includes the plots (preferably placed in a subdirectory).
</details><br>


# 5. Share your work

[drag and drop]



# 6. Check out others' work

All our notebooks and research notes appear under the 'Research' rubric to the left.

You can **comment** in-situ on notebooks and other pages of this website (even this one, try it out!). Select some text and click 'Annotate'. You'll be prompted to login or sign up for a _Hypothesis_ account, after which you can comment and reply.

You can see others' comments using the far right sidebar.


# 7. Help write the paper


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
