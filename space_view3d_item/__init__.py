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
#  Version: 1.1
#
# ##### END INFO BLOCK #####

# blender info
bl_info = {
  'name': 'Item Panel & Batch Naming',
  'author': 'Trentin Frederick (proxe)',
  'version': (1, 1),
  'blender': (2, 75, 0),
  'location': '3D View → Properties Panel → Item',
  'description': 'An improved item panel for the 3D View with included batch naming tools.',
  'category': '3D View'
}

# imports
import bpy
from bpy.props import PointerProperty
from . import interface, settings, operator

##############
## REGISTER ##
##############

# register
def register():
  '''
    Register.
  '''

  # remove default
  bpy.types.VIEW3D_PT_view3d_name.remove(bpy.types.VIEW3D_PT_view3d_name.draw)
  bpy.types.VIEW3D_PT_view3d_name.remove(interface.default.draw)

  # property groups
  bpy.utils.register_class(settings.batch.auto.name)
  bpy.utils.register_class(settings.batch.auto.objects)
  bpy.utils.register_class(settings.batch.auto.constraints)
  bpy.utils.register_class(settings.batch.auto.modifiers)
  bpy.utils.register_class(settings.batch.auto.objectData)
  bpy.utils.register_class(settings.batch.name)
  bpy.utils.register_class(settings.batch.copy)
  bpy.utils.register_class(settings.panel)

  # operators
  bpy.utils.register_class(operator.batch.auto.name)
  bpy.utils.register_class(operator.batch.auto.objects)
  bpy.utils.register_class(operator.batch.auto.constraints)
  bpy.utils.register_class(operator.batch.auto.modifiers)
  bpy.utils.register_class(operator.batch.auto.objectData)
  bpy.utils.register_class(operator.batch.name)
  bpy.utils.register_class(operator.batch.copy)
  bpy.utils.register_class(operator.batch.reset)
  bpy.utils.register_class(operator.batch.transfer)

  # menu
  bpy.utils.register_class(interface.menu)

  # pointer properties
  bpy.types.Screen.batchAutoNameSettings = PointerProperty(type=settings.batch.auto.name)
  bpy.types.Scene.batchAutoNameObjectNames = PointerProperty(type=settings.batch.auto.objects)
  bpy.types.Scene.batchAutoNameConstraintNames = PointerProperty(type=settings.batch.auto.constraints)
  bpy.types.Scene.batchAutoNameModifierNames = PointerProperty(type=settings.batch.auto.modifiers)
  bpy.types.Scene.batchAutoNameObjectDataNames = PointerProperty(type=settings.batch.auto.objectData)
  bpy.types.Screen.batchNameSettings = PointerProperty(type=settings.batch.name)
  bpy.types.Screen.batchCopySettings = PointerProperty(type=settings.batch.copy)
  bpy.types.Screen.itemPanelSettings = PointerProperty(type=settings.panel)

  # append panel
  bpy.types.VIEW3D_PT_view3d_name.append(interface.panel.draw)

# unregister
def unregister():
  '''
    Unregister.
  '''
  # remove panel
  bpy.types.VIEW3D_PT_view3d_name.remove(interface.panel.draw)

  # property groups
  bpy.utils.unregister_class(settings.batch.auto.name)
  bpy.utils.unregister_class(settings.batch.auto.objects)
  bpy.utils.unregister_class(settings.batch.auto.constraints)
  bpy.utils.unregister_class(settings.batch.auto.modifiers)
  bpy.utils.unregister_class(settings.batch.auto.objectData)
  bpy.utils.unregister_class(settings.batch.name)
  bpy.utils.unregister_class(settings.batch.copy)
  bpy.utils.unregister_class(settings.panel)

  # operators
  bpy.utils.unregister_class(operator.batch.auto.name)
  bpy.utils.unregister_class(operator.batch.auto.objects)
  bpy.utils.unregister_class(operator.batch.auto.constraints)
  bpy.utils.unregister_class(operator.batch.auto.modifiers)
  bpy.utils.unregister_class(operator.batch.auto.objectData)
  bpy.utils.unregister_class(operator.batch.name)
  bpy.utils.unregister_class(operator.batch.copy)
  bpy.utils.unregister_class(operator.batch.reset)
  bpy.utils.unregister_class(operator.batch.transfer)

  # menu
  bpy.utils.unregister_class(interface.menu)

  # pointer properties
  del bpy.types.Screen.batchAutoNameSettings
  del bpy.types.Scene.batchAutoNameObjectNames
  del bpy.types.Scene.batchAutoNameConstraintNames
  del bpy.types.Scene.batchAutoNameModifierNames
  del bpy.types.Scene.batchAutoNameObjectDataNames
  del bpy.types.Screen.batchNameSettings
  del bpy.types.Screen.batchCopySettings
  del bpy.types.Screen.itemPanelSettings

  # append default
  bpy.types.VIEW3D_PT_view3d_name.append(interface.default.draw)

if __name__ in '__main__':
  register()
