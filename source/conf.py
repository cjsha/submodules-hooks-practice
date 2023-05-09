from datetime import datetime, timezone

# -*- coding: utf-8 -*-
#
# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = "Open Ephys Documentation"
copyright = "2010-{}, Open Ephys & Contributors".format(datetime.now(timezone.utc).year)
author = "Open Ephys & Contributors"

# The short X.Y version
version = "0.0"
# The full version, including alpha/beta/rc tags
release = "0.0.0"

# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.todo',
    'sphinx.ext.githubpages',
    # 'sphinx-jinja'
    # 'sphinx.ext.graphviz',
    # 'sphinxcontrib.wavedrom',
    # 'breathe',
]


# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
source_suffix = [".rst"]

# The master toctree document.
main_doc = "index"

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'en'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = None

todo_include_todos = True

# Breathe Configuration
# breathe_default_project = 'clroni'
# breathe_projects = { 'clroni': './API Reference/clroni/doxygen-xml' }

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "pydata_sphinx_theme"
html_logo = "_static/images/oe_logo_name.png"
html_scaled_image_link = True

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.

html_sidebars = {
    'index': ['search-field.html'],
    "**": ["search-field.html", "sidebar-nav-bs.html"]
}

# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
html_help_basename = "oe_docs"

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

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (main_doc, "oe-docs.tex", "Open Ephys Documentation", "Open Ephys", "manual"),
]

# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [(main_doc, "oe-docs", "Open Ephys Documentation", [author], 1)]

# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (
        main_doc,
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

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#
# epub_identifier = ''

# A unique identification for the text.
#
# epub_uid = ''

# A list of files that should not be packed into the epub file.
epub_exclude_files = ["search.html"]

# -- Extension configuration -------------------------------------------------
# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.

html_theme = "pydata_sphinx_theme"
html_logo = "_static/images/oe_logo_name.png"
html_scaled_image_link = True

html_theme_options = {
    'external_links': [{'name': 'Open Ephys', 'url': 'https://open-ephys.org'}, ],
    'navigation_with_keys': True,
    'use_edit_page_button': False,
    'show_toc_level': 1,
    'icon_links': [
        dict(name='GitHub',
             url='https://github.com/open-ephys/commutator-docs',
             icon='fab fa-github'),
        dict(name='Twitter',
             url='https://twitter.com/openephys',
             icon='fab fa-twitter'),
        dict(name='Discord',
             url='https://discord.gg/WXAx2URNQU',
             icon='fab fa-discord')
    ],
}
html_favicon = "_static/images/favicon.png"

html_context = {
    "github_user": "open-ephys",
    "github_repo": "commutator-docs",
    "github_version": "main",
    "doc_path": "source",
    "css_files": ["_static/theme_overrides.css"],
    'default_mode': 'light',
}

# Option for linkcheck
linkcheck_anchors = False


def rstjinja(app, docname, source):
    '''
    Render pages as a jinja template.
    '''
    # Make sure we're outputting HTML
    if app.builder.format != 'html':
        return
    src = source[0]
    rendered = app.builder.templates.render_string(
        src, app.config.html_context
    )
    # if src[0:8] == ":orphan:":
    #     print(src)
    #     print(docname)
    #     new_filename = os.path.splitext(docname)[0]+'.html'
    #     with open('source/'+new_filename, 'w') as file:
    #         file.write(rendered)
    #     print(rendered)
    source[0] = rendered


def setup(app):
    app.connect('source-read', rstjinja)
    app.add_js_file('copyURLToClipboard.js')
