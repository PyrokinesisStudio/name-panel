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
  'location': '3D View → Properties Panel',
  'description': "An improved item panel for the 3D View with included batch naming tools.",
  'category': '3D View'
}

# imports
import bpy
import re
from bpy.props import *
from bpy.types import Operator
from bpy.types import Panel, PropertyGroup

###############
## FUNCTIONS ##
###############

# rename
def rename(self, dataPath, batchName, find, replace, prefix, suffix, trimStart, trimEnd):
  """
  Names single proper dataPath variable received from batchRename, check
  variable values from operator class.
  """
  if not batchName:
    targetName = dataPath.name[trimStart:]
  else:
    targetName = batchName
    targetName = targetName[trimStart:]
  if trimEnd > 0:
    targetName = targetName[:-trimEnd]
  targetName = re.sub(find, replace, targetName)
  targetName = prefix + targetName + suffix
  dataPath.name = targetName

# batch rename
def batchRename(self, context, batchType, batchObjects, batchObjectConstraints, batchModifiers, batchObjectData, batchBones, batchBoneConstraints, batchMaterials, batchTextures, batchParticleSystems, batchParticleSettings, batchGroups, batchVertexGroups, batchShapeKeys, batchUVS, batchVertexColors, batchBoneGroups, objectType, constraintType, modifierType, batchName, find, replace, prefix, suffix, trimStart, trimEnd):
  """
  Send dataPath values to rename, check variable values from operator class.
  """
  # objects
  if batchObjects:
    for object in bpy.data.objects[:]:
      if batchType in 'SELECTED':
        if object.select:
          if objectType in 'ALL':
            dataPath = object
          elif objectType in object.type:
            dataPath = object
      else:
        if objectType in 'ALL':
          dataPath = object
        elif objectType in object.type:
          dataPath = object
      try:
        rename(self, dataPath, batchName, find, replace, prefix, suffix, trimStart, trimEnd)
      except:
        pass
  # object constraints
  if batchObjectConstraints:
    for object in bpy.data.objects[:]:
      if batchType in 'SELECTED':
        if object.select:
          for constraint in object.constraints[:]:
            if constraintType in 'ALL':
              dataPath = constraint
            elif constraintType in constraint.type:
              dataPath = constraint
            try:
              rename(self, dataPath, batchName, find, replace, prefix, suffix, trimStart, trimEnd)
            except:
              pass
      else:
        for constraint in object.constraints[:]:
          if constraintType in 'ALL':
            dataPath = constraint
          elif constraintType in constraint.type:
            dataPath = constraint
          try:
            rename(self, dataPath, batchName, find, replace, prefix, suffix, trimStart, trimEnd)
          except:
            pass
  # modifiers
  if batchModifiers:
    for object in bpy.data.objects[:]:
      if batchType in 'SELECTED':
        if object.select:
          for modifier in object.modifiers[:]:
            if modifierType in 'ALL':
              dataPath = modifier
            elif modifierType in modifier.type:
              dataPath = modifier
            try:
              rename(self, dataPath, batchName, find, replace, prefix, suffix, trimStart, trimEnd)
            except:
              pass
      else:
        for modifier in object.modifiers[:]:
          if modifierType in 'ALL':
            dataPath = modifier
          elif modifierType in modifier.type:
            dataPath = modifier
          try:
            rename(self, dataPath, batchName, find, replace, prefix, suffix, trimStart, trimEnd)
          except:
            pass
  # objects data
  if batchObjectData:
    for object in bpy.data.objects[:]:
      if batchType in 'SELECTED':
        if object.select:
          if objectType in 'ALL':
            dataPath = object.data
          elif objectType in object.type:
            dataPath = object.data
      else:
        if objectType in 'ALL':
          dataPath = object.data
        elif objectType in object.type:
          dataPath = object.data
      try:
        rename(self, dataPath, batchName, find, replace, prefix, suffix, trimStart, trimEnd)
      except:
        pass
  # bones
  if batchBones:
    for object in bpy.data.objects[:]:
      if batchType in 'SELECTED':
        if object.select:
          if object.type in 'ARMATURE':
            for bone in object.data.bones:
              if bone.select:
                dataPath = bone
              try:
                rename(self, dataPath, batchName, find, replace, prefix, suffix, trimStart, trimEnd)
              except:
                  pass
      else:
        if object.type in 'ARMATURE':
          for bone in object.data.bones:
            dataPath = bone
            try:
              rename(self, dataPath, batchName, find, replace, prefix, suffix, trimStart, trimEnd)
            except:
                pass
  # bone constraints
  if batchBoneConstraints:
    for object in bpy.data.objects[:]:
      if batchType in 'SELECTED':
        if object.select:
          if object.type in 'ARMATURE':
            for bone in object.pose.bones[:]:
              if bone.bone.select:
                for constraint in bone.constraints[:]:
                  if constraintType in 'ALL':
                    dataPath = constraint
                  elif constraintType in constraint.type:
                    dataPath = constraint
                  try:
                    rename(self, dataPath, batchName, find, replace, prefix, suffix, trimStart, trimEnd)
                  except:
                    pass
      else:
        if object.type in 'ARMATURE':
          for bone in object.pose.bones[:]:
            for constraint in bone.constraints[:]:
              if constraintType in 'ALL':
                dataPath = constraint
              elif constraintType in constraint.type:
                dataPath = constraint
              try:
                rename(self, dataPath, batchName, find, replace, prefix, suffix, trimStart, trimEnd)
              except:
                pass
  # materials
  if batchMaterials:
    for object in bpy.data.objects[:]:
      if batchType in 'SELECTED':
        if object.select:
          for slot in object.material_slots[:]:
            if slot.material != None:
              if objectType in 'ALL':
                dataPath = slot.material
              elif objectType in object.type:
                dataPath = slot.material
              try:
                rename(self, dataPath, batchName, find, replace, prefix, suffix, trimStart, trimEnd)
              except:
                pass
      else:
        for slot in object.material_slots[:]:
          if slot.material != None:
            if objectType in 'ALL':
              dataPath = slot.material
            elif objectType in object.type:
              dataPath = slot.material
            try:
              rename(self, dataPath, batchName, find, replace, prefix, suffix, trimStart, trimEnd)
            except:
              pass
  # textures
  if batchTextures:
    if batchType in 'SELECTED':
      for object in bpy.data.objects[:]:
        if object.select:
          for materialSlot in object.material_slots[:]:
            if materialSlot.material != None:
              for textureSlot in materialSlot.material.texture_slots[:]:
                if textureSlot != None:
                  if objectType in 'ALL':
                    dataPath = textureSlot.texture
                  elif objectType in object.type:
                    dataPath = textureSlot.texture
                  try:
                    rename(self, dataPath, batchName, find, replace, prefix, suffix, trimStart, trimEnd)
                  except:
                    pass
    else:
      for texture in bpy.data.textures[:]:
        dataPath = texture
        try:
          rename(self, dataPath, batchName, find, replace, prefix, suffix, trimStart, trimEnd)
        except:
          pass
  # particle system
  if batchParticleSystems:
    for object in bpy.data.objects[:]:
      if object.type in 'MESH':
        if batchType in 'SELECTED':
          if object.select:
            for system in object.particle_systems[:]:
              if objectType in 'ALL':
                dataPath = system
              elif objectType in object.type:
                dataPath = system
              try:
                rename(self, dataPath, batchName, find, replace, prefix, suffix, trimStart, trimEnd)
              except:
                pass
        else:
          for system in object.particle_systems[:]:
            if objectType in 'ALL':
              dataPath = system
            elif objectType in object.type:
              dataPath = system
            try:
              rename(self, dataPath, batchName, find, replace, prefix, suffix, trimStart, trimEnd)
            except:
              pass
  # particle settings
  if batchParticleSettings:
    for object in bpy.data.objects[:]:
      if object.type in 'MESH':
        if batchType in 'SELECTED':
          if object.select:
            for system in object.particle_systems[:]:
              if objectType in 'ALL':
                dataPath = system.settings
              elif objectType in object.type:
                dataPath = system.settings
              try:
                rename(self, dataPath, batchName, find, replace, prefix, suffix, trimStart, trimEnd)
              except:
                pass
        else:
          for system in object.particle_systems[:]:
            if objectType in 'ALL':
              dataPath = system.settings
            elif objectType in object.type:
              dataPath = system.settings
            try:
              rename(self, dataPath, batchName, find, replace, prefix, suffix, trimStart, trimEnd)
            except:
              pass
  # groups
  if batchGroups:
    for group in bpy.data.groups[:]:
      if batchType in 'SELECTED':
        for object in group.objects[:]:
          if objectType in 'ALL':
            dataPath = group
          elif objectType in object.type:
            dataPath = group
          try:
            rename(self, dataPath, batchName, find, replace, prefix, suffix, trimStart, trimEnd)
          except:
            pass
      else:
        for object in group.objects[:]:
          if objectType in 'ALL':
            dataPath = group
          elif objectType in object.type:
            dataPath = group
          try:
            rename(self, dataPath, batchName, find, replace, prefix, suffix, trimStart, trimEnd)
          except:
            pass
  # vertex groups
  if batchVertexGroups:
    for object in bpy.data.objects[:]:
      if object.type in {'MESH', 'LATTICE'}:
        if batchType in 'SELECTED':
          if object.select:
            for group in object.vertex_groups[:]:
              if objectType in 'ALL':
                dataPath = group
              elif objectType in object.type:
                dataPath = group
              try:
                rename(self, dataPath, batchName, find, replace, prefix, suffix, trimStart, trimEnd)
              except:
                pass
        else:
          for group in object.vertex_groups[:]:
            if objectType in 'ALL':
              dataPath = group
            elif objectType in object.type:
              dataPath = group
            try:
              rename(self, dataPath, batchName, find, replace, prefix, suffix, trimStart, trimEnd)
            except:
              pass

  # shape keys
  if batchShapeKeys:
    for object in bpy.data.objects[:]:
      if object.type in {'MESH', 'CURVE', 'SURFACE', 'LATTICE'}:
        if object.data.shape_keys:
          if batchType in 'SELECTED':
            if object.select:
              for key in object.data.shape_keys.key_blocks[:]:
                if objectType in 'ALL':
                  dataPath = key
                elif objectType in object.type:
                  dataPath = key
                try:
                  rename(self, dataPath, batchName, find, replace, prefix, suffix, trimStart, trimEnd)
                except:
                  pass
          else:
            for key in object.data.shape_keys.key_blocks[:]:
              if objectType in 'ALL':
                dataPath = key
              elif objectType in object.type:
                dataPath = key
              try:
                rename(self, dataPath, batchName, find, replace, prefix, suffix, trimStart, trimEnd)
              except:
                pass
  # uv maps
  if batchUVS:
    for object in bpy.data.objects[:]:
      if object.type in 'MESH':
        if batchType in 'SELECTED':
          if object.select:
            for uv in object.data.uv_textures[:]:
              if objectType in 'ALL':
                dataPath = uv
              elif objectType in object.type:
                dataPath = uv
              try:
                rename(self, dataPath, batchName, find, replace, prefix, suffix, trimStart, trimEnd)
              except:
                pass
        else:
         for uv in object.data.uv_textures[:]:
            if objectType in 'ALL':
              dataPath = uv
            elif objectType in object.type:
              dataPath = uv
            try:
              rename(self, dataPath, batchName, find, replace, prefix, suffix, trimStart, trimEnd)
            except:
              pass
  # vertex colors
  if batchVertexColors:
    for object in bpy.data.objects[:]:
      if object.type in 'MESH':
        if batchType in 'SELECTED':
          if object.select:
            for vertexColor in object.data.vertex_colors[:]:
              if objectType in 'ALL':
                dataPath = vertexColor
              elif objectType in object.type:
                dataPath = vertexColor
              try:
                rename(self, dataPath, batchName, find, replace, prefix, suffix, trimStart, trimEnd)
              except:
                pass
        else:
          for vertexColor in object.data.vertex_colors[:]:
            if objectType in 'ALL':
              dataPath = vertexColor
            elif objectType in object.type:
              dataPath = vertexColor
            try:
              rename(self, dataPath, batchName, find, replace, prefix, suffix, trimStart, trimEnd)
            except:
              pass
  # bone groups
  if batchBoneGroups:
    for object in bpy.data.objects[:]:
      if batchType in 'SELECTED':
        if object.select:
          if object.type in 'ARMATURE':
            for group in object.pose.bone_groups[:]:
              if object.bone.select:
                dataPath = group
                try:
                  rename(self, dataPath, batchName, find, replace, prefix, suffix, trimStart, trimEnd)
                except:
                  pass
      else:
        if object.type in 'ARMATURE':
          for group in object.pose.bone_groups[:]:
            dataPath = group
            try:
              rename(self, dataPath, batchName, find, replace, prefix, suffix, trimStart, trimEnd)
            except:
              pass


