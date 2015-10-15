
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

###############
## FUNCTIONS ##
###############

# modifier icon
def modifierIcon(modifier):
  '''
    Returns a icon based on modifier type.
  '''

  # data transfer
  if modifier.type in 'DATA_TRANSFER':
    icon = 'MOD_DATA_TRANSFER'

  # mesh cache
  elif modifier.type in 'MESH_CACHE':
    icon = 'MOD_MESHDEFORM'

  # normal edit
  elif modifier.type in 'NORMAL_EDIT':
    icon = 'MOD_NORMALEDIT'

  # uvs project
  elif modifier.type in 'UV_PROJECT':
    icon = 'MOD_UVPROJECT'

  # uvs warp
  elif modifier.type in 'UV_WARP':
    icon = 'MOD_UVPROJECT'

  # vertex weight edit
  elif modifier.type in 'VERTEX_WEIGHT_EDIT':
    icon = 'MOD_VERTEX_WEIGHT'

  # vertex weight mix
  elif modifier.type in 'VERTEX_WEIGHT_MIX':
    icon = 'MOD_VERTEX_WEIGHT'

  # vertex weight proximity
  elif modifier.type in 'VERTEX_WEIGHT_PROXIMITY':
    icon = 'MOD_VERTEX_WEIGHT'

  # array
  elif modifier.type in 'ARRAY':
    icon = 'MOD_ARRAY'

  # bevel
  elif modifier.type in 'BEVEL':
    icon = 'MOD_BEVEL'

  # bolean
  elif modifier.type in 'BOOLEAN':
    icon = 'MOD_BOOLEAN'

  # boptionld
  elif modifier.type in 'BUILD':
    icon = 'MOD_BUILD'

  # decimate
  elif modifier.type in 'DECIMATE':
    icon = 'MOD_DECIM'

  # edge split
  elif modifier.type in 'EDGE_SPLIT':
    icon = 'MOD_EDGESPLIT'

  # mask
  elif modifier.type in 'MASK':
    icon = 'MOD_MASK'

  # mirror
  elif modifier.type in 'MIRROR':
    icon = 'MOD_MIRROR'

  # multires
  elif modifier.type in 'MULTIRES':
    icon = 'MOD_MULTIRES'

  # remesh
  elif modifier.type in 'REMESH':
    icon = 'MOD_REMESH'

  # screw
  elif modifier.type in 'SCREW':
    icon = 'MOD_SCREW'

  # skin
  elif modifier.type in 'SKIN':
    icon = 'MOD_SKIN'

  # solidify
  elif modifier.type in 'SOLIDIFY':
    icon = 'MOD_SOLIDIFY'

  # subsurf
  elif modifier.type in 'SUBSURF':
    icon = 'MOD_SUBSURF'

  # triangulate
  elif modifier.type in 'TRIANGULATE':
    icon = 'MOD_TRIANGULATE'

  # wireframe
  elif modifier.type in 'WIREFRAME':
    icon = 'MOD_WIREFRAME'

  # armature
  elif modifier.type in 'ARMATURE':
    icon = 'MOD_ARMATURE'

  # cast
  elif modifier.type in 'CAST':
    icon = 'MOD_CAST'

  # corrective smooth
  elif modifier.type in 'CORRECTIVE_SMOOTH':
    icon = 'MOD_SMOOTH'

  # curve
  elif modifier.type in 'CURVE':
    icon = 'MOD_CURVE'

  # displace
  elif modifier.type in 'DISPLACE':
    icon = 'MOD_DISPLACE'

  # hook
  elif modifier.type in 'HOOK':
    icon = 'HOOK'

  # laplacian smooth
  elif modifier.type in 'LAPLACIANSMOOTH':
    icon = 'MOD_SMOOTH'

  # laplacian deform
  elif modifier.type in 'LAPLACIANDEFORM':
    icon = 'MOD_MESHDEFORM'

  # lattice
  elif modifier.type in 'LATTICE':
    icon = 'MOD_LATTICE'

  # mesh deform
  elif modifier.type in 'MESH_DEFORM':
    icon = 'MOD_MESHDEFORM'

  # shrinkwrap
  elif modifier.type in 'SHRINKWRAP':
    icon = 'MOD_SHRINKWRAP'

  # simple deform
  elif modifier.type in 'SIMPLE_DEFORM':
    icon = 'MOD_SIMPLEDEFORM'

  # smooth
  elif modifier.type in 'SMOOTH':
    icon = 'MOD_SMOOTH'

  # warp
  elif modifier.type in 'WARP':
    icon = 'MOD_WARP'

  # wave
  elif modifier.type in 'WAVE':
    icon = 'MOD_WAVE'

  # cloth
  elif modifier.type in 'CLOTH':
    icon = 'MOD_CLOTH'

  # collision
  elif modifier.type in 'COLLISION':
    icon = 'MOD_PHYSICS'

  # dynamic paint
  elif modifier.type in 'DYNAMIC_PAINT':
    icon = 'MOD_DYNAMICPAINT'

  # explode
  elif modifier.type in 'EXPLODE':
    icon = 'MOD_EXPLODE'

  # floptiond simulation
  elif modifier.type in 'FLUID_SIMULATION':
    icon = 'MOD_FLUIDSIM'

  # ocean
  elif modifier.type in 'OCEAN':
    icon = 'MOD_OCEAN'

  # particle instance
  elif modifier.type in 'PARTICLE_INSTANCE':
    icon = 'MOD_PARTICLES'

  # particle system
  elif modifier.type in 'PARTICLE_SYSTEM':
    icon = 'MOD_PARTICLES'

  # smoke
  elif modifier.type in 'SMOKE':
    icon = 'MOD_SMOKE'

  # soft body
  elif modifier.type in 'SOFT_BODY':
    icon = 'MOD_SOFT'

  # default
  else:
    icon = 'MODIFIER'
  return icon

