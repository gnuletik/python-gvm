# -*- coding: utf-8 -*-
# Copyright (C) 2018-2022 Greenbone AG
#
# SPDX-License-Identifier: GPL-3.0-or-later
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import unittest
from collections import OrderedDict

from gvm.xml import XmlCommand


class XmlCommandTestCase(unittest.TestCase):
    def test_should_create_command(self):
        cmd = XmlCommand("foo")

        self.assertEqual(cmd.to_string(), "<foo/>")

    def test_should_allow_to_add_element(self):
        cmd = XmlCommand("foo")
        cmd.add_element("bar")

        self.assertEqual(cmd.to_string(), "<foo><bar/></foo>")

    def test_should_allow_to_add_element_with_text(self):
        cmd = XmlCommand("foo")
        cmd.add_element("bar", "1")

        self.assertEqual(cmd.to_string(), "<foo><bar>1</bar></foo>")

    def test_should_allow_to_set_attribute(self):
        cmd = XmlCommand("foo")
        cmd.set_attribute("bar", "1")

        self.assertEqual(cmd.to_string(), '<foo bar="1"/>')

    def test_should_allow_to_set_attributes(self):
        cmd = XmlCommand("foo")
        cmd.set_attributes(OrderedDict([("bar", "1"), ("baz", "2")]))

        self.assertEqual(cmd.to_string(), '<foo bar="1" baz="2"/>')

    def test_should_convert_to_string(self):
        cmd = XmlCommand("foo")

        self.assertEqual(str(cmd), "<foo/>")

    def test_invalid_xml(self):
        with self.assertRaises(ValueError):
            XmlCommand("Foo & Bar")

    def test_xml_escaping(self):
        cmd = XmlCommand("foo")
        cmd.add_element("bar", "Foo & Bar")

        self.assertEqual(cmd.to_string(), "<foo><bar>Foo &amp; Bar</bar></foo>")

        cmd = XmlCommand("foo")
        cmd.set_attribute("bar", "Foo & Bar")

        self.assertEqual(cmd.to_string(), '<foo bar="Foo &amp; Bar"/>')

        cmd = XmlCommand("foo")
        cmd.set_attribute("bar", 'Foo "Bar"')

        self.assertEqual(cmd.to_string(), '<foo bar="Foo &quot;Bar&quot;"/>')


if __name__ == "__main__":
    unittest.main()
