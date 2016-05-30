
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

  # draw header
  def draw_header(self, context):
    '''
      Properties panel header.
    '''
    # layout
    layout = self.layout

    # panel
    panel = context.scene.PropertiesPanel

    # display active
    layout.prop(panel, 'displayActive', text='')

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

  # draw header
  def draw_header(self, context):
    '''
      Properties panel header.
    '''
    # layout
    layout = self.layout

    # panel
    panel = context.scene.PropertiesPanel

    # display active
    layout.prop(panel, 'displayActive', text='')

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
    Get the owner, target and context of name panel, populate accordingly.
  '''

  # panel
  panel = context.scene.NamePanel

  # display active
  displayActive = context.scene.PropertiesPanel.displayActive

  # layout
  layout = self.layout

  # context
  layout.prop(panel, 'context', text='')

  # object
  if panel.context == 'OBJECT':

    # datablock
    datablock = context.object if displayActive else bpy.data.objects[panel.target]

    # object
    Object(self, context, layout, datablock)

  # group
  elif panel.context == 'GROUP':

    # group
    Group(self, context, layout, bpy.data.groups[panel.target])

  # action
  elif panel.context == 'ACTION':

    # action
    Action(self, context, layout, bpy.data.actions[panel.target])

  # grease pencil
  elif panel.context == 'GREASE_PENCIL':

    # grease pencil
    GreasePencil(self, context, layout, bpy.data.grease_pencil[panel.target])

  # constraint
  elif panel.context == 'CONSTRAINT':

    # constraint
    Constraint(self, context, layout, bpy.data.objects[panel.owner].constraints[panel.target])

  # modifier
  elif panel.context == 'MODIFIER':

    # modifier
    Modifier(self, context, layout, bpy.data.objects[panel.owner].modifiers[panel.target])

  # object data
  elif panel.context == 'OBJECT_DATA':

    # datablock
    datablock = context.object if displayActive else bpy.data.objects[panel.target]

    # object
    ObjectData(self, context, layout, datablock)

  # bone group
  elif panel.context == 'BONE_GROUP':

    # bone group
    BoneGroup(self, context, layout, bpy.data.objects[panel.target])

  # bone
  elif panel.context == 'BONE':

    # datablock
    datablock = context.active_bone if displayActive else bpy.data.armatures[panel.owner].bones[panel.target] if context.mode == 'POSE' else bpy.data.armatures[panel.owner].editable_bones[panel.target]

    # bone
    Bone(self, context, layout, datablock)


  # bone constraint
  elif panel.context == 'BONE_CONSTRAINT':

    # bone constraint
    BoneConstraint(self, context, layout, bpy.data.objects[context.active_object.name].pose.bones[panel.owner].constraints[panel.target])

  # vertex group
  elif panel.context == 'VERTEX_GROUP':

    # vertex group
    VertexGroup(self, context, layout, bpy.data.objects[panel.owner].vertex_groups[panel.target])

  # shapekey
  elif panel.context == 'SHAPEKEY':

    # shapekey
    Shapekey(self, context, layout, bpy.data.objects[panel.owner].data.shape_keys.key_blocks[panel.target])

  # uv
  elif panel.context == 'UV':

    # uv
    UV(self, context, layout, bpy.data.objects[panel.owner].data.uv_textures[panel.target])

  # vertex color
  elif panel.context == 'VERTEX_COLOR':

    # vertex color
    VertexColor(self, context, layout, bpy.data.objects[panel.owner].data.vertex_colors[panel.target])

  # material
  elif panel.context == 'MATERIAL':

    # material
    Material(self, context, layout, bpy.data.materials[panel.target])

  # texture
  elif panel.context == 'TEXTURE':

    # texture
    Texture(self, context, layout, bpy.data.textures[panel.target])

  # particle system
  elif panel.context == 'PARTICLE_SYSTEM':

    # particle systems
    ParticleSystem(self, context, layout, bpy.data.objects[panel.owner].particle_systems[panel.target])

  # particle setting
  elif panel.context == 'PARTICLE_SETTING':

    # particle settings
    ParticleSettings(self, context, layout, bpy.data.particles[panel.target])


# object
def Object(self, context, layout, datablock):
  '''
    The object properties.
  '''

  # label
  layout.label(text='Display:')

  # split
  split = layout.split()

  # column
  column = split.column()

  # show name
  column.prop(datablock, 'show_name', text='Name')

  # show axis
  column.prop(datablock, 'show_axis', text='Axis')

  # type
  if datablock.type in {'MESH', 'CURVE', 'SURFACE', 'META', 'FONT'} or datablock.dupli_type != None:

    # show wire
    column.prop(datablock, 'show_wire', text='Wire')

  # type
  if datablock.type == 'MESH' or datablock.dupli_type != None:

    # show all edges
    column.prop(datablock, 'show_all_edges')

  # column
  column = split.column()

  # row
  row = column.row()

  # show bounds
  row.prop(datablock, 'show_bounds', text='Bounds')

  # sub
  sub = row.row()

  # active
  sub.active = datablock.show_bounds

  # draw bounds type
  sub.prop(datablock, 'draw_bounds_type', text='')

  # type
  if datablock.type in {'MESH', 'CURVE', 'SURFACE', 'META', 'FONT'}:

    # show texture space
    column.prop(datablock, 'show_texture_space', text='Texture Space')

  # show xray
  column.prop(datablock, 'show_x_ray', text='X-Ray')

  # type
  if datablock.type == 'MESH' or datablock.type == 'EMPTY' and datablock.empty_draw_type == 'IMAGE':

    # show transparent
    column.prop(datablock, 'show_transparent', text='Transparency')

  # split
  split = layout.split()

  # column
  column = split.column()

  # type
  if datablock.type in {'CAMERA', 'EMPTY'}:

    # active
    column.active = datablock.dupli_type != None

    # label
    column.label(text='Maximum Dupli Draw Type:')

  # type
  else:

    # label
    column.label(text='Maximum Draw Type:')

  # draw type
  column.prop(datablock, 'draw_type', text='')

  # column
  column = split.column()

  # type
  if datablock.type in {'MESH', 'CURVE', 'SURFACE', 'META', 'FONT'} or datablock.type == 'EMPTY' and datablock.empty_draw_type == 'IMAGE':

    # label
    column.label(text='Object Color:')

    # color
    column.prop(datablock, 'color', text='')

  # separator
  layout.separator()

  # label
  layout.label(text='Relations:')

  # split
  split = layout.split()

  # column
  column = split.column()

  # layers
  column.prop(datablock, 'layers')

  # separator
  column.separator()

  # pass index
  column.prop(datablock, 'pass_index')

  # column
  column = split.column()

  # label
  column.label(text='Parent:')

  # parent
  column.prop(datablock, 'parent', text='')

  # sub
  sub = column.column()

  # active
  sub.active = datablock.parent is not None

  # parent type
  sub.prop(datablock, 'parent_type', text='')

  # parent
  if datablock.parent and datablock.parent_type == 'BONE' and datablock.parent.type == 'ARMATURE':

    # parent bone
    sub.prop_search(datablock, 'parent_bone', datablock.parent.data, 'bones', text='')

  # separator
  layout.separator()

  # cycles
  if context.scene.render.engine == 'CYCLES':

    # label
    layout.label(text='Cycles Settings:')

    # label
    layout.label(text='Ray Visibility:')

    # split
    split = layout.split()

    # column
    column = split.column()

    # camera
    column.prop(datablock.cycles_visibility, 'camera')

    # diffuse
    column.prop(datablock.cycles_visibility, 'diffuse')

    # glossy
    column.prop(datablock.cycles_visibility, 'glossy')

    # column
    column = split.column()

    # transmission
    column.prop(datablock.cycles_visibility, 'transmission')

    # scatter
    column.prop(datablock.cycles_visibility, 'scatter')

    # type
    if datablock.type != 'LAMP':

      # shadow
      column.prop(datablock.cycles_visibility, 'shadow')

    # column
    column = layout.column()

    # label
    column.label(text='Performance:')

    # row
    row = column.row()

    # active
    row.active = context.scene.render.use_simplify and context.scene.cycles.use_camera_cull

    # use camera cull
    row.prop(datablock.cycles, 'use_camera_cull')

# group
def Group(self, context, layout, datablock):
  '''
    The group properties.
  '''

  # separator
  layout.separator()

  # column
  column = layout.column()

  # split
  split = column.split()

  # column
  column = split.column()

  # layers
  column.prop(datablock, 'layers', text='Dupli Visibility')

  # column
  column = split.column()

  # dulpi offset
  column.prop(datablock, 'dupli_offset', text='')

# action
def Action(self, context, layout, datablock):
  '''
  The action properties.
  '''

  layout.label(text='Nothing to show')

# grease pencil
def GreasePencil(self, context, layout, datablock):
  '''
  The grease pencil properties.
  '''

  layout.label(text='Nothing to show')

# constraint
def Constraint(self, context, layout, datablock):
  '''
  The constraint properties.
  '''

  layout.label(text='Nothing to show')

# modifier
def Modifier(self, context, layout, datablock):
  '''
  The modifier properties.
  '''

  layout.label(text='Nothing to show')

# object data
def ObjectData(self, context, layout, datablock):
  '''
  The object data properties.
  '''

  layout.label(text='Nothing to show')

# bone group
def BoneGroup(self, context, layout, datablock):
  '''
  The bone group properties.
  '''

  layout.label(text='Nothing to show')

# bone
def Bone(self, context, layout, datablock):
  '''
  The bone properties.
  '''

  layout.label(text='Nothing to show')

# bone constraint
def BoneConstraints(self, context, layout, datablock):
  '''
  The bone constraints properties.
  '''

  layout.label(text='Nothing to show')

# vertex group
def VertexGroup(self, context, layout, datablock):
  '''
  The vertex group properties.
  '''

  layout.label(text='Nothing to show')

# uv
def UV(self, context, layout, datablock):
  '''
  The UV properties.
  '''

  layout.label(text='Nothing to show')

# shapekey
def Shapekey(self, context, layout, datablock):
  '''
  The shapekey properties.
  '''

  layout.label(text='Nothing to show')

# vertex color
def VertexColor(self, context, layout, datablock):
  '''
  The vertex color properties.
  '''

  layout.label(text='Nothing to show')

# material
def Material(self, context, layout, datablock):
  '''
  The material properties.
  '''

  layout.label(text='Nothing to show')

# texture
def Texture(self, context, layout, datablock):
  '''
  The texture properties.
  '''

  layout.label(text='Nothing to show')

# particle system
def ParticleSystem(self, context, layout, datablock):
  '''
  The particle system properties.
  '''

  layout.label(text='Nothing to show')

# particle settings
def ParticleSettings(self, context, layout, datablock):
  '''
  The particle settings properties.
  '''

  layout.label(text='Nothing to show')
