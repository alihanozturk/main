#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import mesontools
from pisi.actionsapi import pisitools

def setup():
    mesontools.configure("-Degl_device=true \
                          -Dudev=true \
                          -Dnative_backend=true \
                          -Dprofiler=false \
                          -Dintrospection=true \
                          -Dxwayland_path=/usr/bin/Xwayland \
                          -Dxwayland_initfd=disabled \
                          -Dinstalled_tests=false")

def build():
    mesontools.build()

def install():
    mesontools.install()

    pisitools.dodoc("NEWS", "README.md", "COPYING")

