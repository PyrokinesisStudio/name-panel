
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
from random import random
from .. import storage

# count
count = 0

# tag
tag = False

# shared
class shared:
  '''
    Contains Lists;
      greasePencils
      objectData
      materials
      textures
  '''

  # grease pencils
  greasePencils = []

  particleSettings = []

  # object data
  objectData = []

  # materials
  materials = []

  # textures
  textures = []

# auto
class auto:
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
    option = context.scene.BatchAutoName

    # name
    name = auto.name

    # batch type
    if option.batchType in {'SELECTED', 'OBJECTS'}:

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

              # object type
              elif option.objectType in object.type:

                # name
                name(context, object, True, False, False, False)

          # batch type
          else:

            # object type
            if option.objectType in 'ALL':

              # name
              name(context, object, True, False, False, False)

            # object type
            elif option.objectType in object.type:

              # name
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

                # constraint type
                elif option.constraintType in constraint.type:

                  # name
                  name(context, constraint, False, True, False, False)

          # batch type
          else:
            for constraint in object.constraints[:]:

              # constraint type
              if option.constraintType in 'ALL':

                # name
                name(context, constraint, False, True, False, False)

              # constraint type
              elif option.constraintType in constraint.type:

                # name
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

                # modifier type
                elif option.modifierType in modifier.type:

                  # name
                  name(context, modifier, False, False, True, False)
          else:
            for modifier in object.modifiers[:]:

              # modifier type
              if option.modifierType in 'ALL':

                # name
                name(context, modifier, False, False, True, False)

              # modifier type
              elif option.modifierType in modifier.type:

                # name
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

                # object type
                elif option.objectType in object.type:

                  # name
                  name(context, object, False, False, False, True)

            # batch type
            else:

              # object type
              if option.objectType in 'ALL':

                # name
                name(context, object, False, False, False, True)

              # object type
              elif option.objectType in object.type:

                # name
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

                      # constraint type
                      elif option.constraintType in constraint.type:

                        # name
                        name(context, constraint, False, True, False, False)
          else:
            if object.type in 'ARMATURE':
              for bone in object.pose.bones[:]:
                for constraint in bone.constraints[:]:

                  # constraint type
                  if option.constraintType in 'ALL':

                    # name
                    name(context, constraint, False, True, False, False)

                  # constraint type
                  elif option.constraintType in constraint.type:

                    # name
                    name(context, constraint, False, True, False, False)

    # batch type
    else:
      for object in context.scene.objects[:]:

        # objects
        if option.objects:

          # object type
          if option.objectType in 'ALL':

            # name
            name(context, object, True, False, False, False)

          # object type
          elif option.objectType in object.type:

            # name
            name(context, object, True, False, False, False)

        # constraints
        if option.constraints:
          for constraint in object.constraints[:]:

            # constraint type
            if option.constraintType in 'ALL':

              # name
              name(context, constraint, False, True, False, False)

            # constraint type
            elif option.constraintType in constraint.type:

              # name
              name(context, constraint, False, True, False, False)

        # modifiers
        if option.modifiers:
          for modifier in object.modifiers[:]:

            # modifier type
            if option.modifierType in 'ALL':

              # name
              name(context, modifier, False, False, True, False)

            # modifier type
            elif option.modifierType in modifier.type:

              # name
              name(context, modifier, False, False, True, False)

        # object data
        if option.objectData:
          if object.type not in 'EMPTY':

            # object type
            if option.objectType in 'ALL':

              # name
              name(context, object, False, False, False, True)

            # object type
            elif option.objectType in object.type:

              # name
              name(context, object, False, False, False, True)

        # bone constraints
        if option.boneConstraints:
          if object.type in 'ARMATURE':
            for bone in object.pose.bones[:]:
              for constraint in bone.constraints[:]:

                # constraint type
                if option.constraintType in 'ALL':

                  # name
                  name(context, constraint, False, True, False, False)

                # constraint type
                elif option.constraintType in constraint.type:

                  # name
                  name(context, constraint, False, True, False, False)

  # object
  def name(context, datablock, object, constraint, modifier, objectData):
    '''
      Change the datablock names based on its type.
    '''

    # option
    option = context.scene.BatchAutoName

    # object name
    objectName = context.scene.BatchAutoName_ObjectNames

    # constraint name
    constraintName = context.scene.BatchAutoName_ConstraintNames

    # modifier name
    modifierName = context.scene.BatchAutoName_ModifierNames

    # object data name
    objectDataName = context.scene.BatchAutoName_ObjectDataNames

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

      # follow path
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

    # object data
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

