#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import kde5
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    #shelltools.system("sed -i 's|5.11.0|5.10.0|g' CMakeLists.txt")
    kde5.configure("-DCMAKE_INSTALL_PREFIX=/usr \
                    -DCMAKE_INSTALL_LIBDIR=lib \
                    -DBUILD_TESTING=OFF")

def build():
    kde5.make()

def install():
    kde5.install()

    # Conflicts with plasma-workspace
    pisitools.remove("/usr/share/doc/HTML")
    pisitools.remove("/usr/share/locale/")
    pisitools.remove("/usr/lib/qt5/plugins/kcms/kcm_translations.so")
    pisitools.remove("/usr/share/kpackage/kcms/kcm_translations/*")

    pisitools.dodoc("HACKING", "COPYING")
