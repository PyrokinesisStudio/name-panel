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

bl_info = {'name': 'Item Panel & Batch Naming',
           'author': 'proxe',
           'version': (0, 8, 4),
           'blender': (2, 66, 0),
           'location': '3D View > Properties Panel',
           'warning': 'Work in Progress',
           #'wiki_url': '',
           #'tracker_url': '',
           'description': "An improved item panel for the 3D View with included"
                          " batch naming tools.",
           'category': '3D View'}

import bpy

# ##### BEGIN INFO BLOCK #####
#
#    Author: Trentin Frederick (a.k.a, proxe)
#    Contact: trentin.frederick@gmail.com, proxe.err0r@gmail.com
#    Version: 0.8.4
#
# ##### END INFO BLOCK #####

  # PEP8 Compliant (mostly)

###############
## FUNCTIONS ##
###############
  # Imports
import re


  # reName
def rename(self, dataPath, batchName, find, replace, prefix, suffix,
           trimStart, trimEnd):
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
    targetName = re.sub(find, replace, targetName)  # XXX: Tool-shelf RE error.
    targetName = prefix + targetName + suffix
    if dataPath in {'constraint', 'modifier'}:
        dataPath.name = targetName
    else:
        dataPath.name = targetName[:]


  # Batch Rename
def batchRename(self, context, batchName, find, replace, prefix, suffix,
                trimStart, trimEnd, batchObjects, batchObjectConstraints,
                batchModifiers, batchObjectData, batchBones,
                batchBoneConstraints, objectType, constraintType, modifierType):
    """
    Send dataPath values to rename, check variable values from operator class.
    """
  # Objects
    if batchObjects:
        for object in context.selected_objects:
            if objectType in 'ALL':
                dataPath = object
            else:
                if objectType in object.type:
                    dataPath = object
                else:
                    pass
            try:
                rename(self, dataPath, batchName, find, replace, prefix,
                       suffix, trimStart, trimEnd)
            except:
                pass
    else:
        pass
  # Object Constraints
    if batchObjectConstraints:
        for object in context.selected_objects:
            for constraint in object.constraints[:]:
                if constraintType in 'ALL':
                    dataPath = constraint
                else:
                    if constraintType in constraint.type:
                        dataPath = constraint
                    else:
                        pass
                try:
                    rename(self, dataPath, batchName, find, replace, prefix,
                           suffix, trimStart, trimEnd)
                except:
                    pass
    else:
        pass
  # Modifiers
    if batchModifiers:
        for object in context.selected_objects:
            for modifier in object.modifiers[:]:
                if modifierType in 'ALL':
                    dataPath = modifier
                else:
                    if modifierType in modifier.type:
                        dataPath = modifier
                    else:
                        pass
                try:
                    rename(self, dataPath, batchName, find, replace, prefix,
                           suffix, trimStart, trimEnd)
                except:
                    pass
    else:
        pass
  # Objects Data
    if batchObjectData:
        for object in context.selected_objects:
            if objectType in 'ALL':
                dataPath = object.data
            else:
                if objectType in object.type:
                    dataPath = object.data
                else:
                    pass
            try:
                rename(self, dataPath, batchName, find, replace, prefix,
                       suffix, trimStart, trimEnd)
            except:
                pass
    else:
        pass
  # Bones
    if batchBones:
        if context.selected_pose_bones or context.selected_editable_bones:
            if context.selected_editable_bones:
                selected_bones = context.selected_editable_bones
            else:
                selected_bones = context.selected_pose_bones
            for bone in selected_bones:
                dataPath = bone
                try:
                    rename(self, dataPath, batchName, find, replace, prefix,
                           suffix, trimStart, trimEnd)
                except:
                    pass
        else:
            pass
    else:
        pass
  # Bone Constraints
    if batchBoneConstraints:
        for bone in context.selected_pose_bones:
            for constraint in bone.constraints[:]:
                if constraintType in 'ALL':
                    dataPath = constraint
                else:
                    if constraintType in contraint.type:
                        dataPath = constraint
                    else:
                        pass
                try:
                    rename(self, dataPath, batchName, find, replace, prefix,
                           suffix, trimStart, trimEnd)
                except:
                    pass
    else:
        pass

