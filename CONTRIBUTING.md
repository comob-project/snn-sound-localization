# Contributing Guide for the SNN Sound Localization paper

The project for collaborative modelling of the brain grew out of the 2022 Cosyne tutorial. The aim is to work together, openly on a large scale computational brain modelling project.

This is the first project in the community, so the exact workflow for collaboration is still a work in progress.

# Joining the organization

If you're not already a part of the COMOB community, but you want to get involved, you should open a pull request here
with a small contribution. Once an existing member has reviewed your pull request, you’ll be added to the organization.

# Contributing

## Workflow

First, create a new branch from `main`, for example: `your_name/main`. On this branch, create a notebook
for yourself in the `notebooks/` directory. You might name the notebook `notebooks/your_name.ipynb`, for example. You
can essentially do whatever you want in your notebook!

If you have a result which you think is useful for others, or ready to be incorporated into the central research
project, then you should add it to the `spikeloc/` directory and open a pull request to the `main` branch.

## Keeping your branch up-to-date

Since git branches are essentially sequences of commits, it's likely that your personal branch (`your_name/main`) will fall 
behind the commit sequence in the `main` branch. This happens when new commits are added to the main branch.

To keep your branch up-to-date, you should use  `git fetch origin main:main` and `git rebase main` from time to time. The
first command updates your local `main` branch, and the second command incorporates the new `main` commits into your branch,
and then places your commits at the end of the sequence. You shouldn't use `git merge`, because it can lead to
incompatible sequences of commits.

Of course if you need help with any of this, then please ask and someone will help out!

