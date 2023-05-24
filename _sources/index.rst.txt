.. _oec:

*************************************************
Open Ephys Commutators
*************************************************

..  image:: ../source/_static/commutator-front-thin.jpg
    :align: left
    :width: 190
    :alt: image of coaxial commutator

Open-ephys commutators provide nearly **torque-free** tether management for freely moving recordings. Inertial-
measurement units (IMUs) or video-based pose-estimation methods (e.g.
`DeepLabCut <https://github.com/DeepLabCut/DeepLabCut">`_ or `SLEAP <https://github.com/talmolab/sleap>`_) provide
real-time measurements of animal orientation. Therefore, these technologies can be used  to drive active commutation
instead of relying on tether torque measurement, which is used in conventional active commutators. This permits the
use of exceptionally thin tethers (such as these
`micro coaxial cables <https://open-ephys.github.io/onix-docs/Hardware%20Guide/Headstages/headstage-64/index.html>`_)
that promote natural animal behavior but are to flexible to be used with conventional commutators.

Currently available Open Ephys Commutators include:

*   Coax Commutator:
        Compatible with `UCLA Miniscopes <https://open-ephys.org/miniscope-v4/miniscope-v4>`_ and
        `Open Ephys Headstages <https://open-ephys.github.io/onix-docs/Hardware%20Guide/Headstages/headstage-64/index.html>`_
*   SPI Commutator:
        Compatible with headstages that use SPI digital communication such as those from
        `Open Ephys <https://open-ephys.org/acquisition-system/low-profile-spi-headstage-64ch>`_ and
        `Intan <https://intantech.com/pricing.html>`_

To start using your your Open Ephys Commutator, please refer to the guide that corresponds with your device:

.. grid::

    .. grid-item-card:: Coaxial Commutator
        :text-align: center
        :link-type: doc
        :link: coax/index
        :img-bottom: ../source/_static/coax-cables.jpg
        :img-alt: image of coax cables
        :shadow: md

    .. grid-item-card:: SPI Commutator
        :text-align: center
        :link-type: doc
        :link: spi/index
        :img-bottom: ../source/_static/spi-cables.jpg
        :img-alt: image of spi cables
        :shadow: md


.. toctree::
    :hidden:

    coax/index
    spi/index