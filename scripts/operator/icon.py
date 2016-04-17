
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
import bmesh
from bpy.types import Operator
from bpy.props import BoolProperty, StringProperty, EnumProperty
from ..interface.popup.constraints import ConstraintButtons
from ..interface.popup.modifiers import ModifierButtons

# object
class object(Operator):
  '''
    Assigns an active object.
  '''
  bl_idname = 'view3d.active_object'
  bl_label = 'Active Object'
  bl_description = 'Make this object the active object.'
  bl_options = {'REGISTER', 'UNDO'}

  # target
  target = StringProperty(
    name = 'Target',
    description = 'The target object that will become the active object.',
    default = ''
  )

  # extend
  extend = BoolProperty(
    name = 'Extend Selection',
    description = 'Extend the selection.',
    default = False
  )

  # properties
  properties = BoolProperty(
    name = 'Properties Context',
    description = 'Change any property window\'s context to object.',
    default = True
  )

  # layout
  layout = BoolProperty(
    name = 'Change Layout',
    description = 'Change the current screen layout to an alternate',
    default = True
  )

  # screen
  screen = StringProperty(
    name = 'Screen',
    description = 'The screen to change to.',
    default = ''
  )

  # poll
  @classmethod
  def poll(cls, context):
    '''
      Space data type must be in 3D view.
    '''
    return context.space_data.type in 'VIEW_3D'

  # execute
  def execute(self, context):
    '''
      Execute the operator.
    '''

    # extend
    if self.extend:

      # select
      bpy.data.objects[context.active_object.name].select = True

    # extend
    else:

      # object
      for object in context.scene.objects[:]:

        # deselect
        object.select = False

    # mode set
    if context.mode != 'OBJECT':
      bpy.ops.object.mode_set(mode='OBJECT')

    # warning
    try:

      # select
      bpy.data.objects[self.target].select = True

      # active object
      context.scene.objects.active = bpy.data.objects[self.target]

    # report
    except:
      self.report({'WARNING'}, 'Invalid target')

    # properties
    if self.properties:

      # screen
      if self.screen != '':

        # warning
        try:

          # area
          for area in bpy.data.screens[self.screen].areas:

            # type
            if area.type in 'PROPERTIES':

              # context
              area.spaces.active.context = 'OBJECT'

        # report
        except:
          self.report({'WARNING'}, 'Invalid screen')


      # screen
      else:

        # area
        for area in context.window.screen.areas:

          # type
          if area.type in 'PROPERTIES':

            # context
            area.spaces.active.context = 'OBJECT'

    # layout
    if self.layout:

      # screen
      if self.screen != '':

        # warning
        try:

          # active screen
          context.window.screen = bpy.data.screens[self.screen]

        # report
        except:
          self.report({'WARNING'}, 'Invalid screen')


    return {'FINISHED'}

# group
class group(Operator):
  '''
    Assigns an active group.
  '''
  bl_idname = 'view3d.active_group'
  bl_label = 'Active Group'
  bl_description = 'Make this the active group.'
  bl_options = {'REGISTER', 'UNDO'}

  # object
  object = StringProperty(
    name = 'Object',
    description = 'The group object.',
    default = ''
  )

  # target
  target = StringProperty(
    name = 'Target',
    description = 'The target group',
    default = ''
  )

  # extend
  extend = BoolProperty(
    name = 'Extend Selection',
    description = 'Extend the selection.',
    default = False
  )

  # properties
  properties = BoolProperty(
    name = 'Properties',
    description = 'Change any property window\'s context to object.',
    default = True
  )

  # layout
  layout = BoolProperty(
    name = 'Change Layout',
    description = 'Change the current screen layout to an alternate',
    default = True
  )

  # screen
  screen = StringProperty(
    name = 'Screen',
    description = 'The screen to change to.',
    default = ''
  )

  # poll
  @classmethod
  def poll(cls, context):
    '''
      Space data type must be in 3D view.
    '''
    return context.space_data.type in 'VIEW_3D'

  # execute
  def execute(self, context):
    '''
      Execute the operator.
    '''

    # warning
    try:

      # not active
      if bpy.data.objects[self.object] != context.scene.objects.active:

        # object mode
        if context.mode != 'OBJECT':
          bpy.ops.object.mode_set(mode='OBJECT')

        # extend
        if self.extend:

          # select
          context.scene.objects.active.select = True

        # extend
        else:

          # object
          for object in context.scene.objects[:]:

            # deselect
            object.select = False

        # select
        bpy.data.objects[self.object].select = True

        # active object
        context.scene.objects.active = bpy.data.objects[self.object]

    # report
    except:
      self.report({'WARNING'}, 'Invalid object.')

    # edit mode
    if context.mode != 'EDIT':
      bpy.ops.object.mode_set(mode='EDIT')

    # bmesh
    mesh = bmesh.from_edit_mesh(context.active_object.data)

    # extend
    if not self.extend:

      # clear vertex
      for vertex in mesh.verts:
        vertex.select = False

      # clear edge
      for edge in mesh.edges:
        edge.select = False

      # clear face
      for face in mesh.faces:
        face.select = False

    # warning
    try:

      # group index
      groupIndex = context.active_object.vertex_groups[self.target].index

      # active index
      context.active_object.vertex_groups.active_index = groupIndex

    # report
    except:
      self.report({'WARNING'}, 'Invalid target.')

    # deform layer
    deformLayer = mesh.verts.layers.deform.active

    # select vertices
    for vertex in mesh.verts:
      deformVertex = vertex[deformLayer]
      if groupIndex in deformVertex:
        vertex.select = True

    # flush selection
    mesh.select_flush(True)

    # update viewport
    context.scene.objects.active = context.scene.objects.active

    # properties
    if self.properties:

      # screen
      if self.screen != '':

        # warning
        try:

          # area
          for area in bpy.data.screens[self.screen].areas:

            # type
            if area.type in 'PROPERTIES':

              # context
              area.spaces.active.context = 'DATA'

        # report
        except:
          self.report({'WARNING'}, 'Invalid screen')

      # screen
      else:

        # area
        for area in context.window.screen.areas:

          # type
          if area.type in 'PROPERTIES':

            # context
            area.spaces.active.context = 'DATA'

    # layout
    if self.layout:

      # screen
      if self.screen != '':

        # warning
        try:

          # active screen
          context.window.screen = bpy.data.screens[self.screen]

        # report
        except:
          self.report({'WARNING'}, 'Invalid screen')

    return {'FINISHED'}

