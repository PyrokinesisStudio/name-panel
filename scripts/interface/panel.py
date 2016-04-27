
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

import bpy
import re
from bpy.types import Panel
from .. import storage
from . import icon

# addon
addon = bpy.context.user_preferences.addons.get(__name__.partition('.')[0])

# name
class toolsName(Panel):
  '''
    Name panel.
  '''
  bl_idname = 'VIEW3D_PT_toolshelf_name'
  bl_space_type = 'VIEW_3D'
  bl_label = 'Name'
  bl_region_type = 'TOOLS'
  bl_options = {'HIDE_HEADER'}
  bl_category = 'Name'

  # # poll
  # @classmethod
  # def poll(self, cls):
  #   try: return True if addon.preferences['location'] == 0 else False
  #   except: return True

  # draw
  def draw(self, context):
    '''
      Name panel body.
    '''

    # main
    main(self, context)

# name
class UIName(Panel):
  '''
    Name panel.
  '''
  bl_idname = 'VIEW3D_PT_propertyshelf_name'
  bl_space_type = 'VIEW_3D'
  bl_label = 'Name'
  bl_region_type = 'UI'

  # # poll
  # @classmethod
  # def poll(self, cls):
  #   try: return True if addon.preferences['location'] == 1 else False
  #   except: return False

  # draw
  def draw(self, context):
    '''
      Name panel body.
    '''

    # main
    main(self, context)

# main
def main(self, context):
  '''
    Name panel main.
  '''

  # layout
  layout = self.layout

  # option
  option = context.scene.NamePanel

  # column
  column = layout.column(align=True)

  # filter
  filters(self, context, column, option)

  # search
  search = context.scene.NamePanel.search if option.regex else re.escape(context.scene.NamePanel.search)

  # mode
  if option.mode == 'SELECTED':

    # member
    member = gather(context, {object.name: [] for object in context.selected_objects}) if option.search != '' else {}

  # mode
  else:

    # member
    member = gather(context, {object.name: [] for object in context.scene.objects if True in [x&y for (x,y) in zip(object.layers, context.scene.layers)]}) if option.search != '' else {}

  # pin active object
  if option.pinActiveObject:
    if context.active_object:

      # search
      if search == '' or re.search(search, context.active_object.name, re.I) or [re.search(search, item, re.I) for item in member[context.active_object.name] if re.search(search, item, re.I) != None]:

        # populate
        populate(self, context, layout, context.active_object, option)

    # display names
    if option.displayNames:

      # mode
      if option.mode == 'SELECTED':

        # objects
        objects = [[object.name, object] for object in context.selected_objects]

        # sorted
        for datablock in sorted(objects):
          if datablock[1] != context.active_object:

            # search
            if search == '' or re.search(search, datablock[1].name, re.I) or [re.search(search, item, re.I) for item in member[datablock[1].name] if re.search(search, item, re.I) != None]:

              # populate
              populate(self, context, layout, datablock[1], option)

      # mode
      else:

        # objects
        objects = [[object.name, object] for object in context.scene.objects if True in [x&y for (x,y) in zip(object.layers, context.scene.layers)]]

        # sorted
        for datablock in sorted(objects):
          if datablock[1] != context.active_object:

            # search
            if search == '' or re.search(search, datablock[1].name, re.I) or [re.search(search, item, re.I) for item in member[datablock[1].name] if re.search(search, item, re.I) != None]:

              # populate
              populate(self, context, layout, datablock[1], option)

  # pin active object
  else:

    # display names
    if option.displayNames:

      # mode
      if option.mode == 'SELECTED':

        # objects
        objects = [[object.name, object] for object in context.selected_objects]

        # sorted
        for datablock in sorted(objects):

          # search
          if search == '' or re.search(search, datablock[1].name, re.I) or [re.search(search, item, re.I) for item in member[datablock[1].name] if re.search(search, item, re.I) != None]:

            # populate
            populate(self, context, layout, datablock[1], option)

      # mode
      else:

        # objects
        objects = [[object.name, object] for object in context.scene.objects if True in [x&y for (x,y) in zip(object.layers, context.scene.layers)]]

        # sorted
        for datablock in sorted(objects):

          # search
          if search == '' or re.search(search, datablock[1].name, re.I) or [re.search(search, item, re.I) for item in member[datablock[1].name] if re.search(search, item, re.I) != None]:

            # populate
            populate(self, context, layout, datablock[1], option)
    else:

      # search
      if search == '' or re.search(search, context.active_object.name, re.I) or [re.search(search, item, re.I) for item in member[context.active_object.name] if re.search(search, item, re.I) != None]:

        # populate
        populate(self, context, layout, context.active_object, option)

