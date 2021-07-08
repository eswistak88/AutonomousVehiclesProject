# ----------------------------------------------------------------------
# HTM Community Edition of NuPIC
# Copyright (C) 2015, Numenta, Inc.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero Public License version 3 as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU Affero Public License for more details.
#
# You should have received a copy of the GNU Affero Public License
# along with this program.  If not, see http://www.gnu.org/licenses.
# ----------------------------------------------------------------------

import unittest
import htm.bindings.check as check



class LoadBindingsTest(unittest.TestCase):


  def testImportBindingsInstalled(self):
    """Test that we can import nupic.bindings"""
    check.checkImportBindingsInstalled()


  def testImportBindingsExtensions(self):
    """Test that we can load C extensions under nupic.binding"""
    check.checkImportBindingsExtensions()