# action

# grease pencil

# constraint

# modifier

# bone constraint

# object data
class objectData(Operator):
  '''
    Assigns active object data.
  '''
  bl_idname = 'view3d.active_object_data'
  bl_label = 'Active Object Data'
  bl_description = 'Make this the active object data.'
  bl_options = {'REGISTER', 'UNDO'}

  # target
  target = StringProperty(
    name = 'Target',
    description = 'The target object that will become the active object.',
    default = ''
  )

  # extend
  extend = BoolProperty(
    name = 'Extend Selection',
    description = 'Extend the selection.',
    default = False
  )

  # properties
  properties = BoolProperty(
    name = 'Properties',
    description = 'Change any property window\'s context to object data.',
    default = True
  )

  # layout
  layout = BoolProperty(
    name = 'Change Layout',
    description = 'Change the current screen layout to an alternate',
    default = True
  )

  # screen
  screen = StringProperty(
    name = 'Screen',
    description = 'The screen to change to.',
    default = ''
  )

  # poll
  @classmethod
  def poll(cls, context):
    '''
      Space data type must be in 3D view.
    '''
    return context.space_data.type in 'VIEW_3D'
  # execute
  def execute(self, context):
    '''
      Execute the operator.
    '''

    # extend
    if self.extend:
      bpy.data.objects[context.active_object.name].select = True

    # extend
    else:

      # object
      for object in context.scene.objects[:]:

        # deselect
        object.select = False

    # mode set
    if context.mode != 'OBJECT':
      bpy.ops.object.mode_set(mode='OBJECT')

    # select
    bpy.data.objects[self.target].select = True

    # active object
    context.scene.objects.active = bpy.data.objects[self.target]

    # edit mode
    if context.mode != 'EDIT':
      if bpy.data.objects[self.target].type not in {'EMPTY', 'SPEAKER', 'CAMERA', 'LAMP'}:
        bpy.ops.object.mode_set(mode='EDIT')

    # properties
    if self.properties:

      # screen
      if self.screen != '':

        # warning
        try:

          # area
          for area in bpy.data.screens[self.screen].areas:

            # type
            if area.type in 'PROPERTIES':

              # context
              area.spaces.active.context = 'DATA'

        # report
        except:
          self.report({'WARNING'}, 'Invalid screen')

      # screen
      else:

        # area
        for area in context.window.screen.areas:

          # type
          if area.type in 'PROPERTIES':

            # context
            area.spaces.active.context = 'DATA'

    # layout
    if self.layout:

      # screen
      if self.screen != '':

        # warning
        try:

          # active screen
          context.window.screen = bpy.data.screens[self.screen]

        # report
        except:
          self.report({'WARNING'}, 'Invalid screen')

    return {'FINISHED'}

