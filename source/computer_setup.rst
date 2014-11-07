*************************
Setting Up Your Computer
*************************

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
------------------------------------------

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

Setting your ``pip install`` location
--------------------------------------

You may eventually need to install additional Python packages. By setting an installation location, you ensure that your packages won't be touched if you have to reinstall Ureka.

Caveats for ``ur_update``
--------------------------

SSBREL cannot be updated with ``ur_update``. Even on ``SSBX`` and ``SSBDEV``, ``ur_update`` only updates parts of the Ureka install. Python packages developed at STScI are updated, along with the STScI IRAF distribution, aXe, HSTCAL, and JWST libraries. Notably this does *not* include NumPy, SciPy, matplotlib, IPython, or AstroPy. To update those, you will have to remove and reinstall the Ureka "core" as described in :ref:`update-ureka-core`

On to the training exercises!
================================

The next chapters explain useful tools with exercises interspered with the text. Save the results of your exercises as you go; you will submit them to your trainer once you've completed the section. If you get stuck, you can always ask your trainer for help!

Wondering who your trainer is for a particular section? Check the `Confluence wiki page <https://confluence.stsci.edu/display/INSRIA/RIA+training>`_ for your training group (find your training group in the sidebar, after expanding the "RIA training" category). Other current RIAs have also done this training, so they're a good resource for quick questions if your trainer is busy.

Without further ado, it's time to learn about :doc:`archives`.

.. rubric:: Footnotes

<<<<<<< HEAD
Without further ado, it's time to learn about :doc:`archives`.

(If you're following along on paper, visit http://TODO/ and choose the link for MAST archive training.)
=======
.. [#externalhelpdesk] There's an *external* helpdesk too, help@stsci.edu. For IT issues, though, you want the internal one. The external one is for astronomers to ask questions about things like the archive, SSB software, data characteristics, and the like.
>>>>>>> af799c2ee6c9eb20b8d1e6e3496888e8a2ee13fd