# main
def main(context):
  '''
    Send datablock values to sort then send collections to process.
  '''
  global tag

  # option
  option = context.scene.BatchName

  # batch type
  if option.batchType in {'SELECTED', 'OBJECTS'}:

    # objects
    if option.objects:
      for object in bpy.data.objects[:]:

        # batch type
        if option.batchType in 'SELECTED':
          if object.select:

            # object type
            if option.objectType in 'ALL':

              # sort
              sort(context, object)

            # object type
            elif option.objectType in object.type:

              # sort
              sort(context, object)

        # batch type
        else:

          # object type
          if option.objectType in 'ALL':

            # sort
            sort(context, object)

          # object type
          elif option.objectType in object.type:

            # sort
            sort(context, object)

      # process
      process(context, storage.batch.objects)

    # groups
    if option.groups:
      for object in bpy.data.objects[:]:

        # batch type
        if option.batchType in 'SELECTED':
          if object.select:

            # object type
            if option.objectType in 'ALL':
              for group in bpy.data.groups[:]:
                if object in group.objects[:]:

                  # sort
                  sort(context, group)


            # object type
            elif option.objectType in object.type:
              for group in bpy.data.groups[:]:
                if object in group.objects[:]:

                  # sort
                  sort(context, group)

        # batch type
        else:

            # object type
            if option.objectType in 'ALL':
              for group in bpy.data.groups[:]:
                if object in group.objects[:]:

                  # sort
                  sort(context, group)

            # object type
            elif option.objectType in object.type:
              for group in bpy.data.groups[:]:
                if object in group.objects[:]:

                  # sort
                  sort(context, group)

      # clear duplicates
      objectGroups = []
      [objectGroups.append(item) for item in storage.batch.groups if item not in objectGroups]
      storage.batch.groups.clear()

      # process
      process(context, objectGroups)

    # actions
    if option.actions:
      for object in bpy.data.objects[:]:
        if hasattr(object.animation_data, 'action'):
          if hasattr(object.animation_data.action, 'name'):

            # batch type
            if option.batchType in 'SELECTED':
              if object.select:

                # object type
                if option.objectType in 'ALL':

                  # sort
                  sort(context, object.animation_data.action)

                # object type
                elif option.objectType in object.type:

                  # sort
                  sort(context, object.animation_data.action)

            # batch type
            else:

              # object type
              if option.objectType in 'ALL':

                # sort
                sort(context, object.animation_data.action)

              # object type
              elif option.objectType in object.type:

                # sort
                sort(context, object.animation_data.action)

      # clear duplicates
      actions = []
      [actions.append(item) for item in storage.batch.actions if item not in actions]
      storage.batch.actions.clear()

      # process
      process(context, actions)

    # grease pencil
    if option.greasePencil:
      for object in bpy.data.objects[:]:
        if hasattr(object.grease_pencil, 'name'):

          # batch type
          if option.batchType in 'SELECTED':
            if object.select:

              # object type
              if option.objectType in 'ALL':
                if object.grease_pencil.users == 1:

                  # sort
                  sort(context, object.grease_pencil)

                  # layers
                  for layer in object.grease_pencil.layers[:]:

                    # sort
                    sort(context, layer)
                else:

                  # shared
                  if object.grease_pencil not in shared.greasePencils[:]:
                    shared.greasePencils.append(object.grease_pencil)

                    # sort
                    sort(context, object.grease_pencil)

                    # layers
                    for layer in object.grease_pencil.layers[:]:

                      # sort
                      sort(context, layer)

              # object type
              elif option.objectType in object.type:
                if object.grease_pencil.users == 1:

                  # sort
                  sort(context, object.grease_pencil)

                  # layers
                  for layer in object.grease_pencil.layers[:]:

                    # sort
                    sort(context, layer)
                else:

                  # shared
                  if object.grease_pencil not in shared.greasePencils[:]:
                    shared.greasePencils.append(object.grease_pencil)

                    # sort
                    sort(context, object.grease_pencil)

                    # layers
                    for layer in object.grease_pencil.layers[:]:

                      # sort
                      sort(context, layer)

          # batch type
          else:

            # object type
            if option.objectType in 'ALL':
              if object.grease_pencil.users == 1:

                # sort
                sort(context, object.grease_pencil)

                # layers
                for layer in object.grease_pencil.layers[:]:

                  # sort
                  sort(context, layer)
              else:

                # shared
                if object.grease_pencil not in shared.greasePencils[:]:
                  shared.greasePencils.append(object.grease_pencil)

                  # sort
                  sort(context, object.grease_pencil)

                  # layers
                  for layer in object.grease_pencil.layers[:]:

                    # sort
                    sort(context, layer)

            # object type
            elif option.objectType in object.type:
              if object.grease_pencil.users == 1:

                # sort
                sort(context, object.grease_pencil)

                # layers
                for layer in object.grease_pencil.layers[:]:

                  # sort
                  sort(context, layer)
              else:

                # shared
                if object.grease_pencil not in shared.greasePencils[:]:
                  shared.greasePencils.append(object.grease_pencil)

                  # sort
                  sort(context, object.grease_pencil)

                  # layers
                  for layer in object.grease_pencil.layers[:]:

                    # sort
                    sort(context, layer)

          # process
          process(context, storage.batch.pencilLayers)

      # clear shared
      shared.greasePencils.clear()

      # process
      process(context, storage.batch.greasePencils)

    # constraints
    if option.constraints:
      for object in bpy.data.objects[:]:

        # batch type
        if option.batchType in 'SELECTED':
          if object.select:
            for constraint in object.constraints[:]:

              # constraint type
              if option.constraintType in 'ALL':

                # sort
                sort(context, constraint)

              # constraint type
              elif option.constraintType in constraint.type:

                # sort
                sort(context, constraint)

        # batch type
        else:
          for constraint in object.constraints[:]:

            # constraint type
            if option.constraintType in 'ALL':

              # sort
              sort(context, constraint)

            # constraint type
            elif option.constraintType in constraint.type:

              # sort
              sort(context, constraint)

        # process
        process(context, storage.batch.constraints)

    # modifiers
    if option.modifiers:
      for object in bpy.data.objects[:]:

        # batch type
        if option.batchType in 'SELECTED':
          if object.select:
            for modifier in object.modifiers[:]:

              # modifier type
              if option.modifierType in 'ALL':

                # sort
                sort(context, modifier)

              # modifier tye
              elif option.modifierType in modifier.type:

                # sort
                sort(context, modifier)

        # batch type
        else:
          for modifier in object.modifiers[:]:

            # modifier type
            if option.modifierType in 'ALL':

              # sort
              sort(context, modifier)

            # modifier tye
            elif option.modifierType in modifier.type:

              # sort
              sort(context, modifier)

        # process
        process(context, storage.batch.modifiers)

    # object data
    if option.objectData:
      for object in bpy.data.objects[:]:
        if object.type not in 'EMPTY':

          # batch type
          if option.batchType in 'SELECTED':
            if object.select:

              # object type
              if option.objectType in 'ALL':
                if object.data.users == 1:

                  # sort
                  sort(context, object.data)
                else:

                  # shared
                  if object.data.name not in shared.objectData[:]:
                    shared.objectData.append(object.data.name)

                    # sort
                    sort(context, object.data)

              # object type
              elif option.objectType in object.type:
                if object.data.users == 1:

                  # sort
                  sort(context, object.data)
                else:

                  # shared shared
                  if object.data.name not in shared.objectData[:]:
                    shared.objectData.append(object.data.name)

                    # sort
                    sort(context, object.data)

          # batch type
          else:

            # object type
            if option.objectType in 'ALL':
              if object.data.users == 1:

                # sort
                sort(context, object.data)
              else:

                # shared shared
                if object.data.name not in shared.objectData[:]:
                  shared.objectData.append(object.data.name)

                  # sort
                  sort(context, object.data)

            # object type
            elif option.objectType in object.type:
              if object.data.users == 1:

                # sort
                sort(context, object.data)
              else:

                # shared shared
                if object.data.name not in shared.objectData[:]:
                  shared.objectData.append(object.data.name)

                  # sort
                  sort(context, object.data)

      # clear shared
      shared.objectData.clear()

      # object data
      objectData = [
        storage.batch.curves,
        storage.batch.cameras,
        storage.batch.meshes,
        storage.batch.lamps,
        storage.batch.lattices,
        storage.batch.metaballs,
        storage.batch.speakers,
        storage.batch.armatures
      ]
      for collection in objectData:

        # process
        process(context, collection)

    # bone groups
    if option.boneGroups:
      for object in bpy.data.objects[:]:

        # batch type
        if option.batchType in 'SELECTED':
          if object.select:
            if object.type in 'ARMATURE':
              for group in object.pose.bone_groups[:]:
                if object.select:

                  # sort
                  sort(context, group)

        # batch type
        else:
          if object.type in 'ARMATURE':
            for group in object.pose.bone_groups[:]:

              # sort
              sort(context, group)

        # process
        process(context, storage.batch.boneGroups)

    # bones
    if option.bones:
      for object in bpy.data.objects[:]:
        if object.type in 'ARMATURE':

          # batch type
          if option.batchType in 'SELECTED':
            if object.select:

              # edit mode
              if object.mode in 'EDIT':
                for bone in bpy.data.armatures[object.data.name].edit_bones[:]:
                  if bone.select:

                    # sort
                    sort(context, bone)

              # pose or object mode
              else:
                for bone in bpy.data.armatures[object.data.name].bones[:]:
                  if bone.select:

                    # sort
                    sort(context, bone)

          # batch type
          else:

            # edit mode
            if object.mode in 'EDIT':
              for bone in bpy.data.armatures[object.data.name].edit_bones[:]:

                  # sort
                  sort(context, bone)

            # pose or object mode
            else:
              for bone in bpy.data.armatures[object.data.name].bones[:]:

                  # sort
                  sort(context, bone)

          # process
          process(context, storage.batch.bones)

    # bone constraints
    if option.boneConstraints:
      for object in bpy.data.objects[:]:
        if object.type in 'ARMATURE':

          # batch type
          if option.batchType in 'SELECTED':
            if object.select:
              for bone in object.pose.bones[:]:
                if bone.bone.select:
                  for constraint in bone.constraints[:]:

                    # constraint type
                    if option.constraintType in 'ALL':

                      # sort
                      sort(context, constraint)

                    # constraint type
                    elif option.constraintType in constraint.type:

                      # sort
                      sort(context, constraint)

                  # process
                  process(context, storage.batch.constraints)

          # batch type
          else:
            for bone in object.pose.bones[:]:
              for constraint in bone.constraints[:]:

                # constraint type
                if option.constraintType in 'ALL':

                  # sort
                  sort(context, constraint)

                # constraint type
                elif option.constraintType in constraint.type:

                  # sort
                  sort(context, constraint)

              # process
              process(context, storage.batch.constraints)

    # vertex groups
    if option.vertexGroups:
      for object in bpy.data.objects[:]:
        if hasattr(object, 'vertex_groups'):

          # batch type
          if option.batchType in 'SELECTED':
            if object.select:
              for group in object.vertex_groups[:]:

                # object type
                if option.objectType in 'ALL':

                  # sort
                  sort(context, group)

                # object type
                elif option.objectType in object.type:

                  # sort
                  sort(context, group)

              # process
              process(context, storage.batch.vertexGroups)

          # batch type
          else:
            for group in object.vertex_groups[:]:

              # object type
              if option.objectType in 'ALL':

                # sort
                sort(context, group)

              # object type
              elif option.objectType in object.type:

                # sort
                sort(context, group)

            # process
            process(context, storage.batch.vertexGroups)


    # shapekeys
    if option.shapekeys:
      for object in bpy.data.objects[:]:
        if hasattr(object.data, 'shape_keys'):
          if hasattr(object.data.shape_keys, 'key_blocks'):

            # batch type
            if option.batchType in 'SELECTED':
              if object.select:
                for block in object.data.shape_keys.key_blocks[:]:

                  # object type
                  if option.objectType in 'ALL':

                    # sort
                    sort(context, block)

                  # object type
                  elif option.objectType in object.type:

                    # sort
                    sort(context, block)

            # batch type
            else:
              for block in object.data.shape_keys.key_blocks[:]:

                # object type
                if option.objectType in 'ALL':

                  # sort
                  sort(context, block)

                # object type
                elif option.objectType in object.type:

                  # sort
                  sort(context, block)

            # process
            process(context, storage.batch.shapekeys)

    # uvs
    if option.uvs:
      for object in bpy.data.objects[:]:
        if object.type in 'MESH':

          # batch type
          if option.batchType in 'SELECTED':
            if object.select:
              for uv in object.data.uv_textures[:]:

                # sort
                sort(context, uv)

          # batch type
          else:
           for uv in object.data.uv_textures[:]:

              # sort
              sort(context, uv)

          # process
          process(context, storage.batch.uvs)

    # vertex colors
    if option.vertexColors:
      for object in bpy.data.objects[:]:
        if object.type in 'MESH':

          # batch type
          if option.batchType in 'SELECTED':
            if object.select:
              for color in object.data.vertex_colors[:]:

                # sort
                sort(context, color)

          # batch type
          else:
            for color in object.data.vertex_colors[:]:

              # sort
              sort(context, color)

          # process
          process(context, storage.batch.vertexColors)

    # materials
    if option.materials:
      for object in bpy.data.objects[:]:

        # batch type
        if option.batchType in 'SELECTED':
          if object.select:
            for slot in object.material_slots[:]:
              if slot.material != None:
                if slot.material.users == 1:

                  # object type
                  if option.objectType in 'ALL':

                    # sort
                    sort(context, slot.material)

                  # object type
                  elif option.objectType in object.type:

                    # sort
                    sort(context, slot.material)
                else:

                  # shared
                  if slot.material not in shared.materials[:]:
                    shared.materials.append(slot.material)

                    # sort
                    sort(context, slot.material)

        # batch type
        else:
          for slot in object.material_slots[:]:
            if slot.material != None:
              if slot.material.users == 1:

                # object type
                if option.objectType in 'ALL':

                  # sort
                  sort(context, slot.material)

                # object type
                elif option.objectType in object.type:

                  # sort
                  sort(context, slot.material)
              else:

                # shared
                if slot.material not in shared.materials[:]:
                  shared.materials.append(slot.material)

                  # sort
                  sort(context, slot.material)

      # clear shared
      shared.materials.clear()

      # process
      process(context, storage.batch.materials)

    # textures
    if option.textures:
      for object in bpy.data.objects[:]:
        if context.scene.render.engine not in 'CYCLES':

          # batch type
          if option.batchType in 'SELECTED':
            if object.select:
              for slot in object.material_slots[:]:
                if slot.material != None:
                  if slot.material.users == 1:
                    for texslot in slot.material.texture_slots[:]:
                      if texslot != None:
                        if texslot.texture.users == 1:

                          # object type
                          if option.objectType in 'ALL':

                            # sort
                            sort(context, texslot.texture)

                          # object type
                          elif option.objectType in object.type:

                            # sort
                            sort(context, texslot.texture)
                        else:

                          # shared
                          if texslot.texture not in shared.textures[:]:
                            shared.textures.append(texslot.texture)

                            # sort
                            sort(context, texslot.texture)
                  else:

                    # shared
                    if slot.material not in shared.materials[:]:
                      shared.materials.append(slot.material)
                      for texslot in slot.material.texture_slots[:]:
                        if texslot != None:
                          if texslot.texture.users == 1:

                            # object type
                            if option.objectType in 'ALL':

                              # sort
                              sort(context, texslot.texture)

                            # object type
                            elif option.objectType in object.type:

                              # sort
                              sort(context, texslot.texture)
                          else:

                            # shared
                            if texslot.texture not in shared.textures[:]:
                              shared.textures.append(texslot.texture)

                              # sort
                              sort(context, texslot.texture)

          # batch type
          else:
            for slot in object.material_slots[:]:
              if slot.material != None:
                if slot.material.users == 1:
                  for texslot in slot.material.texture_slots[:]:
                    if texslot != None:
                      if texslot.texture.users == 1:

                        # object type
                        if option.objectType in 'ALL':

                          # sort
                          sort(context, texslot.texture)

                        # object type
                        elif option.objectType in object.type:

                          # sort
                          sort(context, texslot.texture)
                      else:

                        # shared
                        if texslot.texture not in shared[:]:
                          shared.append(texslot.texture)

                          # sort
                          sort(context, texslot.texture)
                else:

                  # shared
                  if slot.material not in shared.materials[:]:
                    shared.materials.append(slot.material)
                    for texslot in slot.material.texture_slots[:]:
                      if texslot != None:
                        if texslot.texture.users == 1:

                          # object type
                          if option.objectType in 'ALL':

                            # sort
                            sort(context, texslot.texture)

                          # object type
                          elif option.objectType in object.type:

                            # sort
                            sort(context, texslot.texture)
                        else:

                          # shared
                          if texslot.texture not in shared.textures[:]:
                            shared.textures.append(texslot.texture)

                            # sort
                            sort(context, texslot.texture)

      # clear shared
      shared.textures.clear()

      # process
      process(context, storage.batch.textures)

    # particle systems
    if option.particleSystems:
      for object in bpy.data.objects[:]:
        if object.type in 'MESH':

          # batch type
          if option.batchType in 'SELECTED':
            if object.select:
              for system in object.particle_systems[:]:

                # object type
                if option.objectType in 'ALL':

                  # sort
                  sort(context, system)

                # object type
                elif option.objectType in object.type:

                  # sort
                  sort(context, system)

          # batch type
          else:
            for system in object.particle_systems[:]:

              # object type
              if option.objectType in 'ALL':

                # sort
                sort(context, system)

              # object type
              elif option.objectType in object.type:

                # sort
                sort(context, system)

          # process
          process(context, storage.batch.particleSystems)

    # particle settings
    if option.particleSettings:
      for object in bpy.data.objects[:]:
        if object.type in 'MESH':

          # batch type
          if option.batchType in 'SELECTED':
            if object.select:
              for system in object.particle_systems[:]:

                # object type
                if option.objectType in 'ALL':
                  if system.settings.users == 1:

                    # sort
                    sort(context, system.settings)
                  else:

                    # shared
                    if system.settings not in shared.particleSettings[:]:
                      shared.particleSettings.append(system.settings)

                      # sort
                      sort(context, system.settings)

                # object type
                elif option.objectType in object.type:
                  if system.settings.users == 1:

                    # sort
                    sort(context, system.settings)
                  else:

                    # shared
                    if system.settings not in shared.particleSettings[:]:
                      shared.particleSettings.append(system.settings)

                      # sort
                      sort(context, system.settings)

          # batch type
          else:
            for system in object.particle_systems[:]:

              # object type
              if option.objectType in 'ALL':
                if system.settings.users == 1:

                  # sort
                  sort(context, system.settings)
                else:

                  # shared
                  if system.settings not in shared.particleSettings[:]:
                    shared.particleSettings.append(system.settings)

                    # sort
                    sort(context, system.settings)

              # object type
              elif option.objectType in object.type:
                if system.settings.users == 1:

                  # sort
                  sort(context, system.settings)
                else:

                  # shared
                  if system.settings not in shared.particleSettings[:]:
                    shared.particleSettings.append(system.settings)

                    # sort
                    sort(context, system.settings)

      # clear shared
      shared.particleSettings.clear()

      # process
      process(context, storage.batch.particleSettings)

  # batch type
  if option.batchType in 'SCENE':

    # objects
    if option.objects:
      for object in context.scene.objects[:]:

        # object type
        if option.objectType in 'ALL':

          # sort
          sort(context, object)

        # object type
        elif option.objectType in object.type:

          # sort
          sort(context, object)

      # process
      process(context, storage.batch.objects)

    # groups
    if option.groups:
      for object in context.scene.objects[:]:

        # object type
        if option.objectType in 'ALL':
          for group in bpy.data.groups[:]:
            if object in group.objects[:]:

              # sort
              sort(context, group)

        # object type
        elif option.objectType in object.type:
          for group in bpy.data.groups[:]:
            if object in group.objects[:]:

              # sort
              sort(context, group)

      # clear duplicates
      objectGroups = []
      [objectGroups.append(item) for item in storage.batch.groups if item not in objectGroups]
      storage.batch.groups.clear()

      # process
      process(context, objectGroups)

    # actions
    if option.actions:
      for object in context.scene.objects[:]:
        if hasattr(object.animation_data, 'action'):
          if hasattr(object.animation_data.action, 'name'):

            # object type
            if option.objectType in 'ALL':

              # sort
              sort(context, object.animation_data.action)

            # object type
            elif option.objectType in object.type:

              # sort
              sort(context, object.animation_data.action)

      # clear duplicates
      actions = []
      [actions.append(item) for item in storage.batch.actions if item not in actions]
      storage.batch.actions.clear()

      # process
      process(context, actions)

    # grease pencil
    if option.greasePencil:
      for object in context.scene.objects[:]:
        if hasattr(object.grease_pencil, 'name'):

          # object type
          if option.objectType in 'ALL':
            if object.grease_pencil.users == 1:

              # sort
              sort(context, object.grease_pencil)

              # layers
              for layer in object.grease_pencil.layers[:]:

                # sort
                sort(context, layer)
            else:

              # shared
              if object.grease_pencil not in shared.greasePencils[:]:
                shared.greasePencils.append(object.grease_pencil)

                # sort
                sort(context, object.grease_pencil)

                # layers
                for layer in object.grease_pencil.layers[:]:

                  # sort
                  sort(context, layer)

          # object type
          elif option.objectType in object.type:
            if object.grease_pencil.users == 1:

              # sort
              sort(context, object.grease_pencil)

              # layers
              for layer in object.grease_pencil.layers[:]:

                # sort
                sort(context, layer)
            else:

              # shared
              if object.grease_pencil not in shared.greasePencils[:]:
                shared.greasePencils.append(object.grease_pencil)

                # sort
                sort(context, object.grease_pencil)

                # layers
                for layer in object.grease_pencil.layers[:]:

                  # sort
                  sort(context, layer)

          # process
          process(context, storage.batch.pencilLayers)

      # clear shared
      shared.greasePencils.clear()

      # process
      process(context, storage.batch.greasePencils)

    # constraints
    if option.constraints:
      for object in context.scene.objects[:]:
        for constraint in object.constraints[:]:

          # constraint type
          if option.constraintType in 'ALL':

            # sort
            sort(context, constraint)

          # constraint type
          elif option.constraintType in constraint.type:

            # sort
            sort(context, constraint)

        # process
        process(context, storage.batch.constraints)

    # modifiers
    if option.modifiers:
      for object in context.scene.objects[:]:
        for modifier in object.modifiers[:]:

          # modifier type
          if option.modifierType in 'ALL':

            # sort
            sort(context, modifier)

          # modifier tye
          elif option.modifierType in modifier.type:

            # sort
            sort(context, modifier)

        # process
        process(context, storage.batch.modifiers)

    # object data
    if option.objectData:
      for object in context.scene.objects[:]:
        if object.type not in 'EMPTY':

          # object type
          if option.objectType in 'ALL':
            if object.data.users == 1:

              # sort
              sort(context, object.data)
            else:

              # shared shared
              if object.data.name not in shared.objectData[:]:
                shared.objectData.append(object.data.name)

                # sort
                sort(context, object.data)

          # object type
          elif option.objectType in object.type:
            if object.data.users == 1:

              # sort
              sort(context, object.data)
            else:

              # shared shared
              if object.data.name not in shared.objectData[:]:
                shared.objectData.append(object.data.name)

                # sort
                sort(context, object.data)

      # clear shared
      shared.objectData.clear()

      # object data
      objectData = [
        storage.batch.curves,
        storage.batch.cameras,
        storage.batch.meshes,
        storage.batch.lamps,
        storage.batch.lattices,
        storage.batch.metaballs,
        storage.batch.speakers,
        storage.batch.armatures
      ]
      for collection in objectData:

        # process
        process(context, collection)

    # bone groups
    if option.boneGroups:
      for object in context.scene.objects[:]:
        if object.type in 'ARMATURE':
          for group in object.pose.bone_groups[:]:

            # sort
            sort(context, group)

        # process
        process(context, storage.batch.boneGroups)

    # bones
    if option.bones:
      for object in context.scene.objects[:]:
        if object.type in 'ARMATURE':

          # edit mode
          if object.mode in 'EDIT':
            for bone in bpy.data.armatures[object.data.name].edit_bones[:]:

                # sort
                sort(context, bone)

          # pose or object mode
          else:
            for bone in bpy.data.armatures[object.data.name].bones[:]:

                # sort
                sort(context, bone)

          # process
          process(context, storage.batch.bones)

    # bone constraints
    if option.boneConstraints:
      for object in context.scene.objects[:]:
        if object.type in 'ARMATURE':
          for bone in object.pose.bones[:]:
            for constraint in bone.constraints[:]:

              # constraint type
              if option.constraintType in 'ALL':

                # sort
                sort(context, constraint)

              # constraint type
              elif option.constraintType in constraint.type:

                # sort
                sort(context, constraint)

            # process
            process(context, storage.batch.constraints)

    # vertex groups
    if option.vertexGroups:
      for object in context.scene.objects[:]:
        if hasattr(object, 'vertex_groups'):
          for group in object.vertex_groups[:]:

            # object type
            if option.objectType in 'ALL':

              # sort
              sort(context, group)

            # object type
            elif option.objectType in object.type:

              # sort
              sort(context, group)

          # process
          process(context, storage.batch.vertexGroups)

    # shapekeys
    if option.shapekeys:
      for object in context.scene.objects[:]:
        if hasattr(object.data, 'shape_keys'):
          if hasattr(object.data.shape_keys, 'key_blocks'):
            for block in object.data.shape_keys.key_blocks[:]:

              # object type
              if option.objectType in 'ALL':

                # sort
                sort(context, block)

              # object type
              elif option.objectType in object.type:

                # sort
                sort(context, block)

            # process
            process(context, storage.batch.shapekeys)

    # uvs
    if option.uvs:
      for object in context.scene.objects[:]:
        if object.type in 'MESH':
          for uv in object.data.uv_textures[:]:

            # sort
            sort(context, uv)

          # process
          process(context, storage.batch.uvs)

    # vertex colors
    if option.vertexColors:
      for object in context.scene.objects[:]:
        if object.type in 'MESH':
          for color in object.data.vertex_colors[:]:

            # sort
            sort(context, color)

          # process
          process(context, storage.batch.vertexColors)

    # materials
    if option.materials:
      for object in context.scene.objects[:]:
        for slot in object.material_slots[:]:
          if slot.material != None:
            if slot.material.users == 1:

              # object type
              if option.objectType in 'ALL':

                # sort
                sort(context, slot.material)

              # object type
              elif option.objectType in object.type:

                # sort
                sort(context, slot.material)
            else:

              # shared
              if slot.material not in shared.materials[:]:
                shared.materials.append(slot.material)

                # sort
                sort(context, slot.material)

      # clear shared
      shared.materials.clear()

      # process
      process(context, storage.batch.materials)

    # textures
    if option.textures:
      for object in context.scene.objects[:]:
        if context.scene.render.engine not in 'CYCLES':
          for slot in object.material_slots[:]:
            if slot.material != None:
              if slot.material.users == 1:
                for texslot in slot.material.texture_slots[:]:
                  if texslot != None:
                    if texslot.texture.users == 1:

                      # object type
                      if option.objectType in 'ALL':

                        # sort
                        sort(context, texslot.texture)

                      # object type
                      elif option.objectType in object.type:

                        # sort
                        sort(context, texslot.texture)
                    else:

                      # shared
                      if texslot.texture not in shared[:]:
                        shared.append(texslot.texture)

                        # sort
                        sort(context, texslot.texture)
              else:

                # shared
                if slot.material not in shared.materials[:]:
                  shared.materials.append(slot.material)
                  for texslot in slot.material.texture_slots[:]:
                    if texslot != None:
                      if texslot.texture.users == 1:

                        # object type
                        if option.objectType in 'ALL':

                          # sort
                          sort(context, texslot.texture)

                        # object type
                        elif option.objectType in object.type:

                          # sort
                          sort(context, texslot.texture)
                      else:

                        # shared
                        if texslot.texture not in shared.textures[:]:
                          shared.textures.append(texslot.texture)

                          # sort
                          sort(context, texslot.texture)

      # clear shared
      shared.textures.clear()

      # process
      process(context, storage.batch.textures)

    # particle systems
    if option.particleSystems:
      for object in context.scene.objects[:]:
        if object.type in 'MESH':
          for system in object.particle_systems[:]:

            # object type
            if option.objectType in 'ALL':

              # sort
              sort(context, system)

            # object type
            elif option.objectType in object.type:

              # sort
              sort(context, system)

          # process
          process(context, storage.batch.particleSystems)

    # particle settings
    if option.particleSettings:
      for object in context.scene.objects[:]:
        if object.type in 'MESH':
          for system in object.particle_systems[:]:

            # object type
            if option.objectType in 'ALL':
              if system.settings.users == 1:

                # sort
                sort(context, system.settings)
              else:

                # shared
                if system.settings not in shared.particleSettings[:]:
                  shared.particleSettings.append(system.settings)

                  # sort
                  sort(context, system.settings)

            # object type
            elif option.objectType in object.type:
              if system.settings.users == 1:

                # sort
                sort(context, system.settings)
              else:

                # shared
                if system.settings not in shared.particleSettings[:]:
                  shared.particleSettings.append(system.settings)

                  # sort
                  sort(context, system.settings)

      # clear shared
      shared.particleSettings.clear()

      # process
      process(context, storage.batch.particleSettings)

  # batch type
  elif option.batchType in 'GLOBAL':

    # objects
    if option.objects:
      for object in bpy.data.objects[:]:

        # sort
        sort(context, object)

      # process
      process(context, storage.batch.objects)

    # groups
    if option.groups:
      for group in bpy.data.groups[:]:

        # sort
        sort(context, group)

      # process
      process(context, storage.batch.groups)

    # actions
    if option.actions:
      for action in bpy.data.actions[:]:

        # sort
        sort(context, action)

      # process
      process(context, storage.batch.actions)

    # grease pencil
    if option.greasePencil:
      for pencil in bpy.data.grease_pencil[:]:

        # sort
        sort(context, pencil)

        # layers
        for layer in pencil.layers[:]:

          # sort
          sort(context, layer)

      # process
      process(context, storage.batch.pencilLayers)
      process(context, storage.batch.greasePencils)

    # constraints
    if option.constraints:
      for object in bpy.data.objects[:]:
        for constraint in object.constraints[:]:

          # sort
          sort(context, constraint)

        # process
        process(context, storage.batch.constraints)

    # modifiers
    if option.modifiers:
      for object in bpy.data.objects[:]:
        for modifier in object.modifiers[:]:

          # sort
          sort(context, modifier)

        # process
        process(context, storage.batch.modifiers)

    # object data
    if option.objectData:

      # cameras
      for camera in bpy.data.cameras[:]:

        # sort
        sort(context, camera)

      # process
      process(context, storage.batch.cameras)

      # meshes
      for mesh in bpy.data.meshes[:]:

        # sort
        sort(context, mesh)

      # process
      process(context, storage.batch.meshes)

      # curves
      for curve in bpy.data.curves[:]:

        # sort
        sort(context, curve)

      # process
      process(context, storage.batch.curves)

      # lamps
      for lamp in bpy.data.lamps[:]:

        # sort
        sort(context, lamp)

      # process
      process(context, storage.batch.lamps)

      # lattices
      for lattice in bpy.data.lattices[:]:

        # sort
        sort(context, lattice)

      # process
      process(context, storage.batch.lattices)

      # metaballs
      for metaball in bpy.data.metaballs[:]:

        # sort
        sort(context, metaball)

      # process
      process(context, storage.batch.metaballs)

      # speakers
      for speaker in bpy.data.speakers[:]:

        # sort
        sort(context, speaker)

      # process
      process(context, storage.batch.speakers)

      # armatures
      for armature in bpy.data.armatures[:]:

        # sort
        sort(context, armature)

      # process
      process(context, storage.batch.armatures)

    # bone groups
    if option.boneGroups:
      for object in bpy.data.objects[:]:
        if object.type in 'ARMATURE':
          for group in object.pose.bone_groups[:]:

            # sort
            sort(context, group)

          # process
          process(context, storage.batch.boneGroups)

    # bones
    if option.bones:
      for armature in bpy.data.armatures[:]:
        for bone in armature.bones[:]:

          # sort
          sort(context, bone)

        # process
        process(context, storage.batch.bones)

    # bone constraints
    if option.boneConstraints:
      for object in bpy.data.objects[:]:
        if object.type in 'ARMATURE':
          for bone in object.pose.bones[:]:
            for constraint in bone.constraints[:]:

              # sort
              sort(context, constraint)

            # process
            process(context, storage.batch.constraints)

    # vertex groups
    if option.vertexGroups:
      for object in bpy.data.objects[:]:
        if object.type in {'MESH', 'LATTICE'}:
          for group in object.vertex_groups[:]:

            # sort
            sort(context, group)

          # process
          process(context, storage.batch.vertexGroups)

    # shape keys
    if option.shapekeys:
      for shapekey in bpy.data.shape_keys[:]:

          # sort
          sort(context, shapekey)
          for block in shapekey.key_blocks[:]:

            # sort
            sort(context, block)

          # process
          process(context, storage.batch.shapekeys)

    # uvs
    if option.uvs:
      for object in bpy.data.objects[:]:
        if object.type in 'MESH':
          for uv in object.data.uv_textures[:]:

            # sort
            sort(context, uv)

          # process
          process(context, storage.batch.uvs)

    # vertex colors
    if option.vertexColors:
      for object in bpy.data.objects[:]:
        if object.type in 'MESH':
          for color in object.data.vertex_colors[:]:

            # sort
            sort(context, color)

          # process
          process(context, storage.batch.vertexColors)

    # materials
    if option.materials:
      for material in bpy.data.materials[:]:

        # sort
        sort(context, material)

      # process
      process(context, storage.batch.materials)

    # textures
    if option.textures:
      for texture in bpy.data.textures[:]:

        # sort
        sort(context, texture)

      # process
      process(context, storage.batch.textures)

    # particles systems
    if option.particleSystems:
      for object in bpy.data.objects[:]:
        if object.type in 'MESH':
          for system in object.particle_systems[:]:

            # sort
            sort(context, system)

          # process
          process(context, storage.batch.particleSystems)

    # particles settings
    if option.particleSettings:
      for settings in bpy.data.particles[:]:

        # sort
        sort(context, settings)

      # process
      process(context, storage.batch.particleSettings)

  # scenes
  if option.scenes:
    for scene in bpy.data.scenes[:]:

      # sort
      sort(context, scene)

    # process
    process(context, storage.batch.scenes)

  # render layers
  if option.renderLayers:
    for scene in bpy.data.scenes[:]:
      for layer in scene.render.layers[:]:

        # sort
        sort(context, layer)

      # process
      process(context, storage.batch.renderLayers)

  # worlds
  if option.worlds:
    for world in bpy.data.worlds[:]:

      # sort
      sort(context, world)

    # process
    process(context, storage.batch.worlds)

  # libraries
  if option.libraries:
    for library in bpy.data.libraries[:]:

      # sort
      sort(context, library)

    # process
    process(context, storage.batch.libraries)

  # images
  if option.images:
    for image in bpy.data.images[:]:

      # sort
      sort(context, image)

    # process
    process(context, storage.batch.images)

  # masks
  if option.masks:
    for mask in bpy.data.masks[:]:

      # sort
      sort(context, mask)

    # process
    process(context, storage.batch.masks)

  # sequences
  if option.sequences:
    for scene in bpy.data.scenes[:]:
      if hasattr(scene.sequence_editor, 'sequence_all'):
        for sequence in scene.sequence_editor.sequences_all[:]:

          # sort
          sort(context, sequence)

        # process
        process(context, storage.batch.sequences)

  # movie clips
  if option.movieClips:
    for clip in bpy.data.movieclips[:]:

      # sort
      sort(context, clip)

    # process
    process(context, storage.batch.movieClips)

  # sounds
  if option.sounds:
    for sound in bpy.data.sounds[:]:

      # sort
      sort(context, sound)

    # process
    process(context, storage.batch.sounds)

  # screens
  if option.screens:
    for screen in bpy.data.screens[:]:

      # sort
      sort(context, screen)

    # process
    process(context, storage.batch.screens)

  # keying sets
  if option.keyingSets:
    for scene in bpy.data.scenes[:]:
      for keyingSet in scene.keying_sets[:]:

        # sort
        sort(context, keyingSet)

      # process
      process(context, storage.batch.keyingSets)

  # palettes
  if option.palettes:
    for palette in bpy.data.palettes[:]:

      # sort
      sort(context, palette)

    # process
    process(context, storage.batch.palettes)

  # brushes
  if option.brushes:
    for brush in bpy.data.brushes[:]:

      # sort
      sort(context, brush)

    # process
    process(context, storage.batch.brushes)

  # line styles
  if option.linestyles:
    for style in bpy.data.linestyles[:]:

      # sort
      sort(context, style)

    # process
    process(context, storage.batch.linestyles)

  # nodes
  if option.nodes:

    # shader
    for material in bpy.data.materials[:]:
      if hasattr(material.node_tree, 'nodes'):
        for node in material.node_tree.nodes[:]:

          # sort
          sort(context, node)

        # process
        process(context, storage.batch.nodes)

    # compositing
    for scene in bpy.data.scenes[:]:
      if hasattr(scene.node_tree, 'nodes'):
        for node in scene.node_tree.nodes[:]:

          # sort
          sort(context, node)

        # process
        process(context, storage.batch.nodes)

    # texture
    for texture in bpy.data.textures[:]:
      if hasattr(texture.node_tree, 'nodes'):
        for node in texture.node_tree.nodes[:]:

          # sort
          sort(context, node)

        # process
        process(context, storage.batch.nodes)

    # groups
    for group in bpy.data.node_groups[:]:
      for node in group.nodes[:]:

        # sort
        sort(context, node)

      # process
      process(context, storage.batch.nodes)

  # node labels
  if option.nodeLabels:

    # batch tag
    tag = True

    # shader
    for material in bpy.data.materials[:]:
      if hasattr(material.node_tree, 'nodes'):
        for node in material.node_tree.nodes[:]:

          # sort
          sort(context, node)

        # process
        process(context, storage.batch.nodeLabels)

    # compositing
    for scene in bpy.data.scenes[:]:
      if hasattr(scene.node_tree, 'nodes'):
        for node in scene.node_tree.nodes[:]:

          # sort
          sort(context, node)

        # process
        process(context, storage.batch.nodeLabels)

    # texture
    for texture in bpy.data.textures[:]:
      if hasattr(texture.node_tree, 'nodes'):
        for node in texture.node_tree.nodes[:]:

          # sort
          sort(context, node)

        # process
        process(context, storage.batch.nodeLabels)

    # groups
    for group in bpy.data.node_groups[:]:
      for node in group.nodes[:]:

        # sort
        sort(context, node)

      # process
      process(context, storage.batch.nodeLabels)

    # batch tag
    tag = False

  # node groups
  if option.nodeGroups:
    for group in bpy.data.node_groups[:]:

      # sort
      sort(context, group)

    # process
    process(context, storage.batch.nodeGroups)

  # texts
  if option.texts:
    for text in bpy.data.texts[:]:

      # sort
      sort(context, text)

    # process
    process(context, storage.batch.texts)