# vertex group
class vertexGroup(Operator):
  '''
    Assigns an active vertex group.
  '''
  bl_idname = 'view3d.active_vertex_group'
  bl_label = 'Active Vertex Group'
  bl_description = 'Make this the active vertex group.'
  bl_options = {'REGISTER', 'UNDO'}

  # object
  object  = StringProperty(
    name = 'Object',
    description = 'The object the vertex group is in.',
    default = ''
  )

  # target
  target = StringProperty(
    name = 'Target',
    description = 'The target vertex group.',
    default = ''
  )

  # extend
  extend = BoolProperty(
    name = 'Extend Selection',
    description = 'Extend the selection.',
    default = False
  )

  # properties
  properties = BoolProperty(
    name = 'Properties',
    description = 'Change any property window\'s context to mesh data',
    default = True
  )

  # layout
  layout = BoolProperty(
    name = 'Change Layout',
    description = 'Change the current screen layout to an alternate',
    default = True
  )

  # screen
  screen = StringProperty(
    name = 'Screen',
    description = 'The screen to change to.',
    default = ''
  )

  # poll
  @classmethod
  def poll(cls, context):
    '''
      Space data type must be in 3D view.
    '''
    return context.space_data.type in 'VIEW_3D'

  # execute
  def execute(self, context):
    '''
      Execute the operator.
    '''
    # warning
    try:

      # not active
      if bpy.data.objects[self.object] != context.scene.objects.active:

        # object mode
        if context.mode != 'OBJECT':
          bpy.ops.object.mode_set(mode='OBJECT')

        # extend
        if self.extend:

          # select
          context.scene.objects.active.select = True

        # extend
        else:

          # object
          for object in context.scene.objects[:]:

            # deselect
            object.select = False

        # select
        bpy.data.objects[self.object].select = True

        # active object
        context.scene.objects.active = bpy.data.objects[self.object]

    # report
    except:
      self.report({'WARNING'}, 'Invalid object.')

    # edit mode
    if context.mode != 'EDIT':
      bpy.ops.object.mode_set(mode='EDIT')

    # bmesh
    mesh = bmesh.from_edit_mesh(context.active_object.data)

    # extend
    if not self.extend:

      # clear vertex
      for vertex in mesh.verts:
        vertex.select = False

      # clear edge
      for edge in mesh.edges:
        edge.select = False

      # clear face
      for face in mesh.faces:
        face.select = False

    # warning
    try:

      # group index
      groupIndex = context.active_object.vertex_groups[self.target].index

      # active index
      context.active_object.vertex_groups.active_index = groupIndex

    # report
    except:
      self.report({'WARNING'}, 'Invalid target.')

    # deform layer
    deformLayer = mesh.verts.layers.deform.active

    # select vertices
    for vertex in mesh.verts:
      deformVertex = vertex[deformLayer]
      if groupIndex in deformVertex:
        vertex.select = True

    # flush selection
    mesh.select_flush(True)

    # update viewport
    context.scene.objects.active = context.scene.objects.active

    # properties
    if self.properties:

      # screen
      if self.screen != '':

        # warning
        try:

          # area
          for area in bpy.data.screens[self.screen].areas:

            # type
            if area.type in 'PROPERTIES':

              # context
              area.spaces.active.context = 'DATA'

        # report
        except:
          self.report({'WARNING'}, 'Invalid screen')

      # screen
      else:

        # area
        for area in context.window.screen.areas:

          # type
          if area.type in 'PROPERTIES':

            # context
            area.spaces.active.context = 'DATA'

    # layout
    if self.layout:

      # screen
      if self.screen != '':

        # warning
        try:

          # active screen
          context.window.screen = bpy.data.screens[self.screen]

        # report
        except:
          self.report({'WARNING'}, 'Invalid screen')

    return {'FINISHED'}

# shapekey

# uv map

# vertex colors

# materials

# textures

