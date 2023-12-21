# Workbench

This is a simple brainstorming space powered by the github frontend, a github action, and a python script. Thank you to [David Marx](https://github.com/dmarx) for coming up with the idea for this and writing the original script, which I have tweaked to work for me!

My personal notes are kept on a different branch of the same local repo that this github repo is the remote for, and I use a private github repo as the remote for that branch. [This](https://stackoverflow.com/a/62213595) is the guide I followed to set that up! For editing I use vscodium on my laptop, and markor on my phone (with the git repo setup using [termux](https://f-droid.org/packages/com.termux/) & managed using scripts through [termux-widgets](https://f-droid.org/en/packages/com.termux.widget/)).

# Setup

1. Click on the "Use this template" button in the top-right to create a new repo based on this one
2. In your repo's settings, give github actions write permissions
3. Change the name of `README.stub.template` to `README.stub`, and change its heading to your liking
4. Go to lines 54 through 66 in [this script](scripts/update_readme.py) and set whatever colors you'd like for whatever tags you'd like

# Usage

1. Add markdown files to the repo's root folder
2. Upon committing, a github action runs that will build the README and tag pages (markdown files that group notes by tag)

The README will contain a table of contents for your notes, which will include a row for each note with:

* The note's modification date, used to sort the table of contents
* A link to the note with the title from its YAML frontmatter as anchor text
* Badges for each tag in the YAML frontmatter, which are links to their respective tag pages

The bottom of the README will have badges for all of the tags present in your notes, ordered by how often they appear.

The table of contents will look something like this:

![example_toc](example_toc.png)

And tag pages will look something like this:

![example_tag_page](example_tag_page.png)

## Rules to keep stuff from breaking

1. Put notes in the repo's root folder
2. Make sure note filenames contain no whitespace and use the `.md` suffix
3. Define each note's title and tags with YAML frontmatter field called "title" and "tags". Multiple tags must be separated by a comma followed by a space: ", ". 

# FAQ

### I added a markdown file and nothing changed

It takes a few seconds for the workflow that updates the README to run. Try waiting a few minutes and refreshing the page. 

If you get impatient, click on the "Actions" tab and make sure there's an entry associated with your most recent commit 
with a green check mark next to it. A red X means something went wrong, a yellow circle means the workflow is still running.

### How does the README build itself?

Discussion here: https://stackoverflow.com/a/72918091/819544
