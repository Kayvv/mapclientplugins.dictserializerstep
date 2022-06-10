MAP Client Plugin - Dict Serializer
===================================

The **Dict Serializer** is MAP Client plugin for saving a Python dictionary to a location outside the workflow.

.. _fig-mcp-dict-serializer-un-configured-step:

.. figure:: _images/un-configured-step.png
   :alt: Un-configured step icon

   An un-configured *Dict Serializer* step icon.

Configure
---------

This step is used for saving a Python dictionary on the local disk outside the workflow directory.
This step uses a *http://physiomeproject.org/workflow/1.0/rdf-schema#dict* and saves it in JSON format to a location on the local disk.
To choose the output location use the *...* button to open a file chooser dialog.
The *Output* input is used to hold the relative path from the workflow to the saved JSON file.

.. _fig-mcp-dict-serializer-configure-dialog:

.. figure:: _images/step-configuration-dialog.png
   :alt: Step configure dialog

   *Dict Serializer* step configuration dialog.

The *Use output default location* checkbox is *deprecated* and will be removed in a future release.

Ports
-----

This plugin:

* **uses**:

  * *http://physiomeproject.org/workflow/1.0/rdf-schema#dict*
