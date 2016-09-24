Content
=======

A nROS node for controlling a Youpi robotic arm.

Content
=======

This package implements a nROS node exposing most of the commands allowing to control the arm provided
by the `Youpi arm control library <https://github.com/pobot-pybot/pybot-youpi2>`_.

Thanks to it, any application or extension within the nROS world,
or connected to it can interact with the arm, without having to deal with the inner details of the steppers
control or whatever similar.

The advantage of exposing as a nROS node over the direct library approach, is that it makes possible
to have several application to interact with it at the same time. Of course they need to coordinate
themselves to avoid sending conflicting commands, but since the low level communication is funneled
by the node, there is no problem with a shared access to the hardware level layers (e.g. SPI bus use to
control the stepper drivers). The node plays thus the same role as a driver for any piece of hardware.

Dependencies
============

In addition to `nROS core <https://github.com/pobot-nros/nros-core>`_, this project depends on the
Youpi interfacing library available on `GitHub <https://github.com/pobot-pybot/pybot-youpi2>`_ too.
