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
#  Version: 0.9
#
# ##### END INFO BLOCK #####

# blender info
bl_info = {
  'name': 'Item Panel & Batch Naming',
  'author': 'proxe',
  'version': (0, 9),
  'blender': (2, 75, 0),
  'location': '3D View → Properties Panel → Item',
  'description': 'An improved item panel for the 3D View with included batch naming tools.',
  'category': '3D View'
}

# imports
import bpy
import re
from bpy.types import PropertyGroup, Operator, Panel
from bpy.props import *

###############
## FUNCTIONS ##
###############

# rename
def rename(self, dataPath, batchName, find, replace, prefix, suffix, trimStart, trimEnd):
  ''' Names single proper dataPath value received from batchRename. '''

  # batch name
  if batchName:
    targetName = batchName

    # trim start
    targetName = targetName[trimStart:]
  else:
    targetName = dataPath.name[trimStart:]

  # trim end
  if trimEnd > 0:
    targetName = targetName[:-trimEnd]

  # re find and replace
  targetName = re.sub(find, replace, targetName)

  # prefix and suffix
  targetName = prefix + targetName + suffix

  # assign name
  dataPath.name = targetName

# batch rename
def batchRename(self, context, batchType, batchObjects, batchObjectConstraints, batchModifiers, batchObjectData, batchBones, batchBoneConstraints, batchMaterials, batchTextures, batchParticleSystems, batchParticleSettings, batchGroups, batchVertexGroups, batchShapeKeys, batchUVS, batchVertexColors, batchBoneGroups, objectType, constraintType, modifierType, batchName, find, replace, prefix, suffix, trimStart, trimEnd):
  ''' Send dataPath values to rename. '''

  # batch objects
  if batchObjects:
    for object in bpy.data.objects[:]:

      # batch type
      if batchType in 'SELECTED':
        if object.select:

          # object type
          if objectType in 'ALL':

            dataPath = object

            # rename
            rename(self, dataPath, batchName, find, replace, prefix, suffix, trimStart, trimEnd)
          elif objectType in object.type:
            dataPath = object
            rename(self, dataPath, batchName, find, replace, prefix, suffix, trimStart, trimEnd)
      else:

        # object type
        if objectType in 'ALL':
          dataPath = object

          # rename
          rename(self, dataPath, batchName, find, replace, prefix, suffix, trimStart, trimEnd)
        elif objectType in object.type:
          dataPath = object
          rename(self, dataPath, batchName, find, replace, prefix, suffix, trimStart, trimEnd)

  # batch object constraints
  if batchObjectConstraints:
    for object in bpy.data.objects[:]:

      # batch type
      if batchType in 'SELECTED':
        if object.select:
          for constraint in object.constraints[:]:

            # constraint type
            if constraintType in 'ALL':
              dataPath = constraint

              # rename
              rename(self, dataPath, batchName, find, replace, prefix, suffix, trimStart, trimEnd)
            elif constraintType in constraint.type:
              dataPath = constraint
              rename(self, dataPath, batchName, find, replace, prefix, suffix, trimStart, trimEnd)
      else:
        for constraint in object.constraints[:]:

          # constraint type
          if constraintType in 'ALL':
            dataPath = constraint

            # rename
            rename(self, dataPath, batchName, find, replace, prefix, suffix, trimStart, trimEnd)
          elif constraintType in constraint.type:
            dataPath = constraint
            rename(self, dataPath, batchName, find, replace, prefix, suffix, trimStart, trimEnd)

  # batch modifiers
  if batchModifiers:
    for object in bpy.data.objects[:]:

      # batch type
      if batchType in 'SELECTED':
        if object.select:
          for modifier in object.modifiers[:]:

            # modifier type
            if modifierType in 'ALL':
              dataPath = modifier

              # rename
              rename(self, dataPath, batchName, find, replace, prefix, suffix, trimStart, trimEnd)
            elif modifierType in modifier.type:
              dataPath = modifier
              rename(self, dataPath, batchName, find, replace, prefix, suffix, trimStart, trimEnd)
      else:
        for modifier in object.modifiers[:]:

          # modifier type
          if modifierType in 'ALL':
            dataPath = modifier

            # rename
            rename(self, dataPath, batchName, find, replace, prefix, suffix, trimStart, trimEnd)
          elif modifierType in modifier.type:
            dataPath = modifier
            rename(self, dataPath, batchName, find, replace, prefix, suffix, trimStart, trimEnd)

  # batch objects data
  if batchObjectData:
    for object in bpy.data.objects[:]:

      # batch type
      if batchType in 'SELECTED':
        if object.select:

          # object type
          if objectType in 'ALL':
            dataPath = object.data

            # rename
            rename(self, dataPath, batchName, find, replace, prefix, suffix, trimStart, trimEnd)
          elif objectType in object.type:
            dataPath = object.data
            rename(self, dataPath, batchName, find, replace, prefix, suffix, trimStart, trimEnd)
      else:

        # object type
        if objectType in 'ALL':
          dataPath = object.data

          # rename
          rename(self, dataPath, batchName, find, replace, prefix, suffix, trimStart, trimEnd)
        elif objectType in object.type:
          dataPath = object.data
          rename(self, dataPath, batchName, find, replace, prefix, suffix, trimStart, trimEnd)

  # batch bones
  if batchBones:
    for object in bpy.data.objects[:]:

      # batch type
      if batchType in 'SELECTED':
        if object.select:
          if object.type in 'ARMATURE':
            for bone in object.data.bones:
              if bone.select:
                dataPath = bone

                # rename
                rename(self, dataPath, batchName, find, replace, prefix, suffix, trimStart, trimEnd)
      else:
        if object.type in 'ARMATURE':
          for bone in object.data.bones:
            dataPath = bone

            # rename
            rename(self, dataPath, batchName, find, replace, prefix, suffix, trimStart, trimEnd)

  # batch bone constraints
  if batchBoneConstraints:
    for object in bpy.data.objects[:]:

      # batch type
      if batchType in 'SELECTED':
        if object.select:
          if object.type in 'ARMATURE':
            for bone in object.pose.bones[:]:
              if bone.bone.select:
                for constraint in bone.constraints[:]:

                  # constraint type
                  if constraintType in 'ALL':
                    dataPath = constraint

                    # rename
                    rename(self, dataPath, batchName, find, replace, prefix, suffix, trimStart, trimEnd)
                  elif constraintType in constraint.type:
                    dataPath = constraint
                    rename(self, dataPath, batchName, find, replace, prefix, suffix, trimStart, trimEnd)
      else:
        if object.type in 'ARMATURE':
          for bone in object.pose.bones[:]:
            for constraint in bone.constraints[:]:

              # constraint type
              if constraintType in 'ALL':
                dataPath = constraint

                # rename
                rename(self, dataPath, batchName, find, replace, prefix, suffix, trimStart, trimEnd)
              elif constraintType in constraint.type:
                dataPath = constraint
                rename(self, dataPath, batchName, find, replace, prefix, suffix, trimStart, trimEnd)

  # batch materials
  if batchMaterials:
    for object in bpy.data.objects[:]:

        # batch type
        if batchType in 'SELECTED':
          if object.select:
            for material in object.material_slots[:]:
              if material.material != None:

                # object type
                if objectType in 'ALL':
                  dataPath = material.material

                  # rename
                  rename(self, dataPath, batchName, find, replace, prefix, suffix, trimStart, trimEnd)
                elif objectType in object.type:
                  dataPath = material.material
                  rename(self, dataPath, batchName, find, replace, prefix, suffix, trimStart, trimEnd)
        else:
          for material in object.material_slots[:]:
            if material.material != None:

              # object type
              if objectType in 'ALL':
                dataPath = material.material

                # rename
                rename(self, dataPath, batchName, find, replace, prefix, suffix, trimStart, trimEnd)
              elif objectType in object.type:
                dataPath = material.material
                rename(self, dataPath, batchName, find, replace, prefix, suffix, trimStart, trimEnd)

  # batch textures
  if batchTextures:
    if context.scene.render.engine != 'CYCLES':
      for object in bpy.data.objects[:]:

        # batch type
        if batchType in 'SELECTED':
          if object.select:
            for material in object.material_slots[:]:
              if material.material != None:
                for texture in material.material.texture_slots[:]:
                  if texture != None:

                    # object type
                    if objectType in 'ALL':
                      dataPath = texture.texture

                      # rename
                      rename(self, dataPath, batchName, find, replace, prefix, suffix, trimStart, trimEnd)
                    elif objectType in object.type:
                      dataPath = texture.texture
                      rename(self, dataPath, batchName, find, replace, prefix, suffix, trimStart, trimEnd)
        else:
          for material in object.material_slots[:]:
            if material.material != None:
              for texture in material.material.texture_slots[:]:
                if texture != None:

                  # object type
                  if objectType in 'ALL':
                    dataPath = texture.texture

                    # rename
                    rename(self, dataPath, batchName, find, replace, prefix, suffix, trimStart, trimEnd)
                  elif objectType in object.type:
                    dataPath = texture.texture
                    rename(self, dataPath, batchName, find, replace, prefix, suffix, trimStart, trimEnd)

  # batch particle system
  if batchParticleSystems:
    for object in bpy.data.objects[:]:
      if object.type in 'MESH':

        # batch type
        if batchType in 'SELECTED':
          if object.select:
            for system in object.particle_systems[:]:

              # object type
              if objectType in 'ALL':
                dataPath = system

                # rename
                rename(self, dataPath, batchName, find, replace, prefix, suffix, trimStart, trimEnd)
              elif objectType in object.type:
                dataPath = system
                rename(self, dataPath, batchName, find, replace, prefix, suffix, trimStart, trimEnd)
        else:
          for system in object.particle_systems[:]:

            # object type
            if objectType in 'ALL':
              dataPath = system

              # rename
              rename(self, dataPath, batchName, find, replace, prefix, suffix, trimStart, trimEnd)
            elif objectType in object.type:
              dataPath = system
              rename(self, dataPath, batchName, find, replace, prefix, suffix, trimStart, trimEnd)

  # batch particle settings
  if batchParticleSettings:
    for object in bpy.data.objects[:]:
      if object.type in 'MESH':

        # batch type
        if batchType in 'SELECTED':
          if object.select:
            for system in object.particle_systems[:]:

              # object type
              if objectType in 'ALL':
                dataPath = system.settings

                # rename
                rename(self, dataPath, batchName, find, replace, prefix, suffix, trimStart, trimEnd)
              elif objectType in object.type:
                dataPath = system.settings
                rename(self, dataPath, batchName, find, replace, prefix, suffix, trimStart, trimEnd)
        else:
          for system in object.particle_systems[:]:

            # object type
            if objectType in 'ALL':
              dataPath = system.settings

              # rename
              rename(self, dataPath, batchName, find, replace, prefix, suffix, trimStart, trimEnd)
            elif objectType in object.type:
              dataPath = system.settings
              rename(self, dataPath, batchName, find, replace, prefix, suffix, trimStart, trimEnd)

  # batch groups
  if batchGroups:
    for object in bpy.data.objects[:]:

      # batch type
      if batchType in 'SELECTED':
        if object.select:

          # object type
          if objectType in 'ALL':
            for group in bpy.data.groups[:]:
              if object in group.objects[:]:
                dataPath = group

                # rename
                rename(self, dataPath, batchName, find, replace, prefix, suffix, trimStart, trimEnd)
          elif objectType in object.type:
            for group in bpy.data.groups[:]:
              if object in group.objects[:]:
                dataPath = group
                rename(self, dataPath, batchName, find, replace, prefix, suffix, trimStart, trimEnd)
      else:

          # object type
          if objectType in 'ALL':
            for group in bpy.data.groups[:]:
              if object in group.objects[:]:
                dataPath = group

                # rename
                rename(self, dataPath, batchName, find, replace, prefix, suffix, trimStart, trimEnd)
          elif objectType in object.type:
            for group in bpy.data.groups[:]:
              if object in group.objects[:]:
                dataPath = group
                rename(self, dataPath, batchName, find, replace, prefix, suffix, trimStart, trimEnd)

  # batch vertex groups
  if batchVertexGroups:
    for object in bpy.data.objects[:]:
      if object.type in {'MESH', 'LATTICE'}:

        # batch type
        if batchType in 'SELECTED':
          if object.select:
            for group in object.vertex_groups[:]:

              # object type
              if objectType in 'ALL':
                dataPath = group

                # rename
                rename(self, dataPath, batchName, find, replace, prefix, suffix, trimStart, trimEnd)
              elif objectType in object.type:
                dataPath = group
                rename(self, dataPath, batchName, find, replace, prefix, suffix, trimStart, trimEnd)
        else:
          for group in object.vertex_groups[:]:

            # object type
            if objectType in 'ALL':
              dataPath = group

              # rename
              rename(self, dataPath, batchName, find, replace, prefix, suffix, trimStart, trimEnd)
            elif objectType in object.type:
              dataPath = group
              rename(self, dataPath, batchName, find, replace, prefix, suffix, trimStart, trimEnd)

  # batch shape keys
  if batchShapeKeys:
    for object in bpy.data.objects[:]:
      if object.type in {'MESH', 'CURVE', 'SURFACE', 'LATTICE'}:
        if object.data.shape_keys:

          # batch type
          if batchType in 'SELECTED':
            if object.select:
              for key in object.data.shape_keys.key_blocks[:]:

                # object type
                if objectType in 'ALL':
                  dataPath = key

                  # rename
                  rename(self, dataPath, batchName, find, replace, prefix, suffix, trimStart, trimEnd)
                elif objectType in object.type:
                  dataPath = key
                  rename(self, dataPath, batchName, find, replace, prefix, suffix, trimStart, trimEnd)
          else:
            for key in object.data.shape_keys.key_blocks[:]:

              # object type
              if objectType in 'ALL':
                dataPath = key

                # rename
                rename(self, dataPath, batchName, find, replace, prefix, suffix, trimStart, trimEnd)
              elif objectType in object.type:
                dataPath = key
                rename(self, dataPath, batchName, find, replace, prefix, suffix, trimStart, trimEnd)


  # batch uv maps
  if batchUVS:
    for object in bpy.data.objects[:]:
      if object.type in 'MESH':

        # batch type
        if batchType in 'SELECTED':
          if object.select:
            for uv in object.data.uv_textures[:]:

              # object type
              if objectType in 'ALL':
                dataPath = uv

                # rename
                rename(self, dataPath, batchName, find, replace, prefix, suffix, trimStart, trimEnd)
              elif objectType in object.type:
                dataPath = uv
                rename(self, dataPath, batchName, find, replace, prefix, suffix, trimStart, trimEnd)
        else:
         for uv in object.data.uv_textures[:]:

            # object type
            if objectType in 'ALL':
              dataPath = uv

              # rename
              rename(self, dataPath, batchName, find, replace, prefix, suffix, trimStart, trimEnd)
            elif objectType in object.type:
              dataPath = uv
              rename(self, dataPath, batchName, find, replace, prefix, suffix, trimStart, trimEnd)

  # batch vertex colors
  if batchVertexColors:
    for object in bpy.data.objects[:]:
      if object.type in 'MESH':

        # batch type
        if batchType in 'SELECTED':
          if object.select:
            for vertexColor in object.data.vertex_colors[:]:

              # object type
              if objectType in 'ALL':
                dataPath = vertexColor

                # rename
                rename(self, dataPath, batchName, find, replace, prefix, suffix, trimStart, trimEnd)
              elif objectType in object.type:
                dataPath = vertexColor
                rename(self, dataPath, batchName, find, replace, prefix, suffix, trimStart, trimEnd)
        else:
          for vertexColor in object.data.vertex_colors[:]:

            # object type
            if objectType in 'ALL':
              dataPath = vertexColor

              # rename
              rename(self, dataPath, batchName, find, replace, prefix, suffix, trimStart, trimEnd)
            elif objectType in object.type:
              dataPath = vertexColor
              rename(self, dataPath, batchName, find, replace, prefix, suffix, trimStart, trimEnd)

  # batch bone groups
  if batchBoneGroups:
    for object in bpy.data.objects[:]:

      # batch type
      if batchType in 'SELECTED':
        if object.select:
          if object.type in 'ARMATURE':
            for group in object.pose.bone_groups[:]:
              if object.bone.select:
                dataPath = group

                # rename
                rename(self, dataPath, batchName, find, replace, prefix, suffix, trimStart, trimEnd)
      else:
        if object.type in 'ARMATURE':
          for group in object.pose.bone_groups[:]:
            dataPath = group

            # rename
            rename(self, dataPath, batchName, find, replace, prefix, suffix, trimStart, trimEnd)

