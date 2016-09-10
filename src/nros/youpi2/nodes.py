# -*- coding: utf-8 -*-

import dbus.service

from nros.core.node import NROSNode, DEFAULT_SERVICE_OBJECT_PATH
from pybot.youpi2.model import YoupiArm

__author__ = 'Eric Pascual'


class ArmNode(NROSNode):
    SO_PATH = DEFAULT_SERVICE_OBJECT_PATH       #: path of the arm service object

    _arm = None
    _so = None

    def init_node(self):
        self._arm = YoupiArm()
        self._so = None

    def configure(self, cfg_file):
        pass

    def prepare_node(self):
        self._arm.initialize()

    def setup_dbus_environment(self, connection):
        self._so = ArmServiceObject(
            self._arm,
            connection, self.SO_PATH,
            logger=self._logger.getChild('arm') if self._logger else None
        )

    def shutdown(self):
        self._arm.shutdown()


class ArmServiceObject(dbus.service.Object):
    INTERFACE_NAME = 'org.pobot.nros.youpi'

    MOTOR_BASE, MOTOR_SHOULDER, MOTOR_ELBOW, MOTOR_WRIST, MOTOR_HAND = \
        YoupiArm.MOTOR_BASE, YoupiArm.MOTOR_SHOULDER, YoupiArm.MOTOR_ELBOW, YoupiArm.MOTOR_WRIST, \
        YoupiArm.MOTOR_HAND_ROT

    def __init__(self, arm, connection, svc_obj_path, logger=None):
        """
        :param YoupiArm arm: the arm
        :param dbus.connection.Connection connection: the D-Bus connection
        :param str svc_obj_path: the path to the service object
        :param logger: class level logger
        """
        self._logger = logger
        self._arm = arm
        super(ArmServiceObject, self).__init__(connection, svc_obj_path)
        if self._logger:
            self._logger.info('service object created at path "%s"', svc_obj_path)

    @dbus.service.method(INTERFACE_NAME, in_signature='b')
    def open_gripper(self, wait):
        self._arm.open_gripper(wait)

    @dbus.service.method(INTERFACE_NAME, in_signature='b')
    def close_gripper(self, wait):
        self._arm.close_gripper(wait)

    @dbus.service.method(INTERFACE_NAME, in_signature='b')
    def calibrate_gripper(self, wait):
        self._arm.calibrate_gripper(wait)

    @dbus.service.method(INTERFACE_NAME, in_signature='ai')
    def seek_origins(self, joint_sequence):
        self._arm.seek_origins(joint_sequence)

    @dbus.service.method(INTERFACE_NAME, in_signature='ib')
    def rotate_hand(self, angle, wait):
        self._arm.rotate_hand(angle, wait)

    @dbus.service.method(INTERFACE_NAME, in_signature='ib')
    def rotate_hand_to(self, angle, wait):
        self._arm.rotate_hand_to(angle, wait)

    @dbus.service.method(INTERFACE_NAME, in_signature='a{id}b')
    def move(self, angles, wait):
        self._arm.coupled_joints_move(angles, wait)

    @dbus.service.method(INTERFACE_NAME, in_signature='a{id}b')
    def goto(self, angles, wait):
        self._arm.coupled_joints_goto(angles, wait)

    @dbus.service.method(INTERFACE_NAME, in_signature='b')
    def shutdown(self, emergency):
        self._arm.shutdown(emergency)

    @dbus.service.method(INTERFACE_NAME)
    def soft_hi_Z(self):
        self._arm.soft_hi_Z()

    @dbus.service.method(INTERFACE_NAME)
    def hard_hi_Z(self):
        self._arm.hard_hi_Z()

    @dbus.service.method(INTERFACE_NAME, out_signature='ad')
    def get_current_positions(self):
        return self._arm.get_joint_positions()


def start_node():
    ArmNode.main()