# sort
def sort(context, datablock):
  '''
    Sort datablocks into proper storage list.
  '''

  # option
  option = context.scene.BatchName

  # objects
  if option.objects:
    if datablock.rna_type.identifier == 'Object':
      storage.batch.objects.append([datablock.name, [1, datablock]])

  # groups
  if option.groups:
    if datablock.rna_type.identifier == 'Group':
      storage.batch.groups.append([datablock.name, [1, datablock]])

  # actions
  if option.actions:
    if datablock.rna_type.identifier == 'Action':
      storage.batch.actions.append([datablock.name, [1, datablock]])

  # grease pencils
  if option.greasePencil:
    if datablock.rna_type.identifier == 'GreasePencil':
      storage.batch.greasePencils.append([datablock.name, [1, datablock]])

    # pencil layers
    if datablock.rna_type.identifier == 'GPencilLayer':
      storage.batch.pencilLayers.append([datablock.info, [1, datablock]])

  # constraints
  if option.constraints:
    if hasattr(datablock.rna_type.base, 'identifier'):
      if datablock.rna_type.base.identifier == 'Constraint':
        storage.batch.constraints.append([datablock.name, [1, datablock]])

  # modifiers
  if option.modifiers:
    if hasattr(datablock.rna_type.base, 'identifier'):
      if datablock.rna_type.base.identifier in 'Modifier':
        storage.batch.modifiers.append([datablock.name, [1, datablock]])

  # object data
  if option.objectData:

    # cameras
    if datablock.rna_type.identifier == 'Camera':
      storage.batch.cameras.append([datablock.name, [1, datablock]])

    # meshes
    if datablock.rna_type.identifier == 'Mesh':
      storage.batch.meshes.append([datablock.name, [1, datablock]])

    # curves
    if datablock.rna_type.identifier in {'SurfaceCurve', 'TextCurve', 'Curve'}:
      storage.batch.curves.append([datablock.name, [1, datablock]])

    # lamps
    if hasattr(datablock.rna_type.base, 'identifier'):
      if datablock.rna_type.base.identifier == 'Lamp':
        storage.batch.lamps.append([datablock.name, [1, datablock]])

    # lattices
    if datablock.rna_type.identifier == 'Lattice':
      storage.batch.lattices.append([datablock.name, [1, datablock]])

    # metaballs
    if datablock.rna_type.identifier == 'MetaBall':
      storage.batch.metaballs.append([datablock.name, [1, datablock]])

    # speakers
    if datablock.rna_type.identifier == 'Speaker':
      storage.batch.speakers.append([datablock.name, [1, datablock]])

    # armatures
    if datablock.rna_type.identifier == 'Armature':
      storage.batch.armatures.append([datablock.name, [1, datablock]])

  # bones
  if option.bones:
    if datablock.rna_type.identifier in {'PoseBone', 'EditBone', 'Bone'}:
      storage.batch.bones.append([datablock.name, [1, datablock]])

  # vertex groups
  if option.vertexGroups:
    if datablock.rna_type.identifier == 'VertexGroup':
      storage.batch.vertexGroups.append([datablock.name, [1, datablock]])

  # shapekeys
  if option.shapekeys:
    if datablock.rna_type.identifier == 'ShapeKey':
      storage.batch.shapekeys.append([datablock.name, [1, datablock]])

  # uvs
  if option.uvs:
    if datablock.rna_type.identifier == 'MeshTexturePolyLayer':
      storage.batch.uvs.append([datablock.name, [1, datablock]])

  # vertex colors
  if option.vertexColors:
    if datablock.rna_type.identifier == 'MeshLoopColorLayer':
      storage.batch.vertexColors.append([datablock.name, [1, datablock]])

  # materials
  if option.materials:
    if datablock.rna_type.identifier == 'Material':
      storage.batch.materials.append([datablock.name, [1, datablock]])

  # textures
  if option.textures:
    if hasattr(datablock.rna_type.base, 'identifier'):
      if datablock.rna_type.base.identifier == 'Texture':
        storage.batch.textures.append([datablock.name, [1, datablock]])

  # particle systems
  if option.particleSystems:
    if datablock.rna_type.identifier == 'ParticleSystem':
      storage.batch.particleSystems.append([datablock.name, [1, datablock]])

  # particle settings
  if option.particleSettings:
    if datablock.rna_type.identifier == 'ParticleSettings':
      storage.batch.particleSettings.append([datablock.name, [1, datablock]])

  # scenes
  if option.scenes:
    if datablock.rna_type.identifier == 'Scene':
      storage.batch.scenes.append([datablock.name, [1, datablock]])

  # render layers
  if option.renderLayers:
    if datablock.rna_type.identifier == 'SceneRenderLayer':
      storage.batch.renderLayers.append([datablock.name, [1, datablock]])

  # worlds
  if option.worlds:
    if datablock.rna_type.identifier == 'World':
      storage.batch.worlds.append([datablock.name, [1, datablock]])

  # libraries
  if option.libraries:
    if datablock.rna_type.identifier == 'Library':
      storage.batch.libraries.append([datablock.name, [1, datablock]])

  # images
  if option.images:
    if datablock.rna_type.identifier == 'Image':
      storage.batch.images.append([datablock.name, [1, datablock]])

  # masks
  if option.masks:
    if datablock.rna_type.identifier == 'Mask':
      storage.batch.masks.append([datablock.name, [1, datablock]])

  # sequences
  if option.sequences:
    if hasattr(datablock.rna_type.base, 'identifier'):
      if datablock.rna_type.base.identifier == 'Sequence':
        storage.batch.sequences.append([datablock.name, [1, datablock]])

  # movie clips
  if option.movieClips:
    if datablock.rna_type.identifier == 'MovieClip':
      storage.batch.movieClips.append([datablock.name, [1, datablock]])

  # sounds
  if option.sounds:
    if datablock.rna_type.identifier == 'Sound':
      storage.batch.sounds.append([datablock.name, [1, datablock]])

  # screens
  if option.screens:
    if datablock.rna_type.identifier == 'Screen':
      storage.batch.screens.append([datablock.name, [1, datablock]])

  # keying sets
  if option.keyingSets:
    if datablock.rna_type.identifier == 'KeyingSet':
      storage.batch.keyingSets.append([datablock.bl_label, [1, datablock]])

  # palettes
  if option.palettes:
    if datablock.rna_type.identifier == 'Palette':
      storage.batch.palettes.append([datablock.name, [1, datablock]])

  # brushes
  if option.brushes:
    if datablock.rna_type.identifier == 'Brush':
      storage.batch.brushes.append([datablock.name, [1, datablock]])

  # linestyles
  if option.linestyles:
    if datablock.rna_type.identifier == 'FreestyleLineStyle':
      storage.batch.linestyles.append([datablock.name, [1, datablock]])

  # nodes
  if option.nodes:
    if hasattr(datablock.rna_type.base, 'base'):
      if hasattr(datablock.rna_type.base.base, 'base'):
        if hasattr(datablock.rna_type.base.base.base, 'identifier'):
          if datablock.rna_type.base.base.base.identifier == 'Node':
            storage.batch.nodes.append([datablock.name, [1, datablock]])

            if tag:
              datablock.label = name(context, datablock.label)

  # node groups
  if option.nodeGroups:
    if hasattr(datablock.rna_type.base, 'identifier'):
      if datablock.rna_type.base.identifier == 'NodeTree':
        storage.batch.nodeGroups.append([datablock.name, [1, datablock]])

  # texts
  if option.texts:
    if datablock.rna_type.identifier == 'Text':
      storage.batch.texts.append([datablock.name, [1, datablock]])