# batch copy
def batchNameCopy(self, context, batchType, source, objects, objectData, material, texture, particleSystem, particleSettings, useActiveObject):
  ''' Assign name values from source type to destination data block. '''

  # source object
  if source in 'OBJECT':

    # objects
    if objects:
      for object in bpy.data.objects[:]:
        try:

          # batch type
          if batchType in 'SELECTED':
            if object.select:

              # use active object
              if useActiveObject:
                object.name = context.active_object.name
              else:
                object.name = object.name
          else:

            # use active object
            if useActiveObject:
              object.name = context.active_object.name
            else:
              object.name = object.name
        except:
          pass

    # object data
    if objectData:
      for object in bpy.data.objects[:]:
        try:

          # batch type
          if batchType in 'SELECTED':
            if object.select:

              # use active object
              if useActiveObject:
                object.data.name = context.active_object.name
              else:
                object.data.name = object.name
          else:

            # use active object
            if useActiveObject:
              object.data.name = context.active_object.name
            else:
              object.data.name = object.name
        except:
          pass

    # material
    if material:
      for object in bpy.data.objects[:]:
        try:

          # batch type
          if batchType in 'SELECTED':
            if object.select:
              for material in object.material_slots[:]:
                if material.material != None:

                  # use active object
                  if useActiveObject:
                    material.material.name = context.active_object.name
                  else:
                    material.material.name = object.name
          else:
            for material in object.material_slots[:]:
              if material.material != None:

                # use active object
                if useActiveObject:
                  material.material.name = context.active_object.name
                else:
                  material.material.name = object.name
        except:
          pass

    # texture
    if texture:
      for object in bpy.data.objects[:]:
        try:

          # batch type
          if batchType in 'SELECTED':
            if object.select:
              for material in object.material_slots[:]:
                if material.material != None:
                  for texture in material.material.texture_slots[:]:
                    if texture != None:

                      # use active object
                      if useActiveObject:
                        texture.texture.name = context.active_object.name
                      else:
                        texture.texture.name = object.name
          else:
            for material in object.material_slots[:]:
              if material.material != None:
                for texture in material.material.texture_slots[:]:
                  if texture != None:

                    # use active object
                    if useActiveObject:
                      texture.texture.name = context.active_object.name
                    else:
                      texture.texture.name = object.name
        except:
          pass

    # particle system
    if particleSystem:
      for object in bpy.data.objects[:]:
        try:

          # batch type
          if batchType in 'SELECTED':
            if object.select:
              for system in object.particle_systems[:]:

                # use active object
                if useActiveObject:
                  system.name = context.active_object.name
                else:
                  system.name = object.name
          else:
            for system in object.particle_systems[:]:

              # use active object
              if useActiveObject:
                system.name = context.active_object.name
              else:
                system.name = object.name
        except:
          pass

    # particle settings
    if particleSettings:
      for object in bpy.data.objects[:]:
        try:

          # batch type
          if batchType in 'SELECTED':
            if object.select:
              for system in object.particle_systems[:]:

                # use active object
                if useActiveObject:
                  system.settings.name = context.active_object.name
                else:
                  system.settings.name = object.name
          else:
            for system in object.particle_systems[:]:

              # use active object
              if useActiveObject:
                system.settings.name = context.active_object.name
              else:
                system.settings.name = object.name
        except:
          pass

  # source object data
  if source in 'OBJECT_DATA':

    # objects
    if objects:
      for object in bpy.data.objects[:]:
        try:

          # batch type
          if batchType in 'SELECTED':
            if object.select:

              # use active object
              if useActiveObject:
                object.name = context.active_object.data.name
              else:
                object.name = object.data.name
          else:

            # use active object
            if useActiveObject:
              object.name = context.active_object.data.name
            else:
              object.name = object.data.name
        except:
          pass

    # object data
    if objectData:
      for object in bpy.data.objects[:]:
        try:

          # batch type
          if batchType in 'SELECTED':
            if object.select:

              # use active object
              if useActiveObject:
                object.data.name = context.active_object.data.name
              else:
                object.data.name = object.data.name
          else:

            # use active object
            if useActiveObject:
              object.data.name = context.active_object.data.name
            else:
              object.data.name = object.data.name
        except:
          pass

    # material
    if material:
      for object in bpy.data.objects[:]:
        try:

          # batch type
          if batchType in 'SELECTED':
            if object.select:
              for material in object.material_slots[:]:
                if material.material != None:

                  # use active object
                  if useActiveObject:
                    material.material.name = context.active_object.data.name
                  else:
                    material.material.name = object.data.name
          else:
            for material in object.material_slots[:]:
              if material.material != None:

                # use active object
                if useActiveObject:
                  material.material.name = context.active_object.data.name
                else:
                  material.material.name = object.data.name
        except:
          pass

    # texture
    if texture:
      for object in bpy.data.objects[:]:
        try:

          # batch type
          if batchType in 'SELECTED':
            if object.select:
              for material in object.material_slots[:]:
                if material.material != None:
                  for texture in material.material.texture_slots[:]:
                    if texture != None:

                      # use active object
                      if useActiveObject:
                        texture.texture.name = context.active_object.data.name
                      else:
                        texture.texture.name = object.data.name
          else:
            for material in object.material_slots[:]:
              if material.material != None:
                for texture in material.material.texture_slots[:]:
                  if texture != None:

                    # use active object
                    if useActiveObject:
                      texture.texture.name = context.active_object.data.name
                    else:
                      texture.texture.name = object.data.name
        except:
          pass

    # particle system
    if particleSystem:
      for object in bpy.data.objects[:]:
        try:

          # batch type
          if batchType in 'SELECTED':
            if object.select:
              for system in object.particle_systems[:]:

                # use active object
                if useActiveObject:
                  system.name = context.active_object.data.name
                else:
                  system.name = object.data.name
          else:
            for system in object.particle_systems[:]:

              # use active object
              if useActiveObject:
                system.name = context.active_object.data.name
              else:
                system.name = object.data.name
        except:
          pass

    # particle settings
    if particleSettings:
      for object in bpy.data.objects[:]:
        try:

          # batch type
          if batchType in 'SELECTED':
            if object.select:
              for system in object.particle_systems[:]:

                # use active object
                if useActiveObject:
                  system.settings.name = context.active_object.data.name
                else:
                  system.settings.name = object.data.name
          else:
            for system in object.particle_systems[:]:

              # use active object
              if useActiveObject:
                system.settings.name = context.active_object.data.name
              else:
                system.settings.name = object.data.name
        except:
          pass

  # source material
  if source in 'MATERIAL':

    # objects
    if objects:
      for object in bpy.data.objects[:]:
        try:

          # batch type
          if batchType in 'SELECTED':
            if object.select:

              # use active object
              if useActiveObject:
                object.name = context.active_object.active_material.name
              else:
                object.name = object.active_material.name
          else:

            # use active object
            if useActiveObject:
              object.name = context.active_object.active_material.name
            else:
              object.name = object.active_material.name
        except:
          pass

    # object data
    if objectData:
      for object in bpy.data.objects[:]:
        try:

          # batch type
          if batchType in 'SELECTED':
            if object.select:

              # use active object
              if useActiveObject:
                object.data.name = context.active_object.active_material.name
              else:
                object.data.name = object.active_material.name
          else:

            # use active object
            if useActiveObject:
              object.data.name = context.active_object.active_material.name
            else:
              object.data.name = object.active_material.name
        except:
          pass

    # material
    if material:
      for object in bpy.data.objects[:]:
        try:

          # batch type
          if batchType in 'SELECTED':
            if object.select:
              for material in object.material_slots[:]:
                if material.material != None:

                  # use active object
                  if useActiveObject:
                    material.material.name = context.active_object.active_material.name
                  else:
                    material.material.name = object.active_material.name
          else:
            for material in object.material_slots[:]:
              if material.material != None:

                # use active object
                if useActiveObject:
                  material.material.name = context.active_object.active_material.name
                else:
                  material.material.name = object.active_material.name
        except:
          pass

    # texture
    if texture:
      for object in bpy.data.objects[:]:
        try:

          # batch type
          if batchType in 'SELECTED':
            if object.select:
              for material in object.material_slots[:]:
                if material.material != None:
                  for texture in material.material.texture_slots[:]:
                    if texture != None:

                      # use active object
                      if useActiveObject:
                        texture.texture.name = context.active_object.active_material.name
                      else:
                        texture.texture.name = object.active_material.name
          else:
            for material in object.material_slots[:]:
              if material.material != None:
                for texture in material.material.texture_slots[:]:
                  if texture != None:

                    # use active object
                    if useActiveObject:
                      texture.texture.name = context.active_object.active_material.name
                    else:
                      texture.texture.name = object.active_material.name
        except:
          pass

    # particle system
    if particleSystem:
      for object in bpy.data.objects[:]:
        try:

          # batch type
          if batchType in 'SELECTED':
            if object.select:
              for system in object.particle_systems[:]:

                # use active object
                if useActiveObject:
                  system.name = context.active_object.active_material.name
                else:
                  system.name = object.active_material.name
          else:
            for system in object.particle_systems[:]:

              # use active object
              if useActiveObject:
                system.name = context.active_object.active_material.name
              else:
                system.name = object.active_material.name
        except:
          pass

    # particle settings
    if particleSettings:
      for object in bpy.data.objects[:]:
        try:

          # batch type
          if batchType in 'SELECTED':
            if object.select:
              for system in object.particle_systems[:]:

                # use active object
                if useActiveObject:
                  system.settings.name = context.active_object.active_material.name
                else:
                  system.settings.name = object.active_material.name
          else:
            for system in object.particle_systems[:]:

              # use active object
              if useActiveObject:
                system.settings.name = context.active_object.active_material.name
              else:
                system.settings.name = object.active_material.name
        except:
          pass

  # source texture
  if source in 'TEXTURE':

    # objects
    if objects:
      for object in bpy.data.objects[:]:
        try:

          # batch type
          if batchType in 'SELECTED':
            if object.select:

              # use active object
              if useActiveObject:
                object.name = context.active_object.active_material.active_texture.name
              else:
                object.name = object.active_material.active_texture.name
          else:

            # use active object
            if useActiveObject:
              object.name = context.active_object.active_material.active_texture.name
            else:
              object.name = object.active_material.active_texture.name
        except:
          pass

    # object data
    if objectData:
      for object in bpy.data.objects[:]:
        try:

          # batch type
          if batchType in 'SELECTED':
            if object.select:

              # use active object
              if useActiveObject:
                object.data.name = context.active_object.active_material.active_texture.name
              else:
                object.data.name = object.active_material.active_texture.name
          else:

            # use active object
            if useActiveObject:
              object.data.name = context.active_object.active_material.active_texture.name
            else:
              object.data.name = object.active_material.active_texture.name
        except:
          pass

    # material
    if material:
      for object in bpy.data.objects[:]:
        try:

          # batch type
          if batchType in 'SELECTED':
            if object.select:
              for material in object.material_slots[:]:
                if material.material != None:

                  # use active object
                  if useActiveObject:
                    material.material.name = context.active_object.active_material.active_texture.name
                  else:
                    material.material.name = object.active_material.active_texture.name
          else:
            for material in object.material_slots[:]:
              if material.material != None:

                # use active object
                if useActiveObject:
                  material.material.name = context.active_object.active_material.active_texture.name
                else:
                  material.material.name = object.active_material.active_texture.name
        except:
          pass

    # texture
    if texture:
      for object in bpy.data.objects[:]:
        try:

          # batch type
          if batchType in 'SELECTED':
            if object.select:
              for material in object.material_slots[:]:
                if material.material != None:
                  for texture in material.material.texture_slots[:]:
                    if texture != None:

                      # use active object
                      if useActiveObject:
                        texture.texture.name = context.active_object.active_material.active_texture.name
                      else:
                        texture.texture.name = object.active_material.active_texture.name
          else:
            for material in object.material_slots[:]:
              if material.material != None:
                for texture in material.material.texture_slots[:]:
                  if texture != None:

                    # use active object
                    if useActiveObject:
                      texture.texture.name = context.active_object.active_material.active_texture.name
                    else:
                      texture.texture.name = object.active_material.active_texture.name
        except:
          pass

    # particle system
    if particleSystem:
      for object in bpy.data.objects[:]:
        try:

          # batch type
          if batchType in 'SELECTED':
            if object.select:
              for system in object.particle_systems[:]:

                # use active object
                if useActiveObject:
                  system.name = context.active_object.active_material.active_texture.name
                else:
                  system.name = object.active_material.active_texture.name
          else:
            for system in object.particle_systems[:]:

              # use active object
              if useActiveObject:
                system.name = context.active_object.active_material.active_texture.name
              else:
                system.name = object.active_material.active_texture.name
        except:
          pass

    # particle settings
    if particleSettings:
      for object in bpy.data.objects[:]:
        try:

          # batch type
          if batchType in 'SELECTED':
            if object.select:
              for system in object.particle_systems[:]:

                # use active object
                if useActiveObject:
                  system.settings.name = context.active_object.active_material.active_texture.name
                else:
                  system.settings.name = object.active_material.active_texture.name
          else:
            for system in object.particle_systems[:]:

              # use active object
              if useActiveObject:
                system.settings.name = context.active_object.active_material.active_texture.name
              else:
                system.settings.name = object.active_material.active_texture.name
        except:
          pass

  # source particle system
  if source in 'PARTICLE_SYSTEM':

    # objects
    if objects:
      for object in bpy.data.objects[:]:
        try:

          # batch type
          if batchType in 'SELECTED':
            if object.select:

              # use active object
              if useActiveObject:
                object.name = context.active_object.particle_systems.active.name
              else:
                object.name = object.particle_systems.active.name
          else:

            # use active object
            if useActiveObject:
              object.name = context.active_object.particle_systems.active.name
            else:
              object.name = object.particle_systems.active.name
        except:
          pass

    # object data
    if objectData:
      for object in bpy.data.objects[:]:
        try:

          # batch type
          if batchType in 'SELECTED':
            if object.select:

              # use active object
              if useActiveObject:
                object.data.name = context.active_object.particle_systems.active.name
              else:
                object.data.name = object.particle_systems.active.name
          else:

            # use active object
            if useActiveObject:
              object.data.name = context.active_object.particle_systems.active.name
            else:
              object.data.name = object.particle_systems.active.name
        except:
          pass

    # material
    if material:
      for object in bpy.data.objects[:]:
        try:

          # batch type
          if batchType in 'SELECTED':
            if object.select:
              for material in object.material_slots[:]:
                if material.material != None:

                  # use active object
                  if useActiveObject:
                    material.material.name = context.active_object.particle_systems.active.name
                  else:
                    material.material.name = object.particle_systems.active.name
          else:
            for material in object.material_slots[:]:
              if material.material != None:

                # use active object
                if useActiveObject:
                  material.material.name = context.active_object.particle_systems.active.name
                else:
                  material.material.name = object.particle_systems.active.name
        except:
          pass

    # texture
    if texture:
      for object in bpy.data.objects[:]:
        try:

          # batch type
          if batchType in 'SELECTED':
            if object.select:
              for material in object.material_slots[:]:
                if material.material != None:
                  for texture in material.material.texture_slots[:]:
                    if texture != None:

                      # use active object
                      if useActiveObject:
                        texture.texture.name = context.active_object.particle_systems.active.name
                      else:
                        texture.texture.name = object.particle_systems.active.name
          else:
            for material in object.material_slots[:]:
              if material.material != None:
                for texture in material.material.texture_slots[:]:
                  if texture != None:

                    # use active object
                    if useActiveObject:
                      texture.texture.name = context.active_object.particle_systems.active.name
                    else:
                      texture.texture.name = object.particle_systems.active.name
        except:
          pass

    # particle system
    if particleSystem:
      for object in bpy.data.objects[:]:
        try:

          # batch type
          if batchType in 'SELECTED':
            if object.select:
              for system in object.particle_systems[:]:

                # use active object
                if useActiveObject:
                  system.name = context.active_object.particle_systems.active.name
                else:
                  system.name = object.particle_systems.active.name
          else:
            for system in object.particle_systems[:]:

              # use active object
              if useActiveObject:
                system.name = context.active_object.particle_systems.active.name
              else:
                system.name = object.particle_systems.active.name
        except:
          pass

    # particle settings
    if particleSettings:
      for object in bpy.data.objects[:]:
        try:

          # batch type
          if batchType in 'SELECTED':
            if object.select:
              for system in object.particle_systems[:]:

                # use active object
                if useActiveObject:
                  system.settings.name = context.active_object.particle_systems.active.name
                else:
                  system.settings.name = object.particle_systems.active.name
          else:
            for system in object.particle_systems[:]:

              # use active object
              if useActiveObject:
                system.settings.name = context.active_object.particle_systems.active.name
              else:
                system.settings.name = object.particle_systems.active.name
        except:
          pass

  # source particle settings
  if source in 'PARTICLE_SETTINGS':

    # objects
    if objects:
      for object in bpy.data.objects[:]:
        try:

          # batch type
          if batchType in 'SELECTED':
            if object.select:

              # use active object
              if useActiveObject:
                object.name = context.active_object.particle_systems.active.settings.name
              else:
                object.name = object.particle_systems.active.settings.name
          else:

            # use active object
            if useActiveObject:
              object.name = context.active_object.particle_systems.active.settings.name
            else:
              object.name = object.particle_systems.active.settings.name
        except:
          pass

    # object data
    if objectData:
      for object in bpy.data.objects[:]:
        try:

          # batch type
          if batchType in 'SELECTED':
            if object.select:

              # use active object
              if useActiveObject:
                object.data.name = context.active_object.particle_systems.active.settings.name
              else:
                object.data.name = object.particle_systems.active.settings.name
          else:

            # use active object
            if useActiveObject:
              object.data.name = context.active_object.particle_systems.active.settings.name
            else:
              object.data.name = object.particle_systems.active.settings.name
        except:
          pass

    # material
    if material:
      for object in bpy.data.objects[:]:
        try:

          # batch type
          if batchType in 'SELECTED':
            if object.select:
              for material in object.material_slots[:]:
                if material.material != None:

                  # use active object
                  if useActiveObject:
                    material.material.name = context.active_object.particle_systems.active.settings.name
                  else:
                    material.material.name = object.particle_systems.active.settings.name
          else:
            for material in object.material_slots[:]:
              if material.material != None:

                # use active object
                if useActiveObject:
                  material.material.name = context.active_object.particle_systems.active.settings.name
                else:
                  material.material.name = object.particle_systems.active.settings.name
        except:
          pass

    # texture
    if texture:
      for object in bpy.data.objects[:]:
        try:

          # batch type
          if batchType in 'SELECTED':
            if object.select:
              for material in object.material_slots[:]:
                if material.material != None:
                  for texture in material.material.texture_slots[:]:
                    if texture != None:

                      # use active object
                      if useActiveObject:
                        texture.texture.name = context.active_object.particle_systems.active.settings.name
                      else:
                        texture.texture.name = object.particle_systems.active.settings.name
          else:
            for material in object.material_slots[:]:
              if material.material != None:
                for texture in material.material.texture_slots[:]:
                  if texture != None:

                    # use active object
                    if useActiveObject:
                      texture.texture.name = context.active_object.particle_systems.active.settings.name
                    else:
                      texture.texture.name = object.particle_systems.active.settings.name
        except:
          pass

    # particle system
    if particleSystem:
      for object in bpy.data.objects[:]:
        try:

          # batch type
          if batchType in 'SELECTED':
            if object.select:
              for system in object.particle_systems[:]:

                # use active object
                if useActiveObject:
                  system.name = context.active_object.particle_systems.active.settings.name
                else:
                  system.name = object.particle_systems.active.settings.name
          else:
            for system in object.particle_systems[:]:

              # use active object
              if useActiveObject:
                system.name = context.active_object.particle_systems.active.settings.name
              else:
                system.name = object.particle_systems.active.settings.name
        except:
          pass

    # particle settings
    if particleSettings:
      for object in bpy.data.objects[:]:
        try:

          # batch type
          if batchType in 'SELECTED':
            if object.select:
              for system in object.particle_systems[:]:

                # use active object
                if useActiveObject:
                  system.settings.name = context.active_object.particle_systems.active.settings.name
                else:
                  system.settings.name = object.particle_systems.active.settings.name
          else:
            for system in object.particle_systems[:]:

              # use active object
              if useActiveObject:
                system.settings.name = context.active_object.particle_systems.active.settings.name
              else:
                system.settings.name = object.particle_systems.active.settings.name
        except:
          pass

