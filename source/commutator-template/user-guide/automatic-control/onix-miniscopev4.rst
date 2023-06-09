
ONIX and UCLA Miniscope v4
******************************************************************

.. image:: ../../../../source/_static/onix-miniscopev4.jpg

This section outlines how to use Bonsai software to automate commutation of the coaxial
tether between a UCLA Miniscope v4 mounted on a freely moving animal and ONIX.

#. Follow the :ref:`quick_start_:dry:`shorthand`` to ensure you can control the commutator using Bonsai.

#. Install the **Bonsai.ONIX** Package from Bonsai's package manager.

    -   Select Community Feed

        ..  image:: ../../../../source/_static/bonsai-community-feed.png
            :alt: Screenshot for selecting package source

    -   Install **Bonsai.ONIX**

        ..  image:: ../../../../source/_static/install-bonsai-onix.png
            :alt: Screenshot for installing Bonsai.Onix

    ..  Note:: You will not be able to open the workflow if ONIX is not already properly installed and connected

#.  Download, configure, and run the following Bonsai workflow for automating commutation using orientation
    data from the headstages’s on-board IMU sensor:

    ..  raw:: html

        {% with static_path = '../../../../../source/_static', name = 'onix-miniscopev4-commutate' %}
            {% include 'workflow.html' %}
        {% endwith %}

    ..  note::  Be sure to configure the **PortName** property of the
                **Commutator** node to reflect the port to which the commutator is
                connected.


#.  Run the workflow in Bonsai. If all above steps are correctly performed, the commutator will follow headstage rotations
