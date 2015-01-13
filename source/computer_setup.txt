*************************
Setting Up Your Computer
*************************

*Authors: Joseph Long, Matthew Bourque, Sara Ogaz, Amber Armstrong, Michael Dulude, and Tiffany Borders*

The Institute provides you a computer when you are hired, and sets it up with a core set of software. (Some new hires get a loaner computer while a new machine is ordered and prepared for them.) They'll buy you a new one every three years, if you're good. Even though ITSD is responsible for installing important things like Office and antivirus software for all, it's up to each RIA to set their system up the way they want. For science-related uses, most new Institute machines are Macs, so this guide will assume that's what you have.

You should have a computer, an ActiveDirectory (AD) username, and a password from ITSD. Let's get started.

Configuring your email
=======================

Space Telescope uses Microsoft Exchange for email. Web-based access is available at https://mail.stsci.edu/. For daily use, you should set up a mail client like Outlook on your computer.

ITSD maintains some `guides for common mail clients <http://www.stsci.edu/institute/itsd/collaboration/exchange/clients>`_.

Adding a printer
=================

Choose a printer near your office from `this list of printers <http://www.stsci.edu/institute/itsd/hardware/printers/printerlocs/printerlocations>`_. There are `instructions for printer setup <http://www.stsci.edu/institute/itsd/hardware/printers>`_ for different operating systems. The one you want is "Adding a Printer in Mac OS X".

Verify network mounts
======================

New computers set up by ITSD automatically connect certain folders to servers on the Institute network. These are called "Central Storage", and you will  Open a terminal and check that you can list the contents of the ``/grp/hst`` and ``/user`` directories, like shown::

    $ ls /grp/hst
    HST_Arch_Proj acs_testing   etc           nicmos        tac           wfc3c         wfc3i
    OTA           adrizzle      etcrlbkup     prd           telemetry     wfc3d         wfc3j
    acs           cdbs          fgs           pyetc         usersupport   wfc3e         wfc3k
    acs2          cos           frc           ssb           wasapsb       wfc3f         wfc3l
    acs3          cos2          frontier1     stis          wfc3a         wfc3g         wfpc2
    acs4          cos3          frontier2     synphot       wfc3b         wfc3h

(If, instead, you see something like this... ::

    $ ls /grp/hst
    ls: /grp/hst: No such file or directory

... then you need to talk to ITSD.)

Setting up your own Central Storage directory
==============================================

Users can store files under their username at ``/user/myusername``. This is useful for sharing large files with your colleagues. In fact, you'll be using your Central Storage directory to send your training exercises to your trainers later on.