# reset options
def resetBatchProperties(self, context):
  ''' Resets the window manager property values for item panel add-on. '''

  # batch naming
  # batch type
  context.window_manager.batchNamingUI.batchType = 'GLOBAL'

  # batch objects
  context.window_manager.batchNamingUI.batchObjects = False

  # batch object constraints
  context.window_manager.batchNamingUI.batchObjectConstraints = False

  # batch modifiers
  context.window_manager.batchNamingUI.batchModifiers = False

  # batch object data
  context.window_manager.batchNamingUI.batchObjectData = False

  # batch bones
  context.window_manager.batchNamingUI.batchBones = False

  # batch bone constraints
  context.window_manager.batchNamingUI.batchBoneConstraints = False

  # batch materials
  context.window_manager.batchNamingUI.batchMaterials = False

  # batch textures
  context.window_manager.batchNamingUI.batchTextures = False

  # batch particle systems
  context.window_manager.batchNamingUI.batchParticleSystems = False

  # batch particle settings
  context.window_manager.batchNamingUI.batchParticleSettings = False

  # batch groups
  context.window_manager.batchNamingUI.batchGroups = False

  # batch vertex groups
  context.window_manager.batchNamingUI.batchVertexGroups = False

  # batch shape keys
  context.window_manager.batchNamingUI.batchShapeKeys = False

  # batch uvs
  context.window_manager.batchNamingUI.batchUVS = False

  # batch vertex colors
  context.window_manager.batchNamingUI.batchVertexColors = False

  # batch bone groups
  context.window_manager.batchNamingUI.batchBoneGroups = False

  # object type
  context.window_manager.batchNamingUI.objectType = 'ALL'

  # constraint type
  context.window_manager.batchNamingUI.constraintType = 'ALL'

  # modifier type
  context.window_manager.batchNamingUI.modifierType = 'ALL'

  # name
  context.window_manager.batchNamingUI.batchName = ''

  # find
  context.window_manager.batchNamingUI.find = ''

  # replace
  context.window_manager.batchNamingUI.replace = ''

  # prefix
  context.window_manager.batchNamingUI.prefix = ''

  # suffix
  context.window_manager.batchNamingUI.suffix = ''

  # trim start
  context.window_manager.batchNamingUI.trimStart = 0

  # trim end
  context.window_manager.batchNamingUI.trimEnd = 0

  # batch name copy
  # batch type
  context.window_manager.batchNameCopyUI.batchType = 'GLOBAL'

  # source
  context.window_manager.batchNameCopyUI.source = 'OBJECT'

  # objects
  context.window_manager.batchNameCopyUI.objects = False

  # object data
  context.window_manager.batchNameCopyUI.objectData = False

  # material
  context.window_manager.batchNameCopyUI.material = False

  # texture
  context.window_manager.batchNameCopyUI.texture = False

  # particle system
  context.window_manager.batchNameCopyUI.particleSystem = False

  # particle settings
  context.window_manager.batchNameCopyUI.particleSettings = False

  # use active object
  context.window_manager.batchNameCopyUI.useActiveObject = False

