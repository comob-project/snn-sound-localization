# Contributing guide

Here's how we're currently organizing contributions, although note that this is the first project in the community, so the exact workflow for collaboration is still a work in progress and may change over time.

## Step 1: Get familiar with the project


You can get a quick feel for the current activity by [starting here](https://comob-project.github.io/snn-sound-localization/main/web/home-page.html). This automatically generated website collates all the parallel subprojects currently underway, listing them in order of how finished they are and how recently they've been modified, so that the most relevant stuff will be at the top.

We will be organizing regular meetings to talk about progress, you might want to come along to these. We'll add a link to those here when we have a regular venue, but for the moment sign up to our [Github Discussions](https://github.com/comob-project/snn-sound-localization/discussions) page and [discord](https://discord.gg/Zpd6RYYyuf) where we'll announce everything.



## Step 5: Finalise your subproject

The aim is to get your subproject into the final form of a figure or table that can be included in the paper we'll write at the end. Let us know when your subproject gets to this stage by opening a pull request to merge into the main branch. We'll do a more thorough review at this stage, and ask you to cut out any extraneous stuff and refactor a little to use the current version of the shared code to keep it all maintainable.

## Step 6: Help write the paper

Once the story is clearer, we'll start an Overleaf document and start writing up the paper. If you can, please join in on this! Write the paragraph for your subproject. Comment on the overall flow of the text and improve it, etc.

# Technical stuff

## Keeping your branch up-to-date

Since git branches are essentially sequences of commits, it's likely that your personal branch (`your_name/main`) will fall 
behind the commit sequence in the `main` branch. This happens when new commits are added to the main branch.

To keep your branch up-to-date, you should use  `git fetch origin main:main` and `git rebase main` from time to time. The
first command updates your local `main` branch, and the second command incorporates the new `main` commits into your branch,
and then places your commits at the end of the sequence. You shouldn't use `git merge`, because it can lead to
incompatible sequences of commits.

Of course if you need help with any of this, then please ask and someone will help out!

## Writing commit messages

Try to make your commit message informative, without going over ~50 characters. Some of us like to use [Conventional
Commits](https://www.conventionalcommits.org/en/v1.0.0/), which look like `<type>: <message>`. For example, `fix: fixes
a bug with the fano factor algorithm`, or `feat: adds a new figure for cross-correlation`.