# object icon
def objectIcon(object):
  '''
    Returns a icon based on object type.
  '''

  # mesh
  if object.type in 'MESH':
    icon = 'OUTLINER_OB_MESH'

  # curve
  elif object.type in 'CURVE':
    icon = 'OUTLINER_OB_CURVE'

  # surface
  elif object.type in 'SURFACE':
    icon = 'OUTLINER_OB_SURFACE'

  # meta
  elif object.type in 'META':
    icon = 'OUTLINER_OB_META'

  # font
  elif object.type in 'FONT':
    icon = 'OUTLINER_OB_FONT'

  # armature
  elif object.type in 'ARMATURE':
    icon = 'OUTLINER_OB_ARMATURE'

  # lattice
  elif object.type in 'LATTICE':
    icon = 'OUTLINER_OB_LATTICE'

  # empty
  elif object.type in 'EMPTY':
    icon = 'OUTLINER_OB_EMPTY'

  # speaker
  elif object.type in 'SPEAKER':
    icon = 'OUTLINER_OB_SPEAKER'

  # camera
  elif object.type in 'CAMERA':
    icon = 'OUTLINER_OB_CAMERA'

  # lamp
  elif object.type in 'LAMP':
    icon = 'OUTLINER_OB_LAMP'

  # default
  else:
    icon = 'OUTLINER_OB_MESH'
  return icon

# object data icon
def objectDataIcon(object):
  '''
    Returns a icon based on object type.
  '''

  # mesh
  if object.type in 'MESH':
    icon = 'MESH_DATA'

  # curve
  elif object.type in 'CURVE':
    icon = 'CURVE_DATA'

  # surface
  elif object.type in 'SURFACE':
    icon = 'SURFACE_DATA'

  # meta
  elif object.type in 'META':
    icon = 'META_DATA'

  # font
  elif object.type in 'FONT':
    icon = 'FONT_DATA'

  # armature
  elif object.type in 'ARMATURE':
    icon = 'ARMATURE_DATA'

  # lattice
  elif object.type in 'LATTICE':
    icon = 'LATTICE_DATA'

  # speaker
  elif object.type in 'SPEAKER':
    icon = 'SPEAKER'

  # camera
  elif object.type in 'CAMERA':
    icon = 'CAMERA_DATA'

  # lamp
  elif object.type in 'LAMP':
    icon = 'LAMP_DATA'

  # default
  else:
    icon = 'MESH_DATA'
  return icon

###########
## PANEL ##
###########