def process(context, collection):
  '''
    Process collection, send names to name.
  '''

  if not collection == []:

    # count
    global count

    # option
    option = context.scene.BatchName

    # count
    counter = [
      # 'datablock.name', ...
    ]

    # datablocks
    datablocks = [
      # ['datablock.name', datablock], [...
    ]

    # duplicates
    duplicates = [
      # 'datablock.name', ...
    ]

    # collection
    for item in collection[:]:

      # sort
      if option.sort:

        # name
        item[0] = name(context, (re.split(r'\W[0-9]*$|_[0-9]*$', item[0]))[0])
      else:
        item[0] = name(context, item[0])

      # count
      counter.append(item[0])

    # name count
    i = 0
    for item in collection[:]:

      # name count
      item[1][0] = counter.count(counter[i])
      i += 1

    # randomize
    for item in collection[:]:

      if option.sort:
        if item[1][0] > 1:

          # name
          if hasattr(item[1][1], 'name'):
            item[1][1].name = str(random())
          elif hasattr(item[1][1], 'info'):
            item[1][1].info = str(random())
          elif hasattr(item[1][1], 'bl_label'):
            item[1][1].bl_label = str(random())

          # count
          count += 1
        elif not option.sortOnly:

          # name
          if hasattr(item[1][1], 'name'):
            item[1][1].name = str(random())
          elif hasattr(item[1][1], 'info'):
            item[1][1].info = str(random())
          elif hasattr(item[1][1], 'bl_label'):
            item[1][1].bl_label = str(random())

          # count
          count += 1
      else:

        # name
        if hasattr(item[1][1], 'name'):
          item[1][1].name = str(random())
        elif hasattr(item[1][1], 'info'):
          item[1][1].info = str(random())
        elif hasattr(item[1][1], 'bl_label'):
          item[1][1].bl_label = str(random())

        # count
        count += 1

    # sort
    if option.sort:
      i = 0
      for item in collection[:]:
        datablocks.append([item[0], i])
        i += 1
      i = 0
      for item in sorted(datablocks):

        # name count
        if collection[item[1]][1][0] > 1:

          # duplicates
          if collection[item[1]][0] not in duplicates:

            # name
            if hasattr(collection[item[1]][1][1], 'name'):
              collection[item[1]][1][1].name = collection[item[1]][0] + option.separator + '0'*option.padding + str(i + option.start).zfill(len(str(collection[item[1]][1][0])))
            elif hasattr(collection[item[1]][1][1], 'info'):
              collection[item[1]][1][1].info = collection[item[1]][0] + option.separator + '0'*option.padding + str(i + option.start).zfill(len(str(collection[item[1]][1][0])))
            elif hasattr(collection[item[1]][1][1], 'bl_label'):
              collection[item[1]][1][1].bl_label = collection[item[1]][0] + option.separator + '0'*option.padding + str(i + option.start).zfill(len(str(collection[item[1]][1][0])))
            i += 1
          if i == collection[item[1]][1][0]:
            i = 0

            # duplicates
            duplicates.append(collection[item[1]][0])

    # assign names
    if not option.sortOnly:
      for item in collection[:]:
        if item[0] not in duplicates:

          # name
          if hasattr(item[1][1], 'name'):
            item[1][1].name = item[0]
          elif hasattr(item[1][1], 'info'):
            item[1][1].info = item[0]
          elif hasattr(item[1][1], 'bl_label'):
            item[1][1].bl_label = item[0]

    # clear counter
    counter.clear()

    # clear datablocks
    datablocks.clear()

    # clear duplicates
    duplicates.clear()

    # clear collection
    collection.clear()