# modifier icon
def modifierIcon(modifier):
  ''' Returns a icon based on modifier type. '''

  # data transfer
  if modifier.type in 'DATA_TRANSFER':
    icon = 'MOD_DATA_TRANSFER'

  # mesh cache
  elif modifier.type in 'MESH_CACHE':
    icon = 'MOD_MESHDEFORM'

  # normal edit
  elif modifier.type in 'NORMAL_EDIT':
    icon = 'MOD_NORMALEDIT'

  # uv project
  elif modifier.type in 'UV_PROJECT':
    icon = 'MOD_UVPROJECT'

  # uv warp
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

  # build
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

  # fluid simulation
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
  ''' Returns a icon based on object type. '''

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
  ''' Returns a icon based on object type. '''

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

#####################
## PROPERTY GROUPS ##
#####################

# batch UI
class batchNamingUI(PropertyGroup):
  ''' Properties that effect how the batch naming operation is performed. '''

  # batch type
  batchType = EnumProperty(
    name = 'Batch Type:',
    description = 'Effect all or only selected objects.',
    items = [
      ('GLOBAL', 'Global', 'Batch naming will effect all objects.'),
      ('SELECTED', 'Selected', 'Batch naming will only effect the objects within the current selection.')
    ],
    default = 'GLOBAL'
  )

  # batch objects
  batchObjects = BoolProperty(
    name = 'Objects',
    description = 'Apply batch naming to object names.',
    default = False
  )

  # batch object constraints
  batchObjectConstraints = BoolProperty(
    name = 'Object Constraints',
    description = 'Apply batch naming to the constraints.',
    default = False
  )

  # batch modifiers
  batchModifiers = BoolProperty(
    name = 'Modifiers',
    description = 'Apply batch naaming to the modifiers.',
    default = False
  )

  # batch object data
  batchObjectData = BoolProperty(
    name = 'Object Data',
    description = 'Apply batch naming to the object data.',
    default = False
  )

  # batch bones
  batchBones = BoolProperty(
    name = 'Bones',
    description = 'Apply batch naming to bones.',
    default = False
  )

  # batch bone constraints
  batchBoneConstraints = BoolProperty(
    name = 'Bone Constraints',
    description = 'Apply batch naming to bone constraints.',
    default = False
  )

  # batch materials
  batchMaterials = BoolProperty(
    name = 'Materials',
    description = 'Apply batch naming to the materials.',
    default = False
  )

  # batch textures
  batchTextures = BoolProperty(
    name = 'Textures',
    description = 'Apply batch naming to the material textures.',
    default = False
  )

  # batch particle systems
  batchParticleSystems = BoolProperty(
    name = 'Particle Systems',
    description = 'Apply batch naming to the particle systems.',
    default = False
  )

  # batch particle settings
  batchParticleSettings = BoolProperty(
    name = 'Particle Settings',
    description = 'Apply batch naming to the settings of the particle systems.',
    default = False
  )

  # batch groups
  batchGroups = BoolProperty(
    name = 'Groups',
    description = 'Apply batch naming to the groups the objects are within.',
    default = False
  )

  # batch vertex groups
  batchVertexGroups = BoolProperty(
    name = 'Vertex Groups',
    description = 'Apply batch naming to the vertex groups of the objects.',
    default = False
  )

  # batch shape keys
  batchShapeKeys = BoolProperty(
    name = 'Shape Keys',
    description = 'Apply batch naming to the shape keys of the objects.',
    default = False
  )

  # batch uvs
  batchUVS = BoolProperty(
    name = 'UV Maps',
    description = 'Apply batch naming to the UV maps of the the objects.',
    default = False
  )

  # batch vertex colors
  batchVertexColors = BoolProperty(
    name = 'Vertex Colors',
    description = 'Apply batch naming to the vertex colors of the objects.',
    default = False
  )

  # batch bone groups
  batchBoneGroups = BoolProperty(
    name = 'Bone Groups',
    description = 'Apply batch naming to the bone groups the armature bones are apart of.',
    default = False
  )

  # object type
  objectType = EnumProperty(
    name = 'Type',
    description = 'The type of object that the batch naming operations will be performed on.',
    items = [
      ('ALL', 'All Objects', '', 'OBJECT_DATA', 0),
      ('MESH', 'Mesh', '', 'OUTLINER_OB_MESH', 1),
      ('CURVE', 'Curve', '', 'OUTLINER_OB_CURVE', 2),
      ('SURFACE', 'Surface', '', 'OUTLINER_OB_SURFACE', 3),
      ('META', 'Meta', '', 'OUTLINER_OB_META', 4),
      ('FONT', 'Font', '', 'OUTLINER_OB_FONT', 5),
      ('ARMATURE', 'Armature', '', 'OUTLINER_OB_ARMATURE', 6),
      ('LATTICE', 'Lattice', '', 'OUTLINER_OB_LATTICE', 7),
      ('EMPTY', 'Empty', '', 'OUTLINER_OB_EMPTY', 8),
      ('SPEAKER', 'Speaker', '', 'OUTLINER_OB_SPEAKER', 9),
      ('CAMERA', 'Camera', '', 'OUTLINER_OB_CAMERA', 10),
      ('LAMP', 'Lamp', '', 'OUTLINER_OB_LAMP', 11)
    ],
    default = 'ALL'
  )

  # constraint type
  constraintType = EnumProperty(
    name = 'Type',
    description = 'The type of constraint that the batch naming operations will be performed on.',
    items = [
      ('ALL', 'All Constraints', '', 'CONSTRAINT', 0),
      ('CAMERA_SOLVER', 'Camera Solver', '', 'CONSTRAINT_DATA', 1),
      ('FOLLOW_TRACK', 'Follow Track', '', 'CONSTRAINT_DATA', 2),
      ('OBJECT_SOLVER', 'Object Solver', '', 'CONSTRAINT_DATA', 3),
      ('COPY_LOCATION', 'Copy Location', '', 'CONSTRAINT_DATA', 4),
      ('COPY_ROTATION', 'Copy Rotation', '', 'CONSTRAINT_DATA', 5),
      ('COPY_SCALE', 'Copy Scale', '', 'CONSTRAINT_DATA', 6),
      ('COPY_TRANSFORMS', 'Copy Transforms', '', 'CONSTRAINT_DATA', 7),
      ('LIMIT_DISTANCE', 'Limit Distance', '', 'CONSTRAINT_DATA', 8),
      ('LIMIT_LOCATION', 'Limit Location', '', 'CONSTRAINT_DATA', 9),
      ('LIMIT_ROTATION', 'Limit Rotation', '', 'CONSTRAINT_DATA', 10),
      ('LIMIT_SCALE', 'Limit Scale', '', 'CONSTRAINT_DATA', 11),
      ('MAINTAIN_VOLUME', 'Maintain Volume', '', 'CONSTRAINT_DATA', 12),
      ('TRANSFORM', 'Transformation', '', 'CONSTRAINT_DATA', 13),
      ('CLAMP_TO', 'Clamp To', '', 'CONSTRAINT_DATA', 14),
      ('DAMPED_TRACK', 'Damped Track', '', 'CONSTRAINT_DATA', 15),
      ('IK', 'Inverse Kinematics', '', 'CONSTRAINT_DATA', 16),
      ('LOCKED_TRACK', 'Locked Track', '', 'CONSTRAINT_DATA', 17),
      ('SPLINE_IK', 'Spline IK', '', 'CONSTRAINT_DATA', 18),
      ('STRETCH_TO', 'Stretch To', '', 'CONSTRAINT_DATA', 19),
      ('TRACK_TO', 'Track To', '', 'CONSTRAINT_DATA', 20),
      ('ACTION', 'Action', '', 'CONSTRAINT_DATA', 21),
      ('CHILD_OF', 'Child Of', '', 'CONSTRAINT_DATA', 22),
      ('FLOOR', 'Floor', '', 'CONSTRAINT_DATA', 23),
      ('FOLLOW_PATH', 'Follow Path', '', 'CONSTRAINT_DATA', 24),
      ('PIVOT', 'Pivot', '', 'CONSTRAINT_DATA', 25),
      ('RIGID_BODY_JOINT', 'Rigid Body Joint', '', 'CONSTRAINT_DATA', 26),
      ('SHRINKWRAP', 'Shrinkwrap', '', 'CONSTRAINT_DATA', 27)
    ],
    default = 'ALL'
  )

  # modifier type
  modifierType = EnumProperty(
    name = 'Type',
    description = 'The type of modifier that the batch naming operations will be performed on.',
    items = [
      ('ALL', 'All Modifiers', '', 'MODIFIER', 0),
      ('DATA_TRANSFER', 'Mesh Cache', '', 'MOD_DATA_TRANSFER', 1),
      ('MESH_CACHE', 'Mesh Cache', '', 'MOD_MESHDEFORM', 2),
      ('NORMAL_EDIT', 'Normal Edit', '', 'MOD_NORMALEDIT', 3),
      ('UV_PROJECT', 'UV Project', '', 'MOD_UVPROJECT', 4),
      ('UV_WARP', 'UV Warp', '', 'MOD_UVPROJECT', 5),
      ('VERTEX_WEIGHT_EDIT', 'Vertex Weight Edit', '', 'MOD_VERTEX_WEIGHT', 6),
      ('VERTEX_WEIGHT_MIX', 'Vertex Weight Mix', '', 'MOD_VERTEX_WEIGHT', 7),
      ('VERTEX_WEIGHT_PROXIMITY', 'Vertex Weight Proximity', '', 'MOD_VERTEX_WEIGHT', 8),
      ('ARRAY', 'Array', '', 'MOD_ARRAY', 9),
      ('BEVEL', 'Bevel', '', 'MOD_BEVEL', 10),
      ('BOOLEAN', 'Boolean', '', 'MOD_BOOLEAN', 11),
      ('BUILD', 'Build', '', 'MOD_BUILD', 12),
      ('DECIMATE', 'Decimate', '', 'MOD_DECIM', 13),
      ('EDGE_SPLIT', 'Edge Split', '', 'MOD_EDGESPLIT', 14),
      ('MASK', 'Mask', '', 'MOD_MASK', 15),
      ('MIRROR', 'Mirror', '', 'MOD_MIRROR', 16),
      ('MULTIRES', 'Multiresolution', '', 'MOD_MULTIRES', 17),
      ('REMESH', 'Remesh', '', 'MOD_REMESH', 18),
      ('SCREW', 'Screw', '', 'MOD_SCREW', 19),
      ('SKIN', 'Skin', '', 'MOD_SKIN', 20),
      ('SOLIDIFY', 'Solidify', '', 'MOD_SOLIDIFY', 21),
      ('SUBSURF', 'Subdivision Surface', '', 'MOD_SUBSURF', 22),
      ('TRIANGULATE', 'Triangulate', '', 'MOD_TRIANGULATE', 23),
      ('WIREFRAME', 'Wireframe', '', 'MOD_WIREFRAME', 24),
      ('ARMATURE', 'Armature', '', 'MOD_ARMATURE', 25),
      ('CAST', 'Cast', '', 'MOD_CAST', 26),
      ('CORRECTIVE_SMOOTH', 'Corrective Smooth', '', 'MOD_SMOOTH', 27),
      ('CURVE', 'Curve', '', 'MOD_CURVE', 28),
      ('DISPLACE', 'Displace', '', 'MOD_DISPLACE', 29),
      ('HOOK', 'Hook', '', 'HOOK', 30),
      ('LAPLACIANSMOOTH', 'Laplacian Smooth', '', 'MOD_SMOOTH', 31),
      ('LAPLACIANDEFORM', 'Laplacian Deform', '', 'MOD_MESHDEFORM', 32),
      ('LATTICE', 'Lattice', '', 'MOD_LATTICE', 33),
      ('MESH_DEFORM', 'Mesh Deform', '', 'MOD_MESHDEFORM', 34),
      ('SHRINKWRAP', 'Shrinkwrap', '', 'MOD_SHRINKWRAP', 35),
      ('SIMPLE_DEFORM', 'Simple Deform', '', 'MOD_SIMPLEDEFORM', 36),
      ('SMOOTH', 'Smooth', '', 'MOD_SMOOTH', 37),
      ('WARP', 'Warp', '', 'MOD_WARP', 38),
      ('WAVE', 'Wave', '', 'MOD_WAVE', 39),
      ('CLOTH', 'Cloth', '', 'MOD_CLOTH', 40),
      ('COLLISION', 'Collision', '', 'MOD_PHYSICS', 41),
      ('DYNAMIC_PAINT', 'Dynamic Paint', '', 'MOD_DYNAMICPAINT', 42),
      ('EXPLODE', 'Explode', '', 'MOD_EXPLODE', 43),
      ('FLUID_SIMULATION', 'Fluid Simulation', '', 'MOD_FLUIDSIM', 44),
      ('OCEAN', 'Ocean', '', 'MOD_OCEAN', 45),
      ('PARTICLE_INSTANCE', 'Particle Instance', '', 'MOD_PARTICLES', 46),
      ('PARTICLE_SYSTEM', 'Particle System', '', 'MOD_PARTICLES', 47),
      ('SMOKE', 'Smoke', '', 'MOD_SMOKE', 48),
      ('SOFT_BODY', 'Soft Body', '', 'MOD_SOFT', 49)
    ],
    default = 'ALL'
  )

  # name
  batchName = StringProperty(
    name = 'Name',
    description = 'Designate a new name, if blank, the current names are effected by any changes to the parameters below.'
  )

  # find
  find = StringProperty(
    name = 'Find',
    description = 'Find this text and remove it from the names. Evaluated as a python regular expression, must escape any RE metacharacters when applicable with \\ before character, ie; \\.'
  )

  # replace
  replace = StringProperty(
    name = 'Replace',
    description = 'Replace found text within the names with the text entered here.'
  )

  # prefix
  prefix = StringProperty(
    name = 'Prefix',
    description = 'Designate a prefix to use for the names.'
  )

  # suffix
  suffix = StringProperty(
    name = 'Suffix',
    description = 'Designate a suffix to use for the names'
  )

  # trim start
  trimStart = IntProperty(
    name = 'Trim Start',
    description = 'Trim the beginning of the names by this amount.',
    min = 0,
    max = 50,
    default = 0
  )

  # trim end
  trimEnd = IntProperty(
    name = 'Trim End',
    description = 'Trim the ending of the names by this amount.',
    min = 0,
    max = 50,
    default = 0
  )