# filters
def filters(self, context, layout, option):
  '''
    The name panel filters
  '''

  # row
  row = layout.row(align=True)

  # scale
  row.scale_y = 1.25

  # icon toggle
  if option.filters:
    iconToggle = 'RADIOBUT_ON'
  else:
    iconToggle = 'RADIOBUT_OFF'

  # filters
  row.prop(option, 'filters', text='Filters', icon=iconToggle, toggle=True)

  # display names
  row.prop(option, 'displayNames', text='', icon='ZOOM_SELECTED')

  # options
  row.prop(option, 'options', text='', icon='SETTINGS')

  # # operator menu
  row.menu('VIEW3D_MT_name_panel_specials', text='', icon='COLLAPSEMENU')

  # filters
  if option.filters:

    # separator
    layout.separator()

    # row
    row = layout.row(align=True)

    # scale
    row.scale_x = 5 # hack: forces buttons to line up correctly

    # action
    row.prop(option, 'action', text='', icon='ACTION')

    # grease pencil
    row.prop(option, 'greasePencil', text='', icon='GREASEPENCIL')

    # groups
    row.prop(option, 'groups', text='', icon='GROUP')

    # constraints
    row.prop(option, 'constraints', text='', icon='CONSTRAINT')

    # modifiers
    row.prop(option, 'modifiers', text='', icon='MODIFIER')

    # bone groups
    row.prop(option, 'boneGroups', text='', icon='GROUP_BONE')

    # bone constraints
    row.prop(option, 'boneConstraints', text='', icon='CONSTRAINT_BONE')

    # row
    row = layout.row(align=True)

    # scale
    row.scale_x = 5 # hack: forces buttons to line up correctly

    # vertex groups
    row.prop(option, 'vertexGroups', text='', icon='GROUP_VERTEX')

    # shapekeys
    row.prop(option, 'shapekeys', text='', icon='SHAPEKEY_DATA')

    # uvs
    row.prop(option, 'uvs', text='', icon='GROUP_UVS')

    # vertex colors
    row.prop(option, 'vertexColors', text='', icon='GROUP_VCOL')

    # materials
    row.prop(option, 'materials', text='', icon='MATERIAL')

    # textures
    row.prop(option, 'textures', text='', icon='TEXTURE')

    # particles systems
    row.prop(option, 'particleSystems', text='', icon='PARTICLES')

    # separator
    layout.separator()

    # hide search
    if option.hideSearch:

      # row
      row = layout.row(align=True)

      # search
      row.prop(option, 'search', text='', icon='VIEWZOOM')
      row.operator('wm.regular_expression_cheatsheet', text='', icon='FILE_TEXT')
      row.prop(option, 'regex', text='', icon='SCRIPTPLUGINS')
      row.operator('wm.batch_name', text='', icon='SORTALPHA').quickBatch = True

  # hide search
  if not option.hideSearch:

    # row
    row = layout.row(align=True)

    # search
    row.prop(option, 'search', text='', icon='VIEWZOOM')
    row.operator('wm.regular_expression_cheatsheet', text='', icon='FILE_TEXT')
    row.prop(option, 'regex', text='', icon='SCRIPTPLUGINS')
    row.operator('wm.batch_name', text='', icon='SORTALPHA').quickBatch = True

  # enabled
  if option.displayNames:

    # separator()
    layout.separator()

    # row
    row = layout.row()

    # mode
    row.prop(option, 'mode', expand=True)

# gather
def gather(context, member):
  '''
    Creates a object datablock dictionary for name panel.
  '''

  # option
  option = context.scene.NamePanel

  # selected
  if option.displayNames:
    if option.mode == 'SELECTED':
      for object in context.selected_objects:
        sort(context, member, object)

    else:
      for object in context.scene.objects:
        if True in [x&y for (x,y) in zip(object.layers, context.scene.layers)]:
          sort(context, member, object)
  else:
    sort(context, member, context.active_object)

  return member

