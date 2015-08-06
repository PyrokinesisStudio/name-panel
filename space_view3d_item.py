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
#  Version: 0.8.9
#
# ##### END INFO BLOCK #####

# blender info
bl_info = {
  'name': 'Item Panel & Batch Naming',
  'author': 'proxe',
  'version': (0, 8, 9),
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
  if dataPath in {'constraint', 'modifier'}:
    dataPath.name = targetName
  else:
    dataPath.name = targetName[:]

# batch rename
def batchRename(self, context, batchName, find, replace, prefix, suffix, trimStart, trimEnd, batchObjects, batchObjectConstraints, batchModifiers, batchObjectData, batchBones, batchBoneConstraints, objectType, constraintType, modifierType):
  """
  Send dataPath values to rename, check variable values from operator class.
  """
  # objects
  if batchObjects:
    for object in context.selected_objects:
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
    for object in context.selected_objects:
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
    for object in context.selected_objects:
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
      for object in context.selected_objects:
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
    if context.selected_pose_bones or context.selected_editable_bones:
      if context.selected_editable_bones:
        selected_bones = context.selected_editable_bones
      else:
        selected_bones = context.selected_pose_bones
      for bone in selected_bones:
        dataPath = bone
        try:
          rename(self, dataPath, batchName, find, replace, prefix, suffix, trimStart, trimEnd)
        except:
            pass
  # bone constraints
  if batchBoneConstraints:
    for bone in context.selected_pose_bones:
      for constraint in bone.constraints[:]:
        if constraintType in 'ALL':
          dataPath = constraint
        elif constraintType in contraint.type:
          dataPath = constraint
        try:
          rename(self, dataPath, batchName, find, replace, prefix, suffix, trimStart, trimEnd)
        except:
            pass
  # materials
  # textures

###############
## OPERATORS ##
###############

# batch naming
class VIEW3D_OT_batch_naming(Operator):
  """ Invoke the batch naming operator. """
  bl_idname = 'view3d.batch_naming'
  bl_label = 'Batch Naming'
  bl_options = {'REGISTER', 'UNDO'}
  # batch objects
  batchObjects = BoolProperty(
    name = 'Objects',
    description = "Apply batch naming to the selected objects.",
    default = False
  )
  # batch object constraints
  batchObjectConstraints = BoolProperty(
    name = 'Object Constraints',
    description = "Apply batch naming to the constraints of the selected objects.",
    default = False
  )
  # batch modifiers
  batchModifiers = BoolProperty(
    name = 'Modifiers',
    description = "Apply batch naaming to the modifiers of the selected objects.",
    default = False
  )
  # batch object data
  batchObjectsData = BoolProperty(
    name = 'Object Data',
    description = "Apply batch naming to the object data of the selected objects.",
    default = False
  )
  # batch bones
  batchBones = BoolProperty(
    name = 'Bones',
    description = "Apply batch naming to the selected bones.",
    default = False
  )
  # batch bone constraints
  batchBoneConstraints = BoolProperty(
    name = 'Bone Constraints',
    description = "Apply batch naming to the constraints of the selected bones.",
    default = False
  )
  # object type
  objectType = EnumProperty(
    name = 'Type',
    description = "The type of object that the batch naming operations will be performed on.",
    items = [
      ('ALL', 'All Objects', ""),
      ('MESH', 'Mesh', ""),
      ('CURVE', 'Curve', ""),
      ('SURFACE', 'Surface', ""),
      ('META', 'Meta', ""),
      ('FONT', 'Font', ""),
      ('ARMATURE', 'Armature', ""),
      ('LATTICE', 'Lattice', ""),
      ('EMPTY', 'Empty', ""),
      ('SPEAKER', 'Speaker', ""),
      ('CAMERA', 'Camera', ""),
      ('LAMP', 'Lamp', "")
    ],
    default = 'ALL'
  )
  # constraint type
  constraintType = EnumProperty(
    name = 'Type',
    description = "The type of constraint that the batch naming operations will be performed on.",
    items = [
      ('ALL', 'All Constraints', ""),
      ('CAMERA_SOLVER', 'Camera Solver', ""),
      ('OBJECT_SOLVER', 'Object Solver', ""),
      ('FOLLOW_TRACK', 'Follow Track', ""),
      ('COPY_LOCATION', 'Copy Location', ""),
      ('COPY_ROTATION', 'Copy Rotation', ""),
      ('COPY_SCALE', 'Copy Scale', ""),
      ('COPY_TRANSFORMS', 'Copy Transforms', ""),
      ('LIMIT_DISTANCE', 'Limit Distance', ""),
      ('LIMIT_LOCATION', 'Limit Location', ""),
      ('LIMIT_ROTATION', 'Limit Rotation', ""),
      ('LIMIT_SCALE', 'Limit Scale', ""),
      ('MAINTAIN_VOLUME', 'Maintain Volume', ""),
      ('TRANSFORM', 'Transformation', ""),
      ('CLAMP_TO', 'Clamp To', ""),
      ('DAMPED_TRACK', 'Damped Track', ""),
      ('IK', 'IK', ""),
      ('LOCKED_TRACK', 'Locked Track', ""),
      ('SPLINE_IK', 'Spline IK', ""),
      ('STRETCH_TO', 'Stretch To', ""),
      ('TRACK_TO', 'TrackTo', ""),
      ('ACTION', 'Action', ""),
      ('CHILD_OF', 'ChildOf', ""),
      ('FLOOR', 'Floor', ""),
      ('FOLLOW_PATH', 'Follow Path', ""),
      ('PIVOT', 'Pivot', ""),
      ('RIGID_BODY_JOINT', 'Rigid Body Joint', ""),
      ('SCRIPT', 'Script', ""),
      ('SHRINKWRAP', 'Shrinkwrap', "")
    ],
    default = 'ALL'
  )
  # modifier type
  modifierType = EnumProperty(
    name = 'Type',
    description = "The type of modifier that the batch naming operations will be performed on.",
    items = [
      ('ALL', 'All Modifiers', ""),
      ('DATA_TRANSFER', 'Mesh Cache', ""),
      ('MESH_CACHE', 'Mesh Cache', ""),
      ('NORMAL_EDIT', 'Normal Edit', ""),
      ('UV_PROJECT', 'UV Project', ""),
      ('VERTEX_WEIGHT_EDIT', 'Vertex Weight Edit', ""),
      ('VERTEX_WEIGHT_MIX', 'Vertex Weight Mix', ""),
      ('VERTEX_WEIGHT_PROXIMITY', 'Vertex Weight Proximity', ""),
      ('ARRAY', 'Array', ""),
      ('BEVEL', 'Bevel', ""),
      ('BOOLEAN', 'Boolean', ""),
      ('BUILD', 'Build', ""),
      ('DECIMATE', 'Decimate', ""),
      ('EDGE_SPLIT', 'Edge Split', ""),
      ('MASK', 'Mask', ""),
      ('MIRROR', 'Mirror', ""),
      ('MULTIRES', 'Multiresolution', ""),
      ('REMESH', 'Remesh', ""),
      ('SCREW', 'Screw', ""),
      ('SKIN', 'Skin', ""),
      ('SOLIDIFY', 'Solidify', ""),
      ('SUBSURF', 'Subdivision Surface', ""),
      ('TRIANGULATE', 'Triangulate', ""),
      ('WIREFRAME', 'Wireframe', ""),
      ('ARMATURE', 'Armature', ""),
      ('CAST', 'Cast', ""),
      ('CURVE', 'Curve', ""),
      ('DISPLACE', 'Displace', ""),
      ('HOOK', 'Hook', ""),
      ('LAPLACIANSMOOTH', 'Laplacian Smooth', ""),
      ('LAPLACIANDEFORM', 'Laplacian Deform', ""),
      ('LATTICE', 'Lattice', ""),
      ('MESH_DEFORM', 'Mesh Deform', ""),
      ('SHRINKWRAP', 'Shrinkwrap', ""),
      ('SIMPLE_DEFORM', 'Simple Deform', ""),
      ('SMOOTH', 'Smooth', ""),
      ('WARP', 'Warp', ""),
      ('WAVE', 'Wave', ""),
      ('CLOTH', 'Cloth', ""),
      ('COLLISION', 'Collision', ""),
      ('DYNAMIC_PAINT', 'Dynamic Paint', ""),
      ('EXPLODE', 'Explode', ""),
      ('FLUID_SIMULATION', 'Fluid Simulation', ""),
      ('OCEAN', 'Ocean', ""),
      ('PARTICLE_INSTANCE', 'Particle Instance', ""),
      ('PARTICLE_SYSTEM', 'Particle System', ""),
      ('SMOKE', 'Smoke', ""),
      ('UV_WARP', 'UV Warp', ""),
      ('SOFT_BODY', 'Soft Body', "")
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
    column = layout.column()
    row = column.row(align=True)
    # type row
    split = column.split(align=True)
    split.prop(self.properties, 'batchObjects', text='', icon='OBJECT_DATA')
    split.prop(self.properties, 'batchObjectConstraints', text='', icon='CONSTRAINT')
    split.prop(self.properties, 'batchModifiers', text='', icon='MODIFIER')
    split.prop(self.properties, 'batchObjectsData', text='', icon='MESH_DATA')
    if context.selected_pose_bones or context.selected_editable_bones:
      split.prop(self.properties, 'batchBones', text='', icon='BONE_DATA')
      if context.selected_pose_bones:
        split.prop(self.properties, 'batchBoneConstraints', text='', icon='CONSTRAINT_BONE')
    # type filters
    column.prop(self.properties, 'objectType', text='', icon='OBJECT_DATA')
    column.prop(self.properties, 'constraintType', text='', icon='CONSTRAINT')
    column.prop(self.properties, 'modifierType', text='', icon='MODIFIER')
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
    batchRename(self, context, self.batchName, self.find, self.replace, self.prefix, self.suffix, self.trimStart, self.trimEnd, self.batchObjects, self.batchObjectConstraints, self.batchModifiers, self.batchObjectsData, self.batchBones, self.batchBoneConstraints, self.objectType, self.constraintType, self.modifierType)
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
  # view constraints
  viewConstraints = BoolProperty(
    name = 'View object constraints',
    description = "Display the object constraints.",
    default = True
  )
  # view modifiers
  viewModifiers = BoolProperty(
    name = 'View object modifiers',
    description = "Display the object modifiers.",
    default = True
  )
  # view bone constraints
  viewBoneConstraints = BoolProperty(
    name = 'View bone constraints',
    description = "Display the bone constraints.",
    default = True
  )
  # view materials
  viewMaterials = BoolProperty(
    name = 'View object materials',
    description = "Display the object materials",
    default = True
  )
  # view textures
  viewTextures = BoolProperty(
    name = 'View material textures.',
    description = "Display the textures of the object's material(s)",
    default = True
  )
  # view hierarchy
  viewHierarchy = BoolProperty(
    name = 'View all selected',
    description = "Display everything within your current selection inside the item panel.",
    default = False
  )

# item panel
class item_panel():
  """
  Item panel
  """

  # draw
  def draw(self, context):
    """ Item panel body. """
    layout = self.layout
    column = layout.column()
    itemUI = context.window_manager.itemUI
    # view options row
    split = column.split(align=True)
    split.prop(itemUI, 'viewConstraints', text='', icon='CONSTRAINT')
    split.prop(itemUI, 'viewModifiers', text='', icon='MODIFIER')
    if context.object.mode in 'POSE':
      split.prop(itemUI, 'viewBoneConstraints', text='', icon='CONSTRAINT_BONE')
    split.prop(itemUI, 'viewMaterials', text='', icon='MATERIAL')
    split.prop(itemUI, 'viewTextures', text='', icon='TEXTURE')
    split.prop(itemUI, 'viewHierarchy', text='', icon='OOPS')
    split.operator('view3d.batch_naming', text='', icon='AUTO')
    # data block list
    row = column.row(align = True)
    row.template_ID(context.scene.objects, 'active')
    # constraints
    if itemUI.viewConstraints:
      for constraint in context.active_object.constraints:
        row = column.row(align=True)
        sub = row.row()
        sub.scale_x = 1.6
        sub.label(text='', icon='CONSTRAINT')
        if constraint.mute:
          iconView = 'RESTRICT_VIEW_ON'
        else:
          iconView = 'RESTRICT_VIEW_OFF'
        row.prop(constraint, 'mute', text='', icon=iconView)
        row.prop(constraint, 'name', text='')
    # modifiers
    if itemUI.viewModifiers:
      for modifier in context.active_object.modifiers:
        row = column.row(align=True)
        sub = row.row()
        sub.scale_x = 1.6
        if modifier.type in 'DATA_TRANSFER':
          iconMod = 'MOD_DATA_TRANSFER'
        elif modifier.type in 'MESH_CACHE':
          iconMod = 'MOD_MESHDEFORM'
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
        elif modifier.type in 'ARMATURE':
          iconMod = 'MOD_ARMATURE'
        elif modifier.type in 'CAST':
          iconMod = 'MOD_CAST'
        elif modifier.type in 'CURVE':
          iconMod = 'MOD_CURVE'
        elif modifier.type in 'DISPLACE':
          iconMod = 'MOD_DISPLACE'
        elif modifier.type in 'HOOK':
          iconMod = 'HOOK'
        elif modifier.type in 'LAPLACIANSMOOTH':
          iconMod = 'MOD_SMOOTH'
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
        if modifier.show_viewport:
          iconView = 'RESTRICT_VIEW_OFF'
        else:
          iconView = 'RESTRICT_VIEW_ON'
        row.prop(modifier, 'show_viewport', text='', icon=iconView)
        row.prop(modifier, 'name', text='')
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
                    if textureSlot.use:
                      iconToggle = 'RADIOBUT_ON'
                    else:
                      iconToggle = 'RADIOBUT_OFF'
                    row.prop(textureSlot, 'use', text='', icon=iconToggle)
                    row.prop(textureSlot.texture, 'name', text='')
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
            # constraints
            if itemUI.viewConstraints:
              for constraint in object.constraints[:]:
                row = column.row(align=True)
                sub = row.row()
                sub.scale_x = 1.6
                sub.label(text='', icon='CONSTRAINT')
                if constraint.mute:
                  iconView = 'RESTRICT_VIEW_ON'
                else:
                  iconView = 'RESTRICT_VIEW_OFF'
                row.prop(constraint, 'mute', text='', icon=iconView)
                row.prop(constraint, 'name', text='')
            # modifiers
            if itemUI.viewModifiers:
              for modifier in object.modifiers[:]:
                row = column.row(align=True)
                sub = row.row()
                sub.scale_x = 1.6
                if modifier.type in 'MESH_CACHE':
                  iconMod = 'MOD_MESHDEFORM'
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
                elif modifier.type in 'ARMATURE':
                  iconMod = 'MOD_ARMATURE'
                elif modifier.type in 'CAST':
                  iconMod = 'MOD_CAST'
                elif modifier.type in 'CURVE':
                  iconMod = 'MOD_CURVE'
                elif modifier.type in 'DISPLACE':
                  iconMod = 'MOD_DISPLACE'
                elif modifier.type in 'HOOK':
                  iconMod = 'HOOK'
                elif modifier.type in 'LAPLACIANSMOOTH':
                  iconMod = 'MOD_SMOOTH'
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
                if modifier.show_viewport:
                  iconView = 'RESTRICT_VIEW_OFF'
                else:
                  iconView = 'RESTRICT_VIEW_ON'
                row.prop(modifier, 'show_viewport', text='', icon=iconView)
                row.prop(modifier, 'name', text='')
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
                            if textureSlot.use:
                              iconToggle = 'RADIOBUT_ON'
                            else:
                              iconToggle = 'RADIOBUT_OFF'
                            row.prop(textureSlot, 'use', text='', icon=iconToggle)
                            row.prop(textureSlot.texture, 'name', text='')
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
    # bones
    if (context.object.type in 'ARMATURE' and
      context.object.mode in {'POSE', 'EDIT'}):
      row = column.row(align=True)
      sub = row.row()
      sub.scale_x = 1.6
      sub.label(text='', icon='BONE_DATA')
      row.prop(context.active_bone, 'name', text='')
      if context.object.mode in 'POSE':
        if itemUI.viewBoneConstraints:
          for constraint in context.active_pose_bone.constraints:
            row = column.row(align=True)
            sub = row.row()
            sub.scale_x = 1.6
            sub.label(text='', icon='CONSTRAINT_BONE')
            if constraint.mute:
              iconView = 'RESTRICT_VIEW_ON'
            else:
              iconView = 'RESTRICT_VIEW_OFF'
            row.prop(constraint, 'mute', text='', icon=iconView)
            row.prop(constraint, 'name', text='')
      if itemUI.viewHierarchy:
        if context.selected_editable_bones:
          selectedBones = context.selected_editable_bones
        else:
          selectedBones = context.selected_pose_bones
        for bone in selectedBones:
          if bone in (context.selected_editable_bones or context.selected_pose_bones):
            if bone != (context.active_pose_bone or context.active_bone):
              row = column.row(align=True)
              sub = row.row()
              sub.scale_x = 1.6
              sub.label(text='', icon='BONE_DATA')
              row.prop(bone, 'name', text='')
              if context.object.mode in 'POSE':
                if itemUI.viewBoneConstraints:
                  for constraint in bone.constraints[:]:
                    row = column.row(align=True)
                    sub = row.row()
                    sub.scale_x = 1.6
                    sub.label(text='', icon='CONSTRAINT_BONE')
                    if constraint.mute:
                      iconView = 'RESTRICT_VIEW_ON'
                    else:
                      iconView = 'RESTRICT_VIEW_OFF'
                    row.prop(constraint, 'mute', text='', icon=iconView)
                    row.prop(constraint, 'name', text='')
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
                    if textureSlot.use:
                      iconToggle = 'RADIOBUT_ON'
                    else:
                      iconToggle = 'RADIOBUT_OFF'
                    row.prop(textureSlot, 'use', text='', icon=iconToggle)
                    row.prop(textureSlot.texture, 'name', text='')
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
                              if textureSlot.use:
                                iconToggle = 'RADIOBUT_ON'
                              else:
                                iconToggle = 'RADIOBUT_OFF'
                              row.prop(textureSlot, 'use', text='', icon=iconToggle)
                              row.prop(textureSlot.texture, 'name', text='')
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
  bpy.types.VIEW3D_PT_view3d_name.append(item_panel.draw)

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
