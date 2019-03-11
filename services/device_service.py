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
from tornado.httputil import parse_body_arguments

import pyrestful.rest
import json

from pyrestful import mediatypes
from pyrestful.rest import get, post, put, delete

import sys
from .config import getDriverInstance

from .httpresponses import HttpSuccessResponse, HttpErrorResponse

class DeviceService(pyrestful.rest.RestHandler):

    def getResource(self, device_type, device_number, resource):
        driver = getDriverInstance(device_type, device_number)
        response = None

        try:
            if (driver is None):
                raise ValueError("Driver not loaded. Check your server configuration.")
                
            # Dynamically call the method/property if it exists 
            attr = getattr(driver, resource)
            if callable(attr):
                # might be a class instance method
                value = attr()
            else:
                # might be a property
                value = attr

            response = {
                "ClientTransactionID": 0,
                "ServerTransactionID": 0,
                "ErrorNumber": 0,
                "ErrorMessage": ""
            }

            if not (value is None):
                response["Value"] = value
            
            pass
        except Exception as exc:
            response = {
                "Value": exc
            }
            self.set_status(500, exc)
    
        self.write(response) 

        self.finish() 

    def setResource(self, device_type, device_number, resource, resource_value):
        driver = getDriverInstance(device_type, device_number)
        response = None

        try:
            if (driver is None):
                raise ValueError("Driver not loaded. Check your server configuration.")
                
            # Dynamically call the method/property if it exists 
            setattr(driver, resource, resource_value)

            response = {
                "ClientTransactionID": 0,
                "ServerTransactionID": 0,
                "ErrorNumber": 0,
                "ErrorMessage": ""
            }
            pass
        except Exception as exc:
            response = {
                "Value": exc
            }
            self.set_status(500, exc)
    
        self.write(response) 

        self.finish() 

    @get(_path="/api/v1/{device_type}/{device_number}/connected", _types=[str, int, str], _produces=mediatypes.APPLICATION_JSON)
    def getConnected(self, device_type, device_number):
        self.getResource(device_type, device_number, "Connected")
        
    @put(_path="/api/v1/{device_type}/{device_number}/connected", _types=[str, int, str], _produces=mediatypes.APPLICATION_JSON)
    def setConnected(self, device_type, device_number):
        # read www/x-www-form-urlencoded parameters
        
        if self.request.headers['Content-Type'] == 'application/x-www-form-urlencoded':
            values = {}
            files = {}
            parse_body_arguments('application/x-www-form-urlencoded', self.request.body, values, files)
            value_str = values["Connected"][0].decode()
            value = (value_str == 'True')
            self.setResource(device_type, device_number, "Connected", value)
        else:
            self.set_status(400, "Value error")

    # TODO PUT !
