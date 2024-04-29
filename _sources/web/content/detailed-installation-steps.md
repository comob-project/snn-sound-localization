<!-- This is based on https://github.com/neural-reckoning/cosyne-tutorial-2022#run-locally- -->

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

- When the installation was successful, run
  ```
  conda activate spikeloc
  ```
  This makes sure that all future commands ran in this terminal
  will use the installed software.
</details>


<details>
<summary>5. <b>Run the notebook server & duplicate the Starting notebook</b></summary>

- Still in this terminal in the exercise directory,
  with the `spikeloc` conda environment activated, run
  ```
  jupyter notebook
  ```
  After a short while, this should open your browser,
  showing a list of the files in the current directory. 

- Click on the `research/` directory. Tick the checkbox next to `Starting-Notebook.ipynb` and click the 'Duplicate' button.

- Open the newly created `Starting-Notebook-Copy1.ipynb` file by clicking on it.

  Try running some of the cells using `Shift`-`Enter`.
  If no errors appear below these cells: congratulations! The installation was successful.

- Some more information on how to work with a Jupyter Notebook can be found
  e.g. [here](https://realpython.com/jupyter-notebook-introduction/#running-cells).

- When you are done with the notebooks, you can exit the notebook server application
  that is still running in your terminal with `Ctrl`-`C`
</details>