# sort
def sort(context, member, object):
  '''
    Sorts object related datablocks for search panel population.
  '''

  # option
  option = context.scene.NamePanel

  # search
  search = context.scene.NamePanel.search if option.regex else re.escape(context.scene.NamePanel.search)

  # group
  if option.groups:
    for group in bpy.data.groups[:]:
      for groupobject in group.objects[:]:
        if groupobject == object:

          # search
          if search == '' or re.search(search, group.name, re.I):

            # member
            member[object.name].append(group.name)

  # action
  if option.action:
    if hasattr(object.animation_data, 'action'):
      if hasattr(object.animation_data.action, 'name'):

        # search
        if search == '' or re.search(search, object.animation_data.action.name, re.I):

          # member
          member[object.name].append(object.animation_data.action.name)

  # grease pencil
  if option.greasePencil:
    if hasattr(object.grease_pencil, 'name'):

      # layers
      layers = [layer.info for layer in bpy.data.objects[object.name].grease_pencil.layers]

      # search
      if search == '' or re.search(search, object.grease_pencil.name, re.I) or [re.search(search, item, re.I) for item in layers if re.search(search, item, re.I) != None]:

        # member
        member[object.name].append(object.grease_pencil.name)

        # pencil layers
        for layer in bpy.data.objects[object.name].grease_pencil.layers:

          # search
          if search == '' or re.search(search, layer.info, re.I):

            # member
            member[object.name].append(layer.info)

  # constraints
  if option.constraints:
    for constraint in object.constraints[:]:

      # search
      if search == '' or re.search(search, constraint.name, re.I):

        # member
        member[object.name].append(constraint.name)

  # modifiers
  if option.modifiers:
    for modifier in object.modifiers[:]:

      if modifier.type == 'PARTICLE_SYSTEM':
        # particle
        particle = [modifier.particle_system.name, modifier.particle_system.settings.name]

        # texture
        texture = [slot.texture.name for slot in modifier.particle_system.settings.texture_slots[:] if slot != None]

      elif modifier.type in {'DISPLACE', 'WARP'}:
        if modifier.texture:

          # texture
          texture = [modifier.texture.name]

      elif modifier.type in {'VERTEX_WEIGHT_MIX', 'VERTEX_WEIGHT_EDIT', 'VERTEX_WEIGHT_PROXIMITY'}:
        if modifier.mask_texture:

          # texture
          texture = [modifier.mask_texture.name]

      else:

        particle = []

        # texture:
        texture = []

      # search
      if search == '' or re.search(search, modifier.name, re.I) or [re.search(search, item, re.I) for item in particle if re.search(search, item, re.I) != None] or [re.search(search, item, re.I) for item in texture if re.search(search, item, re.I) != None]:

        # member
        member[object.name].append(modifier.name)

        # particle systems
        if option.particleSystems:
          if modifier.type in 'PARTICLE_SYSTEM':

            # search
            if search == '' or re.search(search, particle[0], re.I) or re.search(search, particle[1], re.I) or [re.search(search, item, re.I) for item in texture if re.search(search, item, re.I) != None]:

              # member
              member[object.name].append(modifier.particle_system.name)

              # search
              if search == '' or re.search(search, modifier.particle_system.settings.name, re.I) or [re.search(search, item, re.I) for item in texture if re.search(search, item, re.I) != None]:

                # member
                member[object.name].append(modifier.particle_system.settings.name)

                for slot in modifier.particle_system.settings.texture_slots[:]:
                  if slot != None:

                    # search
                    if search == '' or re.search(search, slot.texture.name, re.I):

                      # member
                      member[object.name].append(slot.texture.name)

  # materials
  if option.materials:
    for slot in object.material_slots:
      if slot.material != None:

        # textures
        textures = [tslot.texture.name for tslot in slot.material.texture_slots[:] if hasattr(tslot, 'texture')]

        # search
        if search == '' or re.search(search, slot.material.name, re.I) or [re.search(search, item, re.I) for item in textures if re.search(search, item, re.I) != None]:

          # member
          member[object.name].append(slot.material.name)

          # textures
          if option.textures:
            if context.scene.render.engine in {'BLENDER_RENDER', 'BLENDER_GAME'}:
              for tslot in slot.material.texture_slots[:]:
                if hasattr(tslot, 'texture'):
                  if tslot.texture != None:

                    # search
                    if search == '' or re.search(search, tslot.texture.name, re.I):

                      # member
                      member[object.name].append(tslot.texture.name)

  # object data
  if object.type != 'EMPTY':

    # search
    if search == '' or re.search(search, object.data.name, re.I):

      # member
      member[object.name].append(object.data.name)

  # vertex groups
  if option.vertexGroups:
    if hasattr(object, 'vertex_groups'):
      for group in object.vertex_groups[:]:

        # search
        if search == '' or re.search(search, group.name, re.I):

          # member
          member[object.name].append(group.name)

  # shapekeys
  if option.shapekeys:
    if hasattr(object.data, 'shape_keys'):
      if hasattr(object.data.shape_keys, 'key_blocks'):
        for key in object.data.shape_keys.key_blocks[:]:

          # search
          if search == '' or re.search(search, key.name, re.I):

            # member
            member[object.name].append(key.name)

  # uvs
  if option.uvs:
    if object.type in 'MESH':
      for uv in object.data.uv_textures[:]:

        # search
        if search == '' or re.search(search, uv.name, re.I):

          # member
          member[object.name].append(uv.name)

  # vertex colors
  if option.vertexColors:
    if object.type in 'MESH':
      for vertexColor in object.data.vertex_colors[:]:

        # search
        if search == '' or re.search(search, vertexColor.name, re.I):

          # member
          member[object.name].append(vertexColor.name)

  # bone groups
  if option.boneGroups:
    if object.type in 'ARMATURE':
      for group in object.pose.bone_groups[:]:

        # search
        if search == '' or re.search(search, group.name, re.I):

          # member
          member[object.name].append(group.name)

  # bones
  if object == context.active_object:
    if object.type in 'ARMATURE':
      if object.mode in {'POSE', 'EDIT'}:

        # constraints
        try:
          constraints = [item.name for item in context.active_pose_bone.constraints[:]]
        except:
          constraints = []

        # search
        if search == '' or re.search(search, context.active_bone.name, re.I) or [re.search(search, item, re.I) for item in constraints if re.search(search, item, re.I) != None]:

          # member
          member[object.name].append(context.active_bone.name)

        # bone constraints
        if option.boneConstraints:
          if object.mode in 'POSE':
            for constraint in context.active_pose_bone.constraints[:]:

              # search
              if search == '' or re.search(search, constraint.name, re.I):

                # member
                member[object.name].append(constraint.name)

        # display bones
        if option.displayBones:

          # pose mode
          if object.mode in 'POSE':
            bones = object.pose.bones[:]

          # edit mode
          elif object.mode == 'EDIT':
            bones = object.data.edit_bones[:]

          # other modes
          else:
            bones = object.data.bones[:]

          # sort and display
          for bone in bones:
            if bone.name != context.active_bone:

              # constraints
              try:
                constraints = [constraint.name for constraint in object.pose.bones[bone.name].constraints[:]]
              except:
                constraints = []

              # search
              if search == '' or re.search(search, bone.name, re.I) or [re.search(search, item, re.I) for item in constraints if re.search(search, item, re.I) != None]:

                # member
                member[object.name].append(bone.name)

              # bone constraints
              if option.boneConstraints:
                if object.mode in 'POSE':
                  for constraint in bone.constraints[:]:

                    # search
                    if search == '' or re.search(search, constraint.name, re.I):

                      # member
                      member[object.name].append(constraint.name)

  return member

# populate
def populate(self, context, layout, object, option):
  '''
    Populates the name panel with datablock names.
  '''

  # search
  search = context.scene.NamePanel.search if option.regex else re.escape(context.scene.NamePanel.search)

  # column
  column = layout.column()

  # object
  Object(self, context, column, object, option)

  # action
  block.object.action(self, context, column, object, option)

  # group
  block.object.group(self, context, column, object, option)

  # grease pencil
  block.object.greasePencil(self, context, column, object, option)

  # constraint
  block.object.constraint(self, context, column, object, option)

  # modifier
  block.object.modifier(self, context, column, object, option)

  # material
  block.object.material(self, context, column, object, option)

  # object data
  ObjectData(self, context, column, object, option)

  # vertex group
  block.objectData.vertexGroup(self, context, column, object, option)

  # shapekey
  block.objectData.shapekey(self, context, column, object, option)

  # uv
  block.objectData.uv(self, context, column, object, option)

  # vertex color
  block.objectData.vertexColor(self, context, column, object, option)

  # material
  block.objectData.material(self, context, column, object, option)

  # bone group
  block.objectData.boneGroup(self, context, column, object, option)

  # row
  row = column.row()

  # separator
  row.separator()

  # object
  if object == context.active_object:

    # bone
    block.bone(self, context, column, object, option)

