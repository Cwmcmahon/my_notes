import subprocess
from collections import	defaultdict
from pathlib import	Path
from tag_color_dict import tag_colors
import shutil

# Returns the last commit date for a file as a string
def	get_last_modified_date(fpath, timestamp	= False):
	fmt	= '%as'
	if timestamp:
		fmt = '%at'
	cmd	= f"git	log	--pretty=format:{fmt}__%ae -- {fpath}".split()
	response = subprocess.run(cmd, capture_output =	True)
	commits	= response.stdout.decode().split()
	lm_date, author_email =	commits[0].split('__')
	return lm_date

# Returns a badge link for a tag
def	make_badge(label, count, color,	root):
	return f"[![](https://img.shields.io/badge/{count}-{label}-{color})]({root}/tags/{label}.md)"

# Returns a dictionary mapping the name of each tag to its badge (which links to its tag page). Both tag_counts and tag_colors are dictionaries with tag names as keys
def	make_badges_map(tag_counts,	tag_colors,	root = '.'):
	return {tag_name:make_badge(tag_name, len(tag_counts[tag_name]), tag_colors[tag_name], root) for tag_name in tag_counts}

# Returns a string containing the badges for each tag in the tags argument. Takes a list of tags and a dictionary mapping tags to badges as arguments
def	list_badges(tags, tag_badges_map, sort_by =	None):
	if sort_by:
		tags = sorted(tags,	key	= lambda x:(list(tag_counts.keys()).index(x)))
	return ' '.join([tag_badges_map[t] for t in	tags]) 

# Returns a dictionary based on YAML frontmatter from a string (read from a markdown note)
def	get_frontmatter(text):
	frontmatter	= text.split('---')[1].strip()
	fields = frontmatter.split('\n')
	parsed = defaultdict(lambda: 'Null')
	for	f in fields:
		key, value = f.split(':')
		key	= key.lower().strip()
		value =	value.strip()
		parsed[key]	= value
		if parsed['tags'] != 'Null':
			parsed['tags'] = [t.lower().strip()	for	t in parsed['tags'].split(',')]
	return parsed

# A list of the markdown files in the repo's root directory
md_files = list(Path('.').glob('*.md'))

# A list that will hold the rows in the table of contents
toc_entries	= []

# A dictionary that will map each tag to a list containing a dictionary for each note with that tag
tag_counts = defaultdict(list)

# Removing README.md from the list of notes
try:
	md_files.remove(Path('README.md'))
except:
	pass

# Filling in toc_entries and tag_counts
for	fpath in md_files:
	text = fpath.read_text()
	# A dictionary to hold information about the current note
	d =	{'fpath': fpath}
	# The last commit date for the current note (to display)
	d['lm_date'] = get_last_modified_date(fpath)
	# The last commit timestamp for the current note (for sorting)
	d['lm_timestamp'] = int(get_last_modified_date(fpath, timestamp	= True))
	# Title of the current note
	d['title'] = get_frontmatter(text)['title']
	# The current note's tags
	d['tags'] =	get_frontmatter(text)['tags']
	# That note's dictionary is added to the toc_entries list
	toc_entries.append(d)
	# Add the current note's dictionary to the list of each tag that it contains 
	for	tag	in d['tags']:
		tag_counts[tag].append(d)

# Sort tag_counts in reverse order of frequency
tag_counts = dict(sorted(tag_counts.items(), key = lambda x:len(x[1]), reverse = True))

# Dictionary mapping each tag name to its badge
tag_badges_map = make_badges_map(tag_counts, tag_colors)

# Sort toc_entries in reverse chronological order
toc_entries	= sorted(toc_entries, key =	lambda x:(-x['lm_timestamp'], x['title']))

# Assembling the table of contents
header = "|Title|Tags|Last modified\n|:---|:---|:---|\n"
rows = [f"|[{d['title']}](./{d['fpath']})|{list_badges(d['tags'], tag_badges_map, sort_by = tag_counts)}|{d['lm_date']}|" for d	in toc_entries]
whole_toc =	header + '\n'.join(rows)
# Adding the string containing all tag badges at the bottom
all_tags = list_badges(tag_counts.keys(), tag_badges_map)

# Assembling the custom README if README.stub exists
if Path('README.stub').exists():
	readme_stub	= Path('README.stub').read_text()
	readme = readme_stub.replace('{TOC}', whole_toc)
	readme = readme.replace('{tags}', all_tags).strip()
	readme = readme.replace('{number}', str(len(toc_entries)))
# Assembling the default README if README.stub does not exist (for the template repo)
else:
	readme = Path('empty.stub').read_text()

Path('README.md').write_text(readme)

# Making a new dictionary mapping each tag to its badge, but adjusted so the link still leads to the tag page
tag_pages_badge_map	= make_badges_map(tag_counts, tag_colors, root = '..')

# Removing the old tag pages directory to clear out tag pages for tags that aren't used anymore
shutil.rmtree('tags')

# Making a new tag pages directory and filling it with tag pages for each tag
Path('tags').mkdir(exist_ok	= True)
for	tag, pages in tag_counts.items():
	pages =	sorted(pages, key =	lambda x:(-x['lm_timestamp'], x['title']))
	tag_page_text =	f"#	Pages tagged `{tag}`\n\n"
	rows = [f"|[{d['title']}]({Path('..')/d['fpath']})|{list_badges(d['tags'], tag_pages_badge_map, sort_by = tag_counts)}|{d['lm_date']}|"	for	d in pages]
	tag_page_text += header + '\n'.join(rows)
	Path(f"tags/{tag}.md").write_text(tag_page_text)