Send an email to the STScI *internal* helpdesk at support@stsci.edu, and ask them to make you a Central Storage directory. [#externalhelpdesk]_

Configuring STScI-specific environment variables
=================================================

A lot of tools developed within STScI assume the existence of certain environment variables that point to data on servers within the Institute. The default shell for new computers at the Institute is ``tcsh``, which means you should set these variables in the file ``.cshrc`` in your home directory.

Here is an example ``.cshrc``::

    # Paths and stuff for accessing CDBS stuff
    # For WFC3
    setenv iref /grp/hst/cdbs/iref/
    # For ACS
    setenv jref /grp/hst/cdbs/jref/
    setenv jtab /grp/hst/cdbs/jtab/
    # For COS
    setenv lref /grp/hst/cdbs/lref/
    # For STIS
    setenv oref /grp/hst/cdbs/oref/
    setenv otab /grp/hst/cdbs/otab/
    setenv crrefer /grp/hst/cdbs/
    setenv mtab /grp/hst/cdbs/mtab/

As you may have guessed, setting variables in ``tcsh`` takes the form of ``setenv NAMEOFVAR /value/for/var``.

To check that your changes have taken effect, open a **new terminal window** and type ``echo $mtab``. You should see the value for ``mtab`` from above printed out in the terminal.

Installing Ureka for internal users
====================================

The Institute's Science Software Branch distributes a package containing all of the essentials for scientific computing for astronomy. The version for outside users is called Ureka (you may have it on your home computer), but we use a special version of Ureka internally. Like Ureka, this package includes all the usual suspects: Python, IRAF, PyRAF, IPython + the IPython Notebook, NumPy, SciPy, matplotlib, ds9, etc. For more information, consult the `complete list <http://ssb.stsci.edu/ssbx/docs/components.html>`_ (or the `SSBREL complete list <http://ssb.stsci.edu/ssbrel/docs/components.html>`_).

There are three release channels of the SSB IRAF + Python distribution: SSBDEV, SSBX, and SSBREL. SSBDEV is updated nightly, SSBX weekly, and SSBREL infrequently as it is the most stable option.

You can read the `installation instructions <http://ssb.stsci.edu/ssb_software.shtml#install_yourself>`_, but they're short enough to be reproduced here. Open a terminal and run::

    curl -O http://ssb.stsci.edu/ssb_installer
    sh ssb_installer

You will be given the choice of which release to install. It's a good idea to install both SSBX and SSBDEV. (Simply run the installer again to install the other release.) You will be prompted to add a few lines to your login scripts. This will make available some new commands.

Open a new terminal and use ``ur_setup common ssbx`` to enable the SSBX release. Alternatively, ``ur_setup common ssbdev`` enables SSBDEV. To update some parts of the release, use ``ur_update``. If you want to undo the Ureka changes for a particular window, use ``ur_forget``.

To automatically activate Ureka in new terminal windows, add the ``ur_setup common ssbx`` (or ``ssbdev``) line to the end of ``~/.cshrc``.

Caveats for ``ur_update``
--------------------------

Ureka keeps getting better, but it's still got some rough edges. For instance, SSBREL cannot be updated with ``ur_update``. Even on ``SSBX`` and ``SSBDEV``, ``ur_update`` only updates parts of the Ureka install. Python packages developed at STScI are updated, along with the STScI IRAF distribution, aXe, HSTCAL, and JWST libraries. 

Notably this does **not** include NumPy, SciPy, matplotlib, IPython, or AstroPy. To update those, you will have to remove and reinstall the Ureka "core" as described in :ref:`update-ureka-core`. 

Verify IDL is installed
========================

IDL should be pre-installed on new Institute machines. To check, open a terminal window and type ``idl``. You should see something like this::

   $ idl
   IDL Version 8.2.3, Mac OS X (darwin x86_64 m64). (c) 2013, Exelis Visual Information Solutions, Inc.
   Installation number: 90853.
   Licensed for use by: Space Telescope

   IDL>

Create a MAST (archive) account
================================

MAST is the archive for HST science images and data from various other missions, operated by Space Telescope. You need a separate account to access it, which you can obtain by filling out the `online registration form <http://archive.stsci.edu/registration/registration_form.html>`_.

You'll be assigned a temporary password when you register. You should change it to something **different* from your STScI password using the `password change form <http://archive.stsci.edu/registration/change.html>`_ after verifying that you're able to log in.

Subscribe to mailing lists
===========================

The Institute has more than one way to subscribe to mailing lists, which is a bit confusing.

jDomo subscriptions
--------------------

Subscribe to ``sci_tech`` and ``tips_announce`` through the jDomo interface at http://www.stsci.edu/cgi-bin/jDomo.tcl. You will get a confirmation email from jDomo. To complete the subscription, reply to it with the authorization code in the message (e.g. ``auth 3198f7d8 subscribe sci_tech myname@stsci.edu``).

Outlook subscriptions
----------------------

Subscribe to ``ins_staff``, ``ins_aura``, and ``ins_riab`` through the Outlook Web Access interface at http://mail.stsci.edu/. Log in with your AD username and password. The way to subscribe to lists is well hidden; you must log in, choose "Options", then "See all options", select "Groups" from the sidebar, search for the mailing list name and click "Join".

The lists ``pylunch``, ``python-interested`` and ``macx_users`` can also be subscribed to in the same way. ITSD also provides `more information on Exchange <http://www.stsci.edu/institute/itsd/collaboration/exchange/exchangeLists>`_, if you're interested.

Make sure you can log in to Cisco Jabber
=========================================

Cisco Jabber should already be installed on your machine. (Contact ITSD if it's not.) Open the Cisco Jabber application and sign in with your AD username and password. Cisco Jabber connects with your calendar and phone, and will tell you if the person you're trying to message is in a meeting or does not want to be disturbed. You can also set it up to receive calls through your computer (for example, for teleworking).

ITSD maintains a guide with more information here: http://www.stsci.edu/institute/itsd/phone/jabber

Log in to the Confluence wiki
==============================

Log in to the Confluence wiki at https://confluence.stsci.edu/ using your AD credentials. Some important links to bookmark are:

* the `RIA branch wiki page <https://confluence.stsci.edu/pages/viewpage.action?pageId=32015091>`_ 
* the `RIA training hub <https://confluence.stsci.edu/display/INSRIA/RIA+training>`_
* the training page for your hiring group (click "RIA training" in the sidebar to expand the list)

On to the training exercises!
================================

The next chapters explain useful tools with exercises interspered with the text. Save the results of your exercises as you go; you will submit them to your trainer once you've completed the section. If you get stuck, you can always ask your trainer for help!

Wondering who your trainer is for a particular section? Check the `Confluence wiki page <https://confluence.stsci.edu/display/INSRIA/RIA+training>`_ for your training group (find your training group in the sidebar, after expanding the "RIA training" category). Other current RIAs have also done this training, so they're a good resource for quick questions if your trainer is busy.

Without further ado, it's time to learn about MAST (a.k.a. the Archive).

(If you're following along on paper, visit https://confluence.stsci.edu/display/INSRIA/RIA+training and choose the link for MAST archive training.)

Additional resources
=====================

* The Institute maintains a list of approved software, which you should consult if you need something else for your machine: http://www.stsci.edu/institute/itsd/software

.. rubric:: Footnotes

.. [#externalhelpdesk] There's an *external* helpdesk too, help@stsci.edu. For IT issues, though, you want the internal one. The external one is for astronomers to ask questions about things like the archive, SSB software, data characteristics, and the like.
