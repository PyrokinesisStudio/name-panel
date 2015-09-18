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
import re

###############
## FUNCTIONS ##
###############

# batch
class batch():
  '''
  Contains Class;
    auto

  Contains Functions;
    main
    name
    copy
    reset
    transfer
  '''

  # auto
  class auto():
    '''
      Contains Functions;
        main
        name
    '''

    # name
    def main(context):
      '''
        Send datablock values to name.
      '''

      # option
      option = context.screen.batchAutoNameSettings

      # name
      name = batch.auto.name

      for object in bpy.data.objects[:]:

        # objects
        if option.objects:

          # batch type
          if option.batchType in 'SELECTED':
            if object.select:

              # object type
              if option.objectType in 'ALL':

                # name
                name(context, object, True, False, False, False)
              elif option.objectType in object.type:
                name(context, object, True, False, False, False)
          else:

            # object type
            if option.objectType in 'ALL':

              # name
              name(context, object, True, False, False, False)
            elif option.objectType in object.type:
              name(context, object, True, False, False, False)

        # constraints
        if option.constraints:

          # batch type
          if option.batchType in 'SELECTED':
            if object.select:
              for constraint in object.constraints[:]:

                # constraint type
                if option.constraintType in 'ALL':

                  # name
                  name(context, constraint, False, True, False, False)
                elif option.constraintType in constraint.type:
                  name(context, constraint, False, True, False, False)
          else:
            for constraint in object.constraints[:]:

              # constraint type
              if option.constraintType in 'ALL':

                # name
                name(context, constraint, False, True, False, False)
              elif option.constraintType in constraint.type:
                name(context, constraint, False, True, False, False)

        # modifiers
        if option.modifiers:

          # batch type
          if option.batchType in 'SELECTED':
            if object.select:
              for modifier in object.modifiers[:]:

                # modifier type
                if option.modifierType in 'ALL':

                  # name
                  name(context, modifier, False, False, True, False)
                elif option.modifierType in modifier.type:
                  name(context, modifier, False, False, True, False)
          else:
            for modifier in object.modifiers[:]:

              # modifier type
              if option.modifierType in 'ALL':

                # name
                name(context, modifier, False, False, True, False)
              elif option.modifierType in modifier.type:
                name(context, modifier, False, False, True, False)

        # object data
        if option.objectData:
          if object.type not in 'EMPTY':

            # batch type
            if option.batchType in 'SELECTED':
              if object.select:

                # object type
                if option.objectType in 'ALL':

                  # name
                  name(context, object, False, False, False, True)
                elif option.objectType in object.type:
                  name(context, object, False, False, False, True)
            else:

              # object type
              if option.objectType in 'ALL':

                # name
                name(context, object, False, False, False, True)
              elif option.objectType in object.type:
                name(context, object, False, False, False, True)

        # bone constraints
        if option.boneConstraints:

          # batch type
          if option.batchType in 'SELECTED':
            if object.select:
              if object.type in 'ARMATURE':
                for bone in object.pose.bones[:]:
                  if bone.bone.select:
                    for constraint in bone.constraints[:]:

                      # constraint type
                      if option.constraintType in 'ALL':

                        # name
                        name(context, constraint, False, True, False, False)
                      elif option.constraintType in constraint.type:
                        name(context, constraint, False, True, False, False)
          else:
            if object.type in 'ARMATURE':
              for bone in object.pose.bones[:]:
                for constraint in bone.constraints[:]:

                  # constraint type
                  if option.constraintType in 'ALL':

                    # name
                    name(context, constraint, False, True, False, False)
                  elif option.constraintType in constraint.type:
                    name(context, constraint, False, True, False, False)

    # object
    def name(context, datablock, object, constraint, modifier, objectData):
      '''
        Change the datablock names of objects, constraints, modifiers, object data and bone constraints according to their type.
      '''

      # option
      option = context.screen.batchAutoNameSettings

      # object name
      objectName = context.scene.batchAutoNameObjectNames

      # constraint name
      constraintName = context.scene.batchAutoNameConstraintNames

      # modifier name
      modifierName = context.scene.batchAutoNameModifierNames

      # object data name
      objectDataName = context.scene.batchAutoNameObjectDataNames

      # object
      if object:

        # mesh
        if datablock.type in 'MESH':
          datablock.name = objectName.mesh

        # curve
        if datablock.type in 'CURVE':
          datablock.name = objectName.curve

        # surface
        if datablock.type in 'SURFACE':
          datablock.name = objectName.surface

        # meta
        if datablock.type in 'META':
          datablock.name = objectName.meta

        # font
        if datablock.type in 'FONT':
          datablock.name = objectName.font

        # armature
        if datablock.type in 'ARMATURE':
          datablock.name = objectName.armature

        # lattice
        if datablock.type in 'LATTICE':
          datablock.name = objectName.lattice

        # empty
        if datablock.type in 'EMPTY':
          datablock.name = objectName.empty

        # speaker
        if datablock.type in 'SPEAKER':
          datablock.name = objectName.speaker

        # camera
        if datablock.type in 'CAMERA':
          datablock.name = objectName.camera

        # lamp
        if datablock.type in 'LAMP':
          datablock.name = objectName.lamp

      # constraint (bone constraint)
      if constraint:

        # camera solver
        if datablock.type in 'CAMERA_SOLVER':
          datablock.name = constraintName.cameraSolver

        # follow track
        if datablock.type in 'FOLLOW_TRACK':
          datablock.name = constraintName.followTrack

        # object solver
        if datablock.type in 'OBJECT_SOLVER':
          datablock.name = constraintName.objectSolver

        # copy location
        if datablock.type in 'COPY_LOCATION':
          datablock.name = constraintName.copyLocation

        # copy rotation
        if datablock.type in 'COPY_ROTATION':
          datablock.name = constraintName.copyRotation

        # copy scale
        if datablock.type in 'COPY_SCALE':
          datablock.name = constraintName.copyScale

        # copy transforms
        if datablock.type in 'COPY_TRANSFORMS':
          datablock.name = constraintName.copyTransforms

        # limit distance
        if datablock.type in 'LIMIT_DISTANCE':
          datablock.name = constraintName.limitDistance

        # limit location
        if datablock.type in 'LIMIT_LOCATION':
          datablock.name = constraintName.limitLocation

        # limit rotation
        if datablock.type in 'LIMIT_ROTATION':
          datablock.name = constraintName.limitRotation

        # limit scale
        if datablock.type in 'LIMIT_SCALE':
          datablock.name = constraintName.limitScale

        # maintain volume
        if datablock.type in 'MAINTAIN_VOLUME':
          datablock.name = constraintName.maintainVolume

        # transform
        if datablock.type in 'TRANSFORM':
          datablock.name = constraintName.transform

        # clamp to
        if datablock.type in 'CLAMP_TO':
          datablock.name = constraintName.clampTo

        # damped track
        if datablock.type in 'DAMPED_TRACK':
          datablock.name = constraintName.dampedTrack

        # inverse kinematics
        if datablock.type in 'IK':
          datablock.name = constraintName.inverseKinematics

        # locked track
        if datablock.type in 'LOCKED_TRACK':
          datablock.name = constraintName.lockedTrack

        # spline inverse kinematics
        if datablock.type in 'SPLINE_IK':
          datablock.name = constraintName.splineInverseKinematics

        # stretch to
        if datablock.type in 'STRETCH_TO':
          datablock.name = constraintName.stretchTo

        # track to
        if datablock.type in 'TRACK_TO':
          datablock.name = constraintName.trackTo

        # action
        if datablock.type in 'ACTION':
          datablock.name = constraintName.action

        # child of
        if datablock.type in 'CHILD_OF':
          datablock.name = constraintName.childOf

        # floor
        if datablock.type in 'FLOOR':
          datablock.name = constraintName.floor

        # follor path
        if datablock.type in 'FOLLOW_PATH':
          datablock.name = constraintName.followPath

        # pivot
        if datablock.type in 'PIVOT':
          datablock.name = constraintName.pivot

        # rigid body joint
        if datablock.type in 'RIGID_BODY_JOINT':
          datablock.name = constraintName.rigidBodyJoint

        # shrinkwrap
        if datablock.type in 'SHRINKWRAP':
          datablock.name = constraintName.shrinkwrap

      # modifier
      if modifier:

        # data transfer
        if datablock.type in 'DATA_TRANSFER':
          datablock.name = modifierName.dataTransfer

        # mesh cache
        if datablock.type in 'MESH_CACHE':
          datablock.name = modifierName.meshCache

        # normal edit
        if datablock.type in 'NORMAL_EDIT':
          datablock.name = modifierName.normalEdit

        # uv project
        if datablock.type in 'UV_PROJECT':
          datablock.name = modifierName.uvProject

        # uv warp
        if datablock.type in 'UV_WARP':
          datablock.name = modifierName.uvWarp

        # vertex weight edit
        if datablock.type in 'VERTEX_WEIGHT_EDIT':
          datablock.name = modifierName.vertexWeightEdit

        # vertex weight mix
        if datablock.type in 'VERTEX_WEIGHT_MIX':
          datablock.name = modifierName.vertexWeightMix

        # vertex weight proximity
        if datablock.type in 'VERTEX_WEIGHT_PROXIMITY':
          datablock.name = modifierName.vertexWeightProximity

        # array
        if datablock.type in 'ARRAY':
          datablock.name = modifierName.array

        # bevel
        if datablock.type in 'BEVEL':
          datablock.name = modifierName.bevel

        # boolean
        if datablock.type in 'BOOLEAN':
          datablock.name = modifierName.boolean

        # build
        if datablock.type in 'BUILD':
          datablock.name = modifierName.build

        # decimate
        if datablock.type in 'DECIMATE':
          datablock.name = modifierName.decimate

        # edge split
        if datablock.type in 'EDGE_SPLIT':
          datablock.name = modifierName.edgeSplit

        # mask
        if datablock.type in 'MASK':
          datablock.name = modifierName.mask

        # mirror
        if datablock.type in 'MIRROR':
          datablock.name = modifierName.mirror

        # multiresolution
        if datablock.type in 'MULTIRES':
          datablock.name = modifierName.multiresolution

        # remesh
        if datablock.type in 'REMESH':
          datablock.name = modifierName.remesh

        # screw
        if datablock.type in 'SCREW':
          datablock.name = modifierName.screw

        # skin
        if datablock.type in 'SKIN':
          datablock.name = modifierName.skin

        # solidify
        if datablock.type in 'SOLIDIFY':
          datablock.name = modifierName.solidify

        # subdivision surface
        if datablock.type in 'SUBSURF':
          datablock.name = modifierName.subdivisionSurface

        # triangulate
        if datablock.type in 'TRIANGULATE':
          datablock.name = modifierName.triangulate

        # wireframe
        if datablock.type in 'WIREFRAME':
          datablock.name = modifierName.wireframe

        # armature
        if datablock.type in 'ARMATURE':
          datablock.name = modifierName.armature

        # cast
        if datablock.type in 'CAST':
          datablock.name = modifierName.cast

        # corrective smooth
        if datablock.type in 'CORRECTIVE_SMOOTH':
          datablock.name = modifierName.correctiveSmooth

        # curve
        if datablock.type in 'CURVE':
          datablock.name = modifierName.curve

        # displace
        if datablock.type in 'DISPLACE':
          datablock.name = modifierName.displace

        # hook
        if datablock.type in 'HOOK':
          datablock.name = modifierName.hook

        # laplacian smooth
        if datablock.type in 'LAPLACIANSMOOTH':
          datablock.name = modifierName.laplacianSmooth

        # laplacian deform
        if datablock.type in 'LAPLACIANDEFORM':
          datablock.name = modifierName.laplacianDeform

        # lattice
        if datablock.type in 'LATTICE':
          datablock.name = modifierName.lattice

        # mesh deform
        if datablock.type in 'MESH_DEFORM':
          datablock.name = modifierName.meshDeform

        # shrinkwrap
        if datablock.type in 'SHRINKWRAP':
          datablock.name = modifierName.shrinkwrap

        # simple deform
        if datablock.type in 'SIMPLE_DEFORM':
          datablock.name = modifierName.simpleDeform

        # smooth
        if datablock.type in 'SMOOTH':
          datablock.name = modifierName.smooth

        # warp
        if datablock.type in 'WARP':
          datablock.name = modifierName.warp

        # wave
        if datablock.type in 'WAVE':
          datablock.name = modifierName.wave

        # cloth
        if datablock.type in 'CLOTH':
          datablock.name = modifierName.cloth

        # collision
        if datablock.type in 'COLLISION':
          datablock.name = modifierName.collision

        # dynamic paint
        if datablock.type in 'DYNAMIC_PAINT':
          datablock.name = modifierName.dynamicPaint

        # explode
        if datablock.type in 'EXPLODE':
          datablock.name = modifierName.explode

        # fluid simulation
        if datablock.type in 'FLUID_SIMULATION':
          datablock.name = modifierName.fluidSimulation

        # ocean
        if datablock.type in 'OCEAN':
          datablock.name = modifierName.ocean

        # particle instance
        if datablock.type in 'PARTICLE_INSTANCE':
          datablock.name = modifierName.particleInstance

        # particle system
        if datablock.type in 'PARTICLE_SYSTEM':
          datablock.name = modifierName.particleSystem

        # smoke
        if datablock.type in 'SMOKE':
          datablock.name = modifierName.smoke

        # soft body
        if datablock.type in 'SOFT_BODY':
          datablock.name = modifierName.softBody

      if objectData:

        # mesh
        if datablock.type in 'MESH':
          datablock.data.name = objectDataName.mesh

        # curve
        if datablock.type in 'CURVE':
          datablock.data.name = objectDataName.curve

        # surface
        if datablock.type in 'SURFACE':
          datablock.data.name = objectDataName.surface

        # meta
        if datablock.type in 'META':
          datablock.data.name = objectDataName.meta

        # font
        if datablock.type in 'FONT':
          datablock.data.name = objectDataName.font

        # armature
        if datablock.type in 'ARMATURE':
          datablock.data.name = objectDataName.armature

        # lattice
        if datablock.type in 'LATTICE':
          datablock.data.name = objectDataName.lattice

        # empty
        if datablock.type in 'EMPTY':
          datablock.data.name = objectDataName.empty

        # speaker
        if datablock.type in 'SPEAKER':
          datablock.data.name = objectDataName.speaker

        # camera
        if datablock.type in 'CAMERA':
          datablock.data.name = objectDataName.camera

        # lamp
        if datablock.type in 'LAMP':
          datablock.data.name = objectDataName.lamp

  # name
  def main(context):
    '''
      Send datablock values to name.
    '''

    # option
    option = context.screen.batchNameSettings

    # name
    name = batch.name

    for object in bpy.data.objects[:]:

      # objects
      if option.objects:

        # batch type
        if option.batchType in 'SELECTED':
          if object.select:

            # object type
            if option.objectType in 'ALL':

              # name
              name(context, object)
            elif option.objectType in object.type:
              name(context, object)
        else:

          # object type
          if option.objectType in 'ALL':

            # name
            name(context, object)
          elif option.objectType in object.type:
            name(context, object)

      # constraints
      if option.constraints:

        # batch type
        if option.batchType in 'SELECTED':
          if object.select:
            for constraint in object.constraints[:]:

              # constraint type
              if option.constraintType in 'ALL':

                # name
                name(context, constraint)
              elif option.constraintType in constraint.type:
                name(context, constraint)
        else:
          for constraint in object.constraints[:]:

            # constraint type
            if option.constraintType in 'ALL':

              # name
              name(context, constraint)
            elif option.constraintType in constraint.type:
              name(context, constraint)

      # modifiers
      if option.modifiers:

        # batch type
        if option.batchType in 'SELECTED':
          if object.select:
            for modifier in object.modifiers[:]:

              # modifier type
              if option.modifierType in 'ALL':

                # name
                name(context, modifier)
              elif option.modifierType in modifier.type:
                name(context, modifier)
        else:
          for modifier in object.modifiers[:]:

            # modifier type
            if option.modifierType in 'ALL':

              # name
              name(context, modifier)
            elif option.modifierType in modifier.type:
              name(context, modifier)

      # object data
      if option.objectData:
        if object.type not in 'EMPTY':

          # batch type
          if option.batchType in 'SELECTED':
            if object.select:

              # object type
              if option.objectType in 'ALL':

                # name
                name(context, object.data)
              elif option.objectType in object.type:
                name(context, object.data)
          else:

            # object type
            if option.objectType in 'ALL':

              # name
              name(context, object.data)
            elif option.objectType in object.type:
              name(context, object.data)

      # bones
      if option.bones:

        # batch type
        if option.batchType in 'SELECTED':
          if object.select:
            if object.type in 'ARMATURE':
              for bone in object.data.bones[:]:
                if bone.select:

                  # name
                  name(context, bone)
        else:
          if object.type in 'ARMATURE':
            for bone in object.data.bones[:]:

              # name
              name(context, bone)

      # bone constraints
      if option.boneConstraints:

        # batch type
        if option.batchType in 'SELECTED':
          if object.select:
            if object.type in 'ARMATURE':
              for bone in object.pose.bones[:]:
                if bone.bone.select:
                  for constraint in bone.constraints[:]:

                    # constraint type
                    if option.constraintType in 'ALL':

                      # name
                      name(context, constraint)
                    elif option.constraintType in constraint.type:
                      name(context, constraint)
        else:
          if object.type in 'ARMATURE':
            for bone in object.pose.bones[:]:
              for constraint in bone.constraints[:]:

                # constraint type
                if option.constraintType in 'ALL':

                  # name
                  name(context, constraint)
                elif option.constraintType in constraint.type:
                  name(context, constraint)

      # materials
      if option.materials:

          # batch type
          if option.batchType in 'SELECTED':
            if object.select:
              for material in object.material_slots[:]:
                if material.material != None:

                  # object type
                  if option.objectType in 'ALL':

                    # name
                    name(context, material.material)
                  elif option.objectType in object.type:
                    name(context, material.material)
          else:
            for material in object.material_slots[:]:
              if material.material != None:

                # object type
                if option.objectType in 'ALL':

                  # name
                  name(context, material.material)
                elif option.objectType in object.type:
                  name(context, material.material)

      # textures
      if option.textures:
        if context.scene.render.engine not in 'CYCLES':

          # batch type
          if option.batchType in 'SELECTED':
            if object.select:
              for material in object.material_slots[:]:
                if material.material != None:
                  for texture in material.material.texture_slots[:]:
                    if texture != None:

                      # object type
                      if option.objectType in 'ALL':

                        # name
                        name(context, texture.texture)
                      elif option.objectType in object.type:
                        name(context, texture.texture)
          else:
            for material in object.material_slots[:]:
              if material.material != None:
                for texture in material.material.texture_slots[:]:
                  if texture != None:

                    # object type
                    if option.objectType in 'ALL':

                      # name
                      name(context, texture.texture)
                    elif option.objectType in object.type:
                      name(context, texture.texture)

      # particle systems
      if option.particleSystems:
        if object.type in 'MESH':

          # batch type
          if option.batchType in 'SELECTED':
            if object.select:
              for system in object.particle_systems[:]:

                # object type
                if option.objectType in 'ALL':

                  # name
                  name(context, system)
                elif option.objectType in object.type:
                  name(context, system)
          else:
            for system in object.particle_systems[:]:

              # object type
              if option.objectType in 'ALL':

                # name
                name(context, system)
              elif option.objectType in object.type:
                name(context, system)

      # particle settings
      if option.particleSettings:
        if object.type in 'MESH':

          # batch type
          if option.batchType in 'SELECTED':
            if object.select:
              for system in object.particle_systems[:]:

                # object type
                if option.objectType in 'ALL':

                  # name
                  name(context, system.settings)
                elif option.objectType in object.type:
                  name(context, system.settings)
          else:
            for system in object.particle_systems[:]:

              # object type
              if option.objectType in 'ALL':

                # name
                name(context, system.settings)
              elif option.objectType in object.type:
                name(context, system.settings)

      # groups
      if option.groups:

        # batch type
        if option.batchType in 'SELECTED':
          if object.select:

            # object type
            if option.objectType in 'ALL':
              for group in bpy.data.groups[:]:
                if object in group.objects[:]:

                  # name
                  name(context, group)
            elif option.objectType in object.type:
              for group in bpy.data.groups[:]:
                if object in group.objects[:]:
                  name(context, group)
        else:

            # object type
            if option.objectType in 'ALL':
              for group in bpy.data.groups[:]:
                if object in group.objects[:]:

                  # name
                  name(context, group)
            elif option.objectType in object.type:
              for group in bpy.data.groups[:]:
                if object in group.objects[:]:
                  name(context, group)

      # vertex groups
      if option.vertexGroups:
        if object.type in {'MESH', 'LATTICE'}:

          # batch type
          if option.batchType in 'SELECTED':
            if object.select:
              for group in object.vertex_groups[:]:

                # object type
                if option.objectType in 'ALL':

                  # name
                  name(context, group)
                elif option.objectType in object.type:
                  name(context, group)
          else:
            for group in object.vertex_groups[:]:

              # object type
              if option.objectType in 'ALL':

                # name
                name(context, group)
              elif option.objectType in object.type:
                name(context, group)

      # shapekeys
      if option.shapekeys:
        if object.type in {'MESH', 'CURVE', 'SURFACE', 'LATTICE'}:
          if object.data.shape_keys:

            # batch type
            if option.batchType in 'SELECTED':
              if object.select:
                for key in object.data.shape_keys.key_blocks[:]:

                  # object type
                  if option.objectType in 'ALL':

                    # name
                    name(context, key)
                  elif option.objectType in object.type:
                    name(context, key)
            else:
              for key in object.data.shape_keys.key_blocks[:]:

                # object type
                if option.objectType in 'ALL':

                  # name
                  name(context, key)
                elif option.objectType in object.type:
                  name(context, key)


      # uvs
      if option.uvs:
        if object.type in 'MESH':

          # batch type
          if option.batchType in 'SELECTED':
            if object.select:
              for uv in object.data.uv_textures[:]:

                # object type
                if option.objectType in 'ALL':

                  # name
                  name(context, uv)
                elif option.objectType in object.type:
                  name(context, uv)
          else:
           for uv in object.data.uv_textures[:]:

              # object type
              if option.objectType in 'ALL':

                # name
                name(context, uv)
              elif option.objectType in object.type:
                name(context, uv)

      # vertex colors
      if option.vertexColors:
        if object.type in 'MESH':

          # batch type
          if option.batchType in 'SELECTED':
            if object.select:
              for vertexColor in object.data.vertex_colors[:]:

                # object type
                if option.objectType in 'ALL':

                  # name
                  name(context, vertexColor)
                elif option.objectType in object.type:
                  name(context, vertexColor)
          else:
            for vertexColor in object.data.vertex_colors[:]:

              # object type
              if option.objectType in 'ALL':

                # name
                name(context, vertexColor)
              elif option.objectType in object.type:
                name(context, vertexColor)

      # bone groups
      if option.boneGroups:

        # batch type
        if option.batchType in 'SELECTED':
          if object.select:
            if object.type in 'ARMATURE':
              for group in object.pose.bone_groups[:]:
                if object.select:

                  # name
                  name(context, group)
        else:
          if object.type in 'ARMATURE':
            for group in object.pose.bone_groups[:]:

              # name
              name(context, group)

    # purge re cache
    re.purge()

  # name
  def name(context, datablock):
    '''
      Names datablock received from main.
    '''

    # option
    option = context.screen.batchNameSettings

    # customName
    if option.customName:
      newName = option.customName

      # trim start
      newName = newName[option.trimStart:]
    else:
      newName = datablock.name[option.trimStart:]

    # trim end
    if option.trimEnd > 0:
      newName = newName[:-option.trimEnd]

    # find & replace
    if option.regex:
      newName = re.sub(option.find, option.replace, newName)
    else:
      newName = re.sub(re.escape(option.find), option.replace, newName)

    # prefix & suffix
    newName = option.prefix + newName + option.suffix

    # assign new name
    datablock.name = newName

  # copy
  def copy(context):
    '''
      Assign name values from source type to destination datablock.
    '''

    # option
    option = context.screen.batchCopySettings

    for object in bpy.data.objects[:]:

      # source object
      if option.source in 'OBJECT':

        # objects
        if option.objects:

          # batch type
          if option.batchType in 'SELECTED':
            if object.select:

              # use active object
              if option.useActiveObject:
                object.name = context.active_object.name
              else:
                object.name = object.name
          else:

            # use active object
            if option.useActiveObject:
              object.name = context.active_object.name
            else:
              object.name = object.name

        # object data
        if option.objectData:
          if object.type not in 'EMPTY': ###

            # batch type
            if option.batchType in 'SELECTED':
              if object.select:

                # use active object
                if option.useActiveObject:
                  object.data.name = context.active_object.name
                else:
                  object.data.name = object.name
            else:

              # use active object
              if option.useActiveObject:
                object.data.name = context.active_object.name
              else:
                object.data.name = object.name

        # materials
        if option.materials:

          # batch type
          if option.batchType in 'SELECTED':
            if object.select:
              for material in object.material_slots[:]:
                if material.material != None:

                  # use active object
                  if option.useActiveObject:
                    material.material.name = context.active_object.name
                  else:
                    material.material.name = object.name
          else:
            for material in object.material_slots[:]:
              if material.material != None:

                # use active object
                if option.useActiveObject:
                  material.material.name = context.active_object.name
                else:
                  material.material.name = object.name

        # textures
        if option.textures:

          # batch type
          if option.batchType in 'SELECTED':
            if object.select:
              for material in object.material_slots[:]:
                if material.material != None:
                  for texture in material.material.texture_slots[:]:
                    if texture != None:

                      # use active object
                      if option.useActiveObject:
                        texture.texture.name = context.active_object.name
                      else:
                        texture.texture.name = object.name
          else:
            for material in object.material_slots[:]:
              if material.material != None:
                for texture in material.material.texture_slots[:]:
                  if texture != None:

                    # use active object
                    if option.useActiveObject:
                      texture.texture.name = context.active_object.name
                    else:
                      texture.texture.name = object.name

        # particle systems
        if option.particleSystems:

          # batch type
          if option.batchType in 'SELECTED':
            if object.select:
              for system in object.particle_systems[:]:

                # use active object
                if option.useActiveObject:
                  system.name = context.active_object.name
                else:
                  system.name = object.name
          else:
            for system in object.particle_systems[:]:

              # use active object
              if option.useActiveObject:
                system.name = context.active_object.name
              else:
                system.name = object.name

        # particle settings
        if option.particleSettings:

          # batch type
          if option.batchType in 'SELECTED':
            if object.select:
              for system in object.particle_systems[:]:

                # use active object
                if option.useActiveObject:
                  system.settings.name = context.active_object.name
                else:
                  system.settings.name = object.name
          else:
            for system in object.particle_systems[:]:

              # use active object
              if option.useActiveObject:
                system.settings.name = context.active_object.name
              else:
                system.settings.name = object.name

      # source data
      if option.source in 'DATA':
        if object.type not in 'EMPTY':

          # objects
          if option.objects:

            # batch type
            if option.batchType in 'SELECTED':
              if object.select:

                # use active object
                if option.useActiveObject:
                  object.name = context.active_object.data.name
                else:
                  object.name = object.data.name
            else:

              # use active object
              if option.useActiveObject:
                object.name = context.active_object.data.name
              else:
                object.name = object.data.name

          # object data
          if option.objectData:

            # batch type
            if option.batchType in 'SELECTED':
              if object.select:

                # use active object
                if option.useActiveObject:
                  object.data.name = context.active_object.data.name
                else:
                  object.data.name = object.data.name
            else:

              # use active object
              if option.useActiveObject:
                object.data.name = context.active_object.data.name
              else:
                object.data.name = object.data.name

          # materials
          if option.materials:

            # batch type
            if option.batchType in 'SELECTED':
              if object.select:
                for material in object.material_slots[:]:
                  if material.material != None:

                    # use active object
                    if option.useActiveObject:
                      material.material.name = context.active_object.data.name
                    else:
                      material.material.name = object.data.name
            else:
              for material in object.material_slots[:]:
                if material.material != None:

                  # use active object
                  if option.useActiveObject:
                    material.material.name = context.active_object.data.name
                  else:
                    material.material.name = object.data.name

          # textures
          if option.textures:

            # batch type
            if option.batchType in 'SELECTED':
              if object.select:
                for material in object.material_slots[:]:
                  if material.material != None:
                    for texture in material.material.texture_slots[:]:
                      if texture != None:

                        # use active object
                        if option.useActiveObject:
                          texture.texture.name = context.active_object.data.name
                        else:
                          texture.texture.name = object.data.name
            else:
              for material in object.material_slots[:]:
                if material.material != None:
                  for texture in material.material.texture_slots[:]:
                    if texture != None:

                      # use active object
                      if option.useActiveObject:
                        texture.texture.name = context.active_object.data.name
                      else:
                        texture.texture.name = object.data.name

          # particle systems
          if option.particleSystems:

            # batch type
            if option.batchType in 'SELECTED':
              if object.select:
                for system in object.particle_systems[:]:

                  # use active object
                  if option.useActiveObject:
                    system.name = context.active_object.data.name
                  else:
                    system.name = object.data.name
            else:
              for system in object.particle_systems[:]:

                # use active object
                if option.useActiveObject:
                  system.name = context.active_object.data.name
                else:
                  system.name = object.data.name

          # particle settings
          if option.particleSettings:

            # batch type
            if option.batchType in 'SELECTED':
              if object.select:
                for system in object.particle_systems[:]:

                  # use active object
                  if option.useActiveObject:
                    system.settings.name = context.active_object.data.name
                  else:
                    system.settings.name = object.data.name
            else:
              for system in object.particle_systems[:]:

                # use active object
                if option.useActiveObject:
                  system.settings.name = context.active_object.data.name
                else:
                  system.settings.name = object.data.name

      # source material
      if option.source in 'MATERIAL':

        # objects
        if option.objects:

          # batch type
          if option.batchType in 'SELECTED':
            if object.select:

              # use active object
              if option.useActiveObject:
                if hasattr(context.active_object.active_material, 'name'):
                  object.name = context.active_object.active_material.name
              else:
                if hasattr(object.active_material, 'name'):
                  object.name = object.active_material.name
          else:

            # use active object
            if option.useActiveObject:
              if hasattr(context.active_object.active_material, 'name'):
                object.name = context.active_object.active_material.name
            else:
              if hasattr(object.active_material, 'name'):
                object.name = object.active_material.name

        # object data
        if option.objectData:
          if object.type not in 'EMPTY':

            # batch type
            if option.batchType in 'SELECTED':
              if object.select:

                # use active object
                if option.useActiveObject:
                  if hasattr(context.active_object.active_material, 'name'):
                    object.data.name = context.active_object.active_material.name
                else:
                  if hasattr(object.active_material, 'name'):
                    object.data.name = object.active_material.name
            else:

              # use active object
              if option.useActiveObject:
                if hasattr(context.active_object.active_material, 'name'):
                  object.data.name = context.active_object.active_material.name
              else:
                if hasattr(object.active_material, 'name'):
                  object.data.name = object.active_material.name

        # materials
        if option.materials:

          # batch type
          if option.batchType in 'SELECTED':
            if object.select:
              for material in object.material_slots[:]:
                if material.material != None:

                  # use active object
                  if option.useActiveObject:
                    if hasattr(context.active_object.active_material, 'name'):
                      material.material.name = context.active_object.active_material.name
                  else:
                    if hasattr(object.active_material, 'name'):
                      material.material.name = object.active_material.name
          else:
            for material in object.material_slots[:]:
              if material.material != None:

                # use active object
                if option.useActiveObject:
                  if hasattr(context.active_object.active_material, 'name'):
                    material.material.name = context.active_object.active_material.name
                else:
                  if hasattr(object.active_material, 'name'):
                    material.material.name = object.active_material.name

        # textures
        if option.textures:

          # batch type
          if option.batchType in 'SELECTED':
            if object.select:
              for material in object.material_slots[:]:
                if material.material != None:
                  for texture in material.material.texture_slots[:]:
                    if texture != None:

                      # use active object
                      if option.useActiveObject:
                        if hasattr(context.active_object.active_material, 'name'):
                          texture.texture.name = context.active_object.active_material.name
                      else:
                        if hasattr(object.active_material, 'name'):
                          texture.texture.name = object.active_material.name
          else:
            for material in object.material_slots[:]:
              if material.material != None:
                for texture in material.material.texture_slots[:]:
                  if texture != None:

                    # use active object
                    if option.useActiveObject:
                      if hasattr(context.active_object.active_material, 'name'):
                        texture.texture.name = context.active_object.active_material.name
                    else:
                      if hasattr(object.active_material, 'name'):
                        texture.texture.name = object.active_material.name

        # particle systems
        if option.particleSystems:

          # batch type
          if option.batchType in 'SELECTED':
            if object.select:
              for system in object.particle_systems[:]:

                # use active object
                if option.useActiveObject:
                  if hasattr(context.active_object.active_material, 'name'):
                    system.name = context.active_object.active_material.name
                else:
                  if hasattr(object.active_material, 'name'):
                    system.name = object.active_material.name
          else:
            for system in object.particle_systems[:]:

              # use active object
              if option.useActiveObject:
                if hasattr(context.active_object.active_material, 'name'):
                  system.name = context.active_object.active_material.name
              else:
                if hasattr(object.active_material, 'name'):
                  system.name = object.active_material.name

        # particle settings
        if option.particleSettings:

          # batch type
          if option.batchType in 'SELECTED':
            if object.select:
              for system in object.particle_systems[:]:

                # use active object
                if option.useActiveObject:
                  if hasattr(context.active_object.active_material, 'name'):
                    system.settings.name = context.active_object.active_material.name
                else:
                  if hasattr(object.active_material, 'name'):
                    system.settings.name = object.active_material.name
          else:
            for system in object.particle_systems[:]:

              # use active object
              if option.useActiveObject:
                if hasattr(context.active_object.active_material, 'name'):
                  system.settings.name = context.active_object.active_material.name
              else:
                if hasattr(object.active_material, 'name'):
                  system.settings.name = object.active_material.name

      # source texture
      if option.source in 'TEXTURE':
        if context.scene.render.engine not in 'CYCLES':

          # objects
          if option.objects:

            # batch type
            if option.batchType in 'SELECTED':
              if object.select:

                # use active object
                if option.useActiveObject:
                  if hasattr(context.active_object.active_material, 'active_texture'):
                    if hasattr(context.active_object.active_material.active_texture, 'name'):
                      object.name = context.active_object.active_material.active_texture.name
                else:
                  if hasattr(object.active_material, 'active_texture'):
                    if hasattr(object.active_material.active_texture, 'name'):
                      object.name = object.active_material.active_texture.name
            else:

              # use active object
              if option.useActiveObject:
                if hasattr(context.active_object.active_material, 'active_texture'):
                  if hasattr(context.active_object.active_material.active_texture, 'name'):
                    object.name = context.active_object.active_material.active_texture.name
              else:
                if hasattr(object.active_material, 'active_texture'):
                  if hasattr(object.active_material.active_texture, 'name'):
                    object.name = object.active_material.active_texture.name

          # object data
          if option.objectData:
            if object.type not in 'EMPTY':

              # batch type
              if option.batchType in 'SELECTED':
                if object.select:

                  # use active object
                  if option.useActiveObject:
                    if hasattr(context.active_object.active_material, 'active_texture'):
                      if hasattr(context.active_object.active_material.active_texture, 'name'):
                        object.data.name = context.active_object.active_material.active_texture.name
                  else:
                    if hasattr(object.active_material, 'active_texture'):
                      if hasattr(object.active_material.active_texture, 'name'):
                        object.data.name = object.active_material.active_texture.name
              else:

                # use active object
                if option.useActiveObject:
                  if hasattr(context.active_object.active_material, 'active_texture'):
                    if hasattr(context.active_object.active_material.active_texture, 'name'):
                      object.data.name = context.active_object.active_material.active_texture.name
                else:
                  if hasattr(object.active_material, 'active_texture'):
                    if hasattr(object.active_material.active_texture, 'name'):
                      object.data.name = object.active_material.active_texture.name

          # materials
          if option.materials:

            # batch type
            if option.batchType in 'SELECTED':
              if object.select:
                for material in object.material_slots[:]:
                  if material.material != None:

                    # use active object
                    if option.useActiveObject:
                      if hasattr(context.active_object.active_material, 'active_texture'):
                        if hasattr(context.active_object.active_material.active_texture, 'name'):
                          material.material.name = context.active_object.active_material.active_texture.name
                    else:
                      if hasattr(object.active_material, 'active_texture'):
                        if hasattr(object.active_material.active_texture, 'name'):
                          material.material.name = object.active_material.active_texture.name
            else:
              for material in object.material_slots[:]:
                if material.material != None:

                  # use active object
                  if option.useActiveObject:
                    if hasattr(context.active_object.active_material, 'active_texture'):
                      if hasattr(context.active_object.active_material.active_texture, 'name'):
                        material.material.name = context.active_object.active_material.active_texture.name
                  else:
                    if hasattr(object.active_material, 'active_texture'):
                      if hasattr(object.active_material.active_texture, 'name'):
                        material.material.name = object.active_material.active_texture.name

          # textures
          if option.textures:

            # batch type
            if option.batchType in 'SELECTED':
              if object.select:
                for material in object.material_slots[:]:
                  if material.material != None:
                    for texture in material.material.texture_slots[:]:
                      if texture != None:

                        # use active object
                        if option.useActiveObject:
                          if hasattr(context.active_object.active_material, 'active_texture'):
                            if hasattr(context.active_object.active_material.active_texture, 'name'):
                              texture.texture.name = context.active_object.active_material.active_texture.name
                        else:
                          if hasattr(object.active_material, 'active_texture'):
                            if hasattr(object.active_material.active_texture, 'name'):
                              texture.texture.name = object.active_material.active_texture.name
            else:
              for material in object.material_slots[:]:
                if material.material != None:
                  for texture in material.material.texture_slots[:]:
                    if texture != None:

                      # use active object
                      if option.useActiveObject:
                        if hasattr(context.active_object.active_material, 'active_texture'):
                          if hasattr(context.active_object.active_material.active_texture, 'name'):
                            texture.texture.name = context.active_object.active_material.active_texture.name
                      else:
                        if hasattr(object.active_material, 'active_texture'):
                          if hasattr(object.active_material.active_texture, 'name'):
                            texture.texture.name = object.active_material.active_texture.name

          # particle systems
          if option.particleSystems:

            # batch type
            if option.batchType in 'SELECTED':
              if object.select:
                for system in object.particle_systems[:]:

                  # use active object
                  if option.useActiveObject:
                    if hasattr(context.active_object.active_material, 'active_texture'):
                      if hasattr(context.active_object.active_material.active_texture, 'name'):
                        system.name = context.active_object.active_material.active_texture.name
                  else:
                    if hasattr(object.active_material, 'active_texture'):
                      if hasattr(object.active_material.active_texture, 'name'):
                        system.name = object.active_material.active_texture.name
            else:
              for system in object.particle_systems[:]:

                # use active object
                if option.useActiveObject:
                  if hasattr(context.active_object.active_material, 'active_texture'):
                    if hasattr(context.active_object.active_material.active_texture, 'name'):
                      system.name = context.active_object.active_material.active_texture.name
                else:
                  if hasattr(object.active_material, 'active_texture'):
                    if hasattr(object.active_material.active_texture, 'name'):
                      system.name = object.active_material.active_texture.name

          # particle settings
          if option.particleSettings:

            # batch type
            if option.batchType in 'SELECTED':
              if object.select:
                for system in object.particle_systems[:]:

                  # use active object
                  if option.useActiveObject:
                    if hasattr(context.active_object.active_material, 'active_texture'):
                      if hasattr(context.active_object.active_material.active_texture, 'name'):
                        system.settings.name = context.active_object.active_material.active_texture.name
                  else:
                    if hasattr(object.active_material, 'active_texture'):
                      if hasattr(object.active_material.active_texture, 'name'):
                        system.settings.name = object.active_material.active_texture.name
            else:
              for system in object.particle_systems[:]:

                # use active object
                if option.useActiveObject:
                  if hasattr(context.active_object.active_material, 'active_texture'):
                    if hasattr(context.active_object.active_material.active_texture, 'name'):
                      system.settings.name = context.active_object.active_material.active_texture.name
                else:
                  if hasattr(object.active_material, 'active_texture'):
                    if hasattr(object.active_material.active_texture, 'name'):
                      system.settings.name = object.active_material.active_texture.name

      # source particle system
      if option.source in 'PARTICLE_SYSTEM':

          # objects
          if option.objects:

            # batch type
            if option.batchType in 'SELECTED':
              if object.select:

                # use active object
                if option.useActiveObject:
                  if hasattr(context.active_object.particle_systems.active, 'name'):
                    object.name = context.active_object.particle_systems.active.name
                else:
                  if hasattr(object.particle_systems.active, 'name'):
                    object.name = object.particle_systems.active.name
            else:

              # use active object
              if option.useActiveObject:
                if hasattr(context.active_object.particle_systems.active, 'name'):
                  object.name = context.active_object.particle_systems.active.name
              else:
                if hasattr(object.particle_systems.active, 'name'):
                  object.name = object.particle_systems.active.name

          # object data
          if option.objectData:
            if object.type not in 'EMPTY':

              # batch type
              if option.batchType in 'SELECTED':
                if object.select:

                  # use active object
                  if option.useActiveObject:
                    if hasattr(context.active_object.particle_systems.active, 'name'):
                      object.data.name = context.active_object.particle_systems.active.name
                  else:
                    if hasattr(object.particle_systems.active, 'name'):
                      object.data.name = object.particle_systems.active.name
              else:

                # use active object
                if option.useActiveObject:
                  if hasattr(context.active_object.particle_systems.active, 'name'):
                    object.data.name = context.active_object.particle_systems.active.name
                else:
                  if hasattr(object.particle_systems.active, 'name'):
                    object.data.name = object.particle_systems.active.name

          # materials
          if option.materials:

            # batch type
            if option.batchType in 'SELECTED':
              if object.select:
                for material in object.material_slots[:]:
                  if material.material != None:

                    # use active object
                    if option.useActiveObject:
                      if hasattr(context.active_object.particle_systems.active, 'name'):
                        material.material.name = context.active_object.particle_systems.active.name
                    else:
                      if hasattr(object.particle_systems.active, 'name'):
                        material.material.name = object.particle_systems.active.name
            else:
              for material in object.material_slots[:]:
                if material.material != None:

                  # use active object
                  if option.useActiveObject:
                    if hasattr(context.active_object.particle_systems.active, 'name'):
                      material.material.name = context.active_object.particle_systems.active.name
                  else:
                    if hasattr(object.particle_systems.active, 'name'):
                      material.material.name = object.particle_systems.active.name

          # textures
          if option.textures:

            # batch type
            if option.batchType in 'SELECTED':
              if object.select:
                for material in object.material_slots[:]:
                  if material.material != None:
                    for texture in material.material.texture_slots[:]:
                      if texture != None:

                        # use active object
                        if option.useActiveObject:
                          if hasattr(context.active_object.particle_systems.active, 'name'):
                            texture.texture.name = context.active_object.particle_systems.active.name
                        else:
                          if hasattr(object.particle_systems.active, 'name'):
                            texture.texture.name = object.particle_systems.active.name
            else:
              for material in object.material_slots[:]:
                if material.material != None:
                  for texture in material.material.texture_slots[:]:
                    if texture != None:

                      # use active object
                      if option.useActiveObject:
                        if hasattr(context.active_object.particle_systems.active, 'name'):
                          texture.texture.name = context.active_object.particle_systems.active.name
                      else:
                        if hasattr(object.particle_systems.active, 'name'):
                          texture.texture.name = object.particle_systems.active.name

          # particle system
          if option.particleSystems:

            # batch type
            if option.batchType in 'SELECTED':
              if object.select:
                for system in object.particle_systems[:]:

                  # use active object
                  if option.useActiveObject:
                    if hasattr(context.active_object.particle_systems.active, 'name'):
                      system.name = context.active_object.particle_systems.active.name
                  else:
                    if hasattr(object.particle_systems.active, 'name'):
                      system.name = object.particle_systems.active.name
            else:
              for system in object.particle_systems[:]:

                # use active object
                if option.useActiveObject:
                  if hasattr(context.active_object.particle_systems.active, 'name'):
                    system.name = context.active_object.particle_systems.active.name
                else:
                  if hasattr(object.particle_systems.active, 'name'):
                    system.name = object.particle_systems.active.name

          # particle settings
          if option.particleSettings:

            # batch type
            if option.batchType in 'SELECTED':
              if object.select:
                for system in object.particle_systems[:]:

                  # use active object
                  if option.useActiveObject:
                    if hasattr(context.active_object.particle_systems.active, 'name'):
                      system.settings.name = context.active_object.particle_systems.active.name
                  else:
                    if hasattr(object.particle_systems.active, 'name'):
                      system.settings.name = object.particle_systems.active.name
            else:
              for system in object.particle_systems[:]:

                # use active object
                if option.useActiveObject:
                  if hasattr(context.active_object.particle_systems.active, 'name'):
                    system.settings.name = context.active_object.particle_systems.active.name
                else:
                  if hasattr(object.particle_systems.active, 'name'):
                    system.settings.name = object.particle_systems.active.name

      # source particle settings
      if option.source in 'PARTICLE_SETTINGS':

          # objects
          if option.objects:

            # batch type
            if option.batchType in 'SELECTED':
              if object.select:

                # use active object
                if option.useActiveObject:
                  if hasattr(context.active_object.particle_systems.active, 'settings'):
                    object.name = context.active_object.particle_systems.active.settings.name
                else:
                  if hasattr(object.particle_systems.active, 'settings'):
                    object.name = object.particle_systems.active.settings.name
            else:

              # use active object
              if option.useActiveObject:
                if hasattr(context.active_object.particle_systems.active, 'settings'):
                  object.name = context.active_object.particle_systems.active.settings.name
              else:
                if hasattr(object.particle_systems.active, 'settings'):
                  object.name = object.particle_systems.active.settings.name

          # object data
          if option.objectData:
            if object.type not in 'EMPTY':

              # batch type
              if option.batchType in 'SELECTED':
                if object.select:

                  # use active object
                  if option.useActiveObject:
                    if hasattr(context.active_object.particle_systems.active, 'settings'):
                      object.data.name = context.active_object.particle_systems.active.settings.name
                  else:
                    if hasattr(object.particle_systems.active, 'settings'):
                      object.data.name = object.particle_systems.active.settings.name
              else:

                # use active object
                if option.useActiveObject:
                  if hasattr(context.active_object.particle_systems.active, 'settings'):
                    object.data.name = context.active_object.particle_systems.active.settings.name
                else:
                  if hasattr(object.particle_systems.active, 'settings'):
                    object.data.name = object.particle_systems.active.settings.name

          # materials
          if option.materials:

            # batch type
            if option.batchType in 'SELECTED':
              if object.select:
                for material in object.material_slots[:]:
                  if material.material != None:

                    # use active object
                    if option.useActiveObject:
                      if hasattr(context.active_object.particle_systems.active, 'settings'):
                        material.material.name = context.active_object.particle_systems.active.settings.name
                    else:
                      if hasattr(object.particle_systems.active, 'settings'):
                        material.material.name = object.particle_systems.active.settings.name
            else:
              for material in object.material_slots[:]:
                if material.material != None:

                  # use active object
                  if option.useActiveObject:
                    if hasattr(context.active_object.particle_systems.active, 'settings'):
                      material.material.name = context.active_object.particle_systems.active.settings.name
                  else:
                    if hasattr(object.particle_systems.active, 'settings'):
                      material.material.name = object.particle_systems.active.settings.name

          # textures
          if option.textures:

            # batch type
            if option.batchType in 'SELECTED':
              if object.select:
                for material in object.material_slots[:]:
                  if material.material != None:
                    for texture in material.material.texture_slots[:]:
                      if texture != None:

                        # use active object
                        if option.useActiveObject:
                          if hasattr(context.active_object.particle_systems.active, 'settings'):
                            texture.texture.name = context.active_object.particle_systems.active.settings.name
                        else:
                          if hasattr(object.particle_systems.active, 'settings'):
                            texture.texture.name = object.particle_systems.active.settings.name
            else:
              for material in object.material_slots[:]:
                if material.material != None:
                  for texture in material.material.texture_slots[:]:
                    if texture != None:

                      # use active object
                      if option.useActiveObject:
                        if hasattr(context.active_object.particle_systems.active, 'settings'):
                          texture.texture.name = context.active_object.particle_systems.active.settings.name
                      else:
                        if hasattr(object.particle_systems.active, 'settings'):
                          texture.texture.name = object.particle_systems.active.settings.name

          # particle systems
          if option.particleSystems:

            # batch type
            if option.batchType in 'SELECTED':
              if object.select:
                for system in object.particle_systems[:]:

                  # use active object
                  if option.useActiveObject:
                    if hasattr(context.active_object.particle_systems.active, 'settings'):
                      system.name = context.active_object.particle_systems.active.settings.name
                  else:
                    if hasattr(object.particle_systems.active, 'settings'):
                      system.name = object.particle_systems.active.settings.name
            else:
              for system in object.particle_systems[:]:

                # use active object
                if option.useActiveObject:
                  if hasattr(context.active_object.particle_systems.active, 'settings'):
                    system.name = context.active_object.particle_systems.active.settings.name
                else:
                  if hasattr(object.particle_systems.active, 'settings'):
                    system.name = object.particle_systems.active.settings.name

          # particle settings
          if option.particleSettings:

            # batch type
            if option.batchType in 'SELECTED':
              if object.select:
                for system in object.particle_systems[:]:

                  # use active object
                  if option.useActiveObject:
                    if hasattr(context.active_object.particle_systems.active, 'settings'):
                      system.settings.name = context.active_object.particle_systems.active.settings.name
                  else:
                    if hasattr(object.particle_systems.active, 'settings'):
                      system.settings.name = object.particle_systems.active.settings.name
            else:
              for system in object.particle_systems[:]:

                # use active object
                if option.useActiveObject:
                  if hasattr(context.active_object.particle_systems.active, 'settings'):
                    system.settings.name = context.active_object.particle_systems.active.settings.name
                else:
                  if hasattr(object.particle_systems.active, 'settings'):
                    system.settings.name = object.particle_systems.active.settings.name

  # reset
  def reset(context, auto, names, name, copy):
    '''
      Resets the screen property values for item panel add-on's batch operators.
    '''

    # batch auto name option
    batchAutoNameOption = context.screen.batchAutoNameSettings

    # object name
    objectName = context.scene.batchAutoNameObjectNames

    # constraint name
    constraintName = context.scene.batchAutoNameConstraintNames

    # modifier name
    modifierName = context.scene.batchAutoNameModifierNames

    # object data name
    objectDataName = context.scene.batchAutoNameObjectDataNames

    # batch name option
    batchNameOption = context.screen.batchNameSettings

    # batch copy option
    batchCopyOption = context.screen.batchCopySettings

    # auto
    if auto:

      # batch type
      batchAutoNameOption.batchType = 'SELECTED'

      # objects
      batchAutoNameOption.objects = False

      # constraints
      batchAutoNameOption.constraints = False

      # modifiers
      batchAutoNameOption.modifiers = False

      # objectData
      batchAutoNameOption.objectData = False

      # bone Constraints
      batchAutoNameOption.boneConstraints = False

      # object type
      batchAutoNameOption.objectType = 'ALL'

      # constraint type
      batchAutoNameOption.constraintType = 'ALL'

      # modifier type
      batchAutoNameOption.modifierType = 'ALL'

    # names
    if names:

      # object names

      # mesh
      objectName.mesh = 'Mesh'

      # curve
      objectName.curve = 'Curve'

      # surface
      objectName.surface = 'Surface'

      # meta
      objectName.meta = 'Meta'

      # font
      objectName.font = 'Text'

      # armature
      objectName.armature = 'Armature'

      # lattice
      objectName.lattice = 'Lattice'

      # empty
      objectName.empty = 'Empty'

      # speaker
      objectName.speaker = 'Speaker'

      # camera
      objectName.camera = 'Camera'

      # lamp
      objectName.lamp = 'Lamp'

      # constraint names

      # camera solver
      constraintName.cameraSolver = 'Camera Solver'

      # follow track
      constraintName.followTrack = 'Follow Track'

      # object solver
      constraintName.objectSolver = 'Object Solver'

      # copy location
      constraintName.copyLocation = 'Copy Location'

      # copy rotation
      constraintName.copyRotation = 'Copy Rotation'

      # copy scale
      constraintName.copyScale = 'Copy Scale'

      # copy transforms
      constraintName.copyTransforms = 'Copy Transforms'

      # limit distance
      constraintName.limitDistance = 'Limit Distance'

      # limit location
      constraintName.limitLocation = 'Limit Location'

      # limit rotation
      constraintName.limitRotation = 'Limit Rotation'

      # limit scale
      constraintName.limitScale = 'Limit Scale'

      # maintain volume
      constraintName.maintainVolume = 'Maintain Volume'

      # transform
      constraintName.transform = 'Transform'

      # clamp to
      constraintName.clampTo = 'Clamp To'

      # damped track
      constraintName.dampedTrack = 'Damped Track'

      # inverse kinematics
      constraintName.inverseKinematics = 'Inverse Kinematics'

      # locked track
      constraintName.lockedTrack = 'Locked Track'

      # spline inverse kinematics
      constraintName.splineInverseKinematics = 'Spline Inverse Kinematics'

      # stretch to
      constraintName.stretchTo = 'Stretch To'

      # track to
      constraintName.trackTo = 'Track To'

      # action
      constraintName.action = 'Action'

      # child of
      constraintName.childOf = 'Child Of'

      # floor
      constraintName.floor = 'Floor'

      # follow path
      constraintName.followPath = 'Follow Path'

      # pivot
      constraintName.pivot = 'Pivot'

      # rigid body joint
      constraintName.rigidBodyJoint = 'Rigid Body Joint'

      # shrinkwrap
      constraintName.shrinkwrap = 'Shrinkwrap'

      # modifier names

      # data transfer
      modifierName.dataTransfer = 'Data Transfer'

      # mesh cache
      modifierName.meshCache = 'Mesh Cache'

      # normal edit
      modifierName.normalEdit = 'Normal Edit'

      # uv project
      modifierName.uvProject = 'UV Project'

      # uv warp
      modifierName.uvWarp = 'UV Warp'

      # vertex weight edit
      modifierName.vertexWeightEdit = 'Vertex Weight Edit'

      # vertex weight mix
      modifierName.vertexWeightMix = 'Vertex Weight Mix'

      # vertex weight proximity
      modifierName.vertexWeightProximity = 'Vertex Weight Proximity'

      # array
      modifierName.array = 'Array'

      # bevel
      modifierName.bevel = 'Bevel'

      # boolean
      modifierName.boolean = 'Boolean'

      # build
      modifierName.build = 'Build'

      # decimate
      modifierName.decimate = 'Decimate'

      # edge split
      modifierName.edgeSplit = 'Edge Split'

      # mask
      modifierName.mask = 'Mask'

      # mirror
      modifierName.mirror = 'Mirror'

      # multiresolution
      modifierName.multiresolution = 'Multiresolution'

      # remesh
      modifierName.remesh = 'Remesh'

      # screw
      modifierName.screw = 'Screw'

      # skin
      modifierName.skin = 'Skin'

      # solidify
      modifierName.solidify = 'Solidify'

      # subdivision surface
      modifierName.subdivisionSurface = 'Subdivision Surface'

      # triangulate
      modifierName.triangulate = 'Triangulate'

      # wireframe
      modifierName.wireframe = 'Wireframe'

      # armature
      modifierName.armature = 'Armature'

      # cast
      modifierName.cast = 'Cast'

      # corrective smooth
      modifierName.correctiveSmooth = 'Corrective Smooth'

      # curve
      modifierName.curve = 'Curve'

      # displace
      modifierName.displace = 'Displace'

      # hook
      modifierName.hook = 'Hook'

      # laplacian smooth
      modifierName.laplacianSmooth = 'Laplacian Smooth'

      # laplacian deform
      modifierName.laplacianDeform = 'Laplacian Deform'

      # lattice
      modifierName.lattice = 'Lattice'

      # mesh deform
      modifierName.meshDeform = 'Mesh Deform'

      # shrinkwrap
      modifierName.shrinkwrap = 'Shrinkwrap'

      # simple deform
      modifierName.simpleDeform = 'Simple Deform'

      # smooth
      modifierName.smooth = 'Smooth'

      # warp
      modifierName.warp = 'Warp'

      # wave
      modifierName.wave = 'Wave'

      # cloth
      modifierName.cloth = 'Cloth'

      # collision
      modifierName.collision = 'Collision'

      # dynamic paint
      modifierName.dynamicPaint = 'Dynamic Paint'

      # explode
      modifierName.explode = 'Explode'

      # fluid simulation
      modifierName.fluidSimulation = 'Fluid Simulation'

      # ocean
      modifierName.ocean = 'Ocean'

      # particle instance
      modifierName.particleInstance = 'Particle Instance'

      # particle system
      modifierName.particleSystem = 'Particle System'

      # smoke
      modifierName.smoke = 'Smoke'

      # soft body
      modifierName.softBody = 'Soft Body'

      # object data names

      # mesh
      modifierName.mesh = 'Mesh'

      # curve
      modifierName.curve = 'Curve'

      # surface
      modifierName.surface = 'Surface'

      # meta
      modifierName.meta = 'Meta'

      # font
      modifierName.font = 'Text'

      # armature
      modifierName.armature = 'Armature'

      # lattice
      modifierName.lattice = 'Lattice'

      # empty
      modifierName.empty = 'Empty'

      # speaker
      modifierName.speaker = 'Speaker'

      # camera
      modifierName.camera = 'Camera'

      # lamp
      modifierName.lamp = 'Lamp'

      # object data

      # mesh
      objectDataName.mesh = 'Mesh'

      # curve
      objectDataName.curve = 'Curve'

      # surface
      objectDataName.surface = 'Surface'

      # meta
      objectDataName.meta = 'Meta'

      # font
      objectDataName.font = 'Text'

      # armature
      objectDataName.armature = 'Armature'

      # lattice
      objectDataName.lattice = 'Lattice'

      # speaker
      objectDataName.speaker = 'Speaker'

      # camera
      objectDataName.camera = 'Camera'

      # lamp
      objectDataName.lamp = 'Lamp'

      # name
    if name:

      # batch type
      batchNameOption.batchType = 'SELECTED'

      # batch objects
      batchNameOption.objects = False

      # batch object constraints
      batchNameOption.constraints = False

      # batch modifiers
      batchNameOption.modifiers = False

      # batch object data
      batchNameOption.objectData = False

      # batch bones
      batchNameOption.bones = False

      # batch bone constraints
      batchNameOption.boneConstraints = False

      # batch materials
      batchNameOption.materials = False

      # batch textures
      batchNameOption.textures = False

      # batch particle systems
      batchNameOption.particleSystems = False

      # batch particle settings
      batchNameOption.particleSettings = False

      # batch groups
      batchNameOption.groups = False

      # batch vertex groups
      batchNameOption.vertexGroups = False

      # batch shape keys
      batchNameOption.shapekeys = False

      # batch uvs
      batchNameOption.uvs = False

      # batch vertex colors
      batchNameOption.vertexColors = False

      # batch bone groups
      batchNameOption.boneGroups = False

      # object type
      batchNameOption.objectType = 'ALL'

      # constraint type
      batchNameOption.constraintType = 'ALL'

      # modifier type
      batchNameOption.modifierType = 'ALL'

      # name
      batchNameOption.customName = ''

      # find
      batchNameOption.find = ''

      # regex
      batchNameOption.regex = False

      # replace
      batchNameOption.replace = ''

      # prefix
      batchNameOption.prefix = ''

      # suffix
      batchNameOption.suffix = ''

      # trim start
      batchNameOption.trimStart = 0

      # trim end
      batchNameOption.trimEnd = 0

    # copy
    if copy:

      # batch type
      batchCopyOption.batchType = 'SELECTED'

      # source
      batchCopyOption.source = 'OBJECT'

      # objects
      batchCopyOption.objects = False

      # object datas
      batchCopyOption.objectData = False

      # materials
      batchCopyOption.materials = False

      # textures
      batchCopyOption.textures = False

      # particle systems
      batchCopyOption.particleSystems = False

      # particle settings
      batchCopyOption.particleSettings = False

      # use active object
      batchCopyOption.useActiveObject = False

  # transfer
  def transfer(context, auto, names, name, copy):
    '''
      Resets the screen property values for item panel add-on's batch operators.
    '''

    # auto
    if auto:
      for screen in bpy.data.screens[:]:
        if screen != context.screen:

          # auto name option
          batchAutoNameOption = context.screen.batchAutoNameSettings

          # batch type
          screen.batchAutoNameSettings.batchType = batchAutoNameOption.batchType

          # objects
          screen.batchAutoNameSettings.objects = batchAutoNameOption.objects

          # constraints
          screen.batchAutoNameSettings.constraints = batchAutoNameOption.constraints

          # modifiers
          screen.batchAutoNameSettings.modifiers = batchAutoNameOption.modifiers

          # objectData
          screen.batchAutoNameSettings.objectData = batchAutoNameOption.objectData

          # bone Constraints
          screen.batchAutoNameSettings.boneConstraints = batchAutoNameOption.boneConstraints

          # object type
          screen.batchAutoNameSettings.objectType = batchAutoNameOption.objectType

          # constraint type
          screen.batchAutoNameSettings.constraintType = batchAutoNameOption.constraintType

          # modifier type
          screen.batchAutoNameSettings.modifierType = batchAutoNameOption.modifierType

    # names
    if names:
      for scene in bpy.data.scenes[:]:
        if scene != context.scene:

          # object name
          objectName = context.scene.batchAutoNameObjectNames

          # constraint name
          constraintName = context.scene.batchAutoNameConstraintNames

          # modifier name
          modifierName = context.scene.batchAutoNameModifierNames

          # object data name
          objectDataName = context.scene.batchAutoNameObjectDataNames

          # object names

          # mesh
          scene.batchAutoNameObjectNames.mesh = objectName.mesh

          # curve
          scene.batchAutoNameObjectNames.curve = objectName.curve

          # surface
          scene.batchAutoNameObjectNames.surface = objectName.surface

          # meta
          scene.batchAutoNameObjectNames.meta = objectName.meta

          # font
          scene.batchAutoNameObjectNames.font = objectName.font

          # armature
          scene.batchAutoNameObjectNames.armature = objectName.armature

          # lattice
          scene.batchAutoNameObjectNames.lattice = objectName.lattice

          # empty
          scene.batchAutoNameObjectNames.empty = objectName.empty

          # speaker
          scene.batchAutoNameObjectNames.speaker = objectName.speaker

          # camera
          scene.batchAutoNameObjectNames.camera = objectName.camera

          # lamp
          scene.batchAutoNameObjectNames.lamp = objectName.lamp

          # constraint names

          # camera solver
          scene.batchAutoNameConstraintNames.cameraSolver = constraintName.cameraSolver

          # follow track
          scene.batchAutoNameConstraintNames.followTrack = constraintName.followTrack

          # object solver
          scene.batchAutoNameConstraintNames.objectSolver = constraintName.objectSolver

          # copy location
          scene.batchAutoNameConstraintNames.copyLocation = constraintName.copyLocation

          # copy rotation
          scene.batchAutoNameConstraintNames.copyRotation = constraintName.copyRotation

          # copy scale
          scene.batchAutoNameConstraintNames.copyScale = constraintName.copyScale

          # copy transforms
          scene.batchAutoNameConstraintNames.copyTransforms = constraintName.copyTransforms

          # limit distance
          scene.batchAutoNameConstraintNames.limitDistance = constraintName.limitDistance

          # limit location
          scene.batchAutoNameConstraintNames.limitLocation = constraintName.limitLocation

          # limit rotation
          scene.batchAutoNameConstraintNames.limitRotation = constraintName.limitRotation

          # limit scale
          scene.batchAutoNameConstraintNames.limitScale = constraintName.limitScale

          # maintain volume
          scene.batchAutoNameConstraintNames.maintainVolume = constraintName.maintainVolume

          # transform
          scene.batchAutoNameConstraintNames.transform = constraintName.transform

          # clamp to
          scene.batchAutoNameConstraintNames.clampTo = constraintName.clampTo

          # damped track
          scene.batchAutoNameConstraintNames.dampedTrack = constraintName.dampedTrack

          # inverse kinematics
          scene.batchAutoNameConstraintNames.inverseKinematics = constraintName.inverseKinematics

          # locked track
          scene.batchAutoNameConstraintNames.lockedTrack = constraintName.lockedTrack

          # spline inverse kinematics
          scene.batchAutoNameConstraintNames.splineInverseKinematics = constraintName.splineInverseKinematics

          # stretch to
          scene.batchAutoNameConstraintNames.stretchTo = constraintName.stretchTo

          # track to
          scene.batchAutoNameConstraintNames.trackTo = constraintName.trackTo

          # action
          scene.batchAutoNameConstraintNames.action = constraintName.action

          # child of
          scene.batchAutoNameConstraintNames.childOf = constraintName.childOf

          # floor
          scene.batchAutoNameConstraintNames.floor = constraintName.floor

          # follow path
          scene.batchAutoNameConstraintNames.followPath = constraintName.followPath

          # pivot
          scene.batchAutoNameConstraintNames.pivot = constraintName.pivot

          # rigid body joint
          scene.batchAutoNameConstraintNames.rigidBodyJoint = constraintName.rigidBodyJoint

          # shrinkwrap
          scene.batchAutoNameConstraintNames.shrinkwrap = constraintName.shrinkwrap

          # modifier names

          # data transfer
          scene.batchAutoNameModifierNames.dataTransfer = modifierName.dataTransfer

          # mesh cache
          scene.batchAutoNameModifierNames.meshCache = modifierName.meshCache

          # normal edit
          scene.batchAutoNameModifierNames.normalEdit = modifierName.normalEdit

          # uv project
          scene.batchAutoNameModifierNames.uvProject = modifierName.uvProject

          # uv warp
          scene.batchAutoNameModifierNames.uvWarp = modifierName.uvWarp

          # vertex weight edit
          scene.batchAutoNameModifierNames.vertexWeightEdit = modifierName.vertexWeightEdit

          # vertex weight mix
          scene.batchAutoNameModifierNames.vertexWeightMix = modifierName.vertexWeightMix

          # vertex weight proximity
          scene.batchAutoNameModifierNames.vertexWeightProximity = modifierName.vertexWeightProximity

          # array
          scene.batchAutoNameModifierNames.array = modifierName.array

          # bevel
          scene.batchAutoNameModifierNames.bevel = modifierName.bevel

          # boolean
          scene.batchAutoNameModifierNames.boolean = modifierName.boolean

          # build
          scene.batchAutoNameModifierNames.build = modifierName.build

          # decimate
          scene.batchAutoNameModifierNames.decimate = modifierName.decimate

          # edge split
          scene.batchAutoNameModifierNames.edgeSplit = modifierName.edgeSplit

          # mask
          scene.batchAutoNameModifierNames.mask = modifierName.mask

          # mirror
          scene.batchAutoNameModifierNames.mirror = modifierName.mirror

          # multiresolution
          scene.batchAutoNameModifierNames.multiresolution = modifierName.multiresolution

          # remesh
          scene.batchAutoNameModifierNames.remesh = modifierName.remesh

          # screw
          scene.batchAutoNameModifierNames.screw = modifierName.screw

          # skin
          scene.batchAutoNameModifierNames.skin = modifierName.skin

          # solidify
          scene.batchAutoNameModifierNames.solidify = modifierName.solidify

          # subdivision surface
          scene.batchAutoNameModifierNames.subdivisionSurface = modifierName.subdivisionSurface

          # triangulate
          scene.batchAutoNameModifierNames.triangulate = modifierName.triangulate

          # wireframe
          scene.batchAutoNameModifierNames.wireframe = modifierName.wireframe

          # armature
          scene.batchAutoNameModifierNames.armature = modifierName.armature

          # cast
          scene.batchAutoNameModifierNames.cast = modifierName.cast

          # corrective smooth
          scene.batchAutoNameModifierNames.correctiveSmooth = modifierName.correctiveSmooth

          # curve
          scene.batchAutoNameModifierNames.curve = modifierName.curve

          # displace
          scene.batchAutoNameModifierNames.displace = modifierName.displace

          # hook
          scene.batchAutoNameModifierNames.hook = modifierName.hook

          # laplacian smooth
          scene.batchAutoNameModifierNames.laplacianSmooth = modifierName.laplacianSmooth

          # laplacian deform
          scene.batchAutoNameModifierNames.laplacianDeform = modifierName.laplacianDeform

          # lattice
          scene.batchAutoNameModifierNames.lattice = modifierName.lattice

          # mesh deform
          scene.batchAutoNameModifierNames.meshDeform = modifierName.meshDeform

          # shrinkwrap
          scene.batchAutoNameModifierNames.shrinkwrap = modifierName.shrinkwrap

          # simple deform
          scene.batchAutoNameModifierNames.simpleDeform = modifierName.simpleDeform

          # smooth
          scene.batchAutoNameModifierNames.smooth = modifierName.smooth

          # warp
          scene.batchAutoNameModifierNames.warp = modifierName.warp

          # wave
          scene.batchAutoNameModifierNames.wave = modifierName.wave

          # cloth
          scene.batchAutoNameModifierNames.cloth = modifierName.cloth

          # collision
          scene.batchAutoNameModifierNames.collision = modifierName.collision

          # dynamic paint
          scene.batchAutoNameModifierNames.dynamicPaint = modifierName.dynamicPaint

          # explode
          scene.batchAutoNameModifierNames.explode = modifierName.explode

          # fluid simulation
          scene.batchAutoNameModifierNames.fluidSimulation = modifierName.fluidSimulation

          # ocean
          scene.batchAutoNameModifierNames.ocean = modifierName.ocean

          # particle instance
          scene.batchAutoNameModifierNames.particleInstance = modifierName.particleInstance

          # particle system
          scene.batchAutoNameModifierNames.particleSystem = modifierName.particleSystem

          # smoke
          scene.batchAutoNameModifierNames.smoke = modifierName.smoke

          # soft body
          scene.batchAutoNameModifierNames.softBody = modifierName.softBody

          # object data names

          # mesh
          scene.batchAutoNameObjectDataNames.mesh = objectDataName.mesh

          # curve
          scene.batchAutoNameObjectDataNames.curve = objectDataName.curve

          # surface
          scene.batchAutoNameObjectDataNames.surface = objectDataName.surface

          # meta
          scene.batchAutoNameObjectDataNames.meta = objectDataName.meta

          # font
          scene.batchAutoNameObjectDataNames.font = objectDataName.font

          # armature
          scene.batchAutoNameObjectDataNames.armature = objectDataName.armature

          # lattice
          scene.batchAutoNameObjectDataNames.lattice = objectDataName.lattice

          # speaker
          scene.batchAutoNameObjectDataNames.speaker = objectDataName.speaker

          # camera
          scene.batchAutoNameObjectDataNames.camera = objectDataName.camera

          # lamp
          scene.batchAutoNameObjectDataNames.lamp = objectDataName.lamp


    # name
    if name:
      for screen in bpy.data.screens:
        if screen != context.screen:

          # batch name option
          batchNameOption = context.screen.batchNameSettings

          # batch type
          screen.batchNameSettings.batchType = batchNameOption.batchType

          # batch objects
          screen.batchNameSettings.objects = batchNameOption.objects

          # batch object constraints
          screen.batchNameSettings.constraints = batchNameOption.constraints

          # batch modifiers
          screen.batchNameSettings.modifiers = batchNameOption.modifiers

          # batch object data
          screen.batchNameSettings.objectData = batchNameOption.objectData

          # batch bones
          screen.batchNameSettings.bones = batchNameOption.bones

          # batch bone constraints
          screen.batchNameSettings.boneConstraints = batchNameOption.boneConstraints

          # batch materials
          screen.batchNameSettings.materials = batchNameOption.materials

          # batch textures
          screen.batchNameSettings.textures = batchNameOption.textures

          # batch particle systems
          screen.batchNameSettings.particleSystems = batchNameOption.particleSystems

          # batch particle settings
          screen.batchNameSettings.particleSettings = batchNameOption.particleSettings

          # batch groups
          screen.batchNameSettings.groups = batchNameOption.groups

          # batch vertex groups
          screen.batchNameSettings.vertexGroups = batchNameOption.vertexGroups

          # batch shape keys
          screen.batchNameSettings.shapekeys = batchNameOption.shapekeys

          # batch uvs
          screen.batchNameSettings.uvs = batchNameOption.uvs

          # batch vertex colors
          screen.batchNameSettings.vertexColors = batchNameOption.vertexColors

          # batch bone groups
          screen.batchNameSettings.boneGroups = batchNameOption.boneGroups

          # object type
          screen.batchNameSettings.objectType = batchNameOption.objectType

          # constraint type
          screen.batchNameSettings.constraintType = batchNameOption.constraintType

          # modifier type
          screen.batchNameSettings.modifierType = batchNameOption.modifierType

          # name
          screen.batchNameSettings.customName = batchNameOption.customName

          # find
          screen.batchNameSettings.find = batchNameOption.find

          # regex
          screen.batchNameSettings.regex = batchNameOption.regex

          # replace
          screen.batchNameSettings.replace = batchNameOption.replace

          # prefix
          screen.batchNameSettings.prefix = batchNameOption.prefix

          # suffix
          screen.batchNameSettings.suffix = batchNameOption.suffix

          # trim start
          screen.batchNameSettings.trimStart = batchNameOption.trimStart

          # trim end
          screen.batchNameSettings.trimEnd = batchNameOption.trimEnd

    # copy
    if copy:
      for screen in bpy.data.screens[:]:
        if screen != context.screen:

          # batch copy option
          batchCopyOption = context.screen.batchCopySettings

          # batch type
          screen.batchCopySettings.batchType = batchCopyOption.batchType

          # source
          screen.batchCopySettings.source = batchCopyOption.source

          # objects
          screen.batchCopySettings.objects = batchCopyOption.objects

          # object datas
          screen.batchCopySettings.objectData = batchCopyOption.objectData

          # materials
          screen.batchCopySettings.materials = batchCopyOption.materials

          # textures
          screen.batchCopySettings.textures = batchCopyOption.textures

          # particle systems
          screen.batchCopySettings.particleSystems = batchCopyOption.particleSystems

          # particle settings
          screen.batchCopySettings.particleSettings = batchCopyOption.particleSettings

          # use active object
          screen.batchCopySettings.useActiveObject = batchCopyOption.useActiveObject

