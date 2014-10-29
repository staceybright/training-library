*************************
Setting Up Your Computer
*************************

The Institute provides you a computer when you are hired, and sets it up with a core set of software. (Some new hires get a loaner computer while a new machine is ordered and prepared for them.) They'll buy you a new one every three years, if you're good. Even though ITSD is responsible for installing important things like Office and antivirus software for all, it's up to each RIA to set their system up the way they want. For science-related uses, most new Institute machines are Macs, so this guide will assume that's what you have.

You should have a computer, a username, and a password from ITSD. Let's get started.

Configuring your email
-----------------------

Getting on relevant mailing lists
----------------------------------

Adding a printer
-----------------

Installing Ureka
-----------------

When Ureka finishes installing, it will automatically add some lines to your shell profile. All they do is make certain Ureka commands available to you in the terminal.

Open a new terminal and run ``ur_setup common ssbx``. If that succeeded without errors (i.e. no messages written to the terminal), run ``which python``. You should see something like ``/Users/johndoe/.ureka/.../python``, indicating that you are using Ureka's copy of Python.



Configuring STScI-specific environment variables
-------------------------------------------------

A lot of tools developed within STScI assume the existence of certain environment variables that point to data on servers within the Institute. The following is a table of essential variables you should set in your shell.

The default shell for new computers at the Institute is ``tcsh``, which means you should set these variables in ``~/.cshrc``. That is, you should create a new text file called ``.cshrc`` in your home directory. The end result of defining the above variables will look something like ``link to example cshrc``.

On to the training exercises!
--------------------------------

The next chapters explain useful tools with exercises interspered with the text. Save the results of your exercises as you go; you will submit them to your trainer once you've completed the section. If you get stuck, you can always ask your trainer for help!

Wondering who your trainer is for a particular section? Check the Confluence wiki page for your training group. Other current RIAs have also done this training, so they're a good resource for quick questions if your trainer is busy.

Without further ado, it's time to learn about :doc:`archives`.