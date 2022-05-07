# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'myDSProject'
copyright = '2022, Carlos Ricco van der Ley'
author = 'Carlos Ricco'

release = '0.1'
version = '0.1.1'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

# templates_path = ['_templates']

# -- Options for HTML output

# html_theme = 'sphinx_rtd_theme'
html_theme = 'renku'
html_theme_path = ["_themes", ]

# -- Options for EPUB output
epub_show_urls = 'footnote'