# block
class block:
  '''
    contains classes;
      object
      objectData

    contains functions;
      bone
      material
  '''

  # object
  class object:
    '''
      contains functions;
        group
        action
        greasepencil
        constraint
        modifier
        material
    '''

    # group
    def group(self, context, layout, object, option):
      '''
        group related code block.
      '''

      # search
      search = context.scene.NamePanel.search if option.regex else re.escape(context.scene.NamePanel.search)

      # groups
      if option.groups:
        for group in bpy.data.groups[:]:
          for groupObject in group.objects[:]:
            if groupObject == object:

              # search
              if search == '' or re.search(search, group.name, re.I):

                # group
                Group(self, context, layout, group, object)

    # action
    def action(self, context, layout, object, option):
      '''
        action related code block.
      '''

      # search
      search = context.scene.NamePanel.search if option.regex else re.escape(context.scene.NamePanel.search)

      # action
      if option.action:
        if hasattr(object.animation_data, 'action'):
          if hasattr(object.animation_data.action, 'name'):

            # search
            if search == '' or re.search(search, object.animation_data.action.name, re.I):

              # action
              Action(self, context, layout, object.animation_data.action, object)

    # greasePencil
    def greasePencil(self, context, layout, object, option):
      '''
        grease pencil related code block.
      '''

      # search
      search = context.scene.NamePanel.search if option.regex else re.escape(context.scene.NamePanel.search)

      # grease pencil
      if option.greasePencil:
        if hasattr(object.grease_pencil, 'name'):

          # layers
          layers = [layer.info for layer in bpy.data.objects[object.name].grease_pencil.layers[:]]

          # search
          if search == '' or re.search(search, object.grease_pencil.name, re.I) or [re.search(search, item, re.I) for item in layers if re.search(search, item, re.I) != None]:

            # grease pencil
            GreasePencil(self, context, layout, object.grease_pencil, object, option)

            # pencil layers
            for layer in bpy.data.objects[object.name].grease_pencil.layers[:]:

              # search
              if search == '' or re.search(search, layer.info, re.I):

                # pencil layer
                PencilLayer(self, context, layout, layer, object, option)

    # constraint
    def constraint(self, context, layout, object, option):
      '''
        Constraint related code block.
      '''

      # search
      search = context.scene.NamePanel.search if option.regex else re.escape(context.scene.NamePanel.search)

      # constraints
      if option.constraints:
        for constraint in object.constraints[:]:

          # search
          if search == '' or re.search(search, constraint.name, re.I):

            # constraint
            Constraint(self, context, layout, constraint, object, None, option)

    # modifier
    def modifier(self, context, layout, object, option):
      '''
        Modifier related code block.
      '''

      # search
      search = context.scene.NamePanel.search if option.regex else re.escape(context.scene.NamePanel.search)

      # modifiers
      if option.modifiers:
        for modifier in object.modifiers[:]:

          # particle
          particle = []

          # texture:
          texture = []

          if modifier.type == 'PARTICLE_SYSTEM':
            # particle
            particle = [modifier.particle_system.name, modifier.particle_system.settings.name]

            # texture
            texture = [slot.texture.name for slot in modifier.particle_system.settings.texture_slots[:] if slot != None]

          if modifier.type in {'DISPLACE', 'WARP'}:
            if modifier.texture:

              # texture
              texture = [modifier.texture.name]

          if modifier.type in {'VERTEX_WEIGHT_MIX', 'VERTEX_WEIGHT_EDIT', 'VERTEX_WEIGHT_PROXIMITY'}:
            if modifier.mask_texture:

              # texture
              texture = [modifier.mask_texture.name]

          # member
          member = particle + texture

          # search
          if search == '' or re.search(search, modifier.name, re.I) or [re.search(search, item, re.I) for item in member if re.search(search, item, re.I) != None]:

            # modifier
            Modifier(self, context, layout, modifier, object, option)

            # texture
            if option.textures:
              if modifier.type in {'DISPLACE', 'WARP'}:
                if modifier.texture:

                  # search
                  if search == '' or re.search(search, modifier.texture.name, re.I):

                    # texture
                    Texture(self, context, layout, modifier, object, option)

              # mask texture
              elif modifier.type in {'VERTEX_WEIGHT_MIX', 'VERTEX_WEIGHT_EDIT', 'VERTEX_WEIGHT_PROXIMITY'}:
                if modifier.mask_texture:

                  # search
                  if search == '' or re.search(search, modifier.mask_texture.name, re.I):

                    # mask texture
                    MaskTexture(self, context, layout, modifier, object, option)

            # particle systems
            if option.particleSystems:
              if modifier.type in 'PARTICLE_SYSTEM':

                # search
                if search == '' or re.search(search, particle[0], re.I) or re.search(search, particle[1], re.I) or [re.search(search, item, re.I) for item in texture if re.search(search, item, re.I) != None]:

                  # particle
                  Particle(self, context, layout, modifier, object, option)

                  # texture
                  if option.textures:
                    # if context.scene.render.engine in {'BLENDER_RENDER', 'BLENDER_GAME'}:
                    for slot in modifier.particle_system.settings.texture_slots[:]:
                      if hasattr(slot, 'texture'):
                        if slot.texture:

                          # search
                          if search == '' or re.search(search, slot.texture.name, re.I):

                            # texture
                            Texture(self, context, layout, slot, object, option)

      else:
        context.scene['NamePanel']['particleSystems'] = 0

    # material
    def material(self, context, layout, object, option):
      '''
        Material related code block.
      '''

      # search
      search = context.scene.NamePanel.search if option.regex else re.escape(context.scene.NamePanel.search)

      # materials
      if option.materials:
        for slot in object.material_slots:
          if slot.link == 'OBJECT':
            if slot.material != None:

              # textures
              textures = [tslot.texture.name for tslot in slot.material.texture_slots[:] if hasattr(tslot, 'texture')]

              # search
              if search == '' or re.search(search, slot.material.name, re.I) or [re.search(search, item, re.I) for item in textures if re.search(search, item, re.I) != None]:

                # material
                Material(self, context, layout, slot, object, option)

                # textures
                if option.textures:
                  if context.scene.render.engine in {'BLENDER_RENDER', 'BLENDER_GAME'}:
                    for tslot in slot.material.texture_slots[:]:
                      if hasattr(tslot, 'texture'):
                        if tslot.texture != None:

                          # search
                          if search == '' or re.search(search, tslot.texture.name, re.I):

                            # texture
                            Texture(self, context, layout, tslot, object, option)

  # object data
  class objectData:
    '''
      Constains Functions;
        vertexGroup
        shapekey
        uv
        vertexColor
        material
        boneGroup
    '''

    # vertex group
    def vertexGroup(self, context, layout, object, option):
      '''
        Vertex group related code block.
      '''

      # search
      search = context.scene.NamePanel.search if option.regex else re.escape(context.scene.NamePanel.search)

      # vertex groups
      if option.vertexGroups:
        if hasattr(object, 'vertex_groups'):
          for group in object.vertex_groups[:]:

            # search
            if search == '' or re.search(search, group.name, re.I):

              # vertex group
              VertexGroup(self, context, layout, group, object, option)

    # shapekey
    def shapekey(self, context, layout, object, option):
      '''
        Shapekey related code block.
      '''

      # search
      search = context.scene.NamePanel.search if option.regex else re.escape(context.scene.NamePanel.search)

      # shapekeys
      if option.shapekeys:
        if hasattr(object.data, 'shape_keys'):
          if hasattr(object.data.shape_keys, 'key_blocks'):
            for key in object.data.shape_keys.key_blocks[:]:

              # search
              if search == '' or re.search(search, key.name, re.I):

                # shapekey
                Shapekey(self, context, layout, key, object, option)

    # uv
    def uv(self, context, layout, object, option):
      '''
        UV related code block.
      '''

      # search
      search = context.scene.NamePanel.search if option.regex else re.escape(context.scene.NamePanel.search)

      # uvs
      if option.uvs:
        if object.type in 'MESH':
          for uv in object.data.uv_textures[:]:

            # search
            if search == '' or re.search(search, uv.name, re.I):

              # uv
              UV(self, context, layout, uv, object, option)

    # vertex color
    def vertexColor(self, context, layout, object, option):
      '''
        Vertex color related code block.
      '''

      # search
      search = context.scene.NamePanel.search if option.regex else re.escape(context.scene.NamePanel.search)

      # vertex colors
      if option.vertexColors:
        if object.type in 'MESH':
          for vertexColor in object.data.vertex_colors[:]:

            # search
            if search == '' or re.search(search, vertexColor.name, re.I):

              # vertex color
              VertexColor(self, context, layout, vertexColor, object, option)

    # material
    def material(self, context, layout, object, option):
      '''
        Material related code block.
      '''

      # search
      search = context.scene.NamePanel.search if option.regex else re.escape(context.scene.NamePanel.search)

      # materials
      if option.materials:
        for slot in object.material_slots:
          if slot.link == 'DATA':
            if slot.material != None:

              # textures
              textures = [tslot.texture.name for tslot in slot.material.texture_slots[:] if hasattr(tslot, 'texture')]

              # search
              if search == '' or re.search(search, slot.material.name, re.I) or [re.search(search, item, re.I) for item in textures if re.search(search, item, re.I) != None]:

                # material
                Material(self, context, layout, slot, object, option)

                # textures
                if option.textures:
                  if context.scene.render.engine in {'BLENDER_RENDER', 'BLENDER_GAME'}:
                    for tslot in slot.material.texture_slots[:]:
                      if hasattr(tslot, 'texture'):
                        if tslot.texture != None:

                          # search
                          if search == '' or re.search(search, tslot.texture.name, re.I):

                            # texture
                            Texture(self, context, layout, tslot, object, option)

    # bone groups
    def boneGroup(self, context, layout, object, option):
      '''
        Bone group related code block.
      '''

      # search
      search = context.scene.NamePanel.search if option.regex else re.escape(context.scene.NamePanel.search)

      # bone groups
      if option.boneGroups:
        if object.type in 'ARMATURE':
          for group in object.pose.bone_groups[:]:

            # search
            if search == '' or re.search(search, group.name, re.I):

              # bone group
              BoneGroup(self, context, layout, group, object)

  # bones
  def bone(self, context, layout, object, option):
    '''
      Bone related code block.
    '''

    # search
    search = context.scene.NamePanel.search if option.regex else re.escape(context.scene.NamePanel.search)

    # active bone
    if object.type in 'ARMATURE':
      if object.mode in {'POSE', 'EDIT'}:

        # constraints
        try:
          constraints = [item.name for item in context.active_pose_bone.constraints[:]]
        except:
          constraints = []

        # display bones
        if option.displayBones:

          row = layout.row()

          row.prop(option, 'boneMode', expand=True)

          layout.separator()

        # search
        if search == '' or re.search(search, context.active_bone.name, re.I) or [re.search(search, item, re.I) for item in constraints if re.search(search, item, re.I) != None]:

          # bone
          Bone(self, context, layout, context.active_bone, object, option)

          # bone constraints
          if option.boneConstraints:
            if object.mode in 'POSE':
              bone = context.active_pose_bone
              if bone:
                for constraint in bone.constraints[:]:

                  # search
                  if search == '' or re.search(search, constraint.name, re.I):

                    # constraint
                    Constraint(self, context, layout, constraint, object, bone, option)

                # constraints
                if constraints != []:

                  # row
                  row = layout.row()

                  # separator
                  row.separator()

        # display bones
        if option.displayBones:

          # pose mode
          if object.mode in 'POSE':

            # bones
            bones = object.data.bones[:]

          # edit mode
          else:

            # bones
            bones = object.data.edit_bones[:]

          # selected
          if option.boneMode == 'SELECTED':

            # bones
            bones = [[bone.name, bone] for bone in bones if bone.select]

          # layers
          else:

            # bones
            bones = [[bone.name, bone] for bone in bones if True in [x&y for (x, y) in zip(bone.layers, object.data.layers)]]

          # sort and display
          for bone in sorted(bones):
            if bone[1] != context.active_bone:

              # constraints
              try:
                constraints = [item.name for item in object.pose.bones[bone[1].name].constraints[:]]
              except:
                constraints = []

              # search
              if search == '' or re.search(search, bone[1].name, re.I) or [re.search(search, item, re.I) for item in constraints if re.search(search, item, re.I) != None]:

                # bone
                Bone(self, context, layout, bone[1], object, option)

                # bone constraints
                if option.boneConstraints:
                  if object.mode in 'POSE':
                    for constraint in object.pose.bones[bone[1].name].constraints[:]:

                      # search
                      if search == '' or re.search(search, constraint.name, re.I):

                        # constraint
                        Constraint(self, context, layout, constraint, object, bone[1], option)

                    # constraints
                    if constraints != []:

                      # row
                      row = layout.row()

                      # separator
                      row.separator()