# item
class item:
  '''
    Item panel
  '''

  # draw
  def draw(self, context):
    '''
      Item panel body.
    '''

    # layout
    layout = self.layout

    # option
    option = context.screen.itemPanelSettings

    # column
    column = layout.column(align=True)

    # row
    row = column.row(align=True)

    # scale
    row.scale_y = 1.25

    # icon toggle
    if option.filters:
      iconToggle = 'RADIOBUT_ON'
    else:
      iconToggle = 'RADIOBUT_OFF'

    # filters
    row.prop(option, 'filters', text='Filters', icon=iconToggle, toggle=True)

    # options
    row.prop(option, 'options', text='', icon='SETTINGS')

    # selected
    row.prop(option, 'selected', text='', icon='OOPS')

    # operator menu
    row.menu('VIEW3D_MT_item_panel_specials', text='', icon='DOWNARROW_HLT')

    # filters
    if option.filters:

      # row 1
      row = column.row(align=True)

      # scale
      row.scale_x = 5 # hack: forces buttons to line up correctly

      # groups
      row.prop(option, 'groups', text='', icon='GROUP')

      # action
      row.prop(option, 'action', text='', icon='ACTION')

      # grease pencil
      row.prop(option, 'greasePencil', text='', icon='GREASEPENCIL')

      # constraints
      row.prop(option, 'constraints', text='', icon='CONSTRAINT')

      # modifiers
      row.prop(option, 'modifiers', text='', icon='MODIFIER')

      # bone groups
      row.prop(option, 'boneGroups', text='', icon='GROUP_BONE')

      # bone constraints
      row.prop(option, 'boneConstraints', text='', icon='CONSTRAINT_BONE')

      # row 2
      row = column.row(align=True)

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

    # column
    column = layout.column()

    # row
    row = column.row()

    # seperator
    row.separator()

    # row
    row = column.row(align=True)

    # active object
    row.template_ID(context.scene.objects, 'active')

    # groups
    if option.groups:
      for group in bpy.data.groups[:]:
        for object in group.objects[:]:
          if object == context.active_object:

            # row
            row = column.row(align=True)

            # sub
            sub = row.row()

            # scale
            sub.scale_x = 1.6

            # label
            sub.label(text='', icon='GROUP')

            # name
            row.prop(group, 'name', text='')

    # action
    if option.action:
      if hasattr(context.active_object.animation_data, 'action'):
        if hasattr(context.active_object.animation_data.action, 'name'):

          # row
          row = column.row(align=True)

          # sub
          sub = row.row()

          # scale
          sub.scale_x = 1.6

          # label
          sub.label(text='', icon='ACTION')

          # name
          row.prop(bpy.data.objects[context.active_object.name].animation_data.action, 'name', text='')

    # grease pencil
    if option.greasePencil:
      if hasattr(context.active_object.grease_pencil, 'name'):

        # row
        row = column.row(align=True)

        # sub
        sub = row.row()

        # scale
        sub.scale_x = 1.6

        # label
        sub.label(text='', icon='GREASEPENCIL')

        # name
        row.prop(bpy.data.objects[context.active_object.name].grease_pencil, 'name', text='')

        for layer in bpy.data.objects[context.active_object.name].grease_pencil.layers[:]:

          # row
          row = column.row(align=True)

          # sub
          sub = row.row(align=True)

          # scale
          sub.scale_x = 0.17

          # color
          sub.prop(layer, 'color', text='')

          # info
          row.prop(layer, 'info', text='')

          # options
          if option.options:

            # lock
            row.prop(layer, 'lock', text='')

            # hide
            row.prop(layer, 'hide', text='')

    # constraints
    if option.constraints:
      for constraint in bpy.data.objects[context.active_object.name].constraints[:]:

        # row
        row = column.row(align=True)

        # sub
        sub = row.row()

        # scale
        sub.scale_x = 1.6

        # label
        sub.label(text='', icon='CONSTRAINT')

        # name
        row.prop(constraint, 'name', text='')

        # options
        if option.options:

          # influence
          if constraint.type not in {'RIGID_BODY_JOINT', 'NULL'}:

            # sub
            sub = row.row(align=True)

            # scale
            sub.scale_x = 0.17

            # influence
            sub.prop(constraint, 'influence', text='')

          # icon view
          if constraint.mute:
            iconView = 'RESTRICT_VIEW_ON'
          else:
            iconView = 'RESTRICT_VIEW_OFF'

          # mute
          row.prop(constraint, 'mute', text='', icon=iconView)

    # modifiers
    if option.modifiers:
      for modifier in bpy.data.objects[context.active_object.name].modifiers[:]:

        # row
        row = column.row(align=True)

        # sub
        sub = row.row()
        sub.scale_x = 1.6
        sub.label(text='', icon=modifierIcon(modifier))
        row.prop(modifier, 'name', text='')

        # options
        if option.options:
          if modifier.type not in {'COLLISION', 'SOFT_BODY'}:

            # icon render
            if modifier.show_render:
              iconRender = 'RESTRICT_RENDER_OFF'
            else:
              iconRender = 'RESTRICT_RENDER_ON'

            # show render
            row.prop(modifier, 'show_render', text='', icon=iconRender)

            # icon View
            if modifier.show_viewport:
              iconView = 'RESTRICT_VIEW_OFF'
            else:
              iconView = 'RESTRICT_VIEW_ON'

            # show viewport
            row.prop(modifier, 'show_viewport', text='', icon=iconView)

        # particle systems
        if option.particleSystems:
          if modifier.type in 'PARTICLE_SYSTEM':

            # row
            row = column.row(align=True)

            # sub
            sub = row.row()

            # scale
            sub.scale_x = 1.6

            # label
            sub.label(text='', icon='PARTICLES')

            # name
            row.prop(modifier.particle_system, 'name', text='')

            # particle settings

            # row
            row = column.row(align=True)

            # sub
            sub = row.row()

            # scale
            sub.scale_x = 1.6

            # label
            sub.label(text='', icon='DOT')

            # name
            row.prop(modifier.particle_system.settings, 'name', text='')

    # disable particle system filter
    else:
      option.particleSystems = False

    # materials
    if option.materials:
      for material in bpy.data.objects[context.active_object.name].material_slots[:]:
        if material.material != None:
          if material.link == 'OBJECT':

            # row
            row = column.row(align=True)

            # sub
            sub = row.row()

            # scale
            sub.scale_x = 1.6

            # label
            sub.label(text='', icon='MATERIAL')

            # name
            row.prop(material.material, 'name', text='')

            # texture
            if option.textures:
              if context.scene.render.engine in 'BLENDER_RENDER':
                for texture in material.material.texture_slots[:]:
                  if texture != None:

                    # row
                    row = column.row(align=True)

                    # sub
                    sub = row.row()

                    # scale
                    sub.scale_x = 1.6

                    # label
                    sub.label(text='', icon='TEXTURE')

                    # name
                    row.prop(texture.texture, 'name', text='')

                    # options
                    if option.options:

                      # iconToggle
                      if texture.use:
                        iconToggle = 'RADIOBUT_ON'
                      else:
                        iconToggle = 'RADIOBUT_OFF'

                      # use
                      row.prop(texture, 'use', text='', icon=iconToggle)

    # disable textures filter
    else:
      option.textures = False

    # empty
    if context.object.type in 'EMPTY':

      # empty image draw type
      if context.object.empty_draw_type in 'IMAGE':

        # row
        row = column.row(align=True)

        # image
        row.template_ID(context.active_object, 'data', open='image.open', unlink='image.unlink')

      # row
      row = column.row()

      # separator
      row.separator()

    else:

      # row
      row = column.row(align=True)

      # active object data
      row.template_ID(bpy.data.objects[context.active_object.name], 'data')

      # vertex groups
      if option.vertexGroups:
        if hasattr(bpy.data.objects[context.active_object.name], 'vertex_groups'):
          for group in bpy.data.objects[context.active_object.name].vertex_groups[:]: # shouldn't this be in object data?

            # row
            row = column.row(align=True)

            # sub
            sub = row.row()

            # scale
            sub.scale_x = 1.6

            # label
            sub.label(text='', icon='GROUP_VERTEX')

            # name
            row.prop(group, 'name', text='')

            # options
            if option.options:

              # icon lock
              if group.lock_weight:
                iconLock = 'LOCKED'
              else:
                iconLock = 'UNLOCKED'

              # lock weight
              row.prop(group, 'lock_weight', text='', icon=iconLock)

      # shapekeys
      if option.shapekeys:
        if hasattr(bpy.data.objects[context.active_object.name].data, 'shape_keys'):
          if hasattr(bpy.data.objects[context.active_object.name].data.shape_keys, 'key_blocks'):
            for key in bpy.data.objects[context.active_object.name].data.shape_keys.key_blocks[:]:

              # row
              row = column.row(align=True)

              # sub
              sub = row.row()

              # scale
              sub.scale_x = 1.6

              # label
              sub.label(text='', icon='SHAPEKEY_DATA')

              # name
              row.prop(key, 'name', text='')

              # options
              if option.options:
                if key != bpy.data.objects[context.active_object.name].data.shape_keys.key_blocks[0]:

                  # sub
                  sub = row.row(align=True)

                  # scale
                  sub.scale_x = 0.17

                  # value
                  sub.prop(key, 'value', text='')

                # mute
                row.prop(key, 'mute', text='', icon='RESTRICT_VIEW_OFF')

      # uvs
      if option.uvs:
        if bpy.data.objects[context.active_object.name].type in 'MESH':
          for uvs in bpy.data.objects[context.active_object.name].data.uv_textures[:]:

            # row
            row = column.row(align=True)

            # sub
            sub = row.row()

            # scale
            sub.scale_x = 1.6

            # label
            sub.label(text='', icon='GROUP_UVS')

            # name
            row.prop(uvs, 'name', text='')

            # options
            if option.options:

              # icon active
              if uvs.active_render:
                iconActive = 'RESTRICT_RENDER_OFF'
              else:
                iconActive = 'RESTRICT_RENDER_ON'

              # active render
              row.prop(uvs, 'active_render', text='', icon=iconActive)

      # vertex colors
      if option.vertexColors:
        if bpy.data.objects[context.active_object.name].type in 'MESH':
          for vertexColor in bpy.data.objects[context.active_object.name].data.vertex_colors[:]:

            # row
            row = column.row(align=True)

            # sub
            sub = row.row()

            # scale
            sub.scale_x = 1.6

            # label
            sub.label(text='', icon='GROUP_VCOL')

            # name
            row.prop(vertexColor, 'name', text='')

            # options
            if option.options:

              # icon active
              if vertexColor.active_render:
                iconActive = 'RESTRICT_RENDER_OFF'
              else:
                iconActive = 'RESTRICT_RENDER_ON'

              # active render
              row.prop(vertexColor, 'active_render', text='', icon=iconActive)

      # materials
      if option.materials:
        for material in bpy.data.objects[context.active_object.name].material_slots[:]:
          if material.material != None:
            if material.link == 'DATA':

              # row
              row = column.row(align=True)

              # sub
              sub = row.row()

              # scale
              sub.scale_x = 1.6

              # label
              sub.label(text='', icon='MATERIAL')

              # name
              row.prop(material.material, 'name', text='')

              # textures
              if option.textures:
                if context.scene.render.engine in 'BLENDER_RENDER':
                  for texture in material.material.texture_slots[:]:
                    if texture != None:

                      # row
                      row = column.row(align=True)

                      # sub
                      sub = row.row()

                      # scale
                      sub.scale_x = 1.6

                      # label
                      sub.label(text='', icon='TEXTURE')

                      # name
                      row.prop(texture.texture, 'name', text='')

                      # options
                      if option.options:

                        # icon toggle
                        if texture.use:
                          iconToggle = 'RADIOBUT_ON'
                        else:
                          iconToggle = 'RADIOBUT_OFF'

                        # use
                        row.prop(texture, 'use', text='', icon=iconToggle)
      else:
        option.textures = False

      # bone groups
      if option.boneGroups:
        if bpy.data.objects[context.active_object.name].type in 'ARMATURE':
          for group in bpy.data.objects[context.active_object.name].pose.bone_groups[:]:

            # row
            row = column.row(align=True)

            # sub
            sub = row.row()

            # scale
            sub.scale_x = 1.6

            # label
            sub.label(text='', icon='GROUP_BONE')

            # name
            row.prop(group, 'name', text='')

      # row
      row = column.row()
      row.separator()

      # active bone
      if bpy.data.objects[context.active_object.name].type in 'ARMATURE':
        if context.object.mode in {'POSE', 'EDIT'}:
          if context.active_bone:

            # row
            row = column.row(align=True)

            # sub
            sub = row.row(align=True)

            # scale
            sub.scale_x = 1.6

            # selected bones
            sub.prop(option, 'selectedBones', text='', icon='BONE_DATA')

            # pose mode
            if context.object.mode in 'POSE':

              # name
              row.prop(bpy.data.armatures[context.active_object.data.name].bones.active, 'name', text='')

              # options
              if option.options:

                # icon view
                if bpy.data.armatures[context.active_object.data.name].bones.active.hide:
                  iconView = 'RESTRICT_VIEW_ON'
                else:
                  iconView = 'RESTRICT_VIEW_OFF'

                # hide
                row.prop(bpy.data.armatures[context.active_object.data.name].bones.active, 'hide', text='', icon=iconView)

                # icon hide select
                if bpy.data.armatures[context.active_object.data.name].bones.active.hide_select:
                  iconSelect = 'RESTRICT_SELECT_ON'
                else:
                  iconSelect = 'RESTRICT_SELECT_OFF'

                # hide select
                row.prop(bpy.data.armatures[context.active_object.data.name].bones.active, 'hide_select', text='', icon=iconSelect)

            # edit mode
            else:

              # name
              row.prop(bpy.data.armatures[context.active_object.data.name].edit_bones.active, 'name', text='')

              # options
              if option.options:

                # icon view
                if bpy.data.armatures[context.active_object.data.name].edit_bones.active.hide:
                  iconView = 'RESTRICT_VIEW_ON'
                else:
                  iconView = 'RESTRICT_VIEW_OFF'

                # hide
                row.prop(bpy.data.armatures[context.active_object.data.name].edit_bones.active, 'hide', text='', icon=iconView)

                # icon select
                if bpy.data.armatures[context.active_object.data.name].edit_bones.active.hide_select:
                  iconSelect = 'RESTRICT_SELECT_ON'
                else:
                  iconSelect = 'RESTRICT_SELECT_OFF'

                # hide select
                row.prop(bpy.data.armatures[context.active_object.data.name].edit_bones.active, 'hide_select', text='', icon=iconSelect)

                # icon lock
                if bpy.data.armatures[context.active_object.data.name].edit_bones.active.lock:
                  iconLock = 'LOCKED'
                else:
                  iconLock = 'UNLOCKED'

                # lock
                row.prop(bpy.data.armatures[context.active_object.data.name].edit_bones.active, 'lock', text='', icon=iconLock)

            # bone constraints
            if option.boneConstraints:
              if context.object.mode in 'POSE':
                for constraint in bpy.data.objects[context.active_object.name].pose.bones[context.active_bone.name].constraints[:]:

                  # row
                  row = column.row(align=True)

                  # sub
                  sub = row.row()

                  # scalse
                  sub.scale_x = 1.6

                  # label
                  sub.label(text='', icon='CONSTRAINT_BONE')

                  # name
                  row.prop(constraint, 'name', text='')

                  # options
                  if option.options:

                    # sub
                    sub = row.row(align=True)

                    # scale
                    sub.scale_x = 0.17

                    # influence
                    sub.prop(constraint, 'influence', text='')

                    # icon view
                    if constraint.mute:
                      iconView = 'RESTRICT_VIEW_ON'
                    else:
                      iconView = 'RESTRICT_VIEW_OFF'

                    # mute
                    row.prop(constraint, 'mute', text='', icon=iconView)

            # selected bones
            if option.selectedBones:

              # row
              row = column.row()

              # separator
              row.separator()

              # edit mode
              if context.object.mode in 'EDIT':
                bones = bpy.data.armatures[context.active_object.data.name].edit_bones[:]

              # pose mode
              else:
                bones = bpy.data.armatures[context.active_object.data.name].bones[:]

              # selected bones
              selectedBones = []
              for bone in bones:

                # pose mode
                if context.object.mode in 'POSE':
                  if bone.select:
                    selectedBones.append((bone.name, bone))

                # edit mode
                else:
                  if bone.select:
                    selectedBones.append((bone.name, bone))

              # sort and display
              for bone in sorted(selectedBones):
                if bone[1] != context.active_bone:

                  # row
                  row = column.row(align=True)

                  # bone
                  row.prop(bone[1], 'name', text='', icon='BONE_DATA')

                  # options
                  if option.options:

                    # icon hide
                    if bone[1].hide:
                      iconView = 'RESTRICT_VIEW_ON'
                    else:
                      iconView = 'RESTRICT_VIEW_OFF'

                    # hide
                    row.prop(bone[1], 'hide', text='', icon=iconView)

                    # icon hide select
                    if bone[1].hide_select:
                      iconSelect = 'RESTRICT_SELECT_ON'
                    else:
                      iconSelect = 'RESTRICT_SELECT_OFF'

                    # hide select
                    row.prop(bone[1], 'hide_select', text='', icon=iconSelect)

                    # edit mode
                    if context.object.mode in 'EDIT':

                      # icon lock
                      if bone[1].lock:
                        iconLock = 'LOCKED'
                      else:
                        iconLock = 'UNLOCKED'

                      # lock
                      row.prop(bone[1], 'lock', text='', icon=iconLock)

                  # bone constraints
                  if option.boneConstraints:
                    if context.object.mode in 'POSE':
                      for constraint in bpy.data.objects[context.active_object.name].pose.bones[bone[1].name].constraints[:]:

                        # row
                        row = column.row(align=True)

                        # sub
                        sub = row.row()

                        # scale
                        sub.scale_x = 1.6

                        # label
                        sub.label(text='', icon='CONSTRAINT_BONE')

                        # name
                        row.prop(constraint, 'name', text='')

                        # options
                        if option.options:

                          # sub
                          sub = row.row(align=True)

                          # scale
                          sub.scale_x = 0.17

                          # influence
                          sub.prop(constraint, 'influence', text='')

                          # icon view
                          if constraint.mute:
                            iconView = 'RESTRICT_VIEW_ON'
                          else:
                            iconView = 'RESTRICT_VIEW_OFF'

                          # mute
                          row.prop(constraint, 'mute', text='', icon=iconView)

                  # row
                  row = column.row()

                  # separator
                  row.separator()
            else:

              # row
              row = column.row()

              # separator
              row.separator()

    # selected
    if option.selected:
      for object in bpy.data.objects[:]:
        if object != context.active_object:
          if object.select:

            # row
            row = column.row(align=True)

            # object
            row.prop(object, 'name', text='', icon=objectIcon(object))

            # options
            if option.options:

              # hide
              row.prop(object, 'hide', text='')

              # hide select
              row.prop(object, 'hide_select', text='')

              # hide render
              row.prop(object, 'hide_render', text='')

            # groups
            if option.groups:
              for group in bpy.data.groups[:]:
                for groupObject in group.objects[:]:
                  if groupObject == object:

                    # row
                    row = column.row(align=True)

                    # sub
                    sub = row.row()

                    # scale
                    sub.scale_x = 1.6

                    # label
                    sub.label(text='', icon='GROUP')

                    # name
                    row.prop(group, 'name', text='')

            # actions
            if option.action:
              if hasattr(object.animation_data, 'action'):
                if hasattr(object.animation_data.action, 'name'):

                  # row
                  row = column.row(align=True)

                  # sub
                  sub = row.row()

                  # scale
                  sub.scale_x = 1.6

                  # label
                  sub.label(text='', icon='ACTION')

                  # name
                  row.prop(bpy.data.objects[object.name].animation_data.action, 'name', text='')

            # grease pencil
            if option.greasePencil:
              if hasattr(object.grease_pencil, 'name'):

                # row
                row = column.row(align=True)

                # sub
                sub = row.row()

                # scale
                sub.scale_x = 1.6

                # label
                sub.label(text='', icon='GREASEPENCIL')

                # name
                row.prop(bpy.data.objects[object.name].grease_pencil, 'name', text='')

                # layers
                for layer in bpy.data.objects[object.name].grease_pencil.layers[:]:

                  # row
                  row = column.row(align=True)

                  # sub
                  sub = row.row(align=True)

                  # scale
                  sub.scale_x = 0.175

                  # color
                  sub.prop(layer, 'color', text='')

                  # info (name)
                  row.prop(layer, 'info', text='')

                  # options
                  if option.options:

                    # lock
                    row.prop(layer, 'lock', text='')

                    # hide
                    row.prop(layer, 'hide', text='')

            # constraints
            if option.constraints:
              for constraint in object.constraints[:]:

                # row
                row = column.row(align=True)

                # sub
                sub = row.row()

                # scale
                sub.scale_x = 1.6

                # label
                sub.label(text='', icon='CONSTRAINT')

                # name
                row.prop(constraint, 'name', text='')

                # options
                if option.options:

                  # influence
                  if constraint.type not in {'RIGID_BODY_JOINT', 'NULL'}:

                    # sub
                    sub = row.row(align=True)

                    # scale
                    sub.scale_x = 0.17

                    # influence
                    sub.prop(constraint, 'influence', text='')

                  # icon view
                  if constraint.mute:
                    iconView = 'RESTRICT_VIEW_ON'
                  else:
                    iconView = 'RESTRICT_VIEW_OFF'

                  # mute
                  row.prop(constraint, 'mute', text='', icon=iconView)

            # modifiers
            if option.modifiers:
              for modifier in object.modifiers[:]:

                # row
                row = column.row(align=True)

                # sub
                sub = row.row()

                # scale
                sub.scale_x = 1.6

                # label
                sub.label(text='', icon=modifierIcon(modifier))

                # name
                row.prop(modifier, 'name', text='')

                # options
                if option.options:
                  if modifier.type not in {'COLLISION', 'SOFT_BODY'}:

                    # icon render
                    if modifier.show_render:
                      iconRender = 'RESTRICT_RENDER_OFF'
                    else:
                      iconRender = 'RESTRICT_RENDER_ON'

                    # show render
                    row.prop(modifier, 'show_render', text='', icon=iconRender)

                    # icon view
                    if modifier.show_viewport:
                      iconView = 'RESTRICT_VIEW_OFF'
                    else:
                      iconView = 'RESTRICT_VIEW_ON'

                    # show viewport
                    row.prop(modifier, 'show_viewport', text='', icon=iconView)

                # particle systems
                if option.particleSystems:
                  if modifier.type in 'PARTICLE_SYSTEM':

                    # row
                    row = column.row(align=True)

                    # sub
                    sub = row.row()

                    # scale
                    sub.scale_x = 1.6

                    # label
                    sub.label(text='', icon='PARTICLES')

                    # name
                    row.prop(modifier.particle_system, 'name', text='')

                    # particle settings

                    # row
                    row = column.row(align=True)

                    # sub
                    sub = row.row()

                    # scale
                    sub.scale_x = 1.6

                    # label
                    sub.label(text='', icon='DOT')

                    # name
                    row.prop(modifier.particle_system.settings, 'name', text='')

            # materials
            if option.materials:
              for material in bpy.data.objects[object.name].material_slots[:]:
                if material.material != None:
                  if material.link == 'OBJECT':

                    # row
                    row = column.row(align=True)

                    # sub
                    sub = row.row()

                    # scale
                    sub.scale_x = 1.6

                    # label
                    sub.label(text='', icon='MATERIAL')

                    # name
                    row.prop(material.material, 'name', text='')

                    # textures
                    if option.textures:
                      if context.scene.render.engine in 'BLENDER_RENDER':
                        for texture in material.material.texture_slots[:]:
                          if texture != None:

                            # row
                            row = column.row(align=True)

                            # sub
                            sub = row.row()

                            # scale
                            sub.scale_x = 1.6

                            # label
                            sub.label(text='', icon='TEXTURE')

                            # name
                            row.prop(texture.texture, 'name', text='')

                            # options
                            if option.options:

                              # icon toggle
                              if texture.use:
                                iconToggle = 'RADIOBUT_ON'
                              else:
                                iconToggle = 'RADIOBUT_OFF'

                              # use
                              row.prop(texture, 'use', text='', icon=iconToggle)

            # empty
            if object.type in 'EMPTY':

              # row
              row = column.row()

              # separator
              row.separator()

            # object data
            else:

              # row
              row = column.row(align=True)

              # name
              row.prop(object.data, 'name', text='', icon=objectDataIcon(object))

              # vertex groups
              if option.vertexGroups:
                if hasattr(bpy.data.objects[object.name], 'vertex_groups'):
                  for group in bpy.data.objects[object.name].vertex_groups[:]:

                    # row
                    row = column.row(align=True)

                    # sub
                    sub = row.row()

                    # scale
                    sub.scale_x = 1.6

                    # label
                    sub.label(text='', icon='GROUP_VERTEX')

                    # name
                    row.prop(group, 'name', text='')

                    # options
                    if option.options:

                      # icon lock
                      if group.lock_weight:
                        iconLock = 'LOCKED'
                      else:
                        iconLock = 'UNLOCKED'

                      # lock weight
                      row.prop(group, 'lock_weight', text='', icon=iconLock)

              # shapekeys
              if option.shapekeys:
                if hasattr(bpy.data.objects[object.name].data, 'shape_keys'):
                  if hasattr(bpy.data.objects[object.name].data.shape_keys, 'key_blocks'):
                    for key in bpy.data.objects[object.name].data.shape_keys.key_blocks[:]:

                      # row
                      row = column.row(align=True)

                      # sub
                      sub = row.row()

                      # scale
                      sub.scale_x = 1.6

                      # label
                      sub.label(text='', icon='SHAPEKEY_DATA')

                      # name
                      row.prop(key, 'name', text='')

                      # options
                      if option.options:
                        if key != bpy.data.objects[object.name].data.shape_keys.key_blocks[0]:

                          # sub
                          sub = row.row(align=True)

                          # scale
                          sub.scale_x = 0.17

                          # value
                          sub.prop(key, 'value', text='')

                        # mute
                        row.prop(key, 'mute', text='', icon='RESTRICT_VIEW_OFF')

              # uvs
              if option.uvs:
                if bpy.data.objects[object.name].type in 'MESH':
                  for uvs in bpy.data.objects[object.name].data.uv_textures[:]:

                    # row
                    row = column.row(align=True)

                    # sub
                    sub = row.row()

                    # scale
                    sub.scale_x = 1.6

                    # label
                    sub.label(text='', icon='GROUP_UVS')

                    # name
                    row.prop(uvs, 'name', text='')

                    # options
                    if option.options:

                      # icon active
                      if uvs.active_render:
                        iconActive = 'RESTRICT_RENDER_OFF'
                      else:
                        iconActive = 'RESTRICT_RENDER_ON'

                      # active render
                      row.prop(uvs, 'active_render', text='', icon=iconActive)

              # vertex colors
              if option.vertexColors:
                if bpy.data.objects[object.name].type in 'MESH':
                  for vertexColor in bpy.data.objects[object.name].data.vertex_colors[:]:

                    # row
                    row = column.row(align=True)

                    # sub
                    sub = row.row()

                    # scale
                    sub.scale_x = 1.6

                    # label
                    sub.label(text='', icon='GROUP_VCOL')

                    # name
                    row.prop(vertexColor, 'name', text='')

                    # options
                    if option.options:

                      # icon active
                      if vertexColor.active_render:
                        iconActive = 'RESTRICT_RENDER_OFF'
                      else:
                        iconActive = 'RESTRICT_RENDER_ON'

                      # active_render
                      row.prop(vertexColor, 'active_render', text='', icon=iconActive)

              # materials
              if option.materials:
                for material in bpy.data.objects[object.name].material_slots[:]:
                  if material.material != None:
                    if material.link == 'DATA':

                      # row
                      row = column.row(align=True)

                      # sub
                      sub = row.row()

                      # scale
                      sub.scale_x = 1.6

                      # label
                      sub.label(text='', icon='MATERIAL')

                      # name
                      row.prop(material.material, 'name', text='')

                      # textures
                      if option.textures:
                        if context.scene.render.engine not in 'CYCLES':
                          for texture in material.material.texture_slots[:]:
                            if texture != None:

                              # row
                              row = column.row(align=True)

                              # sub
                              sub = row.row()

                              # scale
                              sub.scale_x = 1.6

                              # label
                              sub.label(text='', icon='TEXTURE')

                              # name
                              row.prop(texture.texture, 'name', text='')

                              # options
                              if option.options:

                                # icon toggle
                                if texture.use:
                                  iconToggle = 'RADIOBUT_ON'
                                else:
                                  iconToggle = 'RADIOBUT_OFF'

                                # use
                                row.prop(texture, 'use', text='', icon=iconToggle)

              # bone groups
              if option.boneGroups:
                if bpy.data.objects[object.name].type in 'ARMATURE':
                  for group in bpy.data.objects[object.name].pose.bone_groups[:]:

                    # row
                    row = column.row(align=True)

                    # sub
                    sub = row.row()

                    # scale
                    sub.scale_x = 1.6

                    # label
                    sub.label(text='', icon='GROUP_BONE')

                    # name
                    row.prop(group, 'name', text='')

              # row
              row = column.row()

              # separator
              row.separator()


# default
class default:
  '''
    Source from the original item panel class, used to return the panel to default usability upon unregiser.
  '''

  # draw
  def draw(self, context):
    '''
      Item panel body.
    '''

    # layout
    layout = self.layout

    # row
    row = layout.row()
    row.label(text='', icon='OBJECT_DATA')
    row.prop(context.active_object, 'name', text='')
    if context.active_object.type == 'ARMATURE' and context.active_object.mode in {'EDIT', 'POSE'}:
      if context.active_bone:

        # row
        row = layout.row()
        row.label(text='', icon='BONE_DATA')
        row.prop(context.acive_bone, 'name', text='')
