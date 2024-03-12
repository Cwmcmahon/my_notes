# This script generates a README.adoc file with collapsible includes for all AsciiDoc files in the folder.

# SETUP
# Remove old README
if File.exist?('README.adoc')
  File.delete('README.adoc')
end

# Remove old tag pages
if Dir.exist?('tags')
  $tag_pages = Dir.glob('tags/*')
  $tag_pages.each do |file|
    File.delete(file)
  end
else 
  Dir.mkdir("tags")
end

# VARIABLES
$tag_pages = Hash.new([])
$tag_badges = {}
badges_list = []
files = Dir.glob('*.adoc')

# FUNCTIONS
# Returns a toc entry to be added to the README or a tag page
def make_toc_entry(file, mode)
  # Returns a note's title or tags from its frontmatter
  def parse_frontmatter(text, mode)
    if mode == "title"
      return text.match(/= (.*)/).captures[0]
    end
    if mode == "tags"
      return text.match(/:keywords: (.*)/).captures[0].split(',').map(&:strip)
    end
  end
  # Returns a badge-style link to a tag page
  def make_badge(label, root)
    # Tag colors
    tag_colors = Hash.new('282828')
    tag_colors['athena'] = 'd3869b'
    tag_colors['project'] =	'458588'
    tag_colors['politics'] = 'cc241d'
    tag_colors['philosophy'] = 'd65d0e'
    tag_colors['wedding'] =	'ebdbb2'
    tag_colors['board_games'] =	'98971a'
    tag_colors['videogames'] = '689d6a'
    tag_colors['survey'] =	'd79921'
    tag_colors['common_place'] = 'a89984'
    "image:https://img.shields.io/badge/#{label}-#{tag_colors[label]}[Static Badge,link=#{root}#{label}.adoc]"
  end
    
  toc_entry = ""
  File.open(file) do |f|
    front_matter = f.first(2)
    title = parse_frontmatter(front_matter[0], "title")
    tags = parse_frontmatter(front_matter[1], "tags")
    # So the links work from both the README and the tag pages
    # prefix is for the links to each note
    # badge_root is for the badge-style links to tag pages 
    if mode == "readme"
      prefix = ""
      badge_root = "tags/"
    elsif mode == "tag_page"
      prefix = "../"
      badge_root = "./"
    end
    # Adds link to file in section title
    toc_entry << "\n== link:#{prefix}#{file}[#{title}]\n"
    # Adds tag badges between the entry's title and collapsible include
    tags.each do |tag|
      badge = make_badge(tag, badge_root)
      toc_entry << "#{badge}\n"
      # So this is only done once...
      if mode == "readme"
        # Adds the note to the current tag's list in the tag_pages dictionary
        $tag_pages[tag] += [file]
        if !$tag_badges.include?(tag)
          # Sets the current tag's badge
          $tag_badges[tag] = badge
        end
      end
    end
    # Adds collapsible note contents
    toc_entry << "\n.Toggle note contents\n[%collapsible]\n====\ninclude::#{prefix}#{file}[lines=4..-1]\n====\n"
  end
  # Returns the toc entry
  toc_entry
end

# MAIN
# Generate the README
readme_text = "= Carter's Notes\n:toc:\n:toclevels: 1\n\nPLACEHOLDER\n"
files.each do |file|
  readme_text << make_toc_entry(file, "readme")
end

# Add a list of all badges
tags = $tag_pages.keys.sort
tags.each do |tag|
  badges_list << $tag_badges[tag]
end
readme_text = readme_text.sub(/PLACEHOLDER/, "== Tags\n\n#{badges_list.join("\n")}")

File.open('README.adoc', 'w') do |readme|
  readme.write(readme_text)
end

# Generate the tag pages
$tag_pages.each do |tag, notes|
  tag_page_text = "= `#{tag}` notes\n:toc:\n:toclevels: 1\n"
  
  notes.each do |note|
    tag_page_text << make_toc_entry(note, "tag_page")
  end
  
  File.open("tags/#{tag}.adoc", 'w') do |tag_page|
    tag_page.write(tag_page_text)
  end
end
    