# object
def Object(self, context, layout, datablock, option):
  '''
    The object name row.
  '''
  # search
  search = context.scene.NamePanel.search if option.regex else re.escape(context.scene.NamePanel.search)

  # active object
  if datablock == context.active_object:

    # row
    row = layout.row(align=True)
    row.enabled = (search == '' or re.search(search, datablock.name, re.I) != None)

    # template
    row.template_ID(context.scene.objects, 'active')

  # selected object
  else:

    # row
    row = layout.row(align=True)
    row.enabled = (search == '' or re.search(search, datablock.name, re.I) != None)

    # sub
    sub = row.row(align=True)

    # scale
    sub.scale_x = 1.6

    # icon
    op = sub.operator('view3d.name_panel_icon', text='', icon=icon.object(datablock))
    op.owner = datablock.name
    op.target = datablock.name
    op.type = 'OBJECT'

    # object
    row.prop(datablock, 'name', text='')

    # options
    if option.options:

      # hide
      row.prop(datablock, 'hide', text='')

      # hide select
      row.prop(datablock, 'hide_select', text='')

      # hide render
      row.prop(datablock, 'hide_render', text='')

# group
def Group(self, context, layout, datablock, object):
  '''
    The object group name row.
  '''

  # row
  row = layout.row(align=True)

  # sub
  sub = row.row()

  # scale
  sub.scale_x = 1.6

  # icon
  op = sub.operator('view3d.name_panel_icon', text='', icon='GROUP', emboss=False)
  op.owner = object.name
  op.target = datablock.name
  op.type = 'GROUP'

  # label
  # sub.label(text='', icon='GROUP')

  # name
  row.prop(datablock, 'name', text='')

