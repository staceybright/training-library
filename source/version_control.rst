*************************
Version Control with git
*************************

Version control systems keep track of changes to code, documents, and other files as you work. While this document will discuss one particular version control system, ``git`` [#gitproject]_ , the *concept* of version control shows up everywhere from iCloud to Wikipedia to NASA project management. That's because the simple idea of tracking changes is very powerful, giving authors and programmers great flexibility in their work.

What can version control do for me?
====================================

It might be instructive to motivate these exercises with some examples. After completing this training, you will know how to do all of these for any given ``git`` repository. Here are a few examples of things version control can do for you.

Figuring out who to ask
------------------------

You notice a calibration pipeline script is failing on a line of code you're not familiar with. By going into the version control system, you can see not only when that line was added to the script, but who wrote it.

Collaborate without clobbering each other's work
-------------------------------------------------

You and a collaborator are both editing a report written in LaTeX on your own computers. She updates a figure in section 1 at the same time as you updating a sentence in that section. Rather than just taking the latest edited version, the version control system combines your edits to make a new report with both her updated figure and your updated sentence. (No more sending ``technical_report_292_revC_final_2_draft2_SmithEdit.tex`` back and forth, trying to figure out what changed!)

Work on two things at once, without going nuts
-----------------------------------------------

You have a script you're working on, and you want to add two major features. Rather than having to work on them one at a time, or risk breaking the script by changing two major things at once, you can use two *branches* to isolate your changes and switch which branch you're working on with a simple command. When you're done, you simply *merge* each branch with the master copy.

Selectively undo specific changes
----------------------------------

Back in 2012, your instrument team decided that all coefficients on a particular model should be normalized to a maximum value of one. Today, they decide that the original constants were better after all, and want you to change the coefficients back to the old values everywhere they appear in the code. By using the repository history, you can find the exact set of changes that normalized the coefficients, and easily undo *only* that set without rolling the whole code back to a 2012 version.

Contributing your changes to the community
-------------------------------------------

You find a great open-source package that implements a source-finding algorithm for science images. You want to extend it with an option to modify the algorithm, without reimplementing it from scratch. By making your own *clone* of their version control repository, you can make your changes there and easily contribute them back to the original project.

Getting started with ``git``
==============================

First, make sure ``git`` is installed: open a Terminal window, type ``git``, and hit :kbd:`Enter`. (If you see ``command not found``, you need to make sure git is installed and available in your Terminal.) This will print out a somewhat intimidating list of all the things you can do with git, most of which are exposed through "sub-commands". Think of it like this: the first two "words" when you type a git command are the real name of the command, and anything after is interpreted as modifiers to that command.

For example, ``git add ./test`` means "add files in the test directory to be committed" and ``git init ./test`` means "initialize a repository in the test directory". On the other hand, if you typed ``git ./test``... ::

   $ git ./test
   git: './test' is not a git command. See 'git --help'.

Every sub-command has thorough documentation accessible through ``git nameofcommand --help``. (You can scroll the help pagewith the arrow keys and exit with :kbd:`q`.)

The first thing we want to do is make a workspace for these exercises. Git commands operate on a **repository**, which is a folder on your computer that contains both the files you want to track and the internal git bookkeeping data #[gitdirectory]_ .

.. admonition:: Exercise

   Create a new git repository in a folder called ``git_training`` using the ``git init`` commmand. (Skim ``git init --help`` to figure out the syntax.)


..
   TODO list
   add, commit, revert
   branches
   merging
   merging with conflicts

.. rubric:: Footnotes

.. [#gitproject] `git <http://git-scm.com/>`_ is free and open source software developed by the creator of Linux (Linus Torvalds) and many others. He once said that "git" (British English for "an unpleasant person") was a good name for a project of his, as he names all of his projects after himself.
.. [#gitdirectory] The vast majority of git repositories you will come across will have a hidden subdirectory named ``.git``, as well as the "working copy" of any files you're editing. To be nit-picky, the ``.git`` directory is the actual *repository*. (For example, you can delete the files of the working copy completely and get a fresh version as long as the ``.git`` directory is intact.)