###############
## OPERATORS ##
###############
  # Imports
from bpy.props import *
from bpy.types import Operator


  # View 3D Batch Naming (OT)
class VIEW3D_OT_batch_naming(Operator):
    """ Invoke the batch naming operator. """
    bl_idname = 'view3d.batch_naming'
    bl_label = 'Batch Naming'
    bl_options = {'REGISTER', 'UNDO'}

    batchName = StringProperty(name='Name', description="Designate a new name, "
                               "if blank, the current names are effected by an"
                               "y changes to the parameters below.")

    find = StringProperty(name='Find', description="Find this text and remove i"
                          "t from the names.")

    replace = StringProperty(name='Replace', description="Replace found text wi"
                             "thin the names with the text entered here.")

    prefix = StringProperty(name='Prefix', description="Designate a prefix to u"
                            "se for the names.")

    suffix = StringProperty(name='Suffix', description="Designate a suffix to u"
                            "se for the names")

    trimStart = IntProperty(name='Trim Start', description="Trim the beginning "
                            "of the names by this amount.", min=0, max=50,
                            default=0)

    trimEnd = IntProperty(name='Trim End', description="Trim the ending of the "
                          "names by this amount.", min=0, max=50, default=0)

    batchObjects = BoolProperty(name='Objects', description="Apply batch naming"
                                " to the selected objects.", default=False)

    batchObjectConstraints = BoolProperty(name='Object Constraints',
                                          description="Apply batch naming to th"
                                          "e constraints of the selected object"
                                          "s.", default=False)

    batchModifiers = BoolProperty(name='Modifiers', description="Apply batch na"
                                  "aming to the modifiers of the selected obje"
                                  "cts.", default=False)

    batchObjectsData = BoolProperty(name='Object Data', description="Apply batc"
                                    "h naming to the object data of the selecte"
                                    "d objects.", default=False)

    batchBones = BoolProperty(name='Bones', description="Apply batch naming to "
                              "the selected bones.", default=False)

    batchBoneConstraints = BoolProperty(name='Bone Constraints',
                                        description="Apply batch naming to the "
                                        "constraints of the selected bones.",
                                        default=False)

    objectType = EnumProperty(name='Type', description="The type of object that"
                              " the batch naming operations will be performed o"
                              "n.", items=[('LAMP', 'Lamp', ""),
                                           ('CAMERA', 'Camera', ""),
                                           ('SPEAKER', 'Speaker', ""),
                                           ('EMPTY', 'Empty', ""),
                                           ('LATTICE', 'Lattice', ""),
                                           ('ARMATURE', 'Armature', ""),
                                           ('FONT', 'Font', ""),
                                           ('META', 'Meta', ""),
                                           ('SURFACE', 'Surface', ""),
                                           ('CURVE', 'Curve', ""),
                                           ('MESH', 'Mesh', ""),
                                           ('ALL', 'All Objects', "")],
                                           default='ALL')

    constraintType = EnumProperty(name='Type', description="The type of constra"
                                  "int that the batch naming operations will be"
                                  " performed on.",
                                  items=[('SHRINKWRAP', 'Shrinkwrap', ""),
                                         ('SCRIPT', 'Script', ""),
                                         ('RIGID_BODY_JOINT',
                                          'Rigid Body Joint', ""),
                                         ('PIVOT', 'Pivot', ""),
                                         ('FOLLOW_PATH', 'Follow Path', ""),
                                         ('FLOOR', 'Floor', ""),
                                         ('CHILD_OF', 'ChildOf', ""),
                                         ('ACTION', 'Action', ""),
                                         ('TRACK_TO', 'TrackTo', ""),
                                         ('STRETCH_TO', 'Stretch To', ""),
                                         ('SPLINE_IK', 'Spline IK', ""),
                                         ('LOCKED_TRACK', 'Locked Track', ""),
                                         ('IK', 'IK', ""),
                                         ('DAMPED_TRACK', 'Damped Track',
                                          ""),
                                         ('CLAMP_TO', 'Clamp To', ""),
                                         ('TRANSFORM', 'Transformation', ""),
                                         ('MAINTAIN_VOLUME', 'Maintain Volume',
                                          ""),
                                         ('LIMIT_SCALE', 'Limit Scale', ""),
                                         ('LIMIT_ROTATION', 'Limit Rotation',
                                          ""),
                                         ('LIMIT_LOCATION', 'Limit Location',
                                          ""),
                                         ('LIMIT_DISTANCE', 'Limit Distance',
                                          ""),
                                         ('COPY_TRANSFORMS', 'Copy Transforms',
                                          ""),
                                         ('COPY_SCALE', 'Copy Scale', ""),
                                         ('COPY_ROTATION', 'Copy Rotation',
                                          ""),
                                         ('COPY_LOCATION', 'Copy Location',
                                          ""),
                                         ('FOLLOW_TRACK', 'Follow Track', ""),
                                         ('OBJECT_SOLVER', 'Object Solver',
                                          ""),
                                         ('CAMERA_SOLVER', 'Camera Solver',
                                          ""),
                                         ('ALL', 'All Constraints', "")],
                                         default='ALL')

    modifierType = EnumProperty(name='Type', description="The type of modifier "
                                "that the batch naming operations will be perfo"
                                "rmed on.",
                                items=[('SOFT_BODY', 'Soft Body', ""),
                                       ('SMOKE', 'Smoke', ""),
                                       ('PARTICLE_SYSTEM', 'Particle System',
                                        ""),
                                       ('PARTICLE_INSTANCE',
                                        'Particle Instance', ""),
                                       ('OCEAN', 'Ocean', ""),
                                       ('FLUID_SIMULATION', 'Fluid Simulation',
                                        ""),
                                       ('EXPLODE', 'Explode', ""),
                                       ('DYNAMIC_PAINT', 'Dynamic Paint', ""),
                                       ('COLLISION', 'Collision', ""),
                                       ('CLOTH', 'Cloth', ""),
                                       ('WAVE', 'Wave', ""),
                                       ('WARP', 'Warp', ""),
                                       ('SMOOTH', 'Smooth', ""),
                                       ('SIMPLE_DEFORM', 'Simple Deform', ""),
                                       ('SHRINKWRAP', 'Shrinkwrap', ""),
                                       ('MESH_DEFORM', 'Mesh Deform', ""),
                                       ('LATTICE', 'Lattice', ""),
                                       ('LAPLACIANSMOOTH', 'Laplacian Smooth',
                                        ""),
                                       ('HOOK', 'Hook', ""),
                                       ('DISPLACE', 'Displace',
                                        ""),
                                       ('CURVE', 'Curve', ""),
                                       ('CAST', 'Cast', ""),
                                       ('ARMATURE', 'Armature', ""),
                                       ('TRIANGULATE', 'Triangulate', ""),
                                       ('SUBSURF', 'Subdivision Surface', ""),
                                       ('SOLIDIFY', 'Solidify', ""),
                                       ('SKIN', 'Skin', ""),
                                       ('SCREW', 'Screw', ""),
                                       ('REMESH', 'Remesh', ""),
                                       ('MULTIRES', 'Multiresolution', ""),
                                       ('MIRROR', 'Mirror', ""),
                                       ('MASK', 'Mask', ""),
                                       ('EDGE_SPLIT', 'Edge Split', ""),
                                       ('DECIMATE', 'Decimate', ""),
                                       ('BUILD', 'Build', ""),
                                       ('BOOLEAN', 'Boolean', ""),
                                       ('BEVEL', 'Bevel', ""),
                                       ('ARRAY', 'Array', ""),
                                       ('VERTEX_WEIGHT_PROXIMITY',
                                        'Vertex Weight Proximity', ""),
                                       ('VERTEX_WEIGHT_MIX',
                                        'Vertex Weight Mix', ""),
                                       ('VERTEX_WEIGHT_EDIT',
                                        'Vertex Weight Edit', ""),
                                       ('UV_WARP', 'UV Warp', ""),
                                       ('UV_PROJECT', 'UV Project', ""),
                                       ('MESH_CACHE', 'Mesh Cache', ""),
                                       ('ALL', 'All Modifiers', "")],
                                       default='ALL')

    @classmethod
    def poll(cls, context):
        """ Space data type must be in 3D view. """
        return context.space_data.type in 'VIEW_3D'

    def draw(self, context):
        """ Draw the operator panel/menu. """
        layout = self.layout
        column = layout.column()
        row = column.row(align=True)
  # Target Row
        split = column.split(align=True)
        split.prop(self.properties, 'batchObjects', text="", icon='OBJECT_DATA')
        split.prop(self.properties, 'batchObjectConstraints', text="",
                   icon='CONSTRAINT')
        split.prop(self.properties, 'batchModifiers', text="", icon='MODIFIER')
        split.prop(self.properties, 'batchObjectsData', text="",
                   icon='MESH_DATA')
        if context.selected_pose_bones or context.selected_editable_bones:
            split.prop(self.properties, 'batchBones', text="", icon='BONE_DATA')
            if context.selected_pose_bones:
                split.prop(self.properties, 'batchBoneConstraints', text="",
                           icon='CONSTRAINT_BONE')
            else:
                pass
        else:
            pass
  # Target Types
        column.prop(self.properties, 'objectType', text="", icon='OBJECT_DATA')
        column.prop(self.properties, 'constraintType', text="",
                    icon='CONSTRAINT')
        column.prop(self.properties, 'modifierType', text="", icon='MODIFIER')
  # Input Fields
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
        row.prop(self.properties, 'trimStart', text="")
        row = column.row()
        row.label(text="Trim End:")
        row.prop(self.properties, 'trimEnd', text="")

    def execute(self, context):
        """Execute the operator."""
        batchRename(self, context, self.batchName, self.find, self.replace,
                    self.prefix, self.suffix, self.trimStart, self.trimEnd,
                    self.batchObjects, self.batchObjectConstraints,
                    self.batchModifiers, self.batchObjectsData,
                    self.batchBones, self.batchBoneConstraints,
                    self.objectType, self.constraintType,
                    self.modifierType)
        return {'FINISHED'}

    def invoke(self, context, event):
        """Invoke the operator panel/menu, control its width."""
        context.window_manager.invoke_props_dialog(self, width=225)

        return {'RUNNING_MODAL'}