# action
def Action(self, context, layout, datablock, object):
  '''
    The object action name row.
  '''

  # row
  row = layout.row(align=True)

  # sub
  sub = row.row()

  # scale
  sub.scale_x = 1.6

  # icon
  op = sub.operator('view3d.name_panel_icon', text='', icon='ACTION', emboss=False)
  op.owner = object.name
  op.target = datablock.name
  op.type = 'ACTION'

  # name
  row.prop(datablock, 'name', text='')

# grease pencil
def GreasePencil(self, context, layout, datablock, object, option):
  '''
    The object grease pencil name row.
  '''

  # search
  search = context.scene.NamePanel.search if option.regex else re.escape(context.scene.NamePanel.search)

  # row
  row = layout.row(align=True)
  row.enabled = (search == '' or re.search(search, datablock.name, re.I) != None)

  # sub
  sub = row.row()

  # scale
  sub.scale_x = 1.6

  # icon
  op = sub.operator('view3d.name_panel_icon', text='', icon='GREASEPENCIL', emboss=False)
  op.owner = object.name
  op.target = datablock.name
  op.type = 'GREASE_PENCIL'

  # name
  row.prop(datablock, 'name', text='')

# pencil layer
def PencilLayer(self, context, layout, datablock, object, option):
  '''
    The object pencil layer name row.
  '''

  # row
  row = layout.row(align=True)

  # sub
  sub = row.row(align=True)

  # scale
  sub.scale_x = 0.085

  # fill color
  sub.prop(datablock, 'fill_color', text='')

  # color
  sub.prop(datablock, 'color', text='')

  # info (name)
  row.prop(datablock, 'info', text='')

  # options
  if option.options:

    # lock
    row.prop(datablock, 'lock', text='')

    # hide
    row.prop(datablock, 'hide', text='')

# constraint
def Constraint(self, context, layout, datablock, object, bone, option):
  '''
    The object or pose bone constraint name row.
  '''

  # row
  row = layout.row(align=True)

  # sub
  sub = row.row()

  # scale
  sub.scale_x = 1.6

  try:

    # popups
    if addon.preferences['popups'] == 1:
      if object.type in 'ARMATURE' and object.mode in 'POSE':

        # icon
        op = sub.operator('view3d.name_panel_constraint_settings', text='', icon='CONSTRAINT', emboss=False)
        op.object = object.name
        op.bone = bone.name
        op.target = datablock.name

      else:

        # icon
        op = sub.operator('view3d.name_panel_constraint_settings', text='', icon='CONSTRAINT', emboss=False)
        op.object = object.name
        op.target = datablock.name

    else:

      # icon
      op = sub.operator('view3d.name_panel_icon', text='', icon='CONSTRAINT', emboss=False)
      op.owner = object.name if not bone else bone.name
      op.target = datablock.name
      op.type = 'CONSTRAINT' if not bone else 'BONE_CONSTRAINT'

  except:

    # icon
    op = sub.operator('view3d.name_panel_icon', text='', icon='CONSTRAINT', emboss=False)
    op.owner = object.name if not bone else bone.name
    op.target = datablock.name
    op.type = 'CONSTRAINT' if not bone else 'BONE_CONSTRAINT'

  # name
  row.prop(datablock, 'name', text='')

  # options
  if option.options:

    # influence
    if datablock.type not in {'RIGID_BODY_JOINT', 'NULL'}:

      # sub
      sub = row.row(align=True)

      # scale
      sub.scale_x = 0.17

      # influence
      sub.prop(datablock, 'influence', text='')

    # icon view
    if datablock.mute:
      iconView = 'RESTRICT_VIEW_ON'
    else:
      iconView = 'RESTRICT_VIEW_OFF'

    # mute
    row.prop(datablock, 'mute', text='', icon=iconView)

