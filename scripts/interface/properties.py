
# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or modify it
#  under the terms of the GNU General Public License as published by the Free
#  Software Foundation; either version 2 of the License, or (at your option)
#  any later version.
#
#  This program is distributed in the hope that it will be useful, but WITHOUT
#  ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
#  this program; if not, write to the Free Software Foundation, Inc.,
#  FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for
#  more details.
#
#  You should have received a copy of the GNU General Public License along with
#  51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

# imports
import bpy
from bpy.types import Panel

# tools properties
class toolsProperties(Panel):
  '''
    Name Panel context sensitive properties panel for the 3D View toolshelf.
  '''
  bl_idname = 'VIEW3D_PT_TOOLS_properties'
  bl_space_type = 'VIEW_3D'
  bl_label = 'Properties'
  bl_region_type = 'TOOLS'
  bl_category = 'Name'

  # draw
  def draw(self, context):
    '''
    Properties panel body.
    '''

    # main
    main(self, context)

# UI properties
class UIProperties(Panel):
  '''
    Name Panel context sensitive properties panel for the 3D View property shelf.
  '''
  bl_idname = 'VIEW3D_PT_UI_properties'
  bl_space_type = 'VIEW_3D'
  bl_label = 'Properties'
  bl_region_type = 'UI'

  # draw
  def draw(self, context):
    '''
      Properties panel body.
    '''

    # main
    main(self, context)

# main
def main(self, context):
  '''
    Get the owner, target and context of name panel and populate accordingly.
  '''