# batch copy UI
class batchNameCopyUI(PropertyGroup):
  ''' Properties that effect how the batch copy operation is performed. '''

  # batch type
  batchType = EnumProperty(
    name = 'Batch Type',
    description = 'Effect all or only selected objects.',
    items = [
      ('GLOBAL', 'Global', 'Batch copy will effect all objects.'),
      ('SELECTED', 'Selected', 'Batch copy will only effect the objects within the current selection.')
    ],
    default = 'GLOBAL'
  )

  # source
  source = EnumProperty(
    name = 'Source',
    description = 'Type of data block to copy the name from.',
    items = [
      ('OBJECT', 'Object', 'Use the name of the object as the source.', 'OBJECT_DATA', 0),
      ('OBJECT_DATA', 'Object Data', 'Use the name of the object\'s data as the source.', 'MESH_DATA', 1),
      ('MATERIAL', 'Material', 'Use the name from the active material of the object as the source.', 'MATERIAL', 2),
      ('TEXTURE', 'Texture', 'Use the name from the active material\'s active texture of the object as the source.', 'TEXTURE', 3),
      ('PARTICLE_SYSTEM', 'Particle System', 'Use the name from the active particle system of the object as the source.', 'PARTICLES', 4),
      ('PARTICLE_SETTINGS', 'Particle Settings', 'Use the name from the active particle system\'s settings of the object as the source.', 'MOD_PARTICLES', 5),
    ],
    default = 'OBJECT'
  )

  # objects
  objects = BoolProperty(
    name = 'Object',
    description = 'Use the source data block to change the object name.',
    default = False
  )

  # object data
  objectData = BoolProperty(
    name = 'Object Data',
    description = 'Use the source data block to change the object data name.',
    default = False
  )

  # material
  material = BoolProperty(
    name = 'Material',
    description = 'Use the source data block to change the object material name.',
    default = False
  )

  # texture
  texture = BoolProperty(
    name = 'Texture',
    description = 'Use the source data block to change the object\'s material texture name.',
    default = False
  )

  # particle system
  particleSystem = BoolProperty(
    name = 'Particle System',
    description = 'Use the source data block to change the object particle system name.',
    default = False
  )

  # particle settings
  particleSettings = BoolProperty(
    name = 'Particle Settings',
    description = 'Use the source data block to change the object particle system settings name.',
    default = False
  )

  # use active object
  useActiveObject = BoolProperty(
    name = 'Use active object',
    description = 'Copy source names from the active object to the other objects.',
    default = False
  )