###############
## INTERFACE ##
###############
  # Imports
from bpy.types import Panel, PropertyGroup


  # Item Panel Property Group
class itemUIPropertyGroup(PropertyGroup):
    """
    UI property group for the add-on "Item Panel & Batch Naming"
    (space_view3d_item.py)

    Bool Properties that effect how the panel displays the item(s) within the
    users current selection

    bpy > types > WindowManager > itemUI
    bpy > context > window_manager > itemUI
    """
    viewOptions = BoolProperty(name='Show/hide view options',
                               description="Toggle view options for this panel,"
                               " the state that they are in is uneffected by th"
                               "is action.", default=False)
    viewConstraints = BoolProperty(name='View object constraints',
                                   description="Display the object constraints "
                                   "of the active object.", default=True)
    viewModifiers = BoolProperty(name='View object modifiers', description="Dis"
                                  "play the object modifiers of the active obje"
                                  "ct.", default=True)
    viewBoneConstraints = BoolProperty(name='View bone constraints',
                                       description="Display the bone constraint"
                                       "s of the active pose bone.",
                                       default=True)
    objectDataUsers = BoolProperty(name='Users', description="Number of times t"
                                   "his datablock is referenced.",
                                   default=False)  # Hack, but it works great.
    viewHierarchy = BoolProperty(name='View all selected', description="Display"
                                 " everything within your current selection ins"
                                 "ide the item panel.", default=False)


  # View 3D Item (PT)
