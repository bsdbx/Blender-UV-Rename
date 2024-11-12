#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, see <http://www.gnu.org/licenses/>
#  and write to the Free Software Foundation, Inc., 51 Franklin Street,
#  Fifth Floor, Boston, MA  02110-1301, USA..
#
#  The Original Code is Copyright (C) 2013-2014 by Gorodetskiy Nikita  ###
#  All rights reserved.

from bpy.props import IntProperty, StringProperty
from bpy.types import DATA_PT_uv_texture, Scene
from bpy.utils import register_class, unregister_class

from .batch_rename import *

__all__ = ["register", "unregister"]


def register() -> None:
    register_class(OT_BatchRenameUV)

    Scene.uv_name = StringProperty(
        name="Name",
        default="map",
        description="Name used to iteratively rename UV Channels",
    )
    Scene.uv_suffix = StringProperty(
        name="Suffix", description="Suffix used to iteratively rename UV Channels",
    )
    Scene.idx_offset = IntProperty(
        name="", default=1, min=0, description="Index of the first UV Chnnel name",
    )

    DATA_PT_uv_texture.append(batch_rename_ui)


def unregister() -> None:
    DATA_PT_uv_texture.remove(batch_rename_ui)

    del Scene.idx_offset
    del Scene.uv_suffix
    del Scene.uv_name

    unregister_class(OT_BatchRenameUV)


if __name__ == "__main__":
    register()