# modifier
def Modifier(self, context, layout, datablock, object, option):
  '''
    The object modifier name row.
  '''

  # search
  search = context.scene.NamePanel.search if option.regex else re.escape(context.scene.NamePanel.search)

  # row
  row = layout.row(align=True)
  row.enabled = (search == '' or re.search(search, datablock.name, re.I) != None)

  # sub
  sub = row.row()

  # scale
  sub.scale_x = 1.6

  # popups
  try:

    # pop ups
    if addon.preferences['popups'] == 1:

      # icon
      op = sub.operator('view3d.name_panel_modifier_settings', text='', icon=icon.modifier(datablock), emboss=False)
      op.object = object.name
      op.target = datablock.name

    else:

      # icon
      op = sub.operator('view3d.name_panel_icon', text='', icon=icon.modifier(datablock), emboss=False)
      op.owner = object.name
      op.target = datablock.name
      op.type = 'MODIFIER'

  except:

    # icon
    op = sub.operator('view3d.name_panel_icon', text='', icon=icon.modifier(datablock), emboss=False)
    op.owner = object.name
    op.target = datablock.name
    op.type = 'MODIFIER'

  # name
  row.prop(datablock, 'name', text='')

  # options
  if option.options:
    if datablock.type not in {'COLLISION', 'SOFT_BODY'}:

      # icon render
      if datablock.show_render:
        iconRender = 'RESTRICT_RENDER_OFF'
      else:
        iconRender = 'RESTRICT_RENDER_ON'

      # show render
      row.prop(datablock, 'show_render', text='', icon=iconRender)

      # icon view
      if datablock.show_viewport:
        iconView = 'RESTRICT_VIEW_OFF'
      else:
        iconView = 'RESTRICT_VIEW_ON'

      # show viewport
      row.prop(datablock, 'show_viewport', text='', icon=iconView)

# object data
def ObjectData(self, context, layout, datablock, option):
  '''
    The object data name row.
  '''

  # search
  search = context.scene.NamePanel.search if option.regex else re.escape(context.scene.NamePanel.search)

  # row
  row = layout.row(align=True)
  if datablock.type != 'EMPTY':
    row.enabled = (search == '' or re.search(search, datablock.data.name, re.I) != None)

  # empty
  if datablock.type in 'EMPTY':

    # empty image draw type
    if datablock.empty_draw_type in 'IMAGE':

      # image
      row.template_ID(datablock, 'data', open='image.open', unlink='image.unlink')

  else:

    if datablock == context.active_object:

      # name
      row.template_ID(datablock, 'data')

    else:

      # sub
      sub = row.row(align=True)
      sub.scale_x = 1.6

      # icon
      op = sub.operator('view3d.name_panel_icon', text='', icon=icon.objectData(datablock))
      op.owner = datablock.name
      op.target = datablock.name
      op.type = 'OBJECT_DATA'

      # name
      row.prop(datablock.data, 'name', text='')

# vertex group
def VertexGroup(self, context, layout, datablock, object, option):
  '''
    The object data vertex group name row.
  '''

  # row
  row = layout.row(align=True)

  # sub
  sub = row.row()

  # scale
  sub.scale_x = 1.6

  # icon
  op = sub.operator('view3d.name_panel_icon', text='', icon='GROUP_VERTEX', emboss=False)
  op.owner = object.name
  op.target = datablock.name
  op.type = 'VERTEX_GROUP'

  # name
  row.prop(datablock, 'name', text='')

  # options
  if option.options:

    # icon lock
    if datablock.lock_weight:
      iconLock = 'LOCKED'
    else:
      iconLock = 'UNLOCKED'

    # lock weight
    row.prop(datablock, 'lock_weight', text='', icon=iconLock)

# shapekey
def Shapekey(self, context, layout, datablock, object, option):
  '''
    The object animation data data shapekey name row.
  '''

  # row
  row = layout.row(align=True)

  # sub
  sub = row.row()

  # scale
  sub.scale_x = 1.6

  # icon
  op = sub.operator('view3d.name_panel_icon', text='', icon='SHAPEKEY_DATA', emboss=False)
  op.owner = object.name
  op.target = datablock.name
  op.type = 'SHAPEKEY'

  # name
  row.prop(datablock, 'name', text='')

  # options
  if option.options:
    if datablock != object.data.shape_keys.key_blocks[0]:

      # sub
      sub = row.row(align=True)

      # scale
      sub.scale_x = 0.17

      # value
      sub.prop(datablock, 'value', text='')

    # mute
    row.prop(datablock, 'mute', text='', icon='RESTRICT_VIEW_OFF')

# uv
def UV(self, context, layout, datablock, object, option):
  '''
    The object data uv name row.
  '''

  # row
  row = layout.row(align=True)

  # sub
  sub = row.row()

  # scale
  sub.scale_x = 1.6

  # icon
  op = sub.operator('view3d.name_panel_icon', text='', icon='GROUP_UVS', emboss=False)
  op.owner = object.name
  op.target = datablock.name
  op.type = 'UV'

  # name
  row.prop(datablock, 'name', text='')

  # options
  if option.options:

    # icon active
    if datablock.active_render:
      iconActive = 'RESTRICT_RENDER_OFF'
    else:
      iconActive = 'RESTRICT_RENDER_ON'

    # active render
    row.prop(datablock, 'active_render', text='', icon=iconActive)

# vertex color
def VertexColor(self, context, layout, datablock, object, option):
  '''
    The object data vertex color name row.
  '''

  # row
  row = layout.row(align=True)

  # sub
  sub = row.row()

  # scale
  sub.scale_x = 1.6

  # icon
  op = sub.operator('view3d.name_panel_icon', text='', icon='GROUP_VCOL', emboss=False)
  op.owner = object.name
  op.target = datablock.name
  op.type = 'VERTEX_COLOR'

  # name
  row.prop(datablock, 'name', text='')

  # options
  if option.options:

    # icon active
    if datablock.active_render:
      iconActive = 'RESTRICT_RENDER_OFF'
    else:
      iconActive = 'RESTRICT_RENDER_ON'

    # active_render
    row.prop(datablock, 'active_render', text='', icon=iconActive)

# material
def Material(self, context, layout, datablock, object, option):
  '''
    The object material name row.
  '''

  # search
  search = context.scene.NamePanel.search if option.regex else re.escape(context.scene.NamePanel.search)

  # row
  row = layout.row(align=True)
  row.enabled = (search == '' or re.search(search, datablock.name, re.I) != None)

  # sub
  sub = row.row()

  # scale
  sub.scale_x = 1.6

  # icon
  op = sub.operator('view3d.name_panel_icon', text='', icon='MATERIAL', emboss=False)
  op.owner = object.name
  op.target = datablock.name
  op.type = 'MATERIAL'

  # name
  row.prop(datablock.material, 'name', text='')