# item UI
class itemPanelUI(PropertyGroup):
  ''' Properties that effect how item panel displays the item(s) within the users current selection. '''

  # view hierarchy
  viewHierarchy = BoolProperty(
    name = 'View all selected',
    description = 'Display everything within your current selection inside the item panel.',
    default = False
  )

  # view filters
  viewFilters = BoolProperty(
    name = 'Data block filters',
    description = 'Display filters for the item panel.',
    default = False
  )

  # view constraints
  viewConstraints = BoolProperty(
    name = 'View object constraints',
    description = 'Display the object constraints.',
    default = False
  )

  # view modifiers
  viewModifiers = BoolProperty(
    name = 'View object modifiers',
    description = 'Display the object modifiers.',
    default = False
  )

  # view bone constraints
  viewBoneConstraints = BoolProperty(
    name = 'View bone constraints',
    description = 'Display the bone constraints.',
    default = False
  )

  # view materials
  viewMaterials = BoolProperty(
    name = 'View object materials',
    description = 'Display the object materials.',
    default = False
  )

  # view textures
  viewTextures = BoolProperty(
    name = 'View material textures.',
    description = 'Display the textures of the object\'s material(s).',
    default = False
  )

  # view particle systems
  viewParticleSystems = BoolProperty(
    name = 'View particle systems',
    description = 'Display the particle systems and settings for the object below the particle system modifier.',
    default = False
  )

  # view groups
  viewGroups = BoolProperty(
    name = 'View groups',
    description = 'Display the groups the selected object is apart of.',
    default = False
  )

  # view vertex groups
  viewVertexGroups = BoolProperty(
    name = 'View vertex groups',
    description = 'Display the objects vertex groups.',
    default = False
  )

  # view shape keys
  viewShapeKeys = BoolProperty(
    name = 'View shapekeys',
    description = 'Display the objects shapekeys.',
    default = False
  )

  # view uvs
  viewUVS = BoolProperty(
    name = 'View UV\'s',
    description = 'Display the mesh objects UV\'s.',
    default = False
  )

  # view vertex colors
  viewVertexColors = BoolProperty(
    name = 'View vertex colors',
    description = 'Display the vertex colors.',
    default = False
  )

  # view bone groups
  viewBoneGroups = BoolProperty(
    name = 'View bone groups',
    description = 'Display bone groups.',
    default = False
  )

  # view selected bones
  viewSelectedBones = BoolProperty(
    name = 'View selected bones',
    description = 'Display selected bones.',
    default = False
  )

###############
## OPERATORS ##
###############

# reset batch options
class VIEW3D_OT_reset_batch_options(Operator):
  ''' Reset batch operators. '''
  bl_idname = 'view3d.reset_batch_options'
  bl_label = 'Reset Batch Properties'
  bl_option = {'REGISTER', 'UNDO'}

  # poll
  @classmethod
  def poll(cls, context):
    ''' Space data type must be in 3D view. '''
    return context.space_data.type in 'VIEW_3D'

  # execute
  def execute(self, context):
    ''' Execute the operator. '''
    resetBatchProperties(self, context)
    return {'FINISHED'}

# batch naming
class VIEW3D_OT_batch_naming(Operator):
  ''' Batch rename data blocks. '''
  bl_idname = 'view3d.batch_naming'
  bl_label = 'Batch Naming'
  bl_options = {'REGISTER', 'UNDO'}

  # poll
  @classmethod
  def poll(cls, context):
    ''' Space data type must be in 3D view. '''
    return context.space_data.type in 'VIEW_3D'

  # draw
  def draw(self, context):
    ''' Operator body. '''
    layout = self.layout

    # batch type
    layout.prop(context.window_manager.batchNamingUI, 'batchType', expand=True)
    column = layout.column(align=True)
    split = column.split(align=True)

    # type rows
    split.prop(context.window_manager.batchNamingUI, 'batchObjects', text='', icon='OBJECT_DATA')
    split.prop(context.window_manager.batchNamingUI, 'batchObjectConstraints', text='', icon='CONSTRAINT')
    split.prop(context.window_manager.batchNamingUI, 'batchModifiers', text='', icon='MODIFIER')
    split.prop(context.window_manager.batchNamingUI, 'batchObjectData', text='', icon='MESH_DATA')
    split.prop(context.window_manager.batchNamingUI, 'batchBones', text='', icon='BONE_DATA')
    split.prop(context.window_manager.batchNamingUI, 'batchBoneConstraints', text='', icon='CONSTRAINT_BONE')
    split.prop(context.window_manager.batchNamingUI, 'batchMaterials', text='', icon='MATERIAL')
    split.prop(context.window_manager.batchNamingUI, 'batchTextures', text='', icon='TEXTURE')
    split.prop(context.window_manager.batchNamingUI, 'batchParticleSystems', text='', icon='PARTICLES')
    split.prop(context.window_manager.batchNamingUI, 'batchParticleSettings', text='', icon='MOD_PARTICLES')
    split = column.split(align=True)
    split.prop(context.window_manager.batchNamingUI, 'batchGroups', text='', icon='GROUP')
    split.prop(context.window_manager.batchNamingUI, 'batchVertexGroups', text='', icon='GROUP_VERTEX')
    split.prop(context.window_manager.batchNamingUI, 'batchShapeKeys', text='', icon='SHAPEKEY_DATA')
    split.prop(context.window_manager.batchNamingUI, 'batchUVS', text='', icon='GROUP_UVS')
    split.prop(context.window_manager.batchNamingUI, 'batchVertexColors', text='', icon='GROUP_VCOL')
    split.prop(context.window_manager.batchNamingUI, 'batchBoneGroups', text='', icon='GROUP_BONE')
    column = layout.column()

    # type filters
    column.prop(context.window_manager.batchNamingUI, 'objectType', text='')
    column.prop(context.window_manager.batchNamingUI, 'constraintType', text='')
    column.prop(context.window_manager.batchNamingUI, 'modifierType', text='')
    column.separator()

    # input fields
    column.prop(context.window_manager.batchNamingUI, 'batchName')
    column.separator()
    column.prop(context.window_manager.batchNamingUI, 'find', icon='VIEWZOOM')
    column.separator()
    column.prop(context.window_manager.batchNamingUI, 'replace', icon='FILE_REFRESH')
    column.separator()
    column.prop(context.window_manager.batchNamingUI, 'prefix', icon='LOOP_BACK')
    column.separator()
    column.prop(context.window_manager.batchNamingUI, 'suffix', icon='LOOP_FORWARDS')
    column.separator()
    row = column.row()
    row.label(text='Trim Start:')
    row.prop(context.window_manager.batchNamingUI, 'trimStart', text='')
    row = column.row()
    row.label(text='Trim End:')
    row.prop(context.window_manager.batchNamingUI, 'trimEnd', text='')

  # execute
  def execute(self, context):
    ''' Execute the operator. '''
    batchRename(self, context, context.window_manager.batchNamingUI.batchType, context.window_manager.batchNamingUI.batchObjects, context.window_manager.batchNamingUI.batchObjectConstraints, context.window_manager.batchNamingUI.batchModifiers, context.window_manager.batchNamingUI.batchObjectData, context.window_manager.batchNamingUI.batchBones, context.window_manager.batchNamingUI.batchBoneConstraints, context.window_manager.batchNamingUI.batchMaterials, context.window_manager.batchNamingUI.batchTextures, context.window_manager.batchNamingUI.batchParticleSystems, context.window_manager.batchNamingUI.batchParticleSettings, context.window_manager.batchNamingUI.batchGroups, context.window_manager.batchNamingUI.batchVertexGroups, context.window_manager.batchNamingUI.batchShapeKeys, context.window_manager.batchNamingUI.batchUVS, context.window_manager.batchNamingUI.batchVertexColors, context.window_manager.batchNamingUI.batchBoneGroups, context.window_manager.batchNamingUI.objectType, context.window_manager.batchNamingUI.constraintType, context.window_manager.batchNamingUI.modifierType, context.window_manager.batchNamingUI.batchName, context.window_manager.batchNamingUI.find, context.window_manager.batchNamingUI.replace, context.window_manager.batchNamingUI.prefix, context.window_manager.batchNamingUI.suffix, context.window_manager.batchNamingUI.trimStart, context.window_manager.batchNamingUI.trimEnd)
    return {'FINISHED'}

  # invoke
  def invoke(self, context, event):
    ''' Invoke the operator panel/menu, control its width. '''
    context.window_manager.invoke_props_dialog(self, width=233)
    return {'RUNNING_MODAL'}

# batch copy
class VIEW3D_OT_batch_name_copy(Operator):
  ''' Copy names from some types of data blocks to others. '''
  bl_idname = 'view3d.batch_name_copy'
  bl_label = 'Batch Name Copy'
  bl_options = {'REGISTER', 'UNDO'}

  # poll
  @classmethod
  def poll(cls, context):
    ''' Space data type must be in 3D view. '''
    return context.space_data.type in 'VIEW_3D'

  # draw
  def draw(self, context):
    ''' Draw the operator panel/menu. '''
    layout = self.layout

    # batch type
    layout.prop(context.window_manager.batchNameCopyUI, 'batchType', expand=True)
    column = layout.column(align=True)
    column.label(text='Copy:', icon='COPYDOWN')
    column = layout.column(align=True)

    # source
    column.prop(context.window_manager.batchNameCopyUI, 'source', expand=True)
    column = layout.column(align=True)
    column.label(text='Paste:', icon='PASTEDOWN')
    column = layout.column(align=True)
    split = column.split(align=True)

    # targets
    split.prop(context.window_manager.batchNameCopyUI, 'objects', text='', icon='OBJECT_DATA')
    split.prop(context.window_manager.batchNameCopyUI, 'objectData', text='', icon='MESH_DATA')
    split.prop(context.window_manager.batchNameCopyUI, 'material', text='', icon='MATERIAL')
    split.prop(context.window_manager.batchNameCopyUI, 'texture', text='', icon='TEXTURE')
    split.prop(context.window_manager.batchNameCopyUI, 'particleSystem', text='', icon='PARTICLES')
    split.prop(context.window_manager.batchNameCopyUI, 'particleSettings', text='', icon='MOD_PARTICLES')
    column = layout.column()

    # use active object
    column.prop(context.window_manager.batchNameCopyUI, 'useActiveObject')

  # execute
  def execute(self, context):
    ''' Execute the operator. '''
    batchNameCopy(self, context, context.window_manager.batchNameCopyUI.batchType, context.window_manager.batchNameCopyUI.source, context.window_manager.batchNameCopyUI.objects, context.window_manager.batchNameCopyUI.objectData, context.window_manager.batchNameCopyUI.material, context.window_manager.batchNameCopyUI.texture, context.window_manager.batchNameCopyUI.particleSystem, context.window_manager.batchNameCopyUI.particleSettings, context.window_manager.batchNameCopyUI.useActiveObject)
    return {'FINISHED'}

  # invoke
  def invoke(self, context, event):
    ''' Invoke the operator panel/menu, control its width. '''
    context.window_manager.invoke_props_dialog(self, width=150)
    return {'RUNNING_MODAL'}

