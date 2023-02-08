#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import cmaketools, pisitools

i = ''.join([
    ' -DCMAKE_BUILD_TYPE=Release',
    ' -DLIBDEFLATE_USE_SHARED_LIB=ON',
    ' -DLIBDEFLATE_BUILD_STATIC_LIB=OFF',
    ' -B_build -L '
    ])

def setup():
	cmaketools.configure(i)

def build():
	cmaketools.make("-C _build")

def install():
	cmaketools.install("-C _build")

	pisitools.dodoc("NEWS.md")