###############
## OPERATORS ##
###############

# batch naming
class VIEW3D_OT_batch_naming(Operator):
  """ Batch rename data blocks. """
  bl_idname = 'view3d.batch_naming'
  bl_label = 'Batch Naming'
  bl_options = {'REGISTER', 'UNDO'}
  # batch type
  batchType = EnumProperty(
    name = 'Batch Type:',
    description = "Effect all or only selected objects.",
    items = [
      ('GLOBAL', 'Global', "Batch naming will effect all objects."),
      ('SELECTED', 'Selected', "Batch naming will only effect the objects within the current selection.")
    ],
    default = 'GLOBAL'
  )
  # batch objects
  batchObjects = BoolProperty(
    name = 'Objects',
    description = "Apply batch naming to object names.",
    default = False
  )
  # batch object constraints
  batchObjectConstraints = BoolProperty(
    name = 'Object Constraints',
    description = "Apply batch naming to the constraints.",
    default = False
  )
  # batch modifiers
  batchModifiers = BoolProperty(
    name = 'Modifiers',
    description = "Apply batch naaming to the modifiers.",
    default = False
  )
  # batch objects data
  batchObjectData = BoolProperty(
    name = 'Object Data',
    description = "Apply batch naming to the object data.",
    default = False
  )
  # batch bones
  batchBones = BoolProperty(
    name = 'Bones',
    description = "Apply batch naming to bones.",
    default = False
  )
  # batch bone constraints
  batchBoneConstraints = BoolProperty(
    name = 'Bone Constraints',
    description = "Apply batch naming to bone constraints. (Does not work globally).",
    default = False
  )
  # batch materials
  batchMaterials = BoolProperty(
    name = 'Materials',
    description = "Apply batch naming to the materials.",
    default = False
  )
  # batch textures
  batchTextures = BoolProperty(
    name = 'Textures',
    description = "Apply batch naming to the material textures.",
    default = False
  )
  # batch particle systems
  batchParticleSystems = BoolProperty(
    name = 'Particle Systems',
    description = "Apply batch naming to the particle systems.",
    default = False
  )
  # batch particle settings
  batchParticleSettings = BoolProperty(
    name = 'Particle Settings',
    description = "Apply batch naming to the settings of the particle systems.",
    default = False
  )
  # batch groups
  batchGroups = BoolProperty(
    name = 'Groups',
    description = "Apply batch naming to the groups the objects are within.",
    default = False
  )
  # batch vertex groups
  batchVertexGroups = BoolProperty(
    name = 'Vertex Groups',
    description = "Apply batch naming to the vertex groups of the objects.",
    default = False
  )
  # batch shape keys
  batchShapeKeys = BoolProperty(
    name = 'Shape Keys',
    description = "Apply batch naming to the shape keys of the objects.",
    default = False
  )
  # batch uv maps
  batchUVS = BoolProperty(
    name = 'UV Maps',
    description = "Apply batch naming to the UV maps of the the objects.",
    default = False
  )
  # batch vertex colors
  batchVertexColors = BoolProperty(
    name = 'Vertex Colors',
    description = "Apply batch naming to the vertex colors of the objects.",
    default = False
  )
  # batch bone groups
  batchBoneGroups = BoolProperty(
    name = 'Bone Groups',
    description = "Apply batch naming to the bone groups the armature bones are apart of.",
    default = False
  )
  # object type
  objectType = EnumProperty(
    name = 'Type',
    description = "The type of object that the batch naming operations will be performed on.",
    items = [
      ('ALL', 'All Objects', "", 'OBJECT_DATA', 0),
      ('MESH', 'Mesh', "", 'OUTLINER_OB_MESH', 1),
      ('CURVE', 'Curve', "", 'OUTLINER_OB_CURVE', 2),
      ('SURFACE', 'Surface', "", 'OUTLINER_OB_SURFACE', 3),
      ('META', 'Meta', "", 'OUTLINER_OB_META', 4),
      ('FONT', 'Font', "", 'OUTLINER_OB_FONT', 5),
      ('ARMATURE', 'Armature', "", 'OUTLINER_OB_ARMATURE', 6),
      ('LATTICE', 'Lattice', "", 'OUTLINER_OB_LATTICE', 7),
      ('EMPTY', 'Empty', "", 'OUTLINER_OB_EMPTY', 8),
      ('SPEAKER', 'Speaker', "", 'OUTLINER_OB_SPEAKER', 9),
      ('CAMERA', 'Camera', "", 'OUTLINER_OB_CAMERA', 10),
      ('LAMP', 'Lamp', "", 'OUTLINER_OB_LAMP', 11)
    ],
    default = 'ALL'
  )
  # constraint type
  constraintType = EnumProperty(
    name = 'Type',
    description = "The type of constraint that the batch naming operations will be performed on.",
    items = [
      ('ALL', 'All Constraints', "", 'CONSTRAINT', 0),
      ('CAMERA_SOLVER', 'Camera Solver', "", 'CONSTRAINT_DATA', 1),
      ('FOLLOW_TRACK', 'Follow Track', "", 'CONSTRAINT_DATA', 2),
      ('OBJECT_SOLVER', 'Object Solver', "", 'CONSTRAINT_DATA', 3),
      ('COPY_LOCATION', 'Copy Location', "", 'CONSTRAINT_DATA', 4),
      ('COPY_ROTATION', 'Copy Rotation', "", 'CONSTRAINT_DATA', 5),
      ('COPY_SCALE', 'Copy Scale', "", 'CONSTRAINT_DATA', 6),
      ('COPY_TRANSFORMS', 'Copy Transforms', "", 'CONSTRAINT_DATA', 7),
      ('LIMIT_DISTANCE', 'Limit Distance', "", 'CONSTRAINT_DATA', 8),
      ('LIMIT_LOCATION', 'Limit Location', "", 'CONSTRAINT_DATA', 9),
      ('LIMIT_ROTATION', 'Limit Rotation', "", 'CONSTRAINT_DATA', 10),
      ('LIMIT_SCALE', 'Limit Scale', "", 'CONSTRAINT_DATA', 11),
      ('MAINTAIN_VOLUME', 'Maintain Volume', "", 'CONSTRAINT_DATA', 12),
      ('TRANSFORM', 'Transformation', "", 'CONSTRAINT_DATA', 13),
      ('CLAMP_TO', 'Clamp To', "", 'CONSTRAINT_DATA', 14),
      ('DAMPED_TRACK', 'Damped Track', "", 'CONSTRAINT_DATA', 15),
      ('IK', 'Inverse Kinematics', "", 'CONSTRAINT_DATA', 16),
      ('LOCKED_TRACK', 'Locked Track', "", 'CONSTRAINT_DATA', 17),
      ('SPLINE_IK', 'Spline IK', "", 'CONSTRAINT_DATA', 18),
      ('STRETCH_TO', 'Stretch To', "", 'CONSTRAINT_DATA', 19),
      ('TRACK_TO', 'Track To', "", 'CONSTRAINT_DATA', 20),
      ('ACTION', 'Action', "", 'CONSTRAINT_DATA', 21),
      ('CHILD_OF', 'Child Of', "", 'CONSTRAINT_DATA', 22),
      ('FLOOR', 'Floor', "", 'CONSTRAINT_DATA', 23),
      ('FOLLOW_PATH', 'Follow Path', "", 'CONSTRAINT_DATA', 24),
      ('PIVOT', 'Pivot', "", 'CONSTRAINT_DATA', 25),
      ('RIGID_BODY_JOINT', 'Rigid Body Joint', "", 'CONSTRAINT_DATA', 26),
      ('SHRINKWRAP', 'Shrinkwrap', "", 'CONSTRAINT_DATA', 27)
    ],
    default = 'ALL'
  )
  # modifier type
  modifierType = EnumProperty(
    name = 'Type',
    description = "The type of modifier that the batch naming operations will be performed on.",
    items = [
      ('ALL', 'All Modifiers', "", 'MODIFIER', 0),
      ('DATA_TRANSFER', 'Mesh Cache', "", 'MOD_DATA_TRANSFER', 1),
      ('MESH_CACHE', 'Mesh Cache', "", 'MOD_MESHDEFORM', 2),
      ('NORMAL_EDIT', 'Normal Edit', "", 'MOD_NORMALEDIT', 3),
      ('UV_PROJECT', 'UV Project', "", 'MOD_UVPROJECT', 4),
      ('UV_WARP', 'UV Warp', "", 'MOD_UVPROJECT', 5),
      ('VERTEX_WEIGHT_EDIT', 'Vertex Weight Edit', "", 'MOD_VERTEX_WEIGHT', 6),
      ('VERTEX_WEIGHT_MIX', 'Vertex Weight Mix', "", 'MOD_VERTEX_WEIGHT', 7),
      ('VERTEX_WEIGHT_PROXIMITY', 'Vertex Weight Proximity', "", 'MOD_VERTEX_WEIGHT', 8),
      ('ARRAY', 'Array', "", 'MOD_ARRAY', 9),
      ('BEVEL', 'Bevel', "", 'MOD_BEVEL', 10),
      ('BOOLEAN', 'Boolean', "", 'MOD_BOOLEAN', 11),
      ('BUILD', 'Build', "", 'MOD_BUILD', 12),
      ('DECIMATE', 'Decimate', "", 'MOD_DECIM', 13),
      ('EDGE_SPLIT', 'Edge Split', "", 'MOD_EDGESPLIT', 14),
      ('MASK', 'Mask', "", 'MOD_MASK', 15),
      ('MIRROR', 'Mirror', "", 'MOD_MIRROR', 16),
      ('MULTIRES', 'Multiresolution', "", 'MOD_MULTIRES', 17),
      ('REMESH', 'Remesh', "", 'MOD_REMESH', 18),
      ('SCREW', 'Screw', "", 'MOD_SCREW', 19),
      ('SKIN', 'Skin', "", 'MOD_SKIN', 20),
      ('SOLIDIFY', 'Solidify', "", 'MOD_SOLIDIFY', 21),
      ('SUBSURF', 'Subdivision Surface', "", 'MOD_SUBSURF', 22),
      ('TRIANGULATE', 'Triangulate', "", 'MOD_TRIANGULATE', 23),
      ('WIREFRAME', 'Wireframe', "", 'MOD_WIREFRAME', 24),
      ('ARMATURE', 'Armature', "", 'MOD_ARMATURE', 25),
      ('CAST', 'Cast', "", 'MOD_CAST', 26),
      ('CORRECTIVE_SMOOTH', 'Corrective Smooth', "", 'MOD_SMOOTH', 27),
      ('CURVE', 'Curve', "", 'MOD_CURVE', 28),
      ('DISPLACE', 'Displace', "", 'MOD_DISPLACE', 29),
      ('HOOK', 'Hook', "", 'HOOK', 30),
      ('LAPLACIANSMOOTH', 'Laplacian Smooth', "", 'MOD_SMOOTH', 31),
      ('LAPLACIANDEFORM', 'Laplacian Deform', "", 'MOD_MESHDEFORM', 32),
      ('LATTICE', 'Lattice', "", 'MOD_LATTICE', 33),
      ('MESH_DEFORM', 'Mesh Deform', "", 'MOD_MESHDEFORM', 34),
      ('SHRINKWRAP', 'Shrinkwrap', "", 'MOD_SHRINKWRAP', 35),
      ('SIMPLE_DEFORM', 'Simple Deform', "", 'MOD_SIMPLEDEFORM', 36),
      ('SMOOTH', 'Smooth', "", 'MOD_SMOOTH', 37),
      ('WARP', 'Warp', "", 'MOD_WARP', 38),
      ('WAVE', 'Wave', "", 'MOD_WAVE', 39),
      ('CLOTH', 'Cloth', "", 'MOD_CLOTH', 40),
      ('COLLISION', 'Collision', "", 'MOD_PHYSICS', 41),
      ('DYNAMIC_PAINT', 'Dynamic Paint', "", 'MOD_DYNAMICPAINT', 42),
      ('EXPLODE', 'Explode', "", 'MOD_EXPLODE', 43),
      ('FLUID_SIMULATION', 'Fluid Simulation', "", 'MOD_FLUIDSIM', 44),
      ('OCEAN', 'Ocean', "", 'MOD_OCEAN', 45),
      ('PARTICLE_INSTANCE', 'Particle Instance', "", 'MOD_PARTICLES', 46),
      ('PARTICLE_SYSTEM', 'Particle System', "", 'MOD_PARTICLES', 47),
      ('SMOKE', 'Smoke', "", 'MOD_SMOKE', 48),
      ('SOFT_BODY', 'Soft Body', "", 'MOD_SOFT', 49)
    ],
    default = 'ALL'
  )
  # name
  batchName = StringProperty(
    name = 'Name',
    description = "Designate a new name, if blank, the current names are effected by any changes to the parameters below."
  )
  # find
  find = StringProperty(
    name = 'Find',
    description = "Find this text and remove it from the names. Evaluated as a python regular expression, must escape any RE metacharacters when applicable with \\ before character, ie; \\."
  )
  # replace
  replace = StringProperty(
    name = 'Replace',
    description = "Replace found text within the names with the text entered here."
  )
  # prefix
  prefix = StringProperty(
    name = 'Prefix',
    description = "Designate a prefix to use for the names."
  )
  # suffix
  suffix = StringProperty(
    name = 'Suffix',
    description = "Designate a suffix to use for the names"
  )
  # trim start
  trimStart = IntProperty(
    name = 'Trim Start',
    description = "Trim the beginning of the names by this amount.",
    min = 0,
    max = 50,
    default = 0
  )
  # trim end
  trimEnd = IntProperty(
    name = 'Trim End',
    description = "Trim the ending of the names by this amount.",
    min = 0,
    max = 50,
    default = 0
  )
  # poll
  @classmethod
  def poll(cls, context):
    """ Space data type must be in 3D view. """
    return context.space_data.type in 'VIEW_3D'

  # draw
  def draw(self, context):
    """ Draw the operator panel/menu. """
    layout = self.layout
    layout.prop(self.properties, 'batchType', expand=True)
    # type rows
    column = layout.column(align=True)
    split = column.split(align=True)
    split.prop(self.properties, 'batchObjects', text='', icon='OBJECT_DATA')
    split.prop(self.properties, 'batchObjectConstraints', text='', icon='CONSTRAINT')
    split.prop(self.properties, 'batchModifiers', text='', icon='MODIFIER')
    split.prop(self.properties, 'batchObjectData', text='', icon='MESH_DATA')
    if context.selected_pose_bones or context.selected_editable_bones:
      split.prop(self.properties, 'batchBones', text='', icon='BONE_DATA')
      if context.selected_pose_bones:
        split.prop(self.properties, 'batchBoneConstraints', text='', icon='CONSTRAINT_BONE')
    split.prop(self.properties, 'batchMaterials', text='', icon='MATERIAL')
    if context.scene.render.engine != 'CYCLES':
      split.prop(self.properties, 'batchTextures', text='', icon='TEXTURE')
    split.prop(self.properties, 'batchParticleSystems', text='', icon='PARTICLES')
    split.prop(self.properties, 'batchParticleSettings', text='', icon='MOD_PARTICLES')
    split = column.split(align=True)
    split.prop(self.properties, 'batchGroups', text='', icon='GROUP')
    split.prop(self.properties, 'batchVertexGroups', text='', icon='GROUP_VERTEX')
    split.prop(self.properties, 'batchShapeKeys', text='', icon='SHAPEKEY_DATA')
    split.prop(self.properties, 'batchUVS', text='', icon='GROUP_UVS')
    split.prop(self.properties, 'batchVertexColors', text='', icon='GROUP_VCOL')
    split.prop(self.properties, 'batchBoneGroups', text="", icon='GROUP_BONE')
    # type filters
    column = layout.column()
    column.prop(self.properties, 'objectType', text='')
    column.prop(self.properties, 'constraintType', text='')
    column.prop(self.properties, 'modifierType', text='')
    # input fields
    column.separator()
    column.prop(self.properties, 'batchName')
    column.separator()
    column.prop(self.properties, 'find', icon='VIEWZOOM')
    column.separator()
    column.prop(self.properties, 'replace', icon='FILE_REFRESH')
    column.separator()
    column.prop(self.properties, 'prefix', icon='LOOP_BACK')
    column.separator()
    column.prop(self.properties, 'suffix', icon='LOOP_FORWARDS')
    column.separator()
    row = column.row()
    row.label(text="Trim Start:")
    row.prop(self.properties, 'trimStart', text='')
    row = column.row()
    row.label(text="Trim End:")
    row.prop(self.properties, 'trimEnd', text='')

  # execute
  def execute(self, context):
    """ Execute the operator. """
    batchRename(self, context, self.batchType, self.batchObjects, self.batchObjectConstraints, self.batchModifiers, self.batchObjectData, self.batchBones, self.batchBoneConstraints, self.batchMaterials, self.batchTextures, self.batchParticleSystems, self.batchParticleSettings, self.batchGroups, self.batchVertexGroups, self.batchShapeKeys, self.batchUVS, self.batchVertexColors, self.batchBoneGroups, self.objectType, self.constraintType, self.modifierType, self.batchName, self.find, self.replace, self.prefix, self.suffix, self.trimStart, self.trimEnd)
    return {'FINISHED'}

  # invoke
  def invoke(self, context, event):
    """ Invoke the operator panel/menu, control its width. """
    context.window_manager.invoke_props_dialog(self, width=200)
    return {'RUNNING_MODAL'}