# texture
def Texture(self, context, layout, datablock, object, option):
  '''
    The texture name row.
  '''

  # row
  row = layout.row(align=True)

  # sub
  sub = row.row()

  # scale
  sub.scale_x = 1.6

  # icon
  op = sub.operator('view3d.name_panel_icon', text='', icon='TEXTURE', emboss=False)
  op.owner = object.name
  op.target = datablock.name
  op.type = 'TEXTURE'

  # name
  row.prop(datablock.texture, 'name', text='')

  # options
  if option.options:
    if hasattr(datablock, 'use'):

      # icon toggle
      if datablock.use:
        iconToggle = 'RADIOBUT_ON'
      else:
        iconToggle = 'RADIOBUT_OFF'

      # use
      row.prop(datablock, 'use', text='', icon=iconToggle)

# mask texture
def MaskTexture(self, context, layout, datablock, object, option):
  '''
    The mask texture name row.
  '''

  # row
  row = layout.row(align=True)

  # sub
  sub = row.row()

  # scale
  sub.scale_x = 1.6

  # icon
  op = sub.operator('view3d.name_panel_icon', text='', icon='TEXTURE', emboss=False)
  op.owner = object.name
  op.target = datablock.name
  op.type = 'TEXTURE'

  # name
  row.prop(datablock.mask_texture, 'name', text='')

  # options
  if option.options:
    if hasattr(datablock, 'use'):

      # icon toggle
      if datablock.use:
        iconToggle = 'RADIOBUT_ON'
      else:
        iconToggle = 'RADIOBUT_OFF'

      # use
      row.prop(datablock, 'use', text='', icon=iconToggle)

# particle
def Particle(self, context, layout, datablock, object, option):
  '''
    The modifier particle system and setting name row.
  '''

  # search
  search = context.scene.NamePanel.search if option.regex else re.escape(context.scene.NamePanel.search)

  # row
  row = layout.row(align=True)
  row.enabled = (search == '' or re.search(search, datablock.particle_system.name, re.I) != None)

  # sub
  sub = row.row()

  # scale
  sub.scale_x = 1.6

  # icon
  op = sub.operator('view3d.name_panel_icon', text='', icon='PARTICLES', emboss=False)
  op.owner = object.name
  op.target = datablock.name
  op.type = 'PARTICLE_SYSTEM'

  # name
  row.prop(datablock.particle_system, 'name', text='')

  # search
  if search == '' or re.search(search, datablock.particle_system.settings.name, re.I):

    # row
    row = layout.row(align=True)

    # sub
    sub = row.row()

    # scale
    sub.scale_x = 1.6

    # icon
    op = sub.operator('view3d.name_panel_icon', text='', icon='DOT', emboss=False)
    op.owner = object.name
    op.target = datablock.name
    op.type = 'PARTICLE_SETTING'

    # name
    row.prop(datablock.particle_system.settings, 'name', text='')

# bone group
def BoneGroup(self, context, layout, datablock, object):
  '''
    The armature data bone group name row.
  '''

  # row
  row = layout.row(align=True)

  # sub
  sub = row.row()

  # scale
  sub.scale_x = 1.6

  # icon
  op = sub.operator('view3d.name_panel_icon', text='', icon='GROUP_BONE', emboss=False)
  op.owner = object.name
  op.target = datablock.name
  op.type = 'BONE_GROUP'

  # name
  row.prop(datablock, 'name', text='')

# bone
def Bone(self, context, layout, datablock, object, option):
  '''
    The object data bone.
  '''

  # search
  search = context.scene.NamePanel.search if option.regex else re.escape(context.scene.NamePanel.search)

  # row
  row = layout.row(align=True)

  # enabled
  row.enabled = (search == '' or re.search(search, datablock.name, re.I) != None)

  # sub
  sub = row.row(align=True)

  # scale
  sub.scale_x = 1.6

  # active
  if datablock == context.active_bone:

    # display bones
    sub.prop(option, 'displayBones', text='', icon='BONE_DATA')

  # pose mode
  if object.mode in 'POSE':

    # datablock
    if not datablock == context.active_bone:

      # icon
      op = sub.operator('view3d.name_panel_icon', text='', icon='BONE_DATA')
      op.owner = object.name
      op.target = datablock.name
      op.type = 'BONE'

      # name
      row.prop(datablock, 'name', text='')

    # datablock
    else:

      # name
      row.prop(datablock, 'name', text='')

    # options
    if option.options:

      # icon view
      if datablock.hide:
        iconView = 'RESTRICT_VIEW_ON'
      else:
        iconView = 'RESTRICT_VIEW_OFF'

      # hide
      row.prop(datablock, 'hide', text='', icon=iconView)

      # icon hide select
      if datablock.hide_select:
        iconSelect = 'RESTRICT_SELECT_ON'
      else:
        iconSelect = 'RESTRICT_SELECT_OFF'

      # hide select
      row.prop(datablock, 'hide_select', text='', icon=iconSelect)

  # edit mode
  else:

    # name
    if not datablock == context.active_bone:

      # icon
      op = sub.operator('view3d.name_panel_icon', text='', icon='BONE_DATA')
      op.owner = object.name
      op.target = datablock.name
      op.type = 'BONE'

    # name
    row.prop(datablock, 'name', text='')

    # options
    if option.options:

      # icon view
      if datablock.hide:
        iconView = 'RESTRICT_VIEW_ON'
      else:
        iconView = 'RESTRICT_VIEW_OFF'

      # hide
      row.prop(datablock, 'hide', text='', icon=iconView)

      # icon select
      if datablock.hide_select:
        iconSelect = 'RESTRICT_SELECT_ON'
      else:
        iconSelect = 'RESTRICT_SELECT_OFF'

      # hide select
      row.prop(datablock, 'hide_select', text='', icon=iconSelect)

      # icon lock
      if datablock.lock:
        iconLock = 'LOCKED'
      else:
        iconLock = 'UNLOCKED'

      # lock
      row.prop(datablock, 'lock', text='', icon=iconLock)

  if object.mode in 'EDIT':
    # row
    row = layout.row()

    # separator
    row.separator()

  elif object.mode in 'POSE':
    if not option.boneConstraints or bpy.data.objects[object.name].pose.bones[datablock.name].constraints[:] == []:

      # row
      row = layout.row()

      # separator
      row.separator()
