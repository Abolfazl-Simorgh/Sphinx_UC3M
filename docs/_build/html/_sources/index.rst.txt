Welcome to Getting Started with Sphinx's documentation!
=======================================================

Introduction
------------
**Overview:** Sphinx is a tool that generates documentation for Python projects. It converts *reStructuredText* files into formats like HTML, PDF, and more.

**Install Sphinx**
::

   pip install sphinx

**Configure Sphinx**
::

   import os
   import sys
   sys.path.insert(0, os.path.abspath('./'))
   sys.path.insert(0, os.path.abspath('../'))
   extensions = ['sphinx.ext.autodoc']

Python Codes
------------

.. toctree::
   :maxdepth: 2
   :caption: Modules
   
   modules

Tables
------

1. This table demonstrates how to include a table in Sphinx documentation.

+------------+-----------------+--------------------------+
| Parameter  | Type            | Description              |
+============+=================+==========================+
| radius     | float           | The radius of the circle |
+------------+-----------------+--------------------------+
| area       | float           | The area of the circle   |
+------------+-----------------+--------------------------+


2. Example Table with list-table

.. list-table:: Circle Properties
   :header-rows: 1

   * - Parameter
     - Type
     - Description
   * - radius
     - float
     - The radius of the circle
   * - area
     - float
     - The area of the circle


Figures
-------

.. image:: images/LogoAerospace.png
  :width: 500
  :align: center
  :alt: Department of Aerospace LOGO
   This is the caption.

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
