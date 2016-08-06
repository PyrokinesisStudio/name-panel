
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

# imports
import bpy
from bpy.types import Menu

class specials(Menu):
  '''
    Menu for name panel operators.
  '''
  bl_idname = 'VIEW3D_MT_name_panel_specials'
  bl_label = 'Operators'
  bl_description = 'Operators and settings.'

  def draw(self, context):
    '''
      Draw the menu body.
    '''

    # layout
    layout = self.layout

    # option
    option = context.scene.NamePanel

    # batch auto name
    layout.operator('view3d.batch_auto_name', icon='AUTO')

    # bath name
    op = layout.operator('wm.batch_name', icon='SORTALPHA')
    op.simple = False
    op.quickBatch = False

    # batch copy
    layout.operator('view3d.batch_copy_name', icon='COPYDOWN')

    # separate
    layout.separator()

    # is display names
    if option.displayNames:

        # pin active object
        layout.prop(option, 'pinActiveObject')

    # is display bone names
    if option.displayBones:

        # pin active bone
        layout.prop(option, 'pinActiveBone')

    # hide search
    layout.prop(option, 'hideFindReplace')

    # separate
    layout.separator()

    # reset panel
    op = layout.operator('wm.reset_name_panel_settings', text='Reset Panel', icon='LOAD_FACTORY')
    op.panel = True
    op.auto = False
    op.names = False
    op.name = False
    op.copy = False

    # is option.regex
    if option.regex or context.scene.BatchName.regex:

        # separate
        layout.separator()

        layout.operator('wm.regular_expression_cheatsheet', icon='NEW')
