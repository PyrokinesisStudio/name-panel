# TODO: implement multi-object bone selection
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
    'author': 'Trentin Frederick a.k.a. proxe',
    'version': (1, '8  dev  commit: 484'),
    'blender': (2, 79, 0),
    'location': '3D View \N{Rightwards Arrow} Tool (T) | Property (N)',
    'description': 'In panel datablock name stack with additional naming and productivity tools.',
    'tracker_url': 'https://github.com/proxeIO/name-panel/issues',
    'category': '3D View'}

import bpy

from bpy.utils import register_module, unregister_module, unregister_class
from bpy.props import PointerProperty

from .addon import menu, operator, panel, preferences, properties
from .addon.utilities import get, update


def register():

    register_module(__name__)

    update.handlers()
    if get.preferences(bpy.context).update_check: update.check(bl_info)
    if get.preferences(bpy.context).remove_item_panel: update.item_panel_poll()

    bpy.types.WindowManager.name_panel = PointerProperty(
        type = properties.name_panel,
        name = 'Name Panel Addon',
        description = 'Storage location for name panel addon options')

    keymap = bpy.context.window_manager.keyconfigs.addon.keymaps.new(name='Window')
    kmi = keymap.keymap_items.new('wm.datablock_settings', 'F7', 'PRESS')
    kmi.properties.object_name = ''
    keymap.keymap_items.new('wm.namer', 'NONE', 'PRESS')



def unregister():

    update.handlers(remove=True)
    update.item_panel_poll(restore=True)

    del bpy.types.WindowManager.name_panel

    keymap = bpy.context.window_manager.keyconfigs.addon.keymaps['Window']
    keymap.keymap_items.remove(keymap.keymap_items['wm.namer'])
    keymap.keymap_items.remove(keymap.keymap_items['wm.datablock_settings'])

    unregister_module(__name__)
