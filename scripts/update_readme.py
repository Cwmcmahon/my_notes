import subprocess
from collections import defaultdict
from pathlib import Path

def get_last_modified_date(fpath, timestamp = False):
    fmt = '%as'
    if timestamp:
        fmt = '%at'
    cmd = f"git log --pretty=format:{fmt}__%ae -- {fpath}".split()
    response = subprocess.run(cmd, capture_output = True)
    commits = response.stdout.decode().split()
    lm_date, author_email = commits[0].split('__')
    return lm_date

def make_badge(label, count, color, root):
    return f"[![](https://img.shields.io/badge/{count}-{label}-{color})]({root}/tags/{label}.md)"

def make_badges_map(tag_counts, tag_colors, root = '.'):
    return {tag_name:make_badge(tag_name, len(tag_counts[tag_name]), tag_colors[tag_name], root) for tag_name in tag_counts}

def list_badges(tags, tag_badges_map, sort = False):
    if sort:
        tags = sorted(tags)
    return ' '.join([tag_badges_map[t] for t in tags]) 

def get_frontmatter(text):
    frontmatter = text.split('---')[1].strip()
    fields = frontmatter.split('\n')
    parsed = defaultdict(lambda: 'Null')
    for f in fields:
        key, value = f.split(': ')
        parsed[key] = value
    parsed['tags'] = parsed['tags'].split(', ')
    return parsed

md_files = list(Path('.').glob('*.md'))
toc_entries = []
tag_counts = defaultdict(list)

for fpath in md_files:
    if fpath.name != 'README.md':
        text = fpath.read_text()
        d = {'fpath': fpath}
        d['lm_date'] = get_last_modified_date(fpath)
        d['lm_timestamp'] = int(get_last_modified_date(fpath, timestamp = True))
        d['title'] = get_frontmatter(text)['title']
        d['tags'] = get_frontmatter(text)['tags']
        toc_entries.append(d)
        for tag in d['tags']:
            tag_counts[tag].append(d)

tag_counts = dict(sorted(tag_counts.items(), key = lambda x:len(x[1]), reverse = True))

# Change the hex color below to pick a default tag badge color
tag_colors = defaultdict(lambda: 'a89984')

# Change the tag names and hex colors below to assign colors to specific tag badges
tag_colors['athena'] = 'd3869b'
tag_colors['parents_skype'] = '458588'
tag_colors['politics'] = 'fb4934'
tag_colors['philosophy'] = 'd65d0e'
tag_colors['wedding'] = 'ebdbb2'
tag_colors['board_games'] = '98971a'
tag_colors['videogames'] = '689d6a'
tag_colors['movies'] = 'b16286'
tag_colors['ranking'] = 'd79921'

tag_badges_map = make_badges_map(tag_counts, tag_colors)

toc_entries = sorted(toc_entries, key = lambda x:(-x['lm_timestamp'], x['title']))

header = "|Last modified|Title|Tags\n|:---|:---|:---|\n"
rows = [f"|{d['lm_date']}|[{d['title']}](./{d['fpath']})|{list_badges(d['tags'], tag_badges_map)}|" for d in toc_entries]
whole_toc = header + '\n'.join(rows)
all_tags = list_badges(tag_counts.keys(), tag_badges_map)

readme = None
if Path('README.stub').exists():
    readme_stub = Path('README.stub').read_text()
    readme = readme_stub.replace('{TOC}', whole_toc)
    readme = readme.replace('{tags}', all_tags).strip()    
if not readme:
    readme = Path('empty.stub').read_text()

Path('README.md').write_text(readme)

tag_pages_badge_map = make_badges_map(tag_counts, tag_colors, root = '..')

Path('tags').mkdir(exist_ok = True)
for tag, pages in tag_counts.items():
    pages = sorted(pages, key = lambda x:(-x['lm_timestamp'], x['title']))
    tag_page_text = f"# Pages tagged `{tag}`\n\n"
    rows = [f"|{d['lm_date']}|[{d['title']}]({Path('..')/d['fpath']})|{list_badges(d['tags'], tag_badges_map)}|" for d in pages]
    tag_page_text += header + '\n'.join(rows)
    Path(f"tags/{tag}.md").write_text(tag_page_text)
