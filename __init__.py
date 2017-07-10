'''
This program is free software: you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free Software
Foundation, either version 3 of the License, or (at your option) any later
version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with
this program. If not, see <http://www.gnu.org/licenses/>.
'''

bl_info = {
    'name': 'Name Panel',
    'author': 'proxe',
    'version': (1, 8, 473),
    'blender': (2, 78, 0),
    'location': '3D View \N{Rightwards Arrow} Property or Tool Shelf.',
    'description': 'In panel datablock name stack with additional naming tools.',
    'wiki_url': 'https://cgcookiemarkets.com/all-products/name-panel/?view=docs',
    'tracker_url': 'https://github.com/proxeIO/name-panel/issues',
    'category': '3D View'
}

import bpy
from bpy.utils import register_module, unregister_module, unregister_class
from bpy.props import PointerProperty

from .addon import menu, operator, panel, preferences, properties
from .addon.utilities import get, update


def register():


    register_module(__name__)

    bpy.types.WindowManager.name_panel = PointerProperty(
        type = properties.name_panel,
        name = 'Name Panel Addon',
        description = 'Storage location for name panel addon options',
    )

    try:
        if get.preferences(bpy.context).remove_item:
            unregister_class(bpy.types.VIEW3D_PT_view3d_name)
    except: pass

    keymap = bpy.context.window_manager.keyconfigs.addon.keymaps.new(name='Window')
    keymap.keymap_items.new('wm.namer', 'F7', 'PRESS')

    update.handlers()


def unregister():

    del bpy.types.WindowManager.name_panel

    keymap = bpy.context.window_manager.keyconfigs.addon.keymaps['Window']
    keymap.keymap_items.remove(keymap.keymap_items['wm.namer'])

    update.handlers(remove=True)

    unregister_module(__name__)
