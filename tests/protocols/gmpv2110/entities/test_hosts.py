# -*- coding: utf-8 -*-
# Copyright (C) 2021 Greenbone Networks GmbH
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

from ...gmpv2110 import Gmpv2110TestCase
from ...gmpv208.entities.hosts import (
    GmpCreateHostTestMixin,
    GmpDeleteHostTestMixin,
    GmpGetHostsTestMixin,
    GmpGetHostTestMixin,
    GmpModifyHostTestMixin,
)


class Gmpv2110CreateHostTestCase(GmpCreateHostTestMixin, Gmpv2110TestCase):
    pass


class Gmpv2110DeleteHostTestCase(GmpDeleteHostTestMixin, Gmpv2110TestCase):
    pass


class Gmpv2110GetHostTestCase(GmpGetHostTestMixin, Gmpv2110TestCase):
    pass


class Gmpv2110GetHostsTestCase(GmpGetHostsTestMixin, Gmpv2110TestCase):
    pass


class Gmpv2110ModifyHostTestCase(GmpModifyHostTestMixin, Gmpv2110TestCase):
    pass