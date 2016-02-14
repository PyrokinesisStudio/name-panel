
# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or modify it
#  under the terms of the GNU General Public License as published by the Free
#  Software Foundation; either version 2 of the License, or (at your option)
#  any later version.
#
#  This program is distributed in the hope that it will be useful, but WITHOUT
#  ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
#  FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for
#  more details.
#
#  You should have received a copy of the GNU General Public License along with
#  this program; if not, write to the Free Software Foundation, Inc.,
#  51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

# ##### BEGIN INFO BLOCK #####
#
#  Author: Trentin Frederick (a.k.a, proxe)
#  Contact: trentin.shaun.frederick@gmail.com
#  Version: 1.5
#
# ##### END INFO BLOCK #####

# blender info
bl_info = {
  'name': 'Name Panel',
  'author': 'Trentin Frederick (proxe)',
  'version': (1, 5),
  'blender': (2, 76, 0),
  'location': '3D View → Tool or Property Shelf → Name',
  'description': 'An improved 3D view name panel with batch name tools.',
  'tracker_url': 'https://github.com/trentinfrederick/name-panel/issues',
  'category': '3D View'
}

# imports
import bpy
import os
from bpy.types import AddonPreferences
from bpy.props import *
from .scripts import settings as PropertyGroup
from .scripts.interface import button, icon, menu, panel
from .scripts.operator import active, auto, batch, copy, shortcuts, select, settings, text

# addon
addon = bpy.context.user_preferences.addons.get(__name__)

# preferences
class preferences(AddonPreferences):
  '''
    Add-on user preferences.
  '''
  bl_idname = __name__

  # dialogues
  dialogues = BoolProperty(
    name = 'Enable Operator Confirm Dialogues',
    description = 'Enable confirm dialogues for batch operators',
    default = True
  )

  # popups
  popups = BoolProperty(
    name = 'Enable Pop Ups (Experimental)',
    description = 'Experimental feature, only works for modifiers and constraints, if even then.',
    default = False
  )

  # location
  location = EnumProperty(
    name = 'Panel Location',
    description = 'The 3D view shelf to use. (Requires Restart)',
    items = [
      ('TOOLS', 'Tool Shelf', 'Places the Name panel in the tool shelf under the tab labeled \'Name\''),
      ('UI', 'Property Shelf', 'Places the Name panel in the property shelf.')
    ],
    default = 'UI'
  )

  def draw(self, context):

    # layout
    layout = self.layout

    # enable popups
    # layout.prop(self, 'dialogues')
    # layout.prop(self, 'popups')

    # row
    row = layout.row()
    row.prop(self, 'location', expand=True)

    # label
    layout.label(text='Links:')

    # split
    split = layout.split(align=True)
    split.scale_y = 2

    # prop = split.operator('wm.url_open', text='BlenderMarket')
    # prop.url = ''

    prop = split.operator('wm.url_open', text='BlenderArtists')
    prop.url = 'http://blenderartists.org/forum/showthread.php?272086-Addon-Item-Panel-amp-Batch-Naming-1-5'

    # prop = split.operator('wm.url_open', text='BlendSwap')
    # prop.url = 'http://www.blendswap.com/blends/view/82472'

    prop = split.operator('wm.url_open', text='Github')
    prop.url = 'https://github.com/trentinfrederick/name-panel'

# register
def register():
  '''
    Register.
  '''

  # remove blender default panel
  try:
    bpy.utils.unregister_class(bpy.types.VIEW3D_PT_view3d_name)
  except:
    pass

  # register module
  bpy.utils.register_module(__name__)

  # shelf position
  # addon
  if addon:
    if addon.preferences['location'] == 0:
      bpy.utils.unregister_class(panel.UIName)
    else:
      bpy.utils.unregister_class(panel.toolsName)
  else:
    bpy.utils.unregister_class(panel.toolsName)

  # pointer properties
  # batch auto name settings
  bpy.types.Scene.BatchAutoName = PointerProperty(
    type = PropertyGroup.batch.auto.name,
    name = 'Batch Auto Name Settings',
    description = 'Storage location for the batch auto name operator settings.'
  )

  # batch auto name object names
  bpy.types.Scene.BatchAutoName_ObjectNames = PointerProperty(
    type = PropertyGroup.batch.auto.objects,
    name = 'Batch Auto Name Object Names',
    description = 'Storage location for the object names used during the auto name operation.'
  )

  # batch auto name constraint names
  bpy.types.Scene.BatchAutoName_ConstraintNames = PointerProperty(
    type = PropertyGroup.batch.auto.constraints,
    name = 'Batch Auto Name Constraint Names',
    description = 'Storage location for the constraint names used during the auto name operation.'
  )

  # batch auto name modifier names
  bpy.types.Scene.BatchAutoName_ModifierNames = PointerProperty(
    type = PropertyGroup.batch.auto.modifiers,
    name = 'Batch Auto Name Modifier Names',
    description = 'Storage location for the modifier names used during the auto name operation.'
  )

  # batch auto name object data names
  bpy.types.Scene.BatchAutoName_ObjectDataNames = PointerProperty(
    type = PropertyGroup.batch.auto.objectData,
    name = 'Batch Auto Name Object Data Names',
    description = 'Storage location for the object data names used during the auto name operation.'
  )

  # batch name settings
  bpy.types.Scene.BatchName = PointerProperty(
    type = PropertyGroup.batch.name,
    name = 'Batch Name Settings',
    description = 'Storage location for the batch name operator settings.'
  )

  # batch copy settings
  bpy.types.Scene.BatchCopyName = PointerProperty(
    type = PropertyGroup.batch.copy,
    name = 'Batch Name Copy Settings',
    description = 'Storage location for the batch copy name operator settings.'
  )

  # name panel settings
  bpy.types.Scene.NamePanel = PointerProperty(
    type = PropertyGroup.panel,
    name = 'Name Panel Settings',
    description = 'Storage location for the name panel settings.'
  )

  # append
  bpy.types.OUTLINER_HT_header.append(button.batchName)

# unregister
def unregister():
  '''
    Unregister.
  '''

  # register module
  bpy.utils.unregister_module(__name__)

  # pointer properties
  del bpy.types.Scene.BatchAutoName
  del bpy.types.Scene.BatchAutoName_ObjectNames
  del bpy.types.Scene.BatchAutoName_ConstraintNames
  del bpy.types.Scene.BatchAutoName_ModifierNames
  del bpy.types.Scene.BatchAutoName_ObjectDataNames
  del bpy.types.Scene.BatchName
  del bpy.types.Scene.BatchCopyName
  del bpy.types.Scene.NamePanel

  # remove batch name button
  bpy.types.OUTLINER_HT_header.remove(interface.button.batchName)

if __name__ == '__main__':
  register()
