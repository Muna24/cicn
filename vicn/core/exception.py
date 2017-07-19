#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (c) 2017 Cisco and/or its affiliates.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at:
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

class VICNException(Exception): pass

class CommandException(VICNException): pass

class ProcessException(VICNException): pass
class NotConfigured(ProcessException): pass

class ParameterException(VICNException): pass
class InvalidResource(ParameterException): pass

class ABCException(VICNException): pass
class NotImplemented(VICNException): pass

class DependencyException(VICNException): pass
class InitializeException(VICNException): pass
class CheckException(VICNException): pass
class SetupException(VICNException): pass

class ResourceNotFound(VICNException): pass

class VICNWouldBlock(VICNException):
    """
    Exception called when a request would block and the user explicitely
    required non-blocking behaviour
    """
    pass
