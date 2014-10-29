Improving These Documents
==========================

These documents live in a Git repository, making it easy for you to modify them and share your changes with other RIAs. The first step to making a change is clone the repository, giving you a local copy to work with::

   git clone git@github.com:josePhoenix/riatraining.git

This creates a ``riatraining`` directory. The web pages are automatically generated from the ``.rst`` files in the ``source`` subdirectory. Before you can do that, you need to install required packages from ``requirements.txt``::

  pip install -r requirements.txt

This installs the program that builds the web pages from the source files. To make a change, edit the ``.rst`` source for the document and then run::

   make html

The generated HTML for the webpages is now in ``build/html/``. You can open ``build/html/index.html`` (or another file) to see your handiwork.

A simpler workflow
-------------------

There's a helper script that will rebuild (``make html``) the pages every time you make a change. Run ``python autobuilder.py`` from your terminal, and a browser window will pop open pointing to http://127.0.0.1:8000/.

While the autobuilder is running, any changes to .rst files will trigger a rebuild when you save them. Make your edits, save, and refresh the page in your browser to see your changes.

Quit the autobuilder by interrupting it with :kbd:`Control-c`.

Sharing your changes
---------------------

TODO depends on how gitlab works