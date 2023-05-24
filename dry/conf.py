from datetime import datetime, timezone
from git import Repo
from pathlib import Path
import yaml
import sys
import os

repo = Repo("..")
repo_url = repo.remotes.origin.url

# try:
#     with open(".github/workflows/sphinx-build.yml", "r+") as yaml_file:
#         data = yaml.safe_load_all(yaml_file)
#         loaded_data = list(data)
#         loaded_data[0]['jobs']['docs']['steps'][6]['run'] = \
#             """"git clone repo_name = {repo_url} --branch gh-pages --single-branch gh-pages
#                 cp -r docs/html/* gh-pages/
#                 cd gh-pages
#                 git config --local user.email "action@github.com"
#                 git config --local user.name "GitHub Action"
#                 git add .
#                 git commit -m "Update documentation" -a || true"""
# except FileNotFoundError:
#     print(".github/workflows/sphinx-docs.yml doesn't exist")
#     exit(1)

# -*- coding: utf-8 -*-
# Configuration file for the Sphinx documentation builder.
# This file does only contain some options. For a full list, view: http://www.sphinx-doc.org/en/master/config

# -- Project information -----------------------------------------------------

project = "Open Ephys Documentation"
project_copyright = "2010-{}, Open Ephys & Contributors".format(datetime.now(timezone.utc).year)
author = "Open Ephys & Contributors"

# The short X.Y version
version = "0.0"
# The full version, including alpha/beta/rc tags
release = "0.0.0"

# -- General configuration ---------------------------------------------------

sys.path.append(os.path.abspath('../_ext'))

# Add any Sphinx extension module here. They can be included in Sphinx (named 'sphinx.ext.*') or custom
extensions = [
    'sphinx.ext.todo',
    'sphinx.ext.githubpages',
    'sphinx.ext.intersphinx',
    'sphinx_design',
    'dry'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["../submodule"]

# The master toctree document.

root_doc = "index"
dry_dir = ""
# The language for content autogenerated by Sphinx. Refer to documentation for a list of supported languages.
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'en'

# List of patterns, relative to root directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["source/**.rst"]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = None

todo_include_todos = True

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages. See the documentation for a list of builtin themes.
html_theme = "pydata_sphinx_theme"
html_logo = "../submodule/oe_logo_name.png"
html_scaled_image_link = True

# Add any paths that contain custom _static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin _static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["../submodule"]

# Custom sidebar templates, must be a dictionary that maps document names to commutator-template names.
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html', 'searchbox.html']``.
# html_sidebars = {
#     'index': ['search-field.html'],
#     "**": ["search-field.html", "sidebar-nav-bs.html"]
# }

# -- Options for HTMLHelp output ---------------------------------------------

# -- Options for LaTeX output ------------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',
    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',
    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',
    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples:
# (source start file, target name, title, author, document class [howto, manual, or own class])
latex_documents = [
    (root_doc, "oe-docs.tex", "Open Ephys Documentation", "Open Ephys", "manual"),
]

# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples:
# (source start file, name, description, authors, manual section).
man_pages = [(root_doc, "oe-docs", "Open Ephys Documentation", [author], 1)]

# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples:
# (source start file, target name, title, author, dir menu entry, description, category)
texinfo_documents = [
    (
        root_doc,
        "Open Ephys Documentation",
        "Open Ephys Documentation",
        author,
        "Open Ephys Documentation",
        "Description",
        "Miscellaneous",
    ),
]

# -- Options for Epub output -------------------------------------------------

# Bibliographic Dublin Core info.
epub_title = project

# The unique identifier of the text. This can be a ISBN or the project homepage.
# epub_identifier = ''

# A unique identification for the text.
# epub_uid = ''

# A list of files that should not be packed into the epub file.
epub_exclude_files = ["search.html"]

# -- Extension configuration -------------------------------------------------

# Theme options are theme-specific and customize the look and feel of a theme further. For a list of options available
# for each theme, see the documentation.

repo_url = repo_url.split('.git')[0]

html_theme_options = {
    'external_links': [{'name': 'Open Ephys', 'url': 'https://open-ephys.org'}, ],
    'navigation_with_keys': True,
    'use_edit_page_button': False,
    'show_toc_level': 1,
    'icon_links': [
        dict(name='GitHub',
             url=repo_url,
             icon='fab fa-github'),
        dict(name='Twitter',
             url='https://twitter.com/openephys',
             icon='fab fa-twitter'),
        dict(name='Discord',
             url='https://discord.gg/WXAx2URNQU',
             icon='fab fa-discord')
    ],
}
html_favicon = "../submodule/favicon.png"

html_css_files = ["theme_overrides.css"]

user_name = repo_url.split('/')[3]
repo_name = repo_url.split('/')[-1]

html_context = {
    "github_user": user_name,
    "github_repo": repo_name,
    "github_version": "main",
    "doc_path": "source",
    'default_mode': 'auto',
}

dry_json = {
    "commutator-template": {
        "coax": {
            "product": "Coax Commutator",
            "shorthand": "coax",
            # "bonsai_packages": [
            #     "Bonsai.Onix"
            # ]
        },
        "spi": {
            "product": "SPI Commutator",
            "shorthand": "spi",
            # "bonsai_packages": [
            #     "Bonsai.Miniscope",
            #     "Bonsai.Onix"
            # ]
        }
    }
}

# Option for linkcheck
linkcheck_anchors = False


def rstjinja(app, _, source):
    """
    Render pages as a jinja commutator-template.
    """
    # Make sure we're outputting HTML
    if app.builder.format != 'html':
        return
    src = source[0]
    rendered = app.builder.templates.render_string(src, app.config.html_context)
    source[0] = rendered


def setup(app):
    app.connect('source-read', rstjinja)
    app.add_js_file('copyURLToClipboard.js')