# name
def name(context, datablock):
  '''
    Name datablocks received from process.
  '''

  # option
  option = context.scene.BatchName

  # name check
  nameCheck = datablock

  # custom name
  if option.customName != '':

    # new name
    newName = option.customName
  else:

    # new name
    newName = datablock

  # trim start
  newName = newName[option.trimStart:]

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

  # name check
  if nameCheck != newName:
    return newName
  else:
    return datablock

# copy
def copy(context):
  '''
    Get names from source datablock and assign to destination datablock.
  '''

  # option
  option = context.scene.BatchCopyName

  # batch type
  if option.batchType in {'SELECTED', 'OBJECTS'}:
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
          if object.type not in 'EMPTY':

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
  # batch type
  else:
    for object in context.scene.objects[:]:

      # source object
      if option.source in 'OBJECT':

        # objects
        if option.objects:

          # use active object
          if option.useActiveObject:
            object.name = context.active_object.name
          else:
            object.name = object.name

        # object data
        if option.objectData:
          if object.type not in 'EMPTY':

            # use active object
            if option.useActiveObject:
              object.data.name = context.active_object.name
            else:
              object.data.name = object.name

        # materials
        if option.materials:
          for material in object.material_slots[:]:
            if material.material != None:

              # use active object
              if option.useActiveObject:
                material.material.name = context.active_object.name
              else:
                material.material.name = object.name

        # textures
        if option.textures:
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
          for system in object.particle_systems[:]:

            # use active object
            if option.useActiveObject:
              system.name = context.active_object.name
            else:
              system.name = object.name

        # particle settings
        if option.particleSettings:
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

            # use active object
            if option.useActiveObject:
              object.name = context.active_object.data.name
            else:
              object.name = object.data.name

          # object data
          if option.objectData:

            # use active object
            if option.useActiveObject:
              object.data.name = context.active_object.data.name
            else:
              object.data.name = object.data.name

          # materials
          if option.materials:
            for material in object.material_slots[:]:
              if material.material != None:

                # use active object
                if option.useActiveObject:
                  material.material.name = context.active_object.data.name
                else:
                  material.material.name = object.data.name

          # textures
          if option.textures:
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
            for system in object.particle_systems[:]:

              # use active object
              if option.useActiveObject:
                system.name = context.active_object.data.name
              else:
                system.name = object.data.name

          # particle settings
          if option.particleSettings:
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

            # use active object
            if option.useActiveObject:
              if hasattr(context.active_object.active_material, 'name'):
                object.data.name = context.active_object.active_material.name
            else:
              if hasattr(object.active_material, 'name'):
                object.data.name = object.active_material.name

        # materials
        if option.materials:
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

              # use active object
              if option.useActiveObject:
                if hasattr(context.active_object.particle_systems.active, 'name'):
                  object.data.name = context.active_object.particle_systems.active.name
              else:
                if hasattr(object.particle_systems.active, 'name'):
                  object.data.name = object.particle_systems.active.name

          # materials
          if option.materials:
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

              # use active object
              if option.useActiveObject:
                if hasattr(context.active_object.particle_systems.active, 'settings'):
                  object.data.name = context.active_object.particle_systems.active.settings.name
              else:
                if hasattr(object.particle_systems.active, 'settings'):
                  object.data.name = object.particle_systems.active.settings.name

          # materials
          if option.materials:
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
            for system in object.particle_systems[:]:

              # use active object
              if option.useActiveObject:
                if hasattr(context.active_object.particle_systems.active, 'settings'):
                  system.settings.name = context.active_object.particle_systems.active.settings.name
              else:
                if hasattr(object.particle_systems.active, 'settings'):
                  system.settings.name = object.particle_systems.active.settings.name
