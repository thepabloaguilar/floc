# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.

import os
import sys
from unittest import mock

sys.path.insert(0, os.path.abspath('..'))


# -- Project information -----------------------------------------------------

def _get_project_meta():
    import tomlkit  # noqa: WPS433

    with open('../pyproject.toml') as pyproject:
        file_contents = pyproject.read()

    return tomlkit.parse(file_contents)['tool']['poetry']


pkg_meta = _get_project_meta()
project = str(pkg_meta['name'])
copyright = '2021, Pablo Aguilar'
author = 'Pablo Aguilar'

version = str(pkg_meta['version'])
release = version


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.viewcode',
    'sphinx.ext.autosummary',

    # Used to include .md files:
    'm2r2',

    # Used to insert typehints into the final docs:
    'sphinx_autodoc_typehints',
]

source_suffix = ['.rst', '.md']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

master_doc = 'index'

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.

html_theme = 'sphinx_typlog_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ['_static']

# -- sphinx_typlog_theme config ----------------------------------------------
html_theme_options = {
    'logo_name': 'FLoC',
    'description': 'A floc simulator wrapper over a Go implementation',
    'github_user': 'thepabloaguilar',
    'github_repo': 'floc',
    'color': '#20b095',
}

html_sidebars = {
    '**': [
        'logo.html',
        'globaltoc.html',
        'github.html',
        'searchbox.html',
    ],
}

# -- autodoc config ----------------------------------------------------------
autodoc_default_options = {
    'members': True,
    'exclude-members': '__dict__,__weakref__',
    'show-inheritance': True,
}