###############
## INTERFACE ##
###############

# item UI property group
class itemUIPropertyGroup(PropertyGroup):
  """
  Bool Properties that effect how item panel displays the item(s) within the users current selection
  """
  # view hierarchy
  viewHierarchy = BoolProperty(
    name = 'View all selected',
    description = "Display everything within your current selection inside the item panel.",
    default = False
  )
  # view filters
  viewFilters = BoolProperty(
    name = 'Data block filters',
    description = "Display filters for the item panel.",
    default = False
  )
  # view constraints
  viewConstraints = BoolProperty(
    name = 'View object constraints',
    description = "Display the object constraints.",
    default = False
  )
  # view modifiers
  viewModifiers = BoolProperty(
    name = 'View object modifiers',
    description = "Display the object modifiers.",
    default = False
  )
  # view bone constraints
  viewBoneConstraints = BoolProperty(
    name = 'View bone constraints',
    description = "Display the bone constraints.",
    default = False
  )
  # view materials
  viewMaterials = BoolProperty(
    name = 'View object materials',
    description = "Display the object materials.",
    default = False
  )
  # view textures
  viewTextures = BoolProperty(
    name = 'View material textures.',
    description = "Display the textures of the object's material(s).",
    default = False
  )
  # view particle systems
  viewParticleSystems = BoolProperty(
    name = 'View particle systems',
    description = "Display the particle systems for the object.",
    default = False
  )
  # view particle settings
  viewParticleSettings = BoolProperty(
    name = 'View particle settings',
    description = "Display the particle system settings for the object.",
    default = False
  )
  # group
  viewGroups = BoolProperty(
    name = 'View groups',
    description = "Display the groups the selected object is apart of.",
    default = False
  )
  # view vertex groups
  viewVertexGroups = BoolProperty(
    name = 'View vertex groups',
    description = "Display the objects vertex groups.",
    default = False
  )
  # view shape keys
  viewShapeKeys = BoolProperty(
    name = 'View shapekeys',
    description = "Display the objects shapekeys.",
    default = False
  )
  # view uvs
  viewUVS = BoolProperty(
    name = 'View UV\'s',
    description = "Display the mesh objects UV's.",
    default = False
  )
  # view vertex colors
  viewVertexColors = BoolProperty(
    name = 'View vertex colors',
    description = "Display the vertex colors.",
    default = False
  )
  # view bone groups
  viewBoneGroups = BoolProperty(
    name = 'View bone groups',
    description = "Display bone groups.",
    default = False
  )
  # view selected bones
  viewSelectedBones = BoolProperty(
    name = 'View selected bones',
    description = "Display selected bones.",
    default = False
  )