###############
## INTERFACE ##
###############

# item panel
class itemPanel():
  ''' Item panel '''
  # draw
  def draw(self, context):
    ''' Item panel body. '''
    layout = self.layout
    column = layout.column(align=True)
    itemPanelUI = context.window_manager.itemPanelUI

    row = column.row(align=True)
    row.scale_y = 1.25

    if context.window_manager.itemPanelUI.viewFilters:
      iconToggle = 'RADIOBUT_ON'
    else:
      iconToggle = 'RADIOBUT_OFF'

    # view filters
    row.prop(context.window_manager.itemPanelUI, 'viewFilters', text='Filters', icon=iconToggle, toggle=True)

    # view hierarchy
    row.prop(context.window_manager.itemPanelUI, 'viewHierarchy', text='', icon='OOPS')

    # item panel reset
    row.operator('view3d.reset_batch_options', text='', icon='RECOVER_AUTO')

    # batch naming
    row.operator('view3d.batch_naming', text='', icon='SORTALPHA')

    # batch copy
    row.operator('view3d.batch_name_copy', text='', icon='COPYDOWN')
    if context.window_manager.itemPanelUI.viewFilters:
      split = column.split(align=True)

      # data block filters
      split.prop(context.window_manager.itemPanelUI, 'viewConstraints', text='', icon='CONSTRAINT')
      split.prop(context.window_manager.itemPanelUI, 'viewModifiers', text='', icon='MODIFIER')
      split.prop(context.window_manager.itemPanelUI, 'viewBoneConstraints', text='', icon='CONSTRAINT_BONE')
      split.prop(context.window_manager.itemPanelUI, 'viewMaterials', text='', icon='MATERIAL')
      split.prop(context.window_manager.itemPanelUI, 'viewTextures', text='', icon='TEXTURE')
      split.prop(context.window_manager.itemPanelUI, 'viewParticleSystems', text='', icon='PARTICLES')
      split = column.split(align=True)
      split.prop(context.window_manager.itemPanelUI, 'viewGroups', text='', icon='GROUP')
      split.prop(context.window_manager.itemPanelUI, 'viewVertexGroups', text='', icon='GROUP_VERTEX')
      split.prop(context.window_manager.itemPanelUI, 'viewShapeKeys', text='', icon='SHAPEKEY_DATA')
      split.prop(context.window_manager.itemPanelUI, 'viewUVS', text='', icon='GROUP_UVS')
      split.prop(context.window_manager.itemPanelUI, 'viewVertexColors', text='', icon='GROUP_VCOL')
      split.prop(context.window_manager.itemPanelUI, 'viewBoneGroups', text='', icon='GROUP_BONE')
    column = layout.column()

    # data block list
    row = column.row(align=True)
    row.template_ID(context.scene.objects, 'active')
    # groups
    if context.window_manager.itemPanelUI.viewGroups:
      for group in bpy.data.groups[:]:
        for object in group.objects[:]:
          if object == context.active_object:
            row = column.row(align=True)
            sub = row.row()
            sub.scale_x = 1.6
            sub.label(text='', icon='GROUP')
            row.prop(group, 'name', text='')

    # constraint
    if context.window_manager.itemPanelUI.viewConstraints:
      for constraint in context.active_object.constraints:
        row = column.row(align=True)
        sub = row.row()
        sub.scale_x = 1.6
        sub.label(text='', icon='CONSTRAINT')
        row.prop(constraint, 'name', text='')
        if constraint.mute:
          iconView = 'RESTRICT_VIEW_ON'
        else:
          iconView = 'RESTRICT_VIEW_OFF'
        row.prop(constraint, 'mute', text='', icon=iconView)

    # modifier
    if not context.window_manager.itemPanelUI.viewModifiers:
      context.window_manager.itemPanelUI.viewParticleSystems = False
    if not context.window_manager.itemPanelUI.viewParticleSystems:
      context.window_manager.itemPanelUI.viewParticleSettings = False
    if context.window_manager.itemPanelUI.viewModifiers:
      for modifier in context.active_object.modifiers:
        row = column.row(align=True)
        sub = row.row()
        sub.scale_x = 1.6
        sub.label(text='', icon=modifierIcon(modifier))
        row.prop(modifier, 'name', text='')
        if modifier.show_viewport:
          iconView = 'RESTRICT_VIEW_OFF'
        else:
          iconView = 'RESTRICT_VIEW_ON'
        row.prop(modifier, 'show_viewport', text='', icon=iconView)

        # particle system
        if context.window_manager.itemPanelUI.viewParticleSystems:
          if modifier.type in {'PARTICLE_INSTANCE', 'PARTICLE_SYSTEM'}:
            row = column.row(align=True)
            sub = row.row()
            sub.scale_x = 1.6
            sub.label(text='', icon='PARTICLES')
            row.prop(modifier.particle_system, 'name', text='')
            if modifier.show_render:
              iconRender = 'RESTRICT_RENDER_OFF'
            else:
              iconRender = 'RESTRICT_RENDER_ON'
            row.prop(modifier, 'show_render', text='', icon=iconRender)

            # particle settings
            row = column.row(align=True)
            sub = row.row()
            sub.scale_x = 1.6
            sub.label(text='', icon='DOT')
            row.prop(modifier.particle_system.settings, 'name', text='')

    # material
    if context.window_manager.itemPanelUI.viewMaterials:
      for material in bpy.data.objects[context.active_object.name].material_slots[:]:
        if material.material != None:
          if material.link == 'OBJECT':
            row = column.row(align=True)
            sub = row.row()
            sub.scale_x = 1.6
            sub.label(text='', icon='MATERIAL')
            row.prop(material.material, 'name', text='')

            # texture
            if context.window_manager.itemPanelUI.viewTextures:
              if context.scene.render.engine != 'CYCLES':
                for texture in material.material.texture_slots[:]:
                  if texture != None:
                    row = column.row(align=True)
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
      context.window_manager.itemPanelUI.viewTextures = False

    # view hierarchy
    if context.window_manager.itemPanelUI.viewHierarchy:

      # object
      for object in bpy.data.objects:
        if object in context.selected_objects:
          if object != context.active_object:
            row = column.row(align=True)
            sub = row.row()
            sub.scale_x = 1.6
            sub.label(text='', icon=objectIcon(object))
            row.prop(object, 'name', text='')

            # group
            if context.window_manager.itemPanelUI.viewGroups:
              for group in bpy.data.groups[:]:
                for groupObject in group.objects[:]:
                  if groupObject == object:
                    row = column.row(align=True)
                    sub = row.row()
                    sub.scale_x = 1.6
                    sub.label(text='', icon='GROUP')
                    row.prop(group, 'name', text='')

            # constraint
            if context.window_manager.itemPanelUI.viewConstraints:
              for constraint in object.constraints[:]:
                row = column.row(align=True)
                sub = row.row()
                sub.scale_x = 1.6
                sub.label(text='', icon='CONSTRAINT')
                row.prop(constraint, 'name', text='')
                if constraint.mute:
                  iconView = 'RESTRICT_VIEW_ON'
                else:
                  iconView = 'RESTRICT_VIEW_OFF'
                row.prop(constraint, 'mute', text='', icon=iconView)

            # modifier
            if context.window_manager.itemPanelUI.viewModifiers:
              for modifier in object.modifiers[:]:
                row = column.row(align=True)
                sub = row.row()
                sub.scale_x = 1.6
                sub.label(text='', icon=modifierIcon(modifier))
                row.prop(modifier, 'name', text='')
                if modifier.show_viewport:
                  iconView = 'RESTRICT_VIEW_OFF'
                else:
                  iconView = 'RESTRICT_VIEW_ON'
                row.prop(modifier, 'show_viewport', text='', icon=iconView)

                # particle system
                if context.window_manager.itemPanelUI.viewParticleSystems:
                  if modifier.type in {'PARTICLE_INSTANCE', 'PARTICLE_SYSTEM'}:
                    row = column.row(align=True)
                    sub = row.row()
                    sub.scale_x = 1.6
                    sub.label(text='', icon='PARTICLES')
                    row.prop(modifier.particle_system, 'name', text='')
                    if modifier.show_render:
                      iconRender = 'RESTRICT_RENDER_OFF'
                    else:
                      iconRender = 'RESTRICT_RENDER_ON'
                    row.prop(modifier, 'show_render', text='', icon=iconRender)

                    # particle settings
                    row = column.row(align=True)
                    sub = row.row()
                    sub.scale_x = 1.6
                    sub.label(text='', icon='DOT')
                    row.prop(modifier.particle_system.settings, 'name', text='')

            # material
            if context.window_manager.itemPanelUI.viewMaterials:
              for material in bpy.data.objects[object.name].material_slots[:]:
                if material.material != None:
                  if material.link == 'OBJECT':
                    row = column.row(align=True)
                    sub = row.row()
                    sub.scale_x = 1.6
                    sub.label(text='', icon='MATERIAL')
                    row.prop(material.material, 'name', text='')

                    # texture
                    if context.window_manager.itemPanelUI.viewTextures:
                      if context.scene.render.engine != 'CYCLES':
                        for texture in material.material.texture_slots[:]:
                          if texture != None:
                            row = column.row(align=True)
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
              context.window_manager.itemPanelUI.viewTextures = False

    # empty
    if context.object.type in 'EMPTY':
      if context.object.empty_draw_type in 'IMAGE':
        row = column.row(align=True)
        row.template_ID(context.active_object, 'data', open='image.open', unlink='image.unlink')

    # object data
    else:
      row = column.row(align=True)
      row.template_ID(context.active_object, 'data')

      # vertex group
      if context.window_manager.itemPanelUI.viewVertexGroups:
        if bpy.data.objects[context.active_object.name].type in {'LATTICE', 'MESH'}:
          for group in bpy.data.objects[context.active_object.name].vertex_groups[:]:
            row = column.row(align=True)
            sub = row.row()
            sub.scale_x = 1.6
            sub.label(text='', icon='GROUP_VERTEX')
            row.prop(group, 'name', text='')
            if group.lock_weight:
              iconLock = 'LOCKED'
            else:
              iconLock = 'UNLOCKED'
            row.prop(group, 'lock_weight', text='', icon=iconLock)

      # shape key
      if context.window_manager.itemPanelUI.viewShapeKeys:
        if bpy.data.objects[context.active_object.name].type in {'MESH', 'CURVE', 'SURFACE', 'LATTICE'}:
          if bpy.data.objects[context.active_object.name].data.shape_keys:
            for key in bpy.data.objects[context.active_object.name].data.shape_keys.key_blocks[:]:
              row = column.row(align=True)
              sub = row.row()
              sub.scale_x = 1.6
              sub.label(text='', icon='SHAPEKEY_DATA')
              row.prop(key, 'name', text='')
              if key != bpy.data.objects[context.active_object.name].data.shape_keys.key_blocks[0]:
                sub = row.row(align=True)
                sub.scale_x = 0.17
                sub.prop(key, 'value', text='')
              row.prop(key, 'mute', text='', icon='RESTRICT_VIEW_OFF')

      # uv
      if context.window_manager.itemPanelUI.viewUVS:
        if bpy.data.objects[context.active_object.name].type in 'MESH':
          for uv in bpy.data.objects[context.active_object.name].data.uv_textures[:]:
            row = column.row(align=True)
            sub = row.row()
            sub.scale_x = 1.6
            sub.label(text='', icon='GROUP_UVS')
            row.prop(uv, 'name', text='')
            if uv.active_render:
              iconActive = 'RESTRICT_RENDER_OFF'
            else:
              iconActive = 'RESTRICT_RENDER_ON'
            row.prop(uv, 'active_render', text='', icon=iconActive)

      # vertex color
      if context.window_manager.itemPanelUI.viewVertexColors:
        if bpy.data.objects[context.active_object.name].type in 'MESH':
          for vertexColor in bpy.data.objects[context.active_object.name].data.vertex_colors[:]:
            row = column.row(align=True)
            sub = row.row()
            sub.scale_x = 1.6
            sub.label(text='', icon='GROUP_VCOL')
            row.prop(vertexColor, 'name', text='')
            if vertexColor.active_render:
              iconActive = 'RESTRICT_RENDER_OFF'
            else:
              iconActive = 'RESTRICT_RENDER_ON'
            row.prop(vertexColor, 'active_render', text='', icon=iconActive)

      # bone group
      if context.window_manager.itemPanelUI.viewBoneGroups:
        if bpy.data.objects[context.active_object.name].type in 'ARMATURE':
          for group in bpy.data.objects[context.active_object.name].pose.bone_groups[:]:
            row = column.row(align=True)
            sub = row.row()
            sub.scale_x = 1.6
            sub.label(text='', icon='GROUP_BONE')
            row.prop(group, 'name', text='')

      # bone
      if (bpy.data.objects[context.active_object.name].type in 'ARMATURE' and
        context.object.mode in {'POSE', 'EDIT'}):
        row = column.row(align=True)
        sub = row.row(align=True)
        sub.scale_x = 1.6
        sub.prop(context.window_manager.itemPanelUI, 'viewSelectedBones', text='', icon='BONE_DATA')
        row.prop(context.active_bone, 'name', text='')

        # bone constraint
        if context.window_manager.itemPanelUI.viewBoneConstraints:
          if context.object.mode in 'POSE':
            for constraint in context.active_pose_bone.constraints:
              row = column.row(align=True)
              sub = row.row()
              sub.scale_x = 1.6
              sub.label(text='', icon='CONSTRAINT_BONE')
              row.prop(constraint, 'name', text='')
              if constraint.mute:
                iconView = 'RESTRICT_VIEW_ON'
              else:
                iconView = 'RESTRICT_VIEW_OFF'
              row.prop(constraint, 'mute', text='', icon=iconView)

        # selected bone
        if context.window_manager.itemPanelUI.viewSelectedBones:
          if context.selected_editable_bones:
            selectedBones = context.selected_editable_bones
          else:
            selectedBones = context.selected_pose_bones
          sortedBones = []
          for bone in selectedBones:
            sortedBones.append((bone.name, bone))
          for bone in sorted(sortedBones):
            if bone[1] in (context.selected_editable_bones or context.selected_pose_bones):
              if bone[1] != (context.active_pose_bone or context.active_bone):
                row = column.row(align=True)
                sub = row.row()
                sub.scale_x = 1.6
                sub.label(text='', icon='BONE_DATA')
                row.prop(bone[1], 'name', text='')
                if context.object.mode in 'POSE':
                  if context.window_manager.itemPanelUI.viewBoneConstraints:
                    for constraint in bone[1].constraints[:]:
                      row = column.row(align=True)
                      sub = row.row()
                      sub.scale_x = 1.6
                      sub.label(text='', icon='CONSTRAINT_BONE')
                      row.prop(constraint, 'name', text='')
                      if constraint.mute:
                        iconView = 'RESTRICT_VIEW_ON'
                      else:
                        iconView = 'RESTRICT_VIEW_OFF'
                      row.prop(constraint, 'mute', text='', icon=iconView)

    # material
    if context.window_manager.itemPanelUI.viewMaterials:
      for material in bpy.data.objects[context.active_object.name].material_slots[:]:
        if material.material != None:
          if material.link == 'DATA':
            row = column.row(align=True)
            sub = row.row()
            sub.scale_x = 1.6
            sub.label(text='', icon='MATERIAL')
            row.prop(material.material, 'name', text='')

            # texture
            if context.window_manager.itemPanelUI.viewTextures:
              if context.scene.render.engine != 'CYCLES':
                for texture in material.material.texture_slots[:]:
                  if texture != None:
                    row = column.row(align=True)
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
      context.window_manager.itemPanelUI.viewTextures = False

    # view hierarchy
    if context.window_manager.itemPanelUI.viewHierarchy:
      for object in bpy.data.objects:
        if object in context.selected_objects:
          if object != context.active_object:
            if object.type != 'EMPTY':
              row = column.row(align=True)
              sub = row.row()
              sub.scale_x = 1.6
              sub.label(text='', icon=objectDataIcon(object))
              row.prop(object.data, 'name', text='')

              # vertex group
              if context.window_manager.itemPanelUI.viewVertexGroups:
                if bpy.data.objects[object.name].type in {'LATTICE', 'MESH'}:
                  for group in bpy.data.objects[object.name].vertex_groups[:]:
                    row = column.row(align=True)
                    sub = row.row()
                    sub.scale_x = 1.6
                    sub.label(text='', icon='GROUP_VERTEX')
                    row.prop(group, 'name', text='')
                    if group.lock_weight:
                      iconLock = 'LOCKED'
                    else:
                      iconLock = 'UNLOCKED'
                    row.prop(group, 'lock_weight', text='', icon=iconLock)

              # shape key
              if context.window_manager.itemPanelUI.viewShapeKeys:
                if bpy.data.objects[object.name].type in {'MESH', 'CURVE', 'SURFACE', 'LATTICE'}:
                  if bpy.data.objects[object.name].data.shape_keys:
                    for key in bpy.data.objects[object.name].data.shape_keys.key_blocks[:]:
                      row = column.row(align=True)
                      sub = row.row()
                      sub.scale_x = 1.6
                      sub.label(text='', icon='SHAPEKEY_DATA')
                      row.prop(key, 'name', text='')
                      if key != bpy.data.objects[object.name].data.shape_keys.key_blocks[0]:
                        sub = row.row(align=True)
                        sub.scale_x = 0.17
                        sub.prop(key, 'value', text='')
                      row.prop(key, 'mute', text='', icon='RESTRICT_VIEW_OFF')

              # uv
              if context.window_manager.itemPanelUI.viewUVS:
                if bpy.data.objects[object.name].type in 'MESH':
                  for uv in bpy.data.objects[object.name].data.uv_textures[:]:
                    row = column.row(align=True)
                    sub = row.row()
                    sub.scale_x = 1.6
                    sub.label(text='', icon='GROUP_UVS')
                    row.prop(uv, 'name', text='')
                    if uv.active_render:
                      iconActive = 'RESTRICT_RENDER_OFF'
                    else:
                      iconActive = 'RESTRICT_RENDER_ON'
                    row.prop(uv, 'active_render', text='', icon=iconActive)

              # vertex color
              if context.window_manager.itemPanelUI.viewVertexColors:
                if bpy.data.objects[object.name].type in 'MESH':
                  for vertexColor in bpy.data.objects[object.name].data.vertex_colors[:]:
                    row = column.row(align=True)
                    sub = row.row()
                    sub.scale_x = 1.6
                    sub.label(text='', icon='GROUP_VCOL')
                    row.prop(vertexColor, 'name', text='')
                    if vertexColor.active_render:
                      iconActive = 'RESTRICT_RENDER_OFF'
                    else:
                      iconActive = 'RESTRICT_RENDER_ON'
                    row.prop(vertexColor, 'active_render', text='', icon=iconActive)

              # bone group
              if context.window_manager.itemPanelUI.viewBoneGroups:
                if bpy.data.objects[object.name].type in 'ARMATURE':
                  for group in bpy.data.objects[object.name].pose.bone_groups[:]:
                    row = column.row(align=True)
                    sub = row.row()
                    sub.scale_x = 1.6
                    sub.label(text='', icon='GROUP_BONE')
                    row.prop(group, 'name', text='')

              # material
              if context.window_manager.itemPanelUI.viewMaterials:
                for material in bpy.data.objects[object.name].material_slots[:]:
                  if material.material != None:
                    if material.link == 'DATA':
                      row = column.row(align=True)
                      sub = row.row()
                      sub.scale_x = 1.6
                      sub.label(text='', icon='MATERIAL')
                      row.prop(material.material, 'name', text='')

                      # texture
                      if context.window_manager.itemPanelUI.viewTextures:
                        if context.scene.render.engine != 'CYCLES':
                          for texture in material.material.texture_slots[:]:
                            if texture != None:
                              row = column.row(align=True)
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
                context.window_manager.itemPanelUI.viewTextures = False

