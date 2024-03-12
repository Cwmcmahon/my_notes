# -*- encoding: utf-8 -*-
# stub: asciidoctor-reducer 1.0.6 ruby lib

Gem::Specification.new do |s|
  s.name = "asciidoctor-reducer".freeze
  s.version = "1.0.6".freeze

  s.required_rubygems_version = Gem::Requirement.new(">= 0".freeze) if s.respond_to? :required_rubygems_version=
  s.metadata = { "bug_tracker_uri" => "https://github.com/asciidoctor/asciidoctor-reducer/issues", "changelog_uri" => "https://github.com/asciidoctor/asciidoctor-reducer/blob/main/CHANGELOG.adoc", "mailing_list_uri" => "https://chat.asciidoctor.org", "source_code_uri" => "https://github.com/asciidoctor/asciidoctor-reducer" } if s.respond_to? :metadata=
  s.require_paths = ["lib".freeze]
  s.authors = ["Dan Allen".freeze]
  s.date = "2024-02-12"
  s.description = "A tool that reduces an AsciiDoc document containing preprocessor directives (includes and conditionals) to a single AsciiDoc document by expanding all includes and evaluating all conditionals.".freeze
  s.email = "dan.j.allen@gmail.com".freeze
  s.executables = ["asciidoctor-reducer".freeze]
  s.files = ["bin/asciidoctor-reducer".freeze]
  s.homepage = "https://asciidoctor.org".freeze
  s.licenses = ["MIT".freeze]
  s.rubygems_version = "3.6.0.dev".freeze
  s.summary = "Reduces an AsciiDoc document containing includes and conditionals to a single AsciiDoc document.".freeze

  s.installed_by_version = "3.6.0.dev".freeze if s.respond_to? :installed_by_version

  s.specification_version = 4

  s.add_runtime_dependency(%q<asciidoctor>.freeze, ["~> 2.0".freeze])
  s.add_development_dependency(%q<rake>.freeze, ["~> 13.1.0".freeze])
  s.add_development_dependency(%q<rspec>.freeze, ["~> 3.13.0".freeze])
end
