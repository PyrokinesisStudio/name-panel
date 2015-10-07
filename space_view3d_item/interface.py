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

# panel
class panel():
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

    # data
    data = bpy.data

    # column
    column = layout.column(align=True)

    # row
    row = column.row(align=True)
    row.scale_y = 1.25

    if option.filters:
      iconToggle = 'RADIOBUT_ON'
    else:
      iconToggle = 'RADIOBUT_OFF'

    # view filters
    row.prop(option, 'filters', text='Filters', icon=iconToggle, toggle=True)

    # view hierarchy
    row.prop(option, 'selected', text='', icon='OOPS')

    # operator menu
    row.menu('VIEW3D_MT_item_panel_specials', text='', icon='DOWNARROW_HLT')
    if option.filters:

      # datablock filters

      # row 1
      row = column.row(align=True)
      row.scale_x = 5 # hack: forces buttons to line up correctly
      row.prop(option, 'groups', text='', icon='GROUP')
      row.prop(option, 'action', text='', icon='ACTION')
      row.prop(option, 'greasePencil', text='', icon='GREASEPENCIL')
      row.prop(option, 'constraints', text='', icon='CONSTRAINT')
      row.prop(option, 'modifiers', text='', icon='MODIFIER')
      row.prop(option, 'boneGroups', text='', icon='GROUP_BONE')
      row.prop(option, 'boneConstraints', text='', icon='CONSTRAINT_BONE')

      # row 2
      row = column.row(align=True)
      row.scale_x = 5 # hack: forces buttons to line up correctly
      row.prop(option, 'vertexGroups', text='', icon='GROUP_VERTEX')
      row.prop(option, 'shapekeys', text='', icon='SHAPEKEY_DATA')
      row.prop(option, 'uvs', text='', icon='GROUP_UVS')
      row.prop(option, 'vertexColors', text='', icon='GROUP_VCOL')
      row.prop(option, 'materials', text='', icon='MATERIAL')
      row.prop(option, 'textures', text='', icon='TEXTURE')
      row.prop(option, 'particleSystems', text='', icon='PARTICLES')

    # column
    column = layout.column()

    # row
    row = column.row()
    row.separator()

    # datablock list

    # row
    row = column.row(align=True)
    row.template_ID(context.scene.objects, 'active')

    # groups
    if option.groups:
      for group in data.groups[:]:
        for object in group.objects[:]:
          if object == context.active_object:

            # row
            row = column.row(align=True)

            # sub
            sub = row.row()
            sub.scale_x = 1.6
            sub.label(text='', icon='GROUP')
            row.prop(group, 'name', text='')

    # action
    if option.action:
      if hasattr(context.active_object.animation_data, 'action'):
        if hasattr(context.active_object.animation_data.action, 'name'):

          # row
          row = column.row(align=True)

          # sub
          sub = row.row()
          sub.scale_x = 1.6
          sub.label(text='', icon='ACTION')
          row.prop(data.objects[context.active_object.name].animation_data.action, 'name', text='')

    # grease pencil
    if option.greasePencil:
      if hasattr(context.active_object.grease_pencil, 'name'):

        # row
        row = column.row(align=True)

        # sub
        sub = row.row()
        sub.scale_x = 1.6
        sub.label(text='', icon='GREASEPENCIL')
        row.prop(data.objects[context.active_object.name].grease_pencil, 'name', text='')

        for layer in data.objects[context.active_object.name].grease_pencil.layers[:]:

          # row
          row = column.row(align=True)

          sub = row.row(align=True)
          sub.scale_x = 0.17
          sub.prop(layer, 'color', text='')
          row.prop(layer, 'info', text='')
          row.prop(layer, 'lock', text='')
          row.prop(layer, 'hide', text='')

    # constraints
    if option.constraints:
      for constraint in data.objects[context.active_object.name].constraints[:]:

        # row
        row = column.row(align=True)

        # sub
        sub = row.row()
        sub.scale_x = 1.6
        sub.label(text='', icon='CONSTRAINT')
        row.prop(constraint, 'name', text='')

        # influence
        if constraint.type not in {'RIGID_BODY_JOINT', 'NULL'}:

          # sub
          sub = row.row(align=True)
          sub.scale_x = 0.17
          sub.prop(constraint, 'influence', text='')
        if constraint.mute:
          iconView = 'RESTRICT_VIEW_ON'
        else:
          iconView = 'RESTRICT_VIEW_OFF'
        row.prop(constraint, 'mute', text='', icon=iconView)

    # modifiers
    if not option.modifiers:
      option.particleSystems = False
    if not option.particleSystems:
      option.viewParticleSettings = False
    if option.modifiers:
      for modifier in data.objects[context.active_object.name].modifiers[:]:

        # row
        row = column.row(align=True)

        # sub
        sub = row.row()
        sub.scale_x = 1.6
        sub.label(text='', icon=modifierIcon(modifier))
        row.prop(modifier, 'name', text='')
        if modifier.type not in {'COLLISION', 'SOFT_BODY'}:
          if modifier.show_render:
            iconRender = 'RESTRICT_RENDER_OFF'
          else:
            iconRender = 'RESTRICT_RENDER_ON'
          row.prop(modifier, 'show_render', text='', icon=iconRender)
          if modifier.show_viewport:
            iconView = 'RESTRICT_VIEW_OFF'
          else:
            iconView = 'RESTRICT_VIEW_ON'
          row.prop(modifier, 'show_viewport', text='', icon=iconView)

        # particle systems
        if option.particleSystems:
          if modifier.type in 'PARTICLE_SYSTEM':

            # row
            row = column.row(align=True)

            # sub
            sub = row.row()
            sub.scale_x = 1.6
            sub.label(text='', icon='PARTICLES')
            row.prop(modifier.particle_system, 'name', text='')

            # particle settings

            # row
            row = column.row(align=True)

            # sub
            sub = row.row()
            sub.scale_x = 1.6
            sub.label(text='', icon='DOT')
            row.prop(modifier.particle_system.settings, 'name', text='')

    # materials
    if option.materials:
      for material in data.objects[context.active_object.name].material_slots[:]:
        if material.material != None:
          if material.link == 'OBJECT':

            # row
            row = column.row(align=True)

            # sub
            sub = row.row()
            sub.scale_x = 1.6
            sub.label(text='', icon='MATERIAL')
            row.prop(material.material, 'name', text='')

            # texture
            if option.textures:
              if context.scene.render.engine not in 'CYCLES':
                for texture in material.material.texture_slots[:]:
                  if texture != None:

                    # row
                    row = column.row(align=True)

                    # sub
                    sub = row.row()
                    sub.scale_x = 1.6
                    sub.label(text='', icon='TEXTURE')
                    row.prop(texture.texture, 'name', text='')
                    if texture.use:
                      iconToggle = 'RADIOBUT_ON'
                    else:
                      iconToggle = 'RADIOBUT_OFF'
                    row.prop(texture, 'use', text='', icon=iconToggle)
    else:
      option.textures = False

    # row
    row = column.row()
    row.separator()

    # selected
    if option.selected:

      # object
      for object in data.objects[:]:
        if object != context.active_object:
          if object.select:

            # row
            row = column.row(align=True)

            # sub
            sub = row.row()
            sub.scale_x = 1.6
            sub.label(text='', icon=objectIcon(object))
            row.prop(object, 'name', text='')

            # groups
            if option.groups:
              for group in data.groups[:]:
                for groupObject in group.objects[:]:
                  if groupObject == object:

                    # row
                    row = column.row(align=True)

                    # sub
                    sub = row.row()
                    sub.scale_x = 1.6
                    sub.label(text='', icon='GROUP')
                    row.prop(group, 'name', text='')

            # actions
            if option.action:
              if hasattr(object.animation_data, 'action'):
                if hasattr(object.animation_data.action, 'name'):

                  # row
                  row = column.row(align=True)

                  # sub
                  sub = row.row()
                  sub.scale_x = 1.6
                  sub.label(text='', icon='ACTION')
                  row.prop(data.objects[object.name].animation_data.action, 'name', text='')

            # grease pencil
            if option.greasePencil:
              if hasattr(object.grease_pencil, 'name'):

                # row
                row = column.row(align=True)

                # sub
                sub = row.row()
                sub.scale_x = 1.6
                sub.label(text='', icon='GREASEPENCIL')
                row.prop(data.objects[object.name].grease_pencil, 'name', text='')

                for layer in data.objects[object.name].grease_pencil.layers[:]:

                  # row
                  row = column.row(align=True)

                  sub = row.row(align=True)
                  sub.scale_x = 0.175
                  sub.prop(layer, 'color', text='')
                  row.prop(layer, 'info', text='')
                  row.prop(layer, 'lock', text='')
                  row.prop(layer, 'hide', text='')

            # constraints
            if option.constraints:
              for constraint in object.constraints[:]:

                # row
                row = column.row(align=True)

                # sub
                sub = row.row()
                sub.scale_x = 1.6
                sub.label(text='', icon='CONSTRAINT')
                row.prop(constraint, 'name', text='')

                # influence
                if constraint.type not in {'RIGID_BODY_JOINT', 'NULL'}:

                  # sub
                  sub = row.row(align=True)
                  sub.scale_x = 0.17
                  sub.prop(constraint, 'influence', text='')
                if constraint.mute:
                  iconView = 'RESTRICT_VIEW_ON'
                else:
                  iconView = 'RESTRICT_VIEW_OFF'
                row.prop(constraint, 'mute', text='', icon=iconView)

            # modifiers
            if option.modifiers:
              for modifier in object.modifiers[:]:

                # row
                row = column.row(align=True)

                # sub
                sub = row.row()
                sub.scale_x = 1.6
                sub.label(text='', icon=modifierIcon(modifier))
                row.prop(modifier, 'name', text='')
                if modifier.type not in {'COLLISION', 'SOFT_BODY'}:
                  if modifier.show_render:
                    iconRender = 'RESTRICT_RENDER_OFF'
                  else:
                    iconRender = 'RESTRICT_RENDER_ON'
                  row.prop(modifier, 'show_render', text='', icon=iconRender)
                  if modifier.show_viewport:
                    iconView = 'RESTRICT_VIEW_OFF'
                  else:
                    iconView = 'RESTRICT_VIEW_ON'
                  row.prop(modifier, 'show_viewport', text='', icon=iconView)

                # particle systems
                if option.particleSystems:
                  if modifier.type in 'PARTICLE_SYSTEM':

                    # row
                    row = column.row(align=True)

                    # sub
                    sub = row.row()
                    sub.scale_x = 1.6
                    sub.label(text='', icon='PARTICLES')
                    row.prop(modifier.particle_system, 'name', text='')

                    # particle settings

                    # row
                    row = column.row(align=True)

                    # sub
                    sub = row.row()
                    sub.scale_x = 1.6
                    sub.label(text='', icon='DOT')
                    row.prop(modifier.particle_system.settings, 'name', text='')

            # materials
            if option.materials:
              for material in data.objects[object.name].material_slots[:]:
                if material.material != None:
                  if material.link == 'OBJECT':

                    # row
                    row = column.row(align=True)

                    # sub
                    sub = row.row()
                    sub.scale_x = 1.6
                    sub.label(text='', icon='MATERIAL')
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
                            sub.scale_x = 1.6
                            sub.label(text='', icon='TEXTURE')
                            row.prop(texture.texture, 'name', text='')
                            if texture.use:
                              iconToggle = 'RADIOBUT_ON'
                            else:
                              iconToggle = 'RADIOBUT_OFF'
                            row.prop(texture, 'use', text='', icon=iconToggle)
            else:
              option.textures = False

            # row
            row = column.row()
            row.separator()

    # empty
    if context.object.type in 'EMPTY':
      if context.object.empty_draw_type in 'IMAGE':

        # row
        row = column.row(align=True)
        row.template_ID(context.active_object, 'data', open='image.open', unlink='image.unlink')

        # row
        row = column.row()
        row.separator()

    # object data
    else:

      # row
      row = column.row(align=True)
      row.template_ID(context.active_object, 'data')

      # vertex groups
      if option.vertexGroups:
        if data.objects[context.active_object.name].type in {'LATTICE', 'MESH'}:
          for group in data.objects[context.active_object.name].vertex_groups[:]:

            # row
            row = column.row(align=True)

            # sub
            sub = row.row()
            sub.scale_x = 1.6
            sub.label(text='', icon='GROUP_VERTEX')
            row.prop(group, 'name', text='')
            if group.lock_weight:
              iconLock = 'LOCKED'
            else:
              iconLock = 'UNLOCKED'
            row.prop(group, 'lock_weight', text='', icon=iconLock)

      # shapekeys
      if option.shapekeys:
        if data.objects[context.active_object.name].type in {'MESH', 'CURVE', 'SURFACE', 'LATTICE'}:
          if data.objects[context.active_object.name].data.shape_keys:
            for key in data.objects[context.active_object.name].data.shape_keys.key_blocks[:]:

              # row
              row = column.row(align=True)

              # sub
              sub = row.row()
              sub.scale_x = 1.6
              sub.label(text='', icon='SHAPEKEY_DATA')
              row.prop(key, 'name', text='')
              if key != data.objects[context.active_object.name].data.shape_keys.key_blocks[0]:

                # sub
                sub = row.row(align=True)
                sub.scale_x = 0.17
                sub.prop(key, 'value', text='')
              row.prop(key, 'mute', text='', icon='RESTRICT_VIEW_OFF')

      # uvs
      if option.uvs:
        if data.objects[context.active_object.name].type in 'MESH':
          for uvs in data.objects[context.active_object.name].data.uv_textures[:]:

            # row
            row = column.row(align=True)

            # sub
            sub = row.row()
            sub.scale_x = 1.6
            sub.label(text='', icon='GROUP_UVS')
            row.prop(uvs, 'name', text='')
            if uvs.active_render:
              iconActive = 'RESTRICT_RENDER_OFF'
            else:
              iconActive = 'RESTRICT_RENDER_ON'
            row.prop(uvs, 'active_render', text='', icon=iconActive)

      # vertex colors
      if option.vertexColors:
        if data.objects[context.active_object.name].type in 'MESH':
          for vertexColor in data.objects[context.active_object.name].data.vertex_colors[:]:

            # row
            row = column.row(align=True)

            # sub
            sub = row.row()
            sub.scale_x = 1.6
            sub.label(text='', icon='GROUP_VCOL')
            row.prop(vertexColor, 'name', text='')
            if vertexColor.active_render:
              iconActive = 'RESTRICT_RENDER_OFF'
            else:
              iconActive = 'RESTRICT_RENDER_ON'
            row.prop(vertexColor, 'active_render', text='', icon=iconActive)

      # materials
      if option.materials:
        for material in data.objects[context.active_object.name].material_slots[:]:
          if material.material != None:
            if material.link == 'DATA':

              # row
              row = column.row(align=True)

              # sub
              sub = row.row()
              sub.scale_x = 1.6
              sub.label(text='', icon='MATERIAL')
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
                      sub.scale_x = 1.6
                      sub.label(text='', icon='TEXTURE')
                      row.prop(texture.texture, 'name', text='')
                      if texture.use:
                        iconToggle = 'RADIOBUT_ON'
                      else:
                        iconToggle = 'RADIOBUT_OFF'
                      row.prop(texture, 'use', text='', icon=iconToggle)
      else:
        option.textures = False

      # bone groups
      if option.boneGroups:
        if data.objects[context.active_object.name].type in 'ARMATURE':
          for group in data.objects[context.active_object.name].pose.bone_groups[:]:

            # row
            row = column.row(align=True)

            # sub
            sub = row.row()
            sub.scale_x = 1.6
            sub.label(text='', icon='GROUP_BONE')
            row.prop(group, 'name', text='')

      # row
      row = column.row()
      row.separator()

      # bone
      if (data.objects[context.active_object.name].type in 'ARMATURE' and
        context.object.mode in {'POSE', 'EDIT'}):

        # row
        row = column.row(align=True)

        # sub
        sub = row.row(align=True)
        sub.scale_x = 1.6
        sub.prop(option, 'selectedBones', text='', icon='BONE_DATA')
        row.prop(context.active_bone, 'name', text='')

        # bone constraints
        if option.boneConstraints:
          if context.object.mode in 'POSE':
            for constraint in context.active_pose_bone.constraints[:]:

              # row
              row = column.row(align=True)

              # sub
              sub = row.row()
              sub.scale_x = 1.6
              sub.label(text='', icon='CONSTRAINT_BONE')
              row.prop(constraint, 'name', text='')

              # sub
              sub = row.row(align=True)
              sub.scale_x = 0.17
              sub.prop(constraint, 'influence', text='')
              if constraint.mute:
                iconView = 'RESTRICT_VIEW_ON'
              else:
                iconView = 'RESTRICT_VIEW_OFF'
              row.prop(constraint, 'mute', text='', icon=iconView)

        # selected bones
        if option.selectedBones:

          #row
          row = column.row()
          row.separator()

          # sort
          if context.selected_editable_bones:
            selectedBones = context.selected_editable_bones
          elif context.selected_pose_bones:
            selectedBones = context.selected_pose_bones
          else:
            selectedBones = []
          sortedBones = []
          for bone in selectedBones:
            sortedBones.append((bone.name, bone))
          for bone in sorted(sortedBones):
            if bone[1] in (context.selected_editable_bones or context.selected_pose_bones):
              if bone[1] != (context.active_pose_bone or context.active_bone):

                # row
                row = column.row(align=True)

                # sub
                sub = row.row()
                sub.scale_x = 1.6
                sub.label(text='', icon='BONE_DATA')
                row.prop(bone[1], 'name', text='')
                if context.object.mode in 'POSE':

                  # bone constraints
                  if option.boneConstraints:
                    if context.object.mode in 'POSE':
                      for constraint in bone[1].constraints[:]:

                        # row
                        row = column.row(align=True)

                        # sub
                        sub = row.row()
                        sub.scale_x = 1.6
                        sub.label(text='', icon='CONSTRAINT_BONE')
                        row.prop(constraint, 'name', text='')

                        # sub
                        sub = row.row(align=True)
                        sub.scale_x = 0.17
                        sub.prop(constraint, 'influence', text='')
                        if constraint.mute:
                          iconView = 'RESTRICT_VIEW_ON'
                        else:
                          iconView = 'RESTRICT_VIEW_OFF'
                        row.prop(constraint, 'mute', text='', icon=iconView)

                # row
                row = column.row()
                row.separator()
        else:

          # row
          row = column.row()
          row.separator()


    # view selected
    if option.selected:
      for object in data.objects[:]:
        if object != context.active_object:
          if object.select:
            if object.type != 'EMPTY':

              # row
              row = column.row(align=True)

              # sub
              sub = row.row()
              sub.scale_x = 1.6
              sub.label(text='', icon=objectDataIcon(object))
              row.prop(object.data, 'name', text='')

              # vertex groups
              if option.vertexGroups:
                if data.objects[object.name].type in {'LATTICE', 'MESH'}:
                  for group in data.objects[object.name].vertex_groups[:]:

                    # row
                    row = column.row(align=True)

                    # sub
                    sub = row.row()
                    sub.scale_x = 1.6
                    sub.label(text='', icon='GROUP_VERTEX')
                    row.prop(group, 'name', text='')
                    if group.lock_weight:
                      iconLock = 'LOCKED'
                    else:
                      iconLock = 'UNLOCKED'
                    row.prop(group, 'lock_weight', text='', icon=iconLock)

              # shapekeys
              if option.shapekeys:
                if data.objects[object.name].type in {'MESH', 'CURVE', 'SURFACE', 'LATTICE'}:
                  if data.objects[object.name].data.shape_keys:
                    for key in data.objects[object.name].data.shape_keys.key_blocks[:]:

                      # row
                      row = column.row(align=True)

                      # sub
                      sub = row.row()
                      sub.scale_x = 1.6
                      sub.label(text='', icon='SHAPEKEY_DATA')
                      row.prop(key, 'name', text='')
                      if key != data.objects[object.name].data.shape_keys.key_blocks[0]:

                        # sub
                        sub = row.row(align=True)
                        sub.scale_x = 0.17
                        sub.prop(key, 'value', text='')
                      row.prop(key, 'mute', text='', icon='RESTRICT_VIEW_OFF')

              # uvs
              if option.uvs:
                if data.objects[object.name].type in 'MESH':
                  for uvs in data.objects[object.name].data.uv_textures[:]:

                    # row
                    row = column.row(align=True)

                    # sub
                    sub = row.row()
                    sub.scale_x = 1.6
                    sub.label(text='', icon='GROUP_UVS')
                    row.prop(uvs, 'name', text='')
                    if uvs.active_render:
                      iconActive = 'RESTRICT_RENDER_OFF'
                    else:
                      iconActive = 'RESTRICT_RENDER_ON'
                    row.prop(uvs, 'active_render', text='', icon=iconActive)

              # vertex colors
              if option.vertexColors:
                if data.objects[object.name].type in 'MESH':
                  for vertexColor in data.objects[object.name].data.vertex_colors[:]:

                    # row
                    row = column.row(align=True)

                    # sub
                    sub = row.row()
                    sub.scale_x = 1.6
                    sub.label(text='', icon='GROUP_VCOL')
                    row.prop(vertexColor, 'name', text='')
                    if vertexColor.active_render:
                      iconActive = 'RESTRICT_RENDER_OFF'
                    else:
                      iconActive = 'RESTRICT_RENDER_ON'
                    row.prop(vertexColor, 'active_render', text='', icon=iconActive)

              # materials
              if option.materials:
                for material in data.objects[object.name].material_slots[:]:
                  if material.material != None:
                    if material.link == 'DATA':

                      # row
                      row = column.row(align=True)

                      # sub
                      sub = row.row()
                      sub.scale_x = 1.6
                      sub.label(text='', icon='MATERIAL')
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
                              sub.scale_x = 1.6
                              sub.label(text='', icon='TEXTURE')
                              row.prop(texture.texture, 'name', text='')
                              if texture.use:
                                iconToggle = 'RADIOBUT_ON'
                              else:
                                iconToggle = 'RADIOBUT_OFF'
                              row.prop(texture, 'use', text='', icon=iconToggle)
              else:
                option.textures = False

              # bone groups
              if option.boneGroups:
                if data.objects[object.name].type in 'ARMATURE':
                  for group in data.objects[object.name].pose.bone_groups[:]:

                    # row
                    row = column.row(align=True)

                    # sub
                    sub = row.row()
                    sub.scale_x = 1.6
                    sub.label(text='', icon='GROUP_BONE')
                    row.prop(group, 'name', text='')

              # row
              row = column.row()
              row.separator()


# default
class default():
  '''
    Source from the original item panel class, used to return the panel to default usability upon unregiser.
  '''
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

##########
## MENU ##
##########

class menu(Menu):
  '''
    Menu for item panel operators.
  '''
  bl_idname = 'VIEW3D_MT_item_panel_specials'
  bl_label = 'Operators'
  bl_description = ''

  def draw(self, context):
    '''
      Draw the menu body.
    '''

    # layout
    layout = self.layout

    # batch auto name
    layout.operator('view3d.batch_auto_name', icon='AUTO')

    # bath name
    layout.operator('wm.batch_name', icon='SORTALPHA')

    # batch copy
    layout.operator('view3d.batch_copy', icon='COPYDOWN')
    layout.separator()

    # batch reset
    layout.operator('view3d.batch_reset', icon='FILE_REFRESH')

    # batch transfer
    layout.operator('view3d.batch_transfer', icon='RECOVER_AUTO')
    # layout.separator()

    # object names
    # layout.operator('view3d.auto_name_object_names', icon='OBJECT_DATA')

    # constraint names
    # layout.operator('view3d.auto_name_constraint_names', icon='CONSTRAINT')

    # modifier names
    # layout.operator('view3d.auto_name_modifier_names', icon='MODIFIER')
