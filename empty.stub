# Workbench

A simple brainstorming space, powered by the github frontend, a github action, and a simple python script.

# Setup

1. Fork this repository
2. Click on the "Actions" tab and activate github action workflows on your fork.
3. Change the name of `README.stub.template` to `README.stub`

<!--
2. Set "write" access on your `${{ secrets.GITHUB_TOKEN }}`, [instructions](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/enabling-features-for-your-repository/managing-github-actions-settings-for-a-repository#configuring-the-default-github_token-permissions) here.
-->


# Usage

1. Select `Add File > Create New File` to add a new markdown file containing the idea you want to log. Let's call this an "article".
2. Upon committing, a github action runs which builds the README, which is customizable from a template.

The generated `README.md` will contain a Table of Contents of your articles, and supports the following features:

* Infers modification date from commit history
* Sort most recently modified ideas at the top
* Hyperlink to document using markdown title as anchor text
* Custom tagging
* Wikipedia-esque "category" pages which group articles by tag

### Rules to keep stuff from breaking

1. Article filenames contain no whitespace and use the `.md` suffix
2. Define each note's title and tags with YAML frontmatter

# FAQ

### I added a markdown file and nothing changed

It takes a few seconds for the workflow that updates the README to run. Try waiting a few minutes and refreshing the page. 

If you get impatient, click on the "Actions" tab and make sure there's an entry associated with your most recent commit 
with a green check mark next to it. A red X means something went wrong, a yellow circle means the workflow is still running.

### How does the README build itself?

Discussion here: https://stackoverflow.com/a/72918091/819544
