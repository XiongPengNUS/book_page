# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'RSOME'
copyright = '2026, Melvyn Sim, Zhi Chen, Peng Xiong'
author = 'Melvyn Sim, Zhi Chen, Peng Xiong'

# -- General configuration ---------------------------------------------------

extensions = [
    "myst_nb",        # Use "nbsphinx" instead if you installed
    "sphinx_design",  # Provides grid/gutter layouts and cards nbsphinx
    "sphinx.ext.mathjax",
    "sphinxcontrib.bibtex",
]

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

language = 'Python'

# -- Options for HTML output -------------------------------------------------
root_doc = "index"

html_theme = 'pydata_sphinx_theme'
html_sidebars = {"**": []}
html_theme_options = {
    "secondary_sidebar_items": [],
    
    "logo": {
        "text": " ",
        "image_light": "logo/logolight.png",
        "image_dark": "logo/logodark.png",
    },

    "article_header_start": [],
    "article_header_end": [],

    "navbar_start": ["navbar-logo"],
    "navbar_center": ["navbar-nav"],
    "navbar_end": ["search-button", "theme-switcher", "navbar-icon-links"],
    #"navbar_align": "content",

    "footer_start": ["copyright"],
    "footer_end": ["sphinx-version"],

    "github_url": "https://github.com/XiongPengNUS/rsome"
}

templates_path = ['_templates']
html_static_path = ['_static']
html_js_files = ["custom.js"]
html_css_files = ["custom.css"]

nb_execution_mode = "auto"
myst_enable_extensions = [
    "colon_fence",
    "dollarmath",
    "amsmath",
]
mathjax3_config = {
    "tex": {
        "tags": "ams",
    },
}
math_numfig = False

# BibTeX configuration
bibtex_bibfiles = ["references.bib"]

# Numerical citation style
bibtex_reference_style = "label"

suppress_warnings = [
    "bibtex.duplicate_citation",
]

# Disable execution of ipynb files for preview
nb_execution_mode = "off"