# item panel
class itemPanel():
  """
  Item panel
  """

  # draw
  def draw(self, context):
    """ Item panel body. """
    layout = self.layout
    column = layout.column(align=True)
    itemUI = context.window_manager.itemUI
    # view options row
    if itemUI.viewFilters:
      row = column.row(align=True)
      row.scale_y = 1.25
      row.prop(itemUI, 'viewHierarchy', text='', icon='OOPS')
      row.prop(itemUI, 'viewFilters', toggle=True)
      row.operator('view3d.batch_naming', text='', icon='AUTO')
      split = column.split(align=True)
      split.prop(itemUI, 'viewConstraints', text='', icon='CONSTRAINT')
      split.prop(itemUI, 'viewModifiers', text='', icon='MODIFIER')
      split.prop(itemUI, 'viewBoneConstraints', text='', icon='CONSTRAINT_BONE')
      split.prop(itemUI, 'viewMaterials', text='', icon='MATERIAL')
      split.prop(itemUI, 'viewTextures', text='', icon='TEXTURE')
      split.prop(itemUI, 'viewParticleSystems', text='', icon='PARTICLES')
      split = column.split(align=True)
      split.prop(itemUI, 'viewGroups', text='', icon='GROUP')
      split.prop(itemUI, 'viewVertexGroups', text='', icon='GROUP_VERTEX')
      split.prop(itemUI, 'viewShapeKeys', text='', icon='SHAPEKEY_DATA')
      split.prop(itemUI, 'viewUVS', text='', icon='GROUP_UVS')
      split.prop(itemUI, 'viewVertexColors', text='', icon='GROUP_VCOL')
      split.prop(itemUI, 'viewBoneGroups', text='', icon='GROUP_BONE')
    else:
      row = column.row(align=True)
      row.scale_y = 1.25
      row.prop(itemUI, 'viewHierarchy', text='', icon='OOPS')
      row.prop(itemUI, 'viewFilters', toggle=True)
      row.operator('view3d.batch_naming', text='', icon='AUTO')
    column = layout.column()
    # data block list
    row = column.row(align=True)
    row.template_ID(context.scene.objects, 'active')
    # groups
    if itemUI.viewGroups:
      for group in bpy.data.groups[:]:
        for object in group.objects[:]:
          if object == context.active_object:
            row = column.row(align=True)
            sub = row.row()
            sub.scale_x = 1.6
            sub.label(text='', icon='GROUP')
            row.prop(group, 'name', text='')
    # constraints
    if itemUI.viewConstraints:
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
    # modifiers
    if not itemUI.viewModifiers:
      itemUI.viewParticleSystems = False
    if not itemUI.viewParticleSystems:
      itemUI.viewParticleSettings = False
    if itemUI.viewModifiers:
      for modifier in context.active_object.modifiers:
        row = column.row(align=True)
        sub = row.row()
        sub.scale_x = 1.6
        if modifier.type in 'DATA_TRANSFER':
          iconMod = 'MOD_DATA_TRANSFER'
        elif modifier.type in 'MESH_CACHE':
          iconMod = 'MOD_MESHDEFORM'
        elif modifier.type in 'NORMAL_EDIT':
          iconMod = 'MOD_NORMALEDIT'
        elif modifier.type in 'UV_PROJECT':
          iconMod = 'MOD_UVPROJECT'
        elif modifier.type in 'UV_WARP':
          iconMod = 'MOD_UVPROJECT'
        elif modifier.type in 'VERTEX_WEIGHT_EDIT':
          iconMod = 'MOD_VERTEX_WEIGHT'
        elif modifier.type in 'VERTEX_WEIGHT_MIX':
          iconMod = 'MOD_VERTEX_WEIGHT'
        elif modifier.type in 'VERTEX_WEIGHT_PROXIMITY':
          iconMod = 'MOD_VERTEX_WEIGHT'
        elif modifier.type in 'ARRAY':
          iconMod = 'MOD_ARRAY'
        elif modifier.type in 'BEVEL':
          iconMod = 'MOD_BEVEL'
        elif modifier.type in 'BOOLEAN':
          iconMod = 'MOD_BOOLEAN'
        elif modifier.type in 'BUILD':
          iconMod = 'MOD_BUILD'
        elif modifier.type in 'DECIMATE':
          iconMod = 'MOD_DECIM'
        elif modifier.type in 'EDGE_SPLIT':
          iconMod = 'MOD_EDGESPLIT'
        elif modifier.type in 'MASK':
          iconMod = 'MOD_MASK'
        elif modifier.type in 'MIRROR':
          iconMod = 'MOD_MIRROR'
        elif modifier.type in 'MULTIRES':
          iconMod = 'MOD_MULTIRES'
        elif modifier.type in 'REMESH':
          iconMod = 'MOD_REMESH'
        elif modifier.type in 'SCREW':
          iconMod = 'MOD_SCREW'
        elif modifier.type in 'SKIN':
          iconMod = 'MOD_SKIN'
        elif modifier.type in 'SOLIDIFY':
          iconMod = 'MOD_SOLIDIFY'
        elif modifier.type in 'SUBSURF':
          iconMod = 'MOD_SUBSURF'
        elif modifier.type in 'TRIANGULATE':
          iconMod = 'MOD_TRIANGULATE'
        elif modifier.type in 'WIREFRAME':
          iconMod = 'MOD_WIREFRAME'
        elif modifier.type in 'ARMATURE':
          iconMod = 'MOD_ARMATURE'
        elif modifier.type in 'CAST':
          iconMod = 'MOD_CAST'
        elif modifier.type in 'CORRECTIVE_SMOOTH':
          iconMod = 'MOD_SMOOTH'
        elif modifier.type in 'CURVE':
          iconMod = 'MOD_CURVE'
        elif modifier.type in 'DISPLACE':
          iconMod = 'MOD_DISPLACE'
        elif modifier.type in 'HOOK':
          iconMod = 'HOOK'
        elif modifier.type in 'LAPLACIANSMOOTH':
          iconMod = 'MOD_SMOOTH'
        elif modifier.type in 'LAPLACIANDEFORM':
          iconMod = 'MOD_MESHDEFORM'
        elif modifier.type in 'LATTICE':
          iconMod = 'MOD_LATTICE'
        elif modifier.type in 'MESH_DEFORM':
          iconMod = 'MOD_MESHDEFORM'
        elif modifier.type in 'SHRINKWRAP':
          iconMod = 'MOD_SHRINKWRAP'
        elif modifier.type in 'SIMPLE_DEFORM':
          iconMod = 'MOD_SIMPLEDEFORM'
        elif modifier.type in 'SMOOTH':
          iconMod = 'MOD_SMOOTH'
        elif modifier.type in 'WARP':
          iconMod = 'MOD_WARP'
        elif modifier.type in 'WAVE':
          iconMod = 'MOD_WAVE'
        elif modifier.type in 'CLOTH':
          iconMod = 'MOD_CLOTH'
        elif modifier.type in 'COLLISION':
          iconMod = 'MOD_PHYSICS'
        elif modifier.type in 'DYNAMIC_PAINT':
          iconMod = 'MOD_DYNAMICPAINT'
        elif modifier.type in 'EXPLODE':
          iconMod = 'MOD_EXPLODE'
        elif modifier.type in 'FLUID_SIMULATION':
          iconMod = 'MOD_FLUIDSIM'
        elif modifier.type in 'OCEAN':
          iconMod = 'MOD_OCEAN'
        elif modifier.type in 'PARTICLE_INSTANCE':
          iconMod = 'MOD_PARTICLES'
        elif modifier.type in 'PARTICLE_SYSTEM':
          iconMod = 'MOD_PARTICLES'
        elif modifier.type in 'SMOKE':
          iconMod = 'MOD_SMOKE'
        elif modifier.type in 'SOFT_BODY':
          iconMod = 'MOD_SOFT'
        else:
          iconMod = 'MODIFIER'
        sub.label(text='', icon=iconMod)
        row.prop(modifier, 'name', text='')
        if modifier.show_viewport:
          iconView = 'RESTRICT_VIEW_OFF'
        else:
          iconView = 'RESTRICT_VIEW_ON'
        row.prop(modifier, 'show_viewport', text='', icon=iconView)
        # particle system
        if itemUI.viewParticleSystems:
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
    # materials
    if itemUI.viewMaterials:
      for materialSlot in bpy.data.objects[context.active_object.name].material_slots[:]:
        if materialSlot.material != None:
          if materialSlot.link == 'OBJECT':
            row = column.row(align=True)
            sub = row.row()
            sub.scale_x = 1.6
            sub.label(text='', icon='MATERIAL')
            row.prop(materialSlot.material, 'name', text='')
            # textures
            if itemUI.viewTextures:
              if context.scene.render.engine != 'CYCLES':
                for textureSlot in materialSlot.material.texture_slots[:]:
                  if textureSlot != None:
                    row = column.row(align=True)
                    sub = row.row()
                    sub.scale_x = 1.6
                    sub.label(text='', icon='TEXTURE')
                    row.prop(textureSlot.texture, 'name', text='')
                    if textureSlot.use:
                      iconToggle = 'RADIOBUT_ON'
                    else:
                      iconToggle = 'RADIOBUT_OFF'
                    row.prop(textureSlot, 'use', text='', icon=iconToggle)
    else:
      itemUI.viewTextures = False
    # view hierarchy
    if itemUI.viewHierarchy:
      # object
      for object in bpy.data.objects:
        if object in context.selected_objects:
          if object != context.active_object:
            row = column.row(align=True)
            sub = row.row()
            sub.scale_x = 1.6
            if object.type in 'MESH':
              iconObject = 'OUTLINER_OB_MESH'
            elif object.type in 'CURVE':
              iconObject = 'OUTLINER_OB_CURVE'
            elif object.type in 'SURFACE':
              iconObject = 'OUTLINER_OB_SURFACE'
            elif object.type in 'META':
              iconObject = 'OUTLINER_OB_META'
            elif object.type in 'FONT':
              iconObject = 'OUTLINER_OB_FONT'
            elif object.type in 'ARMATURE':
              iconObject = 'OUTLINER_OB_ARMATURE'
            elif object.type in 'LATTICE':
              iconObject = 'OUTLINER_OB_LATTICE'
            elif object.type in 'EMPTY':
              iconObject = 'OUTLINER_OB_EMPTY'
            elif object.type in 'SPEAKER':
              iconObject = 'OUTLINER_OB_SPEAKER'
            elif object.type in 'CAMERA':
              iconObject = 'OUTLINER_OB_CAMERA'
            elif object.type in 'LAMP':
              iconObject = 'OUTLINER_OB_LAMP'
            else:
              iconObject = 'OUTLINER_OB_MESH'
            sub.label(text='', icon=iconObject)
            row.prop(object, 'name', text='')
            # group
            if itemUI.viewGroups:
              for group in bpy.data.groups[:]:
                for groupObject in group.objects[:]:
                  if groupObject == object:
                    row = column.row(align=True)
                    sub = row.row()
                    sub.scale_x = 1.6
                    sub.label(text='', icon='GROUP')
                    row.prop(group, 'name', text='')
            # constraints
            if itemUI.viewConstraints:
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
            # modifiers
            if itemUI.viewModifiers:
              for modifier in object.modifiers[:]:
                row = column.row(align=True)
                sub = row.row()
                sub.scale_x = 1.6
                if modifier.type in 'DATA_TRANSFER':
                  iconMod = 'MOD_DATA_TRANSFER'
                elif modifier.type in 'MESH_CACHE':
                  iconMod = 'MOD_MESHDEFORM'
                elif modifier.type in 'NORMAL_EDIT':
                  iconMod = 'MOD_NORMALEDIT'
                elif modifier.type in 'UV_PROJECT':
                  iconMod = 'MOD_UVPROJECT'
                elif modifier.type in 'UV_WARP':
                  iconMod = 'MOD_UVPROJECT'
                elif modifier.type in 'VERTEX_WEIGHT_EDIT':
                  iconMod = 'MOD_VERTEX_WEIGHT'
                elif modifier.type in 'VERTEX_WEIGHT_MIX':
                  iconMod = 'MOD_VERTEX_WEIGHT'
                elif modifier.type in 'VERTEX_WEIGHT_PROXIMITY':
                  iconMod = 'MOD_VERTEX_WEIGHT'
                elif modifier.type in 'ARRAY':
                  iconMod = 'MOD_ARRAY'
                elif modifier.type in 'BEVEL':
                  iconMod = 'MOD_BEVEL'
                elif modifier.type in 'BOOLEAN':
                  iconMod = 'MOD_BOOLEAN'
                elif modifier.type in 'BUILD':
                  iconMod = 'MOD_BUILD'
                elif modifier.type in 'DECIMATE':
                  iconMod = 'MOD_DECIM'
                elif modifier.type in 'EDGE_SPLIT':
                  iconMod = 'MOD_EDGESPLIT'
                elif modifier.type in 'MASK':
                  iconMod = 'MOD_MASK'
                elif modifier.type in 'MIRROR':
                  iconMod = 'MOD_MIRROR'
                elif modifier.type in 'MULTIRES':
                  iconMod = 'MOD_MULTIRES'
                elif modifier.type in 'REMESH':
                  iconMod = 'MOD_REMESH'
                elif modifier.type in 'SCREW':
                  iconMod = 'MOD_SCREW'
                elif modifier.type in 'SKIN':
                  iconMod = 'MOD_SKIN'
                elif modifier.type in 'SOLIDIFY':
                  iconMod = 'MOD_SOLIDIFY'
                elif modifier.type in 'SUBSURF':
                  iconMod = 'MOD_SUBSURF'
                elif modifier.type in 'TRIANGULATE':
                  iconMod = 'MOD_TRIANGULATE'
                elif modifier.type in 'WIREFRAME':
                  iconMod = 'MOD_WIREFRAME'
                elif modifier.type in 'ARMATURE':
                  iconMod = 'MOD_ARMATURE'
                elif modifier.type in 'CAST':
                  iconMod = 'MOD_CAST'
                elif modifier.type in 'CORRECTIVE_SMOOTH':
                  iconMod = 'MOD_SMOOTH'
                elif modifier.type in 'CURVE':
                  iconMod = 'MOD_CURVE'
                elif modifier.type in 'DISPLACE':
                  iconMod = 'MOD_DISPLACE'
                elif modifier.type in 'HOOK':
                  iconMod = 'HOOK'
                elif modifier.type in 'LAPLACIANSMOOTH':
                  iconMod = 'MOD_SMOOTH'
                elif modifier.type in 'LAPLACIANDEFORM':
                  iconMod = 'MOD_MESHDEFORM'
                elif modifier.type in 'LATTICE':
                  iconMod = 'MOD_LATTICE'
                elif modifier.type in 'MESH_DEFORM':
                  iconMod = 'MOD_MESHDEFORM'
                elif modifier.type in 'SHRINKWRAP':
                  iconMod = 'MOD_SHRINKWRAP'
                elif modifier.type in 'SIMPLE_DEFORM':
                  iconMod = 'MOD_SIMPLEDEFORM'
                elif modifier.type in 'SMOOTH':
                  iconMod = 'MOD_SMOOTH'
                elif modifier.type in 'WARP':
                  iconMod = 'MOD_WARP'
                elif modifier.type in 'WAVE':
                  iconMod = 'MOD_WAVE'
                elif modifier.type in 'CLOTH':
                  iconMod = 'MOD_CLOTH'
                elif modifier.type in 'COLLISION':
                  iconMod = 'MOD_PHYSICS'
                elif modifier.type in 'DYNAMIC_PAINT':
                  iconMod = 'MOD_DYNAMICPAINT'
                elif modifier.type in 'EXPLODE':
                  iconMod = 'MOD_EXPLODE'
                elif modifier.type in 'FLUID_SIMULATION':
                  iconMod = 'MOD_FLUIDSIM'
                elif modifier.type in 'OCEAN':
                  iconMod = 'MOD_OCEAN'
                elif modifier.type in 'PARTICLE_INSTANCE':
                  iconMod = 'MOD_PARTICLES'
                elif modifier.type in 'PARTICLE_SYSTEM':
                  iconMod = 'MOD_PARTICLES'
                elif modifier.type in 'SMOKE':
                  iconMod = 'MOD_SMOKE'
                elif modifier.type in 'SOFT_BODY':
                  iconMod = 'MOD_SOFT'
                else:
                  iconMod = 'MODIFIER'
                sub.label(text='', icon=iconMod)
                row.prop(modifier, 'name', text='')
                if modifier.show_viewport:
                  iconView = 'RESTRICT_VIEW_OFF'
                else:
                  iconView = 'RESTRICT_VIEW_ON'
                row.prop(modifier, 'show_viewport', text='', icon=iconView)
                # particle system
                if itemUI.viewParticleSystems:
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
            # materials
            if itemUI.viewMaterials:
              for materialSlot in bpy.data.objects[object.name].material_slots[:]:
                if materialSlot.material != None:
                  if materialSlot.link == 'OBJECT':
                    row = column.row(align=True)
                    sub = row.row()
                    sub.scale_x = 1.6
                    sub.label(text='', icon='MATERIAL')
                    row.prop(materialSlot.material, 'name', text='')
                    # textures
                    if itemUI.viewTextures:
                      if context.scene.render.engine != 'CYCLES':
                        for textureSlot in materialSlot.material.texture_slots[:]:
                          if textureSlot != None:
                            row = column.row(align=True)
                            sub = row.row()
                            sub.scale_x = 1.6
                            sub.label(text='', icon='TEXTURE')
                            row.prop(textureSlot.texture, 'name', text='')
                            if textureSlot.use:
                              iconToggle = 'RADIOBUT_ON'
                            else:
                              iconToggle = 'RADIOBUT_OFF'
                            row.prop(textureSlot, 'use', text='', icon=iconToggle)
            else:
              itemUI.viewTextures = False
    # empty
    if context.object.type in 'EMPTY':
      if context.object.empty_draw_type in 'IMAGE':
        row = column.row(align=True)
        row.template_ID(context.active_object, 'data', open='image.open', unlink='image.unlink')
    # object data
    else:
      row = column.row(align=True)
      row.template_ID(context.active_object, 'data')
      # vertex groups
      if itemUI.viewVertexGroups:
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
      # shape keys
      if itemUI.viewShapeKeys:
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
                sub.scale_x = 0.5
                sub.prop(key, 'value', text='')
              row.prop(key, 'mute', text='', icon='RESTRICT_VIEW_OFF')
      # uv's
      if itemUI.viewUVS:
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
      # vertex colors
      if itemUI.viewVertexColors:
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
      # bone groups
      if itemUI.viewBoneGroups:
        if bpy.data.objects[context.active_object.name].type in 'ARMATURE':
          for group in bpy.data.objects[context.active_object.name].pose.bone_groups[:]:
            row = column.row(align=True)
            sub = row.row()
            sub.scale_x = 1.6
            sub.label(text='', icon='GROUP_BONE')
            row.prop(group, 'name', text='')
      # bones
      if (bpy.data.objects[context.active_object.name].type in 'ARMATURE' and
        context.object.mode in {'POSE', 'EDIT'}):
        row = column.row(align=True)
        sub = row.row(align=True)
        sub.scale_x = 1.6
        sub.prop(itemUI, 'viewSelectedBones', text='', icon='BONE_DATA')
        row.prop(context.active_bone, 'name', text='')
        # bone constraints
        if itemUI.viewBoneConstraints:
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
        # selected bones
        if itemUI.viewSelectedBones:
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
                  if itemUI.viewBoneConstraints:
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
    # materials
    if itemUI.viewMaterials:
      for materialSlot in bpy.data.objects[context.active_object.name].material_slots[:]:
        if materialSlot.material != None:
          if materialSlot.link == 'DATA':
            row = column.row(align=True)
            sub = row.row()
            sub.scale_x = 1.6
            sub.label(text='', icon='MATERIAL')
            row.prop(materialSlot.material, 'name', text='')
            # textures
            if itemUI.viewTextures:
              if context.scene.render.engine != 'CYCLES':
                for textureSlot in materialSlot.material.texture_slots[:]:
                  if textureSlot != None:
                    row = column.row(align=True)
                    sub = row.row()
                    sub.scale_x = 1.6
                    sub.label(text='', icon='TEXTURE')
                    row.prop(textureSlot.texture, 'name', text='')
                    if textureSlot.use:
                      iconToggle = 'RADIOBUT_ON'
                    else:
                      iconToggle = 'RADIOBUT_OFF'
                    row.prop(textureSlot, 'use', text='', icon=iconToggle)
    else:
      itemUI.viewTextures = False
    # view hierarchy
    if itemUI.viewHierarchy:
      for object in bpy.data.objects:
        if object in context.selected_objects:
          if object != context.active_object:
            if object.type != 'EMPTY':
              row = column.row(align=True)
              sub = row.row()
              sub.scale_x = 1.6
              if object.type in 'MESH':
                iconData = 'MESH_DATA'
              elif object.type in 'CURVE':
                iconData = 'CURVE_DATA'
              elif object.type in 'SURFACE':
                iconData = 'SURFACE_DATA'
              elif object.type in 'META':
                iconData = 'META_DATA'
              elif object.type in 'FONT':
                iconData = 'FONT_DATA'
              elif object.type in 'ARMATURE':
                iconData = 'ARMATURE_DATA'
              elif object.type in 'LATTICE':
                iconData = 'LATTICE_DATA'
              elif object.type in 'SPEAKER':
                iconData = 'SPEAKER'
              elif object.type in 'CAMERA':
                iconData = 'CAMERA_DATA'
              elif object.type in 'LAMP':
                iconData = 'LAMP_DATA'
              else:
                iconData = 'MESH_DATA'
              sub.label(text='', icon=iconData)
              row.prop(object.data, 'name', text='')
              # vertex groups
              if itemUI.viewVertexGroups:
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
              # shape keys
              if itemUI.viewShapeKeys:
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
                        sub.scale_x = 0.5
                        sub.prop(key, 'value', text='')
                      row.prop(key, 'mute', text='', icon='RESTRICT_VIEW_OFF')
              # uv's
              if itemUI.viewUVS:
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
              # vertex colors
              if itemUI.viewVertexColors:
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
              # bone groups
              if itemUI.viewBoneGroups:
                if bpy.data.objects[object.name].type in 'ARMATURE':
                  for group in bpy.data.objects[object.name].pose.bone_groups[:]:
                    row = column.row(align=True)
                    sub = row.row()
                    sub.scale_x = 1.6
                    sub.label(text='', icon='GROUP_BONE')
                    row.prop(group, 'name', text='')
              # materials
              if itemUI.viewMaterials:
                for materialSlot in bpy.data.objects[object.name].material_slots[:]:
                  if materialSlot.material != None:
                    if materialSlot.link == 'DATA':
                      row = column.row(align=True)
                      sub = row.row()
                      sub.scale_x = 1.6
                      sub.label(text='', icon='MATERIAL')
                      row.prop(materialSlot.material, 'name', text='')
                      # textures
                      if itemUI.viewTextures:
                        if context.scene.render.engine != 'CYCLES':
                          for textureSlot in materialSlot.material.texture_slots[:]:
                            if textureSlot != None:
                              row = column.row(align=True)
                              sub = row.row()
                              sub.scale_x = 1.6
                              sub.label(text='', icon='TEXTURE')
                              row.prop(textureSlot.texture, 'name', text='')
                              if textureSlot.use:
                                iconToggle = 'RADIOBUT_ON'
                              else:
                                iconToggle = 'RADIOBUT_OFF'
                              row.prop(textureSlot, 'use', text='', icon=iconToggle)
              else:
                itemUI.viewTextures = False

##############
## REGISTER ##
##############

# register
def register():
  """ Register """
  windowManager = bpy.types.WindowManager
  bpy.utils.register_module(__name__)
  windowManager.itemUI = bpy.props.PointerProperty(type=itemUIPropertyGroup)
  bpy.context.window_manager.itemUI.name = 'Item Panel Properties'
  bpy.types.VIEW3D_PT_view3d_name.remove(bpy.types.VIEW3D_PT_view3d_name.draw)
  bpy.types.VIEW3D_PT_view3d_name.append(itemPanel.draw)

# unregister
def unregister():
  """ Unregister """
  bpy.utils.unregister_module(__name__)
  try:
    del bpy.types.WindowManager.itemUI
  except:
    pass
if __name__ in '__main__':
  register()
