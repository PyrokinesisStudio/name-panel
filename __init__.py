
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
  'location': '3D View → Toolshelf → Name Tab',
  'description': 'An improved 3D view name panel with batch name tools.',
  'wiki_url': '',
  'tracker_url': 'https://github.com/trentinfrederick/name-panel/issues',
  'category': '3D View'
}

# imports
import bpy
from bpy.types import AddonPreferences
from bpy.props import *
from .scripts import settings as PropertyGroup
from .scripts.interface import button, icon, menu, panel
from .scripts.operator import active, auto, batch, copy, popups, select, settings

# preferences
class preferences(AddonPreferences):
  '''
    Add-on user preferences.
  '''
  bl_idname = __package__

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

  def draw(self, context):

    # layout
    layout = self.layout

    # enable popups
    # layout.prop(self, 'dialogues')
    layout.prop(self, 'popups')

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

  # preferences
  bpy.utils.register_class(preferences)

  # panel
  bpy.utils.register_class(panel.name)

  # menus
  bpy.utils.register_class(menu.specials)

  # operators
  bpy.utils.register_class(auto.name)
  bpy.utils.register_class(auto.objects)
  bpy.utils.register_class(auto.constraints)
  bpy.utils.register_class(auto.modifiers)
  bpy.utils.register_class(auto.objectData)
  bpy.utils.register_class(batch.name)
  bpy.utils.register_class(batch.generateCheatsheet)
  bpy.utils.register_class(copy.name)
  bpy.utils.register_class(settings.reset)
  bpy.utils.register_class(settings.transfer)
  bpy.utils.register_class(active.object)
  bpy.utils.register_class(active.bone)
  bpy.utils.register_class(select.vertexGroup)
  bpy.utils.register_class(popups.constraint)
  bpy.utils.register_class(popups.modifier)

  # property groups
  bpy.utils.register_class(PropertyGroup.batch.auto.name)
  bpy.utils.register_class(PropertyGroup.batch.auto.objects)
  bpy.utils.register_class(PropertyGroup.batch.auto.constraints)
  bpy.utils.register_class(PropertyGroup.batch.auto.modifiers)
  bpy.utils.register_class(PropertyGroup.batch.auto.objectData)
  bpy.utils.register_class(PropertyGroup.batch.name)
  bpy.utils.register_class(PropertyGroup.batch.copy)
  bpy.utils.register_class(PropertyGroup.panel)

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

  # preferences
  bpy.utils.unregister_class(preferences)

  # panel
  bpy.utils.unregister_class(panel.name)

  # menu
  bpy.utils.unregister_class(menu.specials)

  # operators
  bpy.utils.unregister_class(auto.name)
  bpy.utils.unregister_class(auto.objects)
  bpy.utils.unregister_class(auto.constraints)
  bpy.utils.unregister_class(auto.modifiers)
  bpy.utils.unregister_class(auto.objectData)
  bpy.utils.unregister_class(batch.name)
  bpy.utils.unregister_class(batch.generateCheatsheet)
  bpy.utils.unregister_class(copy.name)
  bpy.utils.unregister_class(settings.reset)
  bpy.utils.unregister_class(settings.transfer)
  bpy.utils.unregister_class(active.object)
  bpy.utils.unregister_class(active.bone)
  bpy.utils.unregister_class(select.vertexGroup)
  bpy.utils.unregister_class(popups.constraint)
  bpy.utils.unregister_class(popups.modifier)

  # property groups
  bpy.utils.unregister_class(PropertyGroup.batch.auto.name)
  bpy.utils.unregister_class(PropertyGroup.batch.auto.objects)
  bpy.utils.unregister_class(PropertyGroup.batch.auto.constraints)
  bpy.utils.unregister_class(PropertyGroup.batch.auto.modifiers)
  bpy.utils.unregister_class(PropertyGroup.batch.auto.objectData)
  bpy.utils.unregister_class(PropertyGroup.batch.name)
  bpy.utils.unregister_class(PropertyGroup.batch.copy)
  bpy.utils.unregister_class(PropertyGroup.panel)

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

if __name__ in '__main__':
  register()
