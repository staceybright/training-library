****************
Tips and Tricks
****************

.. _update-ureka-core:

Updating the Ureka core
------------------------

Ureka contains a ``ur_update`` command to update components developed at the Institute, but you will periodically need to update the Ureka core. This includes the scripts that set up your terminal sessions to use Ureka, as well as important packages from outside the Institute like IPython, SciPy, AstroPy, etc. and the Python interpreter itself.

.. warning::

   If you have installed Python packages with ``pip install`` without configuring an install prefix, you will lose these packages and have to reinstall them. The command ``pip freeze`` will emit a list of all currently installed packages for your reference.