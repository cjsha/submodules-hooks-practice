
Miniscope DAQ and UCLA Miniscope v4
**************************************************************

.. image:: ../../../../source/_static/miniscopedaq-miniscopev4.jpg

There are two applications that can be used to automate commutation with the Miniscope DAQ and UCLA Miniscope v4.
They are :ref:`Bonsai_:dry:`shorthand`` and :ref:`Miniscope-DAQ-QT-GUI_:dry:`shorthand``.

.. _Bonsai_:dry:`shorthand`:

Bonsai
#######

This section outlines how to use Bonsai software to automate commutation of the coaxial
tether between a UCLA Miniscope v4 mounted on a freely moving animal and a UCLA Miniscope DAQ.

#. Follow the :ref:`quick_start_:dry:`shorthand`` to ensure you can control the commutator using Bonsai.

#. Install the **Bonsai.Miniscope** Package from Bonsai's package manager.

    -   Select Community Feed

        ..  image:: ../../../../source/_static/bonsai-community-feed.png
            :alt: Screenshot for selecting package source

    -   Install **Bonsai.Miniscope**

        ..  image:: ../../../../source/_static/install-bonsai-miniscope.png
            :alt: Screenshot for installing Bonsai.Miniscope

#.  Mount the commutator and establish all electrical connections according to
    the information found in the :ref:`mounting_:dry:`shorthand``.

#.  Download, configure, and run the following Bonsai workflow for automating commutation using orientation
    data from the miniscope’s on-board IMU sensor:

    ..  raw:: html

        {% with static_path = '../../../../../source/_static', name = 'miniscopedaq-miniscopev4-commutate' %}
            {% include 'workflow.html' %}
        {% endwith %}

    ..  note:: Be sure to configure the **PortName** property of the
        **Commutator** node to reflect the port to which the commutator is
        connected.


#.  Run the workflow in Bonsai. If all above steps are correctly performed, the
    commutator will follow miniscope rotations

.. _Miniscope-DAQ-QT-GUI_:dry:`shorthand`:

Miniscope-DAQ-QT-GUI
#################################

This section outlines how to use Miniscope software to automate commutation of the coaxial
tether between a UCLA Miniscope v4 mounted on a freely moving animal and a UCLA Miniscope DAQ.

.. TODO:: document
