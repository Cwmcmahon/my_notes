# Workbench

Thank you to [David Marx](https://github.com/dmarx) for coming up with the idea for this, which I have tweaked to work for me!

This is a simple brainstorming space, powered by the github frontend, a github action, and a simple python script.

# Setup

1. Click on the "Use this template" button in the top-right to create a new repo based on this one
2. In your repo's settings, give github actions write permissions
3. Change the name of `README.stub.template` to `README.stub`, and change its heading to your liking
4. Go to lines 54 through 66 in [this script](scripts/update_readme.py) and change the tag badge colors to your liking

# Usage

1. Add markdown files to the repo's root folder
2. Upon committing, a github action runs which builds the README, which is customizable from a template.

The generated `README.md` will contain a Table of Contents of your notes, and supports the following features:

* Infers modification date from commit history
* Sort most recently modified ideas at the top
* Hyperlink to document using markdown title as anchor text
* Custom tagging
* Wikipedia-esque "category" pages which group articles by tag

It'll look something like this:
![example_toc](example_toc.png)

### Rules to keep stuff from breaking

1. Note filenames contain no whitespace and use the `.md` suffix
2. Define each note's title and tags with YAML frontmatter

# FAQ

### I added a markdown file and nothing changed

It takes a few seconds for the workflow that updates the README to run. Try waiting a few minutes and refreshing the page. 

If you get impatient, click on the "Actions" tab and make sure there's an entry associated with your most recent commit 
with a green check mark next to it. A red X means something went wrong, a yellow circle means the workflow is still running.

### How does the README build itself?

Discussion here: https://stackoverflow.com/a/72918091/819544