# bone
class bone(Operator):
  '''
    Assigns an active bone.
  '''
  bl_idname = 'view3d.active_bone'
  bl_label = 'Active Bone'
  bl_description = 'Make this bone the active bone.'
  bl_options = {'REGISTER', 'UNDO'}

  # target
  target = StringProperty(
    name = 'Target',
    description = 'The target bone that will become the active object.',
    default = ''
  )

  # properties
  properties = BoolProperty(
    name = 'Properties',
    description = 'Change any property window\s context to bone.',
    default = False
  )

  # poll
  @classmethod
  def poll(cls, context):
    '''
      Space data type must be in 3D view and there must be an active bone.
    '''
    return context.space_data.type in 'VIEW_3D'

  # execute
  def execute(self, context):
    '''
      Execute the operator.
    '''
    try:

      # edit mode
      if context.object.mode in 'EDIT':

        # select
        context.active_object.data.edit_bones.active.select = True

        # select head
        context.active_object.data.edit_bones.active.select_head = True

        # select tail
        context.active_object.data.edit_bones.active.select_tail = True

        # active bone
        context.scene.objects[context.active_object.name].data.edit_bones.active = bpy.data.armatures[context.active_object.data.name].edit_bones[self.target]

        # select head
        context.active_object.data.edit_bones.active.select_head = True

        # select tail
        context.active_object.data.edit_bones.active.select_tail = True

      # pose mode
      else:

        # select
        context.active_object.data.bones.active.select = True

        # target
        context.scene.objects[context.active_object.name].data.bones.active = bpy.data.armatures[context.active_object.data.name].bones[self.target]
    except:

      # warning messege
      self.report({'WARNING'}, 'Invalid target.')

    # properties
    if self.properties:
      for area in context.screen.areas:
        if area.type in 'PROPERTIES':
          area.spaces.active.context = 'BONE'

    return {'FINISHED'}

# bone constraints

# pop-ups

# constraint
class constraint(ConstraintButtons, Operator):
  '''
    This is operator is used to create the required pop-up panel.
  '''
  bl_idname = 'view3d.constraint_settings'
  bl_label = 'Constraint'
  bl_description = 'Adjust the options for this constraint. (Experimental)'
  bl_options = {'REGISTER', 'UNDO'}

  # object
  object = StringProperty(
    name = 'Object',
    description = 'The object that the constraint is attached to.',
    default = ''
  )

  # bone
  bone = StringProperty(
    name = 'Bone',
    description = 'The bone that the constraint is attached to.'
  )

  # target
  target = StringProperty(
    name = 'Target',
    description = 'The constraint you wish to edit the settings of.',
    default = ''
  )

  # properties
  properties = BoolProperty(
    name = 'Properties',
    description = 'Change any property window\'s context to constraint',
    default = False
  )

  # draw
  def draw(self, context):
    '''
      Draw the constraint options.
    '''

    # layout
    layout = self.layout

    # column
    column = layout.column()

    # label
    column.label(text=self.target + ':')

    # constraint
    if self.bone == '':
      ConstraintButtons.main(ConstraintButtons, context, layout, bpy.data.objects[self.object].constraints[self.target])

    elif context.mode == 'POSE':
      ConstraintButtons.main(ConstraintButtons, context, layout, bpy.data.objects[self.object].pose.bones[self.bone].constraints[self.target])

  # execute
  def execute(self, context):
    '''
      Execute the operator.
    '''

    # properties
    if self.properties:
      for area in context.screen.areas:
        if area.type in 'PROPERTIES':
          if self.bone == '':
            area.spaces.active.context = 'CONSTRAINT'
          elif context.mode == 'POSE':
            area.spaces.active.context = 'BONE_CONSTRAINT'
          else:
            area.spaces.active.context = 'CONSTRAINT'
    return {'FINISHED'}

  # invoke
  def invoke(self, context, event):
    '''
      Invoke the operator panel/menu, control its width.
    '''
    context.window_manager.invoke_popup(self, width=350)
    return {'RUNNING_MODAL'}

# modifier
class modifier(ModifierButtons, Operator):
  '''
    This is operator is used to create the required pop-up panel.
  '''
  bl_idname = 'view3d.modifier_settings'
  bl_label = 'Modifier'
  bl_description = 'Adjust the options for this modifier. (Experimental)'
  bl_options = {'REGISTER', 'UNDO'}

  # object
  object = StringProperty(
    name = 'Object',
    description = 'The object that the modifier is attached to.',
    default = ''
  )

  # target
  target = StringProperty(
    name = 'Target',
    description = 'The modifier you wish to edit the settings of.',
    default = ''
  )

  # properties
  properties = BoolProperty(
    name = 'Properties',
    description = 'Change any property window\'s context to modifier',
    default = False
  )

  # draw
  def draw(self, context):
    '''
      Draw the modifier options.
    '''

    # layout
    layout = self.layout

    # column
    column = layout.column()

    # label
    column.label(text=self.target + ':')

    # modifier
    ModifierButtons.main(ModifierButtons, context, layout, bpy.data.objects[self.object].modifiers[self.target], bpy.data.objects[self.object])


  # execute
  def execute(self, context):
    '''
      Execute the operator.
    '''

    # properties
    if self.properties:
      for area in context.screen.areas:
        if area.type in 'PROPERTIES':
          area.spaces.active.context = 'MODIFIER'

    return {'FINISHED'}

  # invoke
  def invoke(self, context, event):
    '''
      Invoke the operator panel/menu, control its width.
    '''
    context.window_manager.invoke_popup(self, width=350)
    return {'RUNNING_MODAL'}