class VIEW3D_PT_item(Panel):
    """
    Item panel, properties created in Item property group, stored in:
    bpy > context > window_manager > itemUI
    """
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_label = 'Item'

    @classmethod
    def poll(cls, context):
        """ Hide panel if there is not an active object. """
        return bpy.context.active_object

    def draw_header(self, context):
        """ Item panel header. """
        layout = self.layout
        itemUI = context.window_manager.itemUI

        layout.prop(itemUI, 'viewOptions', text="")

    def draw(self, context):
        """ Item panel body. """
        layout = self.layout
        column = layout.column()
        itemUI = context.window_manager.itemUI
  # View options row
        split = column.split(align=True)
        if itemUI.viewOptions:
            split.prop(itemUI, 'viewConstraints', text="",
                       icon='CONSTRAINT')
            split.prop(itemUI, 'viewModifiers', text="", icon='MODIFIER')
            if context.object.mode in 'POSE':
                split.prop(itemUI, 'viewBoneConstraints', text="",
                           icon='CONSTRAINT_BONE')
            else:
                pass
            split.prop(itemUI, 'viewHierarchy', text="", icon='OOPS')
        else:
            pass
  # Data block list
        row = column.row(align=True)
        row.template_ID(context.scene.objects, 'active')
        row.operator('view3d.batch_naming', text="", icon='AUTO')
        if itemUI.viewConstraints:
            for constraint in context.active_object.constraints:
                row = column.row(align=True)
                sub = row.row()
                sub.scale_x = 1.6
                sub.label(text="", icon='CONSTRAINT')
                if constraint.mute:
                    iconView = 'RESTRICT_VIEW_ON'
                else:
                    iconView = 'RESTRICT_VIEW_OFF'
                row.prop(constraint, 'mute', text="", icon=iconView)
                row.prop(constraint, 'name', text="")
        else:
            pass
        if itemUI.viewModifiers:
            for modifier in context.active_object.modifiers:
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
                else: # if modifier.type in 'SOFT_BODY':
                    iconMod = 'MOD_SOFT'
                sub.label(text="", icon=iconMod)
                if modifier.show_viewport:
                    iconView = 'RESTRICT_VIEW_OFF'
                else:
                    iconView = 'RESTRICT_VIEW_ON'
                row.prop(modifier, 'show_viewport', text="", icon=iconView)
                row.prop(modifier, 'name', text="")
        else:
            pass
        if itemUI.viewHierarchy:
            for object in context.selected_objects:
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
                    else:
                        iconObject = 'OUTLINER_OB_LAMP'
                    sub.label(text="", icon=iconObject)
                    row.prop(object, 'name', text="")
                    if itemUI.viewConstraints:
                        for constraint in object.constraints[:]:
                            row = column.row(align=True)
                            sub = row.row()
                            sub.scale_x = 1.6
                            sub.label(text="", icon='CONSTRAINT')
                            if constraint.mute:
                                iconView = 'RESTRICT_VIEW_ON'
                            else:
                                iconView = 'RESTRICT_VIEW_OFF'
                            row.prop(constraint, 'mute', text="", icon=iconView)
                            row.prop(constraint, 'name', text="")
                    else:
                        pass
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
                            else: # if modifier.type in 'SOFT_BODY':
                                iconMod = 'MOD_SOFT'
                            sub.label(text="", icon=iconMod)
                            if modifier.show_viewport:
                                iconView = 'RESTRICT_VIEW_OFF'
                            else:
                                iconView = 'RESTRICT_VIEW_ON'
                            row.prop(modifier, 'show_viewport', text="",
                                     icon=iconView)
                            row.prop(modifier, 'name', text="")
                    else:
                        pass
                else:
                    pass
        else:
            pass
        if context.object.type in 'EMPTY':
            if context.object.empty_draw_type in 'IMAGE':
                row = column.row(align=True)
                row.template_ID(context.active_object, 'data',
                                open='image.open', unlink='image.unlink')
            else:
                pass
        else:
            row = column.row(align=True)
            row.template_ID(context.active_object, 'data')
        if itemUI.viewHierarchy:
            for object in context.selected_objects:
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
                        else:
                            iconData = 'LAMP_DATA'
                        sub.label(text="", icon=iconData)
                        row.prop(object.data, 'name', text="")
                        if object.data.users > 1:
                            subrow = row.row()
                            subrow.enabled = False
                            subrow.scale_x = 0.1
                            users = str(object.data.users)
                            subrow.prop(itemUI, 'objectDataUsers', text=users,
                                        toggle=True)
                            sub = row.row()
                            sub.scale_x = 0.1
                            sub.prop(object.data, 'use_fake_user', text="F",
                                     toggle=True)
                        else:
                            sub = row.row()
                            sub.scale_x = 0.1
                            sub.prop(object.data, 'use_fake_user', text="F",
                                     toggle=True)
                    else:
                        pass
                else:
                    pass
        else:
            pass
        if (context.object.type in 'ARMATURE' and
            context.object.mode in {'POSE', 'EDIT'}):
            row = column.row(align=True)
            sub = row.row()
            sub.scale_x = 1.6
            sub.label(text="", icon='BONE_DATA')
            row.prop(context.active_bone, 'name', text="")
            if context.object.mode in 'POSE':
                if itemUI.viewBoneConstraints:
                    for constraint in context.active_pose_bone.constraints:
                        row = column.row(align=True)
                        sub = row.row()
                        sub.scale_x = 1.6
                        sub.label(text="", icon='CONSTRAINT_BONE')
                        if constraint.mute:
                            iconView = 'RESTRICT_VIEW_ON'
                        else:
                            iconView = 'RESTRICT_VIEW_OFF'
                        row.prop(constraint, 'mute', text="", icon=iconView)
                        row.prop(constraint, 'name', text="")
                else:
                    pass
            else:
                pass
            if itemUI.viewHierarchy:
                if context.selected_editable_bones:
                    selected_bones = context.selected_editable_bones
                else:
                    selected_bones = context.selected_pose_bones
                try:
                    for bone in selected_bones:
                        if bone != (context.active_pose_bone or
                                    context.active_bone):
                            row = column.row(align=True)
                            sub = row.row()
                            sub.scale_x = 1.6
                            sub.label(text="", icon='BONE_DATA')
                            row.prop(bone, 'name', text="")
                            if context.object.mode in 'POSE':
                                if itemUI.viewBoneConstraints:
                                    for constraint in bone.constraints[:]:
                                        row = column.row(align=True)
                                        sub = row.row()
                                        sub.scale_x = 1.6
                                        sub.label(text="",
                                                  icon='CONSTRAINT_BONE')
                                        if constraint.mute:
                                            iconView = 'RESTRICT_VIEW_ON'
                                        else:
                                            iconView = 'RESTRICT_VIEW_OFF'
                                        row.prop(constraint, 'mute', text="",
                                                 icon=iconView)
                                        row.prop(constraint, 'name', text="")
                                else:
                                    pass
                            else:
                                pass
                        else:
                            pass
                except TypeError:
                    pass
            else:
                pass
        else:
            pass

##############
## REGISTER ##
##############


def register():
    """ Register """
    windowManager = bpy.types.WindowManager

    bpy.utils.register_module(__name__)
    windowManager.itemUI = bpy.props.PointerProperty(type=itemUIPropertyGroup)
    bpy.context.window_manager.itemUI.name = 'Item Panel Properties'


def unregister():
    """ Unregister """
    bpy.utils.unregister_module(__name__)
    try:
        del bpy.types.WindowManager.itemUI
    except:
        pass

if __name__ in '__main__':
    register()
