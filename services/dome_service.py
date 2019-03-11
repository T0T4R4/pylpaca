#!/usr/bin/env python
#
# Copyright 2013 Rodrigo Ancavil del Pino
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

# -*- coding: utf-8 -*-

import tornado.ioloop
import pyrestful.rest

from pyrestful import mediatypes
from pyrestful.rest import get, post, put, delete

from .device_service import DeviceService


class DomeService(DeviceService):

    # SHOULD BE IMPLEMENTED HERE ONLY THE RESOURCES WHICH CANNOT BE EASILY QUERIED ONTO
    # THE ASCOM DRIVER USING REFLECTION AT THE DeviceService LEVEL.

    @get(_path="/api/v1/{device_type}/{device_number}/shutterstatus", _types=[str, str], _produces=mediatypes.APPLICATION_JSON)
    def getShutterState(self, device_type, device_number):
        super().getResource(device_type, device_number, "ShutterStatus")

    @put(_path="/api/v1/{device_type}/{device_number}/openshutter", _types=[str, str], _produces=mediatypes.APPLICATION_JSON)
    def openShutter(self, device_type, device_number):
        super().getResource(device_type, device_number, "OpenShutter")

    @put(_path="/api/v1/{device_type}/{device_number}/closeshutter", _types=[str, str], _produces=mediatypes.APPLICATION_JSON)
    def closeShutter(self, device_type, device_number):
        super().getResource(device_type, device_number, "CloseShutter")