# name
class name():
  ''' Source from the original item panel class, used to return the panel to default usability upon unregiser. '''
  def draw(self, context):
    ''' Item panel body. '''
    layout = self.layout
    row = layout.row()
    row.label(text='', icon='OBJECT_DATA')
    row.prop(context.active_object, 'name', text='')
    if context.active_object.type == 'ARMATURE' and context.active_object.mode in {'EDIT', 'POSE'}:
      if context.active_bone:
        row = layout.row()
        row.label(text='', icon='BONE_DATA')
        row.prop(context.active_bone, 'name', text='')

##############
## REGISTER ##
##############

# register
def register():
  ''' Register '''
  bpy.types.VIEW3D_PT_view3d_name.remove(bpy.types.VIEW3D_PT_view3d_name.draw)
  bpy.types.VIEW3D_PT_view3d_name.remove(name.draw)
  bpy.utils.register_class(batchNamingUI)
  bpy.utils.register_class(batchNameCopyUI)
  bpy.utils.register_class(itemPanelUI)
  bpy.utils.register_class(VIEW3D_OT_reset_batch_options)
  bpy.utils.register_class(VIEW3D_OT_batch_naming)
  bpy.utils.register_class(VIEW3D_OT_batch_name_copy)
  bpy.types.WindowManager.itemPanelUI = bpy.props.PointerProperty(type=itemPanelUI)
  bpy.types.WindowManager.batchNamingUI = bpy.props.PointerProperty(type=batchNamingUI)
  bpy.types.WindowManager.batchNameCopyUI = bpy.props.PointerProperty(type=batchNameCopyUI)
  bpy.types.VIEW3D_PT_view3d_name.append(itemPanel.draw)

# unregister
def unregister():
  ''' Unregister '''
  bpy.types.VIEW3D_PT_view3d_name.remove(itemPanel.draw)
  bpy.utils.unregister_class(batchNamingUI)
  bpy.utils.unregister_class(batchNameCopyUI)
  bpy.utils.unregister_class(itemPanelUI)
  bpy.utils.unregister_class(VIEW3D_OT_reset_batch_options)
  bpy.utils.unregister_class(VIEW3D_OT_batch_naming)
  bpy.utils.unregister_class(VIEW3D_OT_batch_copy)
  del bpy.types.WindowManager.itemPanelUI
  del bpy.types.WindowManager.batchNamingUI
  del bpy.types.WindowManager.batchNameCopyUI
  bpy.types.VIEW3D_PT_view3d_name.append(name.draw)

if __name__ in '__main__':
  register()
