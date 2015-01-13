**************************
Improving These Documents
**************************

These documents live in a Git repository, making it easy for you to modify them and share your changes with other RIAs. The first step to making a change is clone the repository, giving you a local copy to work with::

   git clone git@github.com:josePhoenix/riatraining.git

This creates a ``riatraining`` directory. The web pages are automatically generated from the ``.rst`` files in the ``source`` subdirectory. Before you can do that, you need to install required packages from ``requirements.txt``::

  pip install -r requirements.txt

This installs the program that builds the web pages from the source files, as well as components it depends on. To make a change, edit the ``.rst`` source for the document and then run::

   make html

The generated HTML for the webpages is now in ``build/html/``. You can open ``build/html/index.html`` (or another file) to see your handiwork.

See :ref:`sharing_doc_changes` for how to incorporate your changes in the published version.

A simpler workflow
-------------------

There's a helper script that will rebuild (``make html``) the pages every time you edit and save a file. Run ``python autobuilder.py`` from your terminal, and a browser window will pop open pointing to http://127.0.0.1:8000/.

While the autobuilder is running, any changes to .rst files will trigger a rebuild when you save them. Make your edits, save, and refresh the page in your browser to see your changes.

Quit the autobuilder by interrupting it with :kbd:`Control-c`.

Writing with reST
------------------

Writing with reST is a lot like writing a plain-text email. Bullet points are asterisks at the beginning of a line, emphasis is accomplished by putting asterisks on either side of a word, and so forth. If you're not sure how some formatting was achieved in these documents, just have a look at the ``.rst`` source file!

Here are some very common patterns for quick reference:

+-----------------------------------+-------------------------------------------------------------+
|Type of formatting                 | Example code                                                |
+===================================+=============================================================+
| Bold                              | |  ``**bold text**``                                        |
+-----------------------------------+-------------------------------------------------------------+
| Italic/emphasis                   | | ``*emphasized text*``                                     |
+-----------------------------------+-------------------------------------------------------------+
| Chapter heading                   | | ``*****************``                                     |
|                                   | | ``Chapter Heading``                                       |
|                                   | | ``*****************``                                     |
+-----------------------------------+-------------------------------------------------------------+
| Section heading                   | | ``Section Heading``                                       |
|                                   | | ``=================``                                     |
+-----------------------------------+-------------------------------------------------------------+
| Link to another training document | | ``:doc:`filename_without_extension```                     |
+-----------------------------------+-------------------------------------------------------------+
| Link to a web page                | | ```text of link <http://example.com/>`_``                 |
+-----------------------------------+-------------------------------------------------------------+
| Exercise prompt                   | | ``.. admonition:: Exercise``                              |
|                                   | |                                                           |
|                                   | | Indent your exercise instructions with three spaces, and  |
|                                   | | leave a blank line after the ``admonition`` line but      |
|                                   | | before the instructions                                   |
+-----------------------------------+-------------------------------------------------------------+

For more advanced formatting information, there's a very good `syntax quickstart guide <http://sphinx-doc.org/rest.html>`_ maintained by the Sphinx project.


.. _sharing_doc_changes:

Sharing your changes
---------------------

You may wish to review :doc:`version_control` for more information on Git.