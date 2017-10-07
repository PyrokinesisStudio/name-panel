
import bpy

from bpy.utils import escape_identifier
from bl_ui.properties_animviz import MotionPathButtonsPanel, OnionSkinButtonsPanel
from rna_prop_ui import PropertyPanel

from .cycles_interface import *
from .utilities import get, rna_prop_ui


class name_panel:


    def __init__(self, panel, context):

        self.layout = panel.layout

        self.option = get.name_panel.options(context)

        self.find_and_replace(context)

        self.layout.separator()

        self.name_stack(context)


    def find_and_replace(self, context):

        column = self.layout.column(align=True)

        row = column.row(align=True)

        row.prop(self.option, 'find', text='', icon='VIEWZOOM')

        if self.option.find:

            row.operator('view3d.name_panel_clear_find', text='', icon='X')

        row.operator('view3d.name_panel_options', text='', icon='FILTER')

        row.menu('view3d.name_panel_specials', text='', icon='COLLAPSEMENU')

        if self.option.find:

            row = column.row(align=True)

            row.prop(self.option, 'replace', text='', icon='FILE_REFRESH')

            if self.option.replace:

                row.operator('view3d.name_panel_clear_replace', text='', icon='X')

            sub = row.row(align=True)
            sub.scale_x = 0.2

            sub.operator('view3d.name_panel_options', text='OK')


    def name_stack(self, context):

        self.stack = get.name_panel.name_stack(context)

        # TODO: add display limit
        if self.stack:

            for object in self.stack['datablocks']:

                self.stack_object(self, context, object)

        else:

            self.no_stack()


    def no_stack(self):

        option = self.option.filters['options']

        row = self.layout.row()
        row.alignment = 'CENTER'

        # if self.option.find:
        #
        #     row.label(text='No matches found')

        if option.display_mode == 'ACTIVE':

            row.label(text='No active object')

        elif option.display_mode == 'SELECTED':

            row.label(text='No selected objects')

        else: # option.display_mode == 'VISIBLE':

            row.label(text='No visible objects')

        self.layout.separator()


    def specials(panel, context):

        option = get.name_panel.options(context)

        layout = panel.layout

        layout.label(text='Find & Replace')

        layout.separator()

        layout.prop(option, 'case_sensitive')
        layout.prop(option, 'regex')

        layout.separator()

        layout.label(text='Batch Naming')

        layout.separator()

        layout.operator('wm.namer', text='Transfer Names')
        layout.operator('wm.namer', text='Count Names')

        layout.separator()

        layout.operator('wm.namer', text='Namer', icon='SORTALPHA')


    class stack_object:


        def __init__(self, panel, context, object):

            self.option = get.name_panel.options(context).filters['options']
            self.context = context
            self.object = object

            column = panel.layout.column(align=True)

            self.row(panel.stack['objects'], column, self.object, get.icon.object(self.object), emboss=True if self.object.select or self.object == self.context.active_object else False, active=not (self.object == self.context.scene.objects.active and not self.object.select))

            for type in panel.stack['objects'][object.name]['types']:

                getattr(self, type)(panel.stack['objects'][object.name][type], column)

            for _ in range(get.preferences(self.context).separators):

                panel.layout.separator()


        def row(self, location, column, datablock, icon, name_type='name', emboss=False, active=True):

            if datablock:

                row = column.row(align=True)
                row.active = location[getattr(datablock, name_type)]['active']

                sub = row.row(align=True if emboss else False)
                sub.scale_x = 1.5 if not emboss else 1.6
                sub.active = active

                operator_prop = 'view3d.name_panel_datablock_click_through' if get.preferences(self.context).click_through else 'view3d.name_panel_datablock'
                operator = sub.operator(operator_prop, text='', icon=icon, emboss=emboss)
                operator.object_name = self.object.name
                operator.target_name = getattr(datablock, name_type)
                operator.identifier = get.identifier(datablock)

                row.prop(datablock, name_type, text='')


        def groups(self, location, column):

            for group in location['datablocks']:

                self.row(location, column, group, get.icon('groups'))


        def grease_pencils(self, location, column):

            self.row(location, column, location['datablocks'][0], get.icon('grease_pencils'))

            for layer in location[location['datablocks'][0].name]['grease_pencil_layers']['datablocks']:

                self.row(location[location['datablocks'][0].name]['grease_pencil_layers'], column, layer, get.icon('grease_pencil_layers'), name_type='info')


        def actions(self, location, column):

            self.row(location, column, location['datablocks'][0], get.icon('actions'))


        def constraints(self, location, column):

            for constraint in location['datablocks']:

                self.row(location, column, constraint, get.icon('constraints'))


        def modifiers(self, location, column):

            for modifier in location['datablocks']:

                self.row(location, column, modifier, get.icon.modifier(modifier))

                if 'particle_system' in location[modifier.name]:

                    self.row(location[modifier.name]['particle_system'], column, location[modifier.name]['particle_system'][modifier.particle_system.name]['datablock'], get.icon.subtype('particle_system'))
                    self.row(location[modifier.name]['particle_system'][modifier.particle_system.name]['particle_settings'], column, location[modifier.name]['particle_system'][modifier.particle_system.name]['particle_settings'][modifier.particle_system.settings.name]['datablock'], 'DOT')

                    if 'textures' in location[modifier.name]['particle_system'][modifier.particle_system.name]['particle_settings'][modifier.particle_system.settings.name]:

                        for texture in location[modifier.name]['particle_system'][modifier.particle_system.name]['particle_settings'][modifier.particle_system.settings.name]['textures']['datablocks']:

                            self.row(location[modifier.name]['particle_system'][modifier.particle_system.name]['particle_settings'][modifier.particle_system.settings.name]['textures'], column,  location[modifier.name]['particle_system'][modifier.particle_system.name]['particle_settings'][modifier.particle_system.settings.name]['textures'][texture.name]['datablock'], get.icon('textures'))


        def object_data(self, location, column):

            self.row(location, column, location['datablocks'][0], get.icon.object_data(self.object), emboss=True if self.object.select or self.object == self.context.active_object else False, active=not (self.object == self.context.scene.objects.active and not self.object.select))


        def bone_groups(self, location, column):

            for group in location['datablocks']:

                self.row(location, column, group, get.icon('bone_groups'))


        def bones(self, location, column): # TODO: implement bones for all armatures in namestack

            if location['datablocks']:

                column.separator()

            for bone in location['datablocks']:

                active_bone = self.context.active_bone if self.context.mode == 'EDIT_ARMATURE' else self.context.active_pose_bone
                bone_selected = bone.select if self.context.mode == 'EDIT_ARMATURE' else bone.bone.select

                self.row(location, column, bone, get.icon('bones'), emboss=True if bone_selected or bone == active_bone else False, active=not (bone == active_bone and not bone_selected))

                if 'bone_constraints' in location[bone.name]:

                    self.constraints(location[bone.name]['bone_constraints'], column)


        def shapekeys(self, location, column):

            for shapekey in location['datablocks']:

                self.row(location, column, shapekey, get.icon('shapekeys'))


        def vertex_groups(self, location, column):

            for vertex_group in location['datablocks']:

                self.row(location, column, vertex_group, get.icon('vertex_groups'))


        def uv_maps(self, location, column):

            for uv_map in location['datablocks']:

                self.row(location, column, uv_map, get.icon('uv_maps'))


        def vertex_colors(self, location, column):

            for vertex_color in location['datablocks']:

                self.row(location, column, vertex_color, get.icon('vertex_colors'))


        def materials(self, location, column):

            for material in location['datablocks']:

                self.row(location, column, material, get.icon('materials'))

                if material:

                    if 'textures' in location[material.name]:

                        for texture in location[material.name]['textures']['datablocks']:

                            self.row(location[material.name]['textures'], column, texture, get.icon('textures'))


    class options:


        def __init__(self, operator, context):

            self.option = get.name_panel.options(context).filters['options']

            split = operator.layout.column().split(percentage=0.15)
            column = split.column()
            column.prop(self.option, 'mode', expand=True)

            # self.set_height(column, 4)

            self.split = split.column(align=True)

            if self.option.mode == 'FILTERS':

                self.display_mode(context)
                self.filters(context)

            else:

                self.extra_options(context)


        @staticmethod
        def set_height(column, separators):

            for _ in range(0, separators): column.separator()


        def display_mode(self, context):

            row = self.split.row(align=True)

            row.prop(self.option, 'display_mode', expand=True)


        def filters(self, context):

            column = self.split.column(align=True)

            row = column.row(align=True)
            split = row.split(percentage=0.1, align=True)
            column = split.column(align=True)
            column.scale_y = 2
            column.prop(self.option, 'toggle_all', text='', icon='RADIOBUT_OFF' if not self.option.toggle_all else 'RADIOBUT_ON')

            column = split.column(align=True)
            row = column.row(align=True)
            row.scale_x = 2
            row.prop(self.option, 'groups', text='', icon=get.icon('groups'))
            row.prop(self.option, 'grease_pencils', text='', icon=get.icon('grease_pencils'))
            row.prop(self.option, 'actions', text='', icon=get.icon('actions'))
            row.prop(self.option, 'constraints', text='', icon=get.icon('constraints'))
            row.prop(self.option, 'modifiers', text='', icon=get.icon('modifiers'))
            row.prop(self.option, 'bones', text='', icon=get.icon('bones'))
            row.prop(self.option, 'bone_groups', text='', icon=get.icon('bone_groups'))
            row.prop(self.option, 'bone_constraints', text='', icon=get.icon('bone_constraints'))

            row = column.row(align=True)
            row.scale_x = 2
            row.prop(self.option, 'shapekeys', text='', icon=get.icon('shapekeys'))
            row.prop(self.option, 'vertex_groups', text='', icon=get.icon('vertex_groups'))
            row.prop(self.option, 'uv_maps', text='', icon=get.icon('uv_maps'))
            row.prop(self.option, 'vertex_colors', text='', icon=get.icon('vertex_colors'))
            row.prop(self.option, 'particle_systems', text='', icon=get.icon('particle_systems'))
            row.prop(self.option, 'materials', text='', icon=get.icon('materials'))
            row.prop(self.option, 'textures', text='', icon=get.icon('textures'))
            row.prop(self.option, 'images', text='', icon=get.icon('images'))


        def extra_options(self, context):

            row = self.split.row(align=True)
            row.prop(get.preferences(context), 'location', expand=True)

            row = self.split.row(align=True)
            row.prop(get.preferences(context), 'popup_width', text='Pop-up Width')

            row = self.split.row(align=True)
            row.prop(get.preferences(context), 'pin_active', toggle=True)
            row.prop(get.preferences(context), 'click_through', toggle=True)


class datablock:

    # TODO: Create a properties pop-up that behaves the same as the properties window place it on the search row, right after filters
    def __init__(self, operator, context):

        pass

    # context row
    def context(self, operator, context, layout):

        # draw row enum here, needs to be dynamic like properties window (detects type and filters out buttons, also changes icons)
        pass


    # def __init__(self, operator, context):
    #
    #     layout = operator.layout
    #
    #     column = layout.column()
    #
    #     getattr(self, operator.identifier)(operator, context)
    #
    #
    # class Object:
    #
    #     boxes = [
    #         ('Levels of Detail', 'levels_of_detail'),
    #         ('Transform', 'transform'),
    #         ('Delta Transform', 'delta_transform'),
    #         ('Transform Locks', 'transform_locks'),
    #         ('Display', 'display'),
    #         ('Groups', 'groups'),
    #         ('Relations', 'relations'),
    #         ('Relations Extras', 'relations_extras'),
    #         ('Duplication', 'duplication'),
    #         ('Motion Paths', 'motion_paths'),
    #         ('Motion Blur', 'motion_blur', {'MESH', 'CURVE', 'SURFACE', 'FONT', 'META'}),
    #         ('Cycles Settings', 'cycles_settings', {'MESH', 'CURVE', 'SURFACE', 'FONT', 'META', 'LAMP'}),
    #         ('Custom Properties', 'custom_properties'),
    #     ]
    #
    #
    #     def __init__(self, operator, context):
    #
    #         self.layout = operator.layout
    #         self.context = context
    #         self.object = self.context.active_object
    #         self.preferences = get.preferences(self.context)
    #
    #         self.layout.separator()
    #         row = self.layout.row()
    #         row.alignment = 'CENTER'
    #         row.scale_x = 2
    #         row.template_ID(context.scene.objects, 'active')
    #         self.layout.separator()
    #
    #         for box_type in self.boxes:
    #
    #             option = 'object_{}{}'.format(box_type[1], '_expanded')
    #             expanded = getattr(self.preferences, option)
    #
    #             if len(box_type) == 3:
    #
    #                 if self.object.type in box_type[2]:
    #
    #                     if box_type[1] == 'motion_blur':
    #                         if self.context.scene.render.engine == 'CYCLES':
    #
    #                             box_column = self.layout.column(align=True)
    #                             self.header(box_column, box_type, option, expanded, toggle_prop='use_motion_blur', toggle_prop_target=self.object.cycles)
    #
    #                             if expanded:
    #
    #                                 self.motion_blur(box_column)
    #
    #                     elif box_type[1] == 'cycles_settings':
    #                         if self.context.scene.render.engine == 'CYCLES':
    #
    #                             box_column = self.layout.column(align=True)
    #                             self.header(box_column, box_type, option, expanded)
    #
    #                             if expanded:
    #
    #                                 self.cycles_settings(box_column)
    #
    #                     else:
    #
    #                         box_column = self.layout.column(align=True)
    #                         self.header(box_column, box_type, option, expanded)
    #
    #                         if expanded:
    #
    #                             getattr(self, box_type[1])(box_column)
    #
    #             else:
    #
    #                 if box_type[1] == 'levels_of_detail':
    #                     if context.scene.render.engine == 'BLENDER_GAME':
    #
    #                         box_column = self.layout.column(align=True)
    #                         self.header(box_column, box_type, option, expanded)
    #
    #                         if expanded:
    #
    #                             self.levels_of_detail(box_column)
    #
    #                 elif box_type[1] == 'custom_properties':
    #
    #                     rna_item, context_member = rna_prop_ui.rna_idprop_context_value(self.context, 'object', bpy.types.Object)
    #
    #                     if rna_item and bool(rna_item):
    #
    #                         box_column = self.layout.column(align=True)
    #                         self.header(box_column, box_type, option, expanded)
    #
    #                         if expanded:
    #
    #                             self.custom_properties(box_column)
    #
    #                 else:
    #
    #                     box_column = self.layout.column(align=True)
    #                     self.header(box_column, box_type, option, expanded)
    #
    #                     if expanded:
    #
    #                         getattr(self, box_type[1])(box_column)
    #
    #
    #     def header(self, box_column, box_type, option, expanded, toggle_prop='', toggle_prop_target=None):
    #
    #         box = box_column.box()
    #
    #         row = box.row(align=True)
    #         row.alignment = 'LEFT'
    #
    #         sub = row.row(align=True)
    #         sub.scale_x = 0.5
    #         sub.prop(self.preferences, option, text='', icon='TRIA_DOWN' if expanded else 'TRIA_RIGHT', emboss=False)
    #
    #         if toggle_prop:
    #
    #             sub = row.row(align=True)
    #             sub.scale_x = 0.8
    #             sub.prop(toggle_prop_target, toggle_prop, text='')
    #
    #         row.prop(self.preferences, option, text=box_type[0], toggle=True, emboss=False)
    #
    #         sub = row.row(align=True)
    #         sub.prop(self.preferences, option, text=' ', toggle=True, emboss=False)
    #
    #
    #     def levels_of_detail(self, box_column):
    #
    #         game_settings = self.context.scene.game_settings
    #
    #         box = box_column.box()
    #         column = box.column()
    #
    #         for i, level in enumerate(self.object.lod_levels):
    #             if i == 0:
    #
    #                 continue
    #
    #             box = column.box()
    #
    #             row = box.row()
    #             row.prop(level, 'object', text='')
    #             row.operator('object.lod_remove', text='', icon='PANEL_CLOSE').index = i
    #
    #             row = box.row()
    #             row.prop(level, 'distance')
    #
    #             row = row.row(align=True)
    #             row.prop(level, 'use_mesh', text='')
    #             row.prop(level, 'use_material', text='')
    #
    #             row = box.row()
    #             row.active = game_settings.use_scene_hysteresis
    #             row.prop(level, 'use_object_hysteresis', text='Hysteresis Override')
    #
    #             row = box.row()
    #             row.active = game_settings.use_scene_hysteresis and level.use_object_hysteresis
    #             row.prop(level, 'object_hysteresis_percentage', text='')
    #
    #         row = column.row(align=True)
    #         row.operator('object.lod_add', text='Add', icon='ZOOMIN')
    #         row.menu('OBJECT_MT_lod_tools', text='', icon='TRIA_DOWN')
    #
    #
    #     def transform(self, box_column):
    #
    #         box = box_column.box()
    #         split = box.split()
    #
    #         column = split.column()
    #         column.prop(self.object, 'location')
    #
    #         if self.object.rotation_mode == 'QUATERNION':
    #
    #             column = split.column()
    #             column.prop(self.object, 'rotation_quaternion', text='Rotation')
    #
    #         elif self.object.rotation_mode == 'AXIS_ANGLE':
    #
    #             column = split.column()
    #             column.prop(self.object, 'rotation_axis_angle', text='Rotation')
    #
    #         else:
    #
    #             column = split.column()
    #             column.prop(self.object, 'rotation_euler', text='Rotation')
    #
    #         column = split.column()
    #         column.prop(self.object, 'scale')
    #
    #         box.prop(self.object, 'rotation_mode')
    #
    #
    #     def delta_transform(self, box_column):
    #
    #         box = box_column.box()
    #         split = box.split()
    #
    #         column = split.column()
    #         column.prop(self.object, 'delta_location')
    #
    #         if self.object.rotation_mode == 'QUATERNION':
    #
    #             column = split.column()
    #             column.prop(self.object, 'delta_rotation_quaternion', text='Rotation')
    #
    #         elif self.object.rotation_mode == 'AXIS_ANGLE':
    #
    #             column = split.column()
    #             column.label(text='Not for Axis-Angle')
    #
    #         else:
    #
    #             column = split.column()
    #             column.prop(self.object, 'delta_rotation_euler', text='Delta Rotation')
    #
    #         column = split.column()
    #         column.prop(self.object, 'delta_scale')
    #
    #
    #     def transform_locks(self, box_column):
    #
    #         box = box_column.box()
    #         split = box.split(percentage=0.1)
    #
    #         column = split.column(align=True)
    #         column.label(text='')
    #         column.label(text='X:')
    #         column.label(text='Y:')
    #         column.label(text='Z:')
    #
    #         split.column().prop(self.object, 'lock_location', text='Location')
    #         split.column().prop(self.object, 'lock_rotation', text='Rotation')
    #         split.column().prop(self.object, 'lock_scale', text='Scale')
    #
    #         if self.object.rotation_mode in {'QUATERNION', 'AXIS_ANGLE'}:
    #
    #             row = box.row()
    #             row.prop(self.object, 'lock_rotations_4d', text='Lock Rotation')
    #
    #             sub = row.row()
    #             sub.active = self.object.lock_rotations_4d
    #             sub.prop(self.object, 'lock_rotation_w', text='W')
    #
    #
    #     def relations(self, box_column):
    #
    #         box = box_column.box()
    #         split = box.split()
    #
    #         column = split.column()
    #         column.prop(self.object, 'layers')
    #         column.separator()
    #         column.prop(self.object, 'pass_index')
    #
    #         column = split.column()
    #         column.label(text='Parent:')
    #         column.prop(self.object, 'parent', text='')
    #
    #         sub = column.column()
    #         sub.active = self.object.parent != None
    #         sub.prop(self.object, 'parent_type', text='')
    #
    #         if self.object.parent and self.object.parent_type == 'BONE' and self.object.parent.type == 'ARMATURE':
    #
    #             sub.prop_search(self.object, 'parent_bone', self.object.parent.data, 'bones', text='')
    #
    #
    #     def groups(self, box_column):
    #
    #         box = box_column.box()
    #         row = box.row(align=True)
    #
    #         if get.name_panel.name_stack.groups(self.context, self.object):
    #
    #             row.operator('object.group_link', text='Add to Group')
    #
    #         else:
    #
    #             row.operator('object.group_add', text='Add to Group')
    #
    #         row.operator('object.group_add', text='', icon='ZOOMIN')
    #
    #         groups = get.name_panel.name_stack.groups(self.context, self.object)
    #
    #         for group in groups:
    #
    #             column = box.box().column(align=True)
    #
    #             column.context_pointer_set('group', group)
    #
    #             row = column.box().row()
    #             row.prop(group, 'name', text='')
    #             row.operator('object.group_remove', text='', icon='X', emboss=False)
    #             row.menu('GROUP_MT_specials', icon='DOWNARROW_HLT', text='')
    #
    #             split = column.box().split()
    #
    #             column = split.column()
    #             column.prop(group, 'layers', text='Dupli Visibility')
    #
    #             column = split.column()
    #             column.prop(group, 'dupli_offset', text='')
    #
    #
    #     def display(self, box_column):
    #
    #         is_geometry = self.object.type in {'MESH', 'CURVE', 'SURFACE', 'META', 'FONT'}
    #         is_wire = self.object.type in {'CAMERA', 'EMPTY'}
    #         is_empty_image = self.object.type == 'EMPTY' and self.object.empty_draw_type == 'IMAGE'
    #         is_dupli = self.object.dupli_type != 'NONE'
    #
    #         box = box_column.box()
    #         split = box.split()
    #
    #         column = split.column()
    #         column.prop(self.object, 'show_name', text='Name')
    #         column.prop(self.object, 'show_axis', text='Axis')
    #
    #         if is_geometry or is_dupli:
    #
    #             column.prop(self.object, 'show_wire', text='Wire')
    #
    #         if self.object.type == 'MESH' or is_dupli:
    #
    #             column.prop(self.object, 'show_all_edges')
    #
    #         column = split.column()
    #         row = column.row()
    #         row.prop(self.object, 'show_bounds', text='Bounds')
    #
    #         sub = row.row()
    #         sub.active = self.object.show_bounds
    #         sub.prop(self.object, 'draw_bounds_type', text='')
    #
    #         if is_geometry:
    #
    #             column.prop(self.object, 'show_texture_space', text='Texture Space')
    #
    #         column.prop(self.object, 'show_x_ray', text='X-Ray')
    #
    #         if self.object.type == 'MESH' or is_empty_image:
    #
    #             column.prop(self.object, 'show_transparent', text='Transparency')
    #
    #         split = box.split()
    #         column = split.column()
    #
    #         if is_wire:
    #
    #             column.active = is_dupli
    #             column.label(text='Maximum Dupli Draw Type:')
    #
    #         else:
    #
    #             column.label(text='Maximum Draw Type:')
    #
    #         column.prop(self.object, 'draw_type', text='')
    #
    #         column = split.column()
    #
    #         if is_geometry or is_empty_image:
    #
    #             column.label(text='Object Color:')
    #             column.prop(self.object, 'color', text='')
    #
    #
    #     def duplication(self, box_column):
    #
    #         box = box_column.box()
    #         row = box.row()
    #         row.prop(self.object, 'dupli_type', expand=True)
    #
    #         if self.object.dupli_type == 'FRAMES':
    #
    #             split = box.split()
    #             column = split.column(align=True)
    #             column.prop(self.object, 'dupli_frames_start', text='Start')
    #             column.prop(self.object, 'dupli_frames_end', text='End')
    #
    #             column = split.column(align=True)
    #             column.prop(self.object, 'dupli_frames_on', text='On')
    #             column.prop(self.object, 'dupli_frames_off', text='Off')
    #
    #             box.prop(self.object, 'use_dupli_frames_speed', text='Speed')
    #
    #         elif self.object.dupli_type == 'VERTS':
    #
    #             box.prop(self.object, 'use_dupli_vertices_rotation', text='Rotation')
    #
    #         elif self.object.dupli_type == 'FACES':
    #
    #             row = box.row()
    #             row.prop(self.object, 'use_dupli_faces_scale', text='Scale')
    #
    #             sub = row.row()
    #             sub.active = self.object.use_dupli_faces_scale
    #             sub.prop(self.object, 'dupli_faces_scale', text='Inherit Scale')
    #
    #         elif self.object.dupli_type == 'GROUP':
    #
    #             box.prop(self.object, 'dupli_group', text='Group')
    #
    #
    #     def relations_extras(self, box_column):
    #
    #         box = box_column.box()
    #         split = box.split()
    #
    #         if self.context.scene.render.engine != 'BLENDER_GAME':
    #
    #             column = split.column()
    #             column.label(text='Tracking Axes:')
    #             column.prop(self.object, 'track_axis', text='Axis')
    #             column.prop(self.object, 'up_axis', text='Up Axis')
    #
    #         column = split.column()
    #         column.prop(self.object, 'use_slow_parent')
    #
    #         row = column.row()
    #         row.active = self.object.parent != None and self.object.use_slow_parent
    #         row.prop(self.object, 'slow_parent_offset', text='Offset')
    #
    #         box.prop(self.object, 'use_extra_recalc_object')
    #         box.prop(self.object, 'use_extra_recalc_data')
    #
    #
    #     def motion_paths(self, box_column):
    #
    #         box = box_column.box()
    #
    #         row = box.row()
    #         row.prop(self.object.animation_visualization.motion_path, 'type', expand=True)
    #
    #         split = box.split()
    #         column = split.column()
    #         column.label(text='Display Range:')
    #
    #         sub = column.column(align=True)
    #
    #         if self.object.animation_visualization.motion_path.type == 'CURRENT_FRAME':
    #
    #            sub.prop(self.object.animation_visualization.motion_path, 'frame_before', text='Before')
    #            sub.prop(self.object.animation_visualization.motion_path, 'frame_after', text='After')
    #
    #         elif self.object.animation_visualization.motion_path.type == 'RANGE':
    #
    #            sub.prop(self.object.animation_visualization.motion_path, 'frame_start', text='Start')
    #            sub.prop(self.object.animation_visualization.motion_path, 'frame_end', text='End')
    #
    #         sub.prop(self.object.animation_visualization.motion_path, 'frame_step', text='Step')
    #
    #         column = split.column()
    #         column.label(text='Cache:')
    #
    #         if self.object.motion_path:
    #
    #            sub = column.column(align=True)
    #            sub.enabled = False
    #            sub.prop(self.object.motion_path, 'frame_start', text='From')
    #            sub.prop(self.object.motion_path, 'frame_end', text='To')
    #
    #            sub = column.row(align=True)
    #            sub.operator('object.paths_update', text='Update Paths', icon='OBJECT_DATA')
    #            sub.operator('object.paths_clear', text='', icon='X')
    #
    #         else:
    #
    #            sub = column.column(align=True)
    #            sub.label(text='Nothing to show yet...', icon='ERROR')
    #            sub.operator('object.paths_calculate', text='Calculate...', icon='OBJECT_DATA')
    #
    #         split = box.split()
    #         column = split.column()
    #         column.label(text='Show:')
    #         column.prop(self.object.animation_visualization.motion_path, 'show_frame_numbers', text='Frame Numbers')
    #
    #         column = split.column()
    #         column.prop(self.object.animation_visualization.motion_path, 'show_keyframe_highlight', text='Keyframes')
    #
    #         sub = column.column()
    #         sub.enabled = self.object.animation_visualization.motion_path.show_keyframe_highlight
    #         sub.prop(self.object.animation_visualization.motion_path, 'show_keyframe_numbers', text='Keyframe Numbers')
    #
    #
    #     # def motion_blur(self, box_column):
    #     #
    #     #     box = box_column.box()
    #     #
    #     #     split = box.split()
    #     #     split.active = self.context.scene.render.use_motion_blur and self.object.cycles.use_motion_blur
    #     #     split.prop(self.object.cycles, 'use_deform_motion', text='Deformation')
    #     #
    #     #     sub = split.row()
    #     #     sub.active = self.object.cycles.use_deform_motion
    #     #     sub.prop(self.object.cycles, 'motion_steps', text='Steps')
    #     #
    #     #
    #     # def cycles_settings(self, box_column):
    #     #
    #     #     box = box_column.box()
    #     #
    #     #     box.label(text='Ray Visibility:')
    #     #     flow = box.column_flow()
    #     #
    #     #     flow.prop(self.object.cycles_visibility, 'camera')
    #     #     flow.prop(self.object.cycles_visibility, 'diffuse')
    #     #     flow.prop(self.object.cycles_visibility, 'glossy')
    #     #     flow.prop(self.object.cycles_visibility, 'transmission')
    #     #     flow.prop(self.object.cycles_visibility, 'scatter')
    #     #
    #     #     if self.object.type != 'LAMP':
    #     #         flow.prop(self.object.cycles_visibility, 'shadow')
    #     #
    #     #     column = box.column()
    #     #     column.label(text='Performance:')
    #     #     row = column.row()
    #     #     sub = row.row()
    #     #     sub.active = self.context.scene.render.use_simplify and self.context.scene.cycles.use_camera_cull
    #     #     sub.prop(self.object.cycles, 'use_camera_cull')
    #     #
    #     #     sub = row.row()
    #     #     sub.active = self.context.scene.render.use_simplify and self.context.scene.cycles.use_distance_cull
    #     #     sub.prop(self.object.cycles, 'use_distance_cull')
    #
    #
    #     def custom_properties(self, box_column, use_edit=True):
    #
    #
    #         def assign_props(prop, val, key):
    #
    #             prop.data_path = context_member
    #             prop.property = key
    #
    #             try: prop.value = str(val)
    #             except: pass
    #
    #
    #         rna_item, context_member = rna_prop_ui.rna_idprop_context_value(self.context, 'object', bpy.types.Object)
    #
    #         if rna_item.id_data.library is not None:
    #
    #             use_edit = False
    #
    #         assert(isinstance(rna_item, bpy.types.Object))
    #
    #         items = rna_item.items()
    #         items.sort()
    #
    #         box = box_column.box()
    #
    #         if use_edit:
    #
    #             row = box.row()
    #             operator = row.operator("wm.properties_add", text="Add")
    #             operator.data_path = context_member
    #
    #         rna_properties = {prop.identifier for prop in rna_item.bl_rna.properties if prop.is_runtime} if items else None
    #
    #         for key, value in items:
    #
    #             if key == '_RNA_UI':
    #                 continue
    #
    #             to_dict = getattr(value, "to_dict", None)
    #             to_list = getattr(value, "to_list", None)
    #
    #             if to_dict:
    #
    #                 value = to_dict()
    #                 value_draw = str(value)
    #
    #             elif to_list:
    #
    #                 value = to_list()
    #                 value_draw = str(value)
    #
    #             else:
    #
    #                 value_draw = value
    #
    #             if use_edit:
    #
    #                 split = box.row().box().split(percentage=0.75)
    #                 row = split.row()
    #
    #             else:
    #
    #                 row = box.row().box().row()
    #
    #             row.label(text=key, translate=False)
    #
    #             is_rna = (key in rna_properties)
    #
    #             if to_dict or to_list:
    #
    #                 row.label(text=value_draw, translate=False)
    #
    #             else:
    #
    #                 if is_rna:
    #
    #                     row.prop(rna_item, key, text="")
    #
    #                 else:
    #
    #                     row.prop(rna_item, '["{}"]'.format(escape_identifier(key)), text="")
    #
    #             if use_edit:
    #
    #                 row = split.row(align=True)
    #
    #                 if not is_rna:
    #
    #                     operator = row.operator("wm.properties_edit", text="Edit")
    #                     assign_props(operator, value_draw, key)
    #
    #                 else:
    #
    #                     row.label(text="API Defined")
    #
    #                 operator = row.operator("wm.properties_remove", text="", icon='ZOOMOUT')
    #                 assign_props(operator, value_draw, key)
    #
    #
    # class Mesh:
    #
    #     # boxes = [
    #     #     ('Levels of Detail', 'levels_of_detail'),
    #     #     ('Transform', 'transform'),
    #     #     ('Delta Transform', 'delta_transform'),
    #     #     ('Transform Locks', 'transform_locks'),
    #     #     ('Display', 'display'),
    #     #     ('Groups', 'groups'),
    #     #     ('Relations', 'relations'),
    #     #     ('Relations Extras', 'relations_extras'),
    #     #     ('Duplication', 'duplication'),
    #     #     ('Motion Paths', 'motion_paths'),
    #     #     ('Motion Blur', 'motion_blur', {'MESH', 'CURVE', 'SURFACE', 'FONT', 'META'}),
    #     #     ('Cycles Settings', 'cycles_settings', {'MESH', 'CURVE', 'SURFACE', 'FONT', 'META', 'LAMP'}),
    #     #     ('Custom Properties', 'custom_properties'),
    #     # ]
    #     #
    #     #
    #     # def __init__(self, operator, context):
    #     #
    #     #     self.layout = operator.layout
    #     #     self.context = context
    #     #     self.object = self.context.active_object
    #     #     self.preferences = get.preferences(self.context)
    #     #
    #     #     self.layout.separator()
    #     #     row = self.layout.row()
    #     #     row.alignment = 'CENTER'
    #     #     row.scale_x = 2
    #     #     row.template_ID(context.scene.objects, 'active')
    #     #     self.layout.separator()
    #     #
    #     #     for box_type in self.boxes:
    #     #
    #     #         option = 'object_{}{}'.format(box_type[1], '_expanded')
    #     #         expanded = getattr(self.preferences, option)
    #     #
    #     #         if len(box_type) == 3:
    #     #
    #     #             if self.object.type in box_type[2]:
    #     #
    #     #                 if box_type[1] == 'motion_blur':
    #     #                     if self.context.scene.render.engine == 'CYCLES':
    #     #
    #     #                         box_column = self.layout.column(align=True)
    #     #                         self.header(box_column, box_type, option, expanded, toggle_prop='use_motion_blur', toggle_prop_target=self.object.cycles)
    #     #
    #     #                         if expanded:
    #     #
    #     #                             self.motion_blur(box_column)
    #     #
    #     #                 elif box_type[1] == 'cycles_settings':
    #     #                     if self.context.scene.render.engine == 'CYCLES':
    #     #
    #     #                         box_column = self.layout.column(align=True)
    #     #                         self.header(box_column, box_type, option, expanded)
    #     #
    #     #                         if expanded:
    #     #
    #     #                             self.cycles_settings(box_column)
    #     #
    #     #                 else:
    #     #
    #     #                     box_column = self.layout.column(align=True)
    #     #                     self.header(box_column, box_type, option, expanded)
    #     #
    #     #                     if expanded:
    #     #
    #     #                         getattr(self, box_type[1])(box_column)
    #     #
    #     #         else:
    #     #
    #     #             if box_type[1] == 'levels_of_detail':
    #     #                 if context.scene.render.engine == 'BLENDER_GAME':
    #     #
    #     #                     box_column = self.layout.column(align=True)
    #     #                     self.header(box_column, box_type, option, expanded)
    #     #
    #     #                     if expanded:
    #     #
    #     #                         self.levels_of_detail(box_column)
    #     #
    #     #             elif box_type[1] == 'custom_properties':
    #     #
    #     #                 rna_item, context_member = rna_prop_ui.rna_idprop_context_value(self.context, 'object', bpy.types.Object)
    #     #
    #     #                 if rna_item and bool(rna_item):
    #     #
    #     #                     box_column = self.layout.column(align=True)
    #     #                     self.header(box_column, box_type, option, expanded)
    #     #
    #     #                     if expanded:
    #     #
    #     #                         self.custom_properties(box_column)
    #     #
    #     #             else:
    #     #
    #     #                 box_column = self.layout.column(align=True)
    #     #                 self.header(box_column, box_type, option, expanded)
    #     #
    #     #                 if expanded:
    #     #
    #     #                     getattr(self, box_type[1])(box_column)
    #     #
    #     #
    #     # class DATA_PT_normals(MeshButtonsPanel, Panel):
    #     #     bl_label = "Normals"
    #     #     COMPAT_ENGINES = {'BLENDER_RENDER', 'BLENDER_GAME'}
    #     #
    #     #     def draw(self, context):
    #     #         layout = self.layout
    #     #
    #     #         mesh = context.mesh
    #     #
    #     #         split = layout.split()
    #     #
    #     #         col = split.column()
    #     #         col.prop(mesh, "use_auto_smooth")
    #     #         sub = col.column()
    #     #         sub.active = mesh.use_auto_smooth and not mesh.has_custom_normals
    #     #         sub.prop(mesh, "auto_smooth_angle", text="Angle")
    #     #
    #     #         split.prop(mesh, "show_double_sided")
    #     #
    #     #
    #     # class DATA_PT_texture_space(MeshButtonsPanel, Panel):
    #     #     bl_label = "Texture Space"
    #     #     bl_options = {'DEFAULT_CLOSED'}
    #     #     COMPAT_ENGINES = {'BLENDER_RENDER', 'BLENDER_GAME'}
    #     #
    #     #     def draw(self, context):
    #     #         layout = self.layout
    #     #
    #     #         mesh = context.mesh
    #     #
    #     #         layout.prop(mesh, "texture_mesh")
    #     #
    #     #         layout.separator()
    #     #
    #     #         layout.prop(mesh, "use_auto_texspace")
    #     #         row = layout.row()
    #     #         row.column().prop(mesh, "texspace_location", text="Location")
    #     #         row.column().prop(mesh, "texspace_size", text="Size")
    #     #
    #     #
    #     # class DATA_PT_vertex_groups(MeshButtonsPanel, Panel):
    #     #     bl_label = "Vertex Groups"
    #     #     COMPAT_ENGINES = {'BLENDER_RENDER', 'BLENDER_GAME'}
    #     #
    #     #     @classmethod
    #     #     def poll(cls, context):
    #     #         engine = context.scene.render.engine
    #     #         obj = context.object
    #     #         return (obj and obj.type in {'MESH', 'LATTICE'} and (engine in cls.COMPAT_ENGINES))
    #     #
    #     #     def draw(self, context):
    #     #         layout = self.layout
    #     #
    #     #         ob = context.object
    #     #         group = ob.vertex_groups.active
    #     #
    #     #         rows = 2
    #     #         if group:
    #     #             rows = 4
    #     #
    #     #         row = layout.row()
    #     #         row.template_list("MESH_UL_vgroups", "", ob, "vertex_groups", ob.vertex_groups, "active_index", rows=rows)
    #     #
    #     #         col = row.column(align=True)
    #     #         col.operator("object.vertex_group_add", icon='ZOOMIN', text="")
    #     #         col.operator("object.vertex_group_remove", icon='ZOOMOUT', text="").all = False
    #     #         col.menu("MESH_MT_vertex_group_specials", icon='DOWNARROW_HLT', text="")
    #     #         if group:
    #     #             col.separator()
    #     #             col.operator("object.vertex_group_move", icon='TRIA_UP', text="").direction = 'UP'
    #     #             col.operator("object.vertex_group_move", icon='TRIA_DOWN', text="").direction = 'DOWN'
    #     #
    #     #         if ob.vertex_groups and (ob.mode == 'EDIT' or (ob.mode == 'WEIGHT_PAINT' and ob.type == 'MESH' and ob.data.use_paint_mask_vertex)):
    #     #             row = layout.row()
    #     #
    #     #             sub = row.row(align=True)
    #     #             sub.operator("object.vertex_group_assign", text="Assign")
    #     #             sub.operator("object.vertex_group_remove_from", text="Remove")
    #     #
    #     #             sub = row.row(align=True)
    #     #             sub.operator("object.vertex_group_select", text="Select")
    #     #             sub.operator("object.vertex_group_deselect", text="Deselect")
    #     #
    #     #             layout.prop(context.tool_settings, "vertex_group_weight", text="Weight")
    #     #
    #     #
    #     # class DATA_PT_shape_keys(MeshButtonsPanel, Panel):
    #     #     bl_label = "Shape Keys"
    #     #     COMPAT_ENGINES = {'BLENDER_RENDER', 'BLENDER_GAME'}
    #     #
    #     #     @classmethod
    #     #     def poll(cls, context):
    #     #         engine = context.scene.render.engine
    #     #         obj = context.object
    #     #         return (obj and obj.type in {'MESH', 'LATTICE', 'CURVE', 'SURFACE'} and (engine in cls.COMPAT_ENGINES))
    #     #
    #     #     def draw(self, context):
    #     #         layout = self.layout
    #     #
    #     #         ob = context.object
    #     #         key = ob.data.shape_keys
    #     #         kb = ob.active_shape_key
    #     #
    #     #         enable_edit = ob.mode != 'EDIT'
    #     #         enable_edit_value = False
    #     #
    #     #         if ob.show_only_shape_key is False:
    #     #             if enable_edit or (ob.type == 'MESH' and ob.use_shape_key_edit_mode):
    #     #                 enable_edit_value = True
    #     #
    #     #         row = layout.row()
    #     #
    #     #         rows = 2
    #     #         if kb:
    #     #             rows = 4
    #     #         row.template_list("MESH_UL_shape_keys", "", key, "key_blocks", ob, "active_shape_key_index", rows=rows)
    #     #
    #     #         col = row.column()
    #     #
    #     #         sub = col.column(align=True)
    #     #         sub.operator("object.shape_key_add", icon='ZOOMIN', text="").from_mix = False
    #     #         sub.operator("object.shape_key_remove", icon='ZOOMOUT', text="").all = False
    #     #         sub.menu("MESH_MT_shape_key_specials", icon='DOWNARROW_HLT', text="")
    #     #
    #     #         if kb:
    #     #             col.separator()
    #     #
    #     #             sub = col.column(align=True)
    #     #             sub.operator("object.shape_key_move", icon='TRIA_UP', text="").type = 'UP'
    #     #             sub.operator("object.shape_key_move", icon='TRIA_DOWN', text="").type = 'DOWN'
    #     #
    #     #             split = layout.split(percentage=0.4)
    #     #             row = split.row()
    #     #             row.enabled = enable_edit
    #     #             row.prop(key, "use_relative")
    #     #
    #     #             row = split.row()
    #     #             row.alignment = 'RIGHT'
    #     #
    #     #             sub = row.row(align=True)
    #     #             sub.label()  # XXX, for alignment only
    #     #             subsub = sub.row(align=True)
    #     #             subsub.active = enable_edit_value
    #     #             subsub.prop(ob, "show_only_shape_key", text="")
    #     #             sub.prop(ob, "use_shape_key_edit_mode", text="")
    #     #
    #     #             sub = row.row()
    #     #             if key.use_relative:
    #     #                 sub.operator("object.shape_key_clear", icon='X', text="")
    #     #             else:
    #     #                 sub.operator("object.shape_key_retime", icon='RECOVER_LAST', text="")
    #     #
    #     #             if key.use_relative:
    #     #                 if ob.active_shape_key_index != 0:
    #     #                     row = layout.row()
    #     #                     row.active = enable_edit_value
    #     #                     row.prop(kb, "value")
    #     #
    #     #                     split = layout.split()
    #     #
    #     #                     col = split.column(align=True)
    #     #                     col.active = enable_edit_value
    #     #                     col.label(text="Range:")
    #     #                     col.prop(kb, "slider_min", text="Min")
    #     #                     col.prop(kb, "slider_max", text="Max")
    #     #
    #     #                     col = split.column(align=True)
    #     #                     col.active = enable_edit_value
    #     #                     col.label(text="Blend:")
    #     #                     col.prop_search(kb, "vertex_group", ob, "vertex_groups", text="")
    #     #                     col.prop_search(kb, "relative_key", key, "key_blocks", text="")
    #     #
    #     #             else:
    #     #                 layout.prop(kb, "interpolation")
    #     #                 row = layout.column()
    #     #                 row.active = enable_edit_value
    #     #                 row.prop(key, "eval_time")
    #     #
    #     #
    #     # class DATA_PT_uv_texture(MeshButtonsPanel, Panel):
    #     #     bl_label = "UV Maps"
    #     #     COMPAT_ENGINES = {'BLENDER_RENDER', 'BLENDER_GAME'}
    #     #
    #     #     def draw(self, context):
    #     #         layout = self.layout
    #     #
    #     #         me = context.mesh
    #     #
    #     #         row = layout.row()
    #     #         col = row.column()
    #     #
    #     #         col.template_list("MESH_UL_uvmaps_vcols", "uvmaps", me, "uv_textures", me.uv_textures, "active_index", rows=1)
    #     #
    #     #         col = row.column(align=True)
    #     #         col.operator("mesh.uv_texture_add", icon='ZOOMIN', text="")
    #     #         col.operator("mesh.uv_texture_remove", icon='ZOOMOUT', text="")
    #     #
    #     #
    #     # class DATA_PT_vertex_colors(MeshButtonsPanel, Panel):
    #     #     bl_label = "Vertex Colors"
    #     #     COMPAT_ENGINES = {'BLENDER_RENDER', 'BLENDER_GAME'}
    #     #
    #     #     def draw(self, context):
    #     #         layout = self.layout
    #     #
    #     #         me = context.mesh
    #     #
    #     #         row = layout.row()
    #     #         col = row.column()
    #     #
    #     #         col.template_list("MESH_UL_uvmaps_vcols", "vcols", me, "vertex_colors", me.vertex_colors, "active_index", rows=1)
    #     #
    #     #         col = row.column(align=True)
    #     #         col.operator("mesh.vertex_color_add", icon='ZOOMIN', text="")
    #     #         col.operator("mesh.vertex_color_remove", icon='ZOOMOUT', text="")
    #     #
    #     #
    #     # class DATA_PT_customdata(MeshButtonsPanel, Panel):
    #     #     bl_label = "Geometry Data"
    #     #     bl_options = {'DEFAULT_CLOSED'}
    #     #     COMPAT_ENGINES = {'BLENDER_RENDER', 'BLENDER_GAME'}
    #     #
    #     #     def draw(self, context):
    #     #         layout = self.layout
    #     #
    #     #         obj = context.object
    #     #         me = context.mesh
    #     #         col = layout.column()
    #     #
    #     #         col.operator("mesh.customdata_mask_clear", icon='X')
    #     #         col.operator("mesh.customdata_skin_clear", icon='X')
    #     #
    #     #         if me.has_custom_normals:
    #     #             col.operator("mesh.customdata_custom_splitnormals_clear", icon='X')
    #     #         else:
    #     #             col.operator("mesh.customdata_custom_splitnormals_add", icon='ZOOMIN')
    #     #
    #     #         col = layout.column()
    #     #
    #     #         col.enabled = (obj.mode != 'EDIT')
    #     #         col.prop(me, "use_customdata_vertex_bevel")
    #     #         col.prop(me, "use_customdata_edge_bevel")
    #     #         col.prop(me, "use_customdata_edge_crease")
    #     #
    #     #
    #     # class DATA_PT_custom_props_mesh(MeshButtonsPanel, PropertyPanel, Panel):
    #     #     COMPAT_ENGINES = {'BLENDER_RENDER', 'BLENDER_GAME'}
    #     #     _context_path = "object.data"
    #     #     _property_type = bpy.types.Mesh
    #     #
    #     #
    #     # classes = (
    #     #     MESH_MT_vertex_group_specials,
    #     #     MESH_MT_shape_key_specials,
    #     #     MESH_UL_vgroups,
    #     #     MESH_UL_shape_keys,
    #     #     MESH_UL_uvmaps_vcols,
    #     #     DATA_PT_context_mesh,
    #     #     DATA_PT_normals,
    #     #     DATA_PT_texture_space,
    #     #     DATA_PT_vertex_groups,
    #     #     DATA_PT_shape_keys,
    #     #     DATA_PT_uv_texture,
    #     #     DATA_PT_vertex_colors,
    #     #     DATA_PT_customdata,
    #     #     DATA_PT_custom_props_mesh,
    #     # )
    #     #
    #     # # if __name__ == "__main__":  # only for live edit.
    #         from bpy.utils import register_class
    #         for cls in classes:
    #             register_class(cls)
    #
    #
    # class Curve:
    #
    #
    #     def __init__(self, operator, context):
    #
    #         pass
    #
    #
    #     # class CurveButtonsPanel:
    #     #     bl_space_type = 'PROPERTIES'
    #     #     bl_region_type = 'WINDOW'
    #     #     bl_context = "data"
    #     #
    #     #     @classmethod
    #     #     def poll(cls, context):
    #     #         return (context.curve is not None)
    #     #
    #     #
    #     # class CurveButtonsPanelCurve(CurveButtonsPanel):
    #     #     @classmethod
    #     #     def poll(cls, context):
    #     #         return (type(context.curve) is Curve)
    #     #
    #     #
    #     # class CurveButtonsPanelSurface(CurveButtonsPanel):
    #     #     @classmethod
    #     #     def poll(cls, context):
    #     #         return (type(context.curve) is SurfaceCurve)
    #     #
    #     #
    #     # class CurveButtonsPanelText(CurveButtonsPanel):
    #     #     @classmethod
    #     #     def poll(cls, context):
    #     #         return (type(context.curve) is TextCurve)
    #     #
    #     #
    #     # class CurveButtonsPanelActive(CurveButtonsPanel):
    #     #     """Same as above but for curves only"""
    #     #
    #     #     @classmethod
    #     #     def poll(cls, context):
    #     #         curve = context.curve
    #     #         return (curve and type(curve) is not TextCurve and curve.splines.active)
    #     #
    #     #
    #     # class DATA_PT_context_curve(CurveButtonsPanel, Panel):
    #     #     bl_label = ""
    #     #     bl_options = {'HIDE_HEADER'}
    #     #
    #     #     def draw(self, context):
    #     #         layout = self.layout
    #     #
    #     #         obj = context.object
    #     #         curve = context.curve
    #     #         space = context.space_data
    #     #
    #     #         if obj:
    #     #             layout.template_ID(obj, "data")
    #     #         elif curve:
    #     #             layout.template_ID(space, "pin_id")
    #     #
    #     #
    #     # class DATA_PT_shape_curve(CurveButtonsPanel, Panel):
    #     #     bl_label = "Shape"
    #     #
    #     #     def draw(self, context):
    #     #         layout = self.layout
    #     #
    #     #         curve = context.curve
    #     #         is_surf = type(curve) is SurfaceCurve
    #     #         is_curve = type(curve) is Curve
    #     #         is_text = type(curve) is TextCurve
    #     #
    #     #         if is_curve:
    #     #             row = layout.row()
    #     #             row.prop(curve, "dimensions", expand=True)
    #     #
    #     #         split = layout.split()
    #     #
    #     #         col = split.column()
    #     #         col.label(text="Resolution:")
    #     #         sub = col.column(align=True)
    #     #         sub.prop(curve, "resolution_u", text="Preview U")
    #     #         sub.prop(curve, "render_resolution_u", text="Render U")
    #     #         if is_curve:
    #     #             col.label(text="Twisting:")
    #     #             col.prop(curve, "twist_mode", text="")
    #     #             col.prop(curve, "twist_smooth", text="Smooth")
    #     #         elif is_text:
    #     #             col.label(text="Display:")
    #     #             col.prop(curve, "use_fast_edit", text="Fast Editing")
    #     #
    #     #         col = split.column()
    #     #
    #     #         if is_surf:
    #     #             sub = col.column()
    #     #             sub.label(text="")
    #     #             sub = col.column(align=True)
    #     #             sub.prop(curve, "resolution_v", text="Preview V")
    #     #             sub.prop(curve, "render_resolution_v", text="Render V")
    #     #
    #     #         if is_curve or is_text:
    #     #             col.label(text="Fill:")
    #     #             sub = col.column()
    #     #             sub.active = (curve.dimensions == '2D' or (curve.bevel_object is None and curve.dimensions == '3D'))
    #     #             sub.prop(curve, "fill_mode", text="")
    #     #             col.prop(curve, "use_fill_deform")
    #     #
    #     #         if is_curve:
    #     #             col.label(text="Path/Curve-Deform:")
    #     #             sub = col.column()
    #     #             subsub = sub.row()
    #     #             subsub.prop(curve, "use_radius")
    #     #             subsub.prop(curve, "use_stretch")
    #     #             sub.prop(curve, "use_deform_bounds")
    #     #
    #     #
    #     # class DATA_PT_curve_texture_space(CurveButtonsPanel, Panel):
    #     #     bl_label = "Texture Space"
    #     #     bl_options = {'DEFAULT_CLOSED'}
    #     #     COMPAT_ENGINES = {'BLENDER_RENDER', 'BLENDER_GAME'}
    #     #
    #     #     def draw(self, context):
    #     #         layout = self.layout
    #     #
    #     #         curve = context.curve
    #     #
    #     #         row = layout.row()
    #     #         row.prop(curve, "use_auto_texspace")
    #     #         row.prop(curve, "use_uv_as_generated")
    #     #
    #     #         row = layout.row()
    #     #         row.column().prop(curve, "texspace_location", text="Location")
    #     #         row.column().prop(curve, "texspace_size", text="Size")
    #     #
    #     #         layout.operator("curve.match_texture_space")
    #     #
    #     #
    #     # class DATA_PT_geometry_curve(CurveButtonsPanelCurve, Panel):
    #     #     bl_label = "Geometry"
    #     #
    #     #     @classmethod
    #     #     def poll(cls, context):
    #     #         return (type(context.curve) in {Curve, TextCurve})
    #     #
    #     #     def draw(self, context):
    #     #         layout = self.layout
    #     #
    #     #         curve = context.curve
    #     #
    #     #         split = layout.split()
    #     #
    #     #         col = split.column()
    #     #         col.label(text="Modification:")
    #     #         col.prop(curve, "offset")
    #     #         col.prop(curve, "extrude")
    #     #         col.label(text="Taper Object:")
    #     #         col.prop(curve, "taper_object", text="")
    #     #
    #     #         col = split.column()
    #     #         col.label(text="Bevel:")
    #     #         col.prop(curve, "bevel_depth", text="Depth")
    #     #         col.prop(curve, "bevel_resolution", text="Resolution")
    #     #         col.label(text="Bevel Object:")
    #     #         col.prop(curve, "bevel_object", text="")
    #     #
    #     #         if type(curve) is not TextCurve:
    #     #             col = layout.column(align=True)
    #     #             row = col.row()
    #     #             row.label(text="Bevel Factor:")
    #     #
    #     #             col = layout.column()
    #     #             col.active = (
    #     #                     (curve.bevel_depth > 0.0) or
    #     #                     (curve.extrude > 0.0) or
    #     #                     (curve.bevel_object is not None))
    #     #             row = col.row(align=True)
    #     #             row.prop(curve, "bevel_factor_mapping_start", text="")
    #     #             row.prop(curve, "bevel_factor_start", text="Start")
    #     #             row = col.row(align=True)
    #     #             row.prop(curve, "bevel_factor_mapping_end", text="")
    #     #             row.prop(curve, "bevel_factor_end", text="End")
    #     #
    #     #             row = layout.row()
    #     #             sub = row.row()
    #     #             sub.active = curve.taper_object is not None
    #     #             sub.prop(curve, "use_map_taper")
    #     #             sub = row.row()
    #     #             sub.active = curve.bevel_object is not None
    #     #             sub.prop(curve, "use_fill_caps")
    #     #
    #     #
    #     # class DATA_PT_pathanim(CurveButtonsPanelCurve, Panel):
    #     #     bl_label = "Path Animation"
    #     #
    #     #     def draw_header(self, context):
    #     #         curve = context.curve
    #     #
    #     #         self.layout.prop(curve, "use_path", text="")
    #     #
    #     #     def draw(self, context):
    #     #         layout = self.layout
    #     #
    #     #         curve = context.curve
    #     #
    #     #         layout.active = curve.use_path
    #     #
    #     #         col = layout.column()
    #     #         col.prop(curve, "path_duration", text="Frames")
    #     #         col.prop(curve, "eval_time")
    #     #
    #     #         # these are for paths only
    #     #         row = layout.row()
    #     #         row.prop(curve, "use_path_follow")
    #     #
    #     #
    #     # class DATA_PT_active_spline(CurveButtonsPanelActive, Panel):
    #     #     bl_label = "Active Spline"
    #     #
    #     #     def draw(self, context):
    #     #         layout = self.layout
    #     #
    #     #         curve = context.curve
    #     #         act_spline = curve.splines.active
    #     #         is_surf = type(curve) is SurfaceCurve
    #     #         is_poly = (act_spline.type == 'POLY')
    #     #
    #     #         split = layout.split()
    #     #
    #     #         if is_poly:
    #     #             # These settings are below but its easier to have
    #     #             # polys set aside since they use so few settings
    #     #             row = layout.row()
    #     #             row.label(text="Cyclic:")
    #     #             row.prop(act_spline, "use_cyclic_u", text="U")
    #     #
    #     #             layout.prop(act_spline, "use_smooth")
    #     #         else:
    #     #             col = split.column()
    #     #             col.label(text="Cyclic:")
    #     #             if act_spline.type == 'NURBS':
    #     #                 col.label(text="Bezier:")
    #     #                 col.label(text="Endpoint:")
    #     #                 col.label(text="Order:")
    #     #
    #     #             col.label(text="Resolution:")
    #     #
    #     #             col = split.column()
    #     #             col.prop(act_spline, "use_cyclic_u", text="U")
    #     #
    #     #             if act_spline.type == 'NURBS':
    #     #                 sub = col.column()
    #     #                 # sub.active = (not act_spline.use_cyclic_u)
    #     #                 sub.prop(act_spline, "use_bezier_u", text="U")
    #     #                 sub.prop(act_spline, "use_endpoint_u", text="U")
    #     #
    #     #                 sub = col.column()
    #     #                 sub.prop(act_spline, "order_u", text="U")
    #     #             col.prop(act_spline, "resolution_u", text="U")
    #     #
    #     #             if is_surf:
    #     #                 col = split.column()
    #     #                 col.prop(act_spline, "use_cyclic_v", text="V")
    #     #
    #     #                 # its a surface, assume its a nurbs
    #     #                 sub = col.column()
    #     #                 sub.active = (not act_spline.use_cyclic_v)
    #     #                 sub.prop(act_spline, "use_bezier_v", text="V")
    #     #                 sub.prop(act_spline, "use_endpoint_v", text="V")
    #     #                 sub = col.column()
    #     #                 sub.prop(act_spline, "order_v", text="V")
    #     #                 sub.prop(act_spline, "resolution_v", text="V")
    #     #
    #     #             if act_spline.type == 'BEZIER':
    #     #                 col = layout.column()
    #     #                 col.label(text="Interpolation:")
    #     #
    #     #                 sub = col.column()
    #     #                 sub.active = (curve.dimensions == '3D')
    #     #                 sub.prop(act_spline, "tilt_interpolation", text="Tilt")
    #     #
    #     #                 col.prop(act_spline, "radius_interpolation", text="Radius")
    #     #
    #     #             layout.prop(act_spline, "use_smooth")
    #     #
    #     #
    #     # class DATA_PT_font(CurveButtonsPanelText, Panel):
    #     #     bl_label = "Font"
    #     #
    #     #     def draw(self, context):
    #     #         layout = self.layout
    #     #
    #     #         text = context.curve
    #     #         char = context.curve.edit_format
    #     #
    #     #         row = layout.split(percentage=0.25)
    #     #         row.label(text="Regular")
    #     #         row.template_ID(text, "font", open="font.open", unlink="font.unlink")
    #     #         row = layout.split(percentage=0.25)
    #     #         row.label(text="Bold")
    #     #         row.template_ID(text, "font_bold", open="font.open", unlink="font.unlink")
    #     #         row = layout.split(percentage=0.25)
    #     #         row.label(text="Italic")
    #     #         row.template_ID(text, "font_italic", open="font.open", unlink="font.unlink")
    #     #         row = layout.split(percentage=0.25)
    #     #         row.label(text="Bold & Italic")
    #     #         row.template_ID(text, "font_bold_italic", open="font.open", unlink="font.unlink")
    #     #
    #     #         # layout.prop(text, "font")
    #     #
    #     #         split = layout.split()
    #     #
    #     #         col = split.column()
    #     #         col.prop(text, "size", text="Size")
    #     #         col = split.column()
    #     #         col.prop(text, "shear")
    #     #
    #     #         split = layout.split()
    #     #
    #     #         col = split.column()
    #     #         col.label(text="Object Font:")
    #     #         col.prop(text, "family", text="")
    #     #
    #     #         col = split.column()
    #     #         col.label(text="Text on Curve:")
    #     #         col.prop(text, "follow_curve", text="")
    #     #
    #     #         split = layout.split()
    #     #
    #     #         col = split.column()
    #     #         sub = col.column(align=True)
    #     #         sub.label(text="Underline:")
    #     #         sub.prop(text, "underline_position", text="Position")
    #     #         sub.prop(text, "underline_height", text="Thickness")
    #     #
    #     #         col = split.column()
    #     #         col.label(text="Character:")
    #     #         col.prop(char, "use_bold")
    #     #         col.prop(char, "use_italic")
    #     #         col.prop(char, "use_underline")
    #     #
    #     #         row = layout.row()
    #     #         row.prop(text, "small_caps_scale", text="Small Caps")
    #     #         row.prop(char, "use_small_caps")
    #     #
    #     #
    #     # class DATA_PT_paragraph(CurveButtonsPanelText, Panel):
    #     #     bl_label = "Paragraph"
    #     #
    #     #     def draw(self, context):
    #     #         layout = self.layout
    #     #
    #     #         text = context.curve
    #     #
    #     #         layout.label(text="Horizontal Alignment:")
    #     #         layout.row().prop(text, "align_x", expand=True)
    #     #
    #     #         layout.label(text="Vertical Alignment:")
    #     #         layout.row().prop(text, "align_y", expand=True)
    #     #
    #     #         split = layout.split()
    #     #
    #     #         col = split.column(align=True)
    #     #         col.label(text="Spacing:")
    #     #         col.prop(text, "space_character", text="Letter")
    #     #         col.prop(text, "space_word", text="Word")
    #     #         col.prop(text, "space_line", text="Line")
    #     #
    #     #         col = split.column(align=True)
    #     #         col.label(text="Offset:")
    #     #         col.prop(text, "offset_x", text="X")
    #     #         col.prop(text, "offset_y", text="Y")
    #     #
    #     #
    #     # class DATA_PT_text_boxes(CurveButtonsPanelText, Panel):
    #     #     bl_label = "Text Boxes"
    #     #
    #     #     def draw(self, context):
    #     #         layout = self.layout
    #     #
    #     #         text = context.curve
    #     #
    #     #         split = layout.split()
    #     #         col = split.column()
    #     #         col.operator("font.textbox_add", icon='ZOOMIN')
    #     #         col = split.column()
    #     #
    #     #         for i, box in enumerate(text.text_boxes):
    #     #
    #     #             boxy = layout.box()
    #     #
    #     #             row = boxy.row()
    #     #
    #     #             split = row.split()
    #     #
    #     #             col = split.column(align=True)
    #     #
    #     #             col.label(text="Dimensions:")
    #     #             col.prop(box, "width", text="Width")
    #     #             col.prop(box, "height", text="Height")
    #     #
    #     #             col = split.column(align=True)
    #     #
    #     #             col.label(text="Offset:")
    #     #             col.prop(box, "x", text="X")
    #     #             col.prop(box, "y", text="Y")
    #     #
    #     #             row.operator("font.textbox_remove", text="", icon='X', emboss=False).index = i
    #     #
    #     #
    #     # class DATA_PT_custom_props_curve(CurveButtonsPanel, PropertyPanel, Panel):
    #     #     COMPAT_ENGINES = {'BLENDER_RENDER', 'BLENDER_GAME'}
    #     #     _context_path = "object.data"
    #     #     _property_type = bpy.types.Curve
    #     #
    #     #
    #     # classes = (
    #     #     DATA_PT_context_curve,
    #     #     DATA_PT_shape_curve,
    #     #     DATA_PT_curve_texture_space,
    #     #     DATA_PT_geometry_curve,
    #     #     DATA_PT_pathanim,
    #     #     DATA_PT_active_spline,
    #     #     DATA_PT_font,
    #     #     DATA_PT_paragraph,
    #     #     DATA_PT_text_boxes,
    #     #     DATA_PT_custom_props_curve,
    #     # )
    #     #
    #     # if __name__ == "__main__":  # only for live edit.
    #     #     from bpy.utils import register_class
    #     #     for cls in classes:
    #     #         register_class(cls)
    #
    #
    # class MetaBall:
    #
    #
    #     def __init__(self, operator, context):
    #
    #         pass
    #
    #     # # <pep8 compliant>
    #     # import bpy
    #     # from bpy.types import Panel
    #     # from rna_prop_ui import PropertyPanel
    #     #
    #     #
    #     # class DataButtonsPanel:
    #     #     bl_space_type = 'PROPERTIES'
    #     #     bl_region_type = 'WINDOW'
    #     #     bl_context = "data"
    #     #
    #     #     @classmethod
    #     #     def poll(cls, context):
    #     #         return context.meta_ball
    #     #
    #     #
    #     # class DATA_PT_context_metaball(DataButtonsPanel, Panel):
    #     #     bl_label = ""
    #     #     bl_options = {'HIDE_HEADER'}
    #     #
    #     #     def draw(self, context):
    #     #         layout = self.layout
    #     #
    #     #         ob = context.object
    #     #         mball = context.meta_ball
    #     #         space = context.space_data
    #     #
    #     #         if ob:
    #     #             layout.template_ID(ob, "data")
    #     #         elif mball:
    #     #             layout.template_ID(space, "pin_id")
    #     #
    #     #
    #     # class DATA_PT_metaball(DataButtonsPanel, Panel):
    #     #     bl_label = "Metaball"
    #     #
    #     #     def draw(self, context):
    #     #         layout = self.layout
    #     #
    #     #         mball = context.meta_ball
    #     #
    #     #         split = layout.split()
    #     #
    #     #         col = split.column()
    #     #         col.label(text="Resolution:")
    #     #         sub = col.column(align=True)
    #     #         sub.prop(mball, "resolution", text="View")
    #     #         sub.prop(mball, "render_resolution", text="Render")
    #     #
    #     #         col = split.column()
    #     #         col.label(text="Settings:")
    #     #         col.prop(mball, "threshold", text="Threshold")
    #     #
    #     #         layout.label(text="Update:")
    #     #         layout.row().prop(mball, "update_method", expand=True)
    #     #
    #     #
    #     # class DATA_PT_mball_texture_space(DataButtonsPanel, Panel):
    #     #     bl_label = "Texture Space"
    #     #     bl_options = {'DEFAULT_CLOSED'}
    #     #     COMPAT_ENGINES = {'BLENDER_RENDER', 'BLENDER_GAME'}
    #     #
    #     #     def draw(self, context):
    #     #         layout = self.layout
    #     #
    #     #         mball = context.meta_ball
    #     #
    #     #         layout.prop(mball, "use_auto_texspace")
    #     #
    #     #         row = layout.row()
    #     #         row.column().prop(mball, "texspace_location", text="Location")
    #     #         row.column().prop(mball, "texspace_size", text="Size")
    #     #
    #     #
    #     # class DATA_PT_metaball_element(DataButtonsPanel, Panel):
    #     #     bl_label = "Active Element"
    #     #
    #     #     @classmethod
    #     #     def poll(cls, context):
    #     #         return (context.meta_ball and context.meta_ball.elements.active)
    #     #
    #     #     def draw(self, context):
    #     #         layout = self.layout
    #     #
    #     #         metaelem = context.meta_ball.elements.active
    #     #
    #     #         layout.prop(metaelem, "type")
    #     #
    #     #         split = layout.split()
    #     #
    #     #         col = split.column(align=True)
    #     #         col.label(text="Settings:")
    #     #         col.prop(metaelem, "stiffness", text="Stiffness")
    #     #         col.prop(metaelem, "use_negative", text="Negative")
    #     #         col.prop(metaelem, "hide", text="Hide")
    #     #
    #     #         col = split.column(align=True)
    #     #
    #     #         if metaelem.type in {'CUBE', 'ELLIPSOID'}:
    #     #             col.label(text="Size:")
    #     #             col.prop(metaelem, "size_x", text="X")
    #     #             col.prop(metaelem, "size_y", text="Y")
    #     #             col.prop(metaelem, "size_z", text="Z")
    #     #
    #     #         elif metaelem.type == 'TUBE':
    #     #             col.label(text="Size:")
    #     #             col.prop(metaelem, "size_x", text="X")
    #     #
    #     #         elif metaelem.type == 'PLANE':
    #     #             col.label(text="Size:")
    #     #             col.prop(metaelem, "size_x", text="X")
    #     #             col.prop(metaelem, "size_y", text="Y")
    #     #
    #     #
    #     # class DATA_PT_custom_props_metaball(DataButtonsPanel, PropertyPanel, Panel):
    #     #     COMPAT_ENGINES = {'BLENDER_RENDER', 'BLENDER_GAME'}
    #     #     _context_path = "object.data"
    #     #     _property_type = bpy.types.MetaBall
    #     #
    #     #
    #     # classes = (
    #     #     DATA_PT_context_metaball,
    #     #     DATA_PT_metaball,
    #     #     DATA_PT_mball_texture_space,
    #     #     DATA_PT_metaball_element,
    #     #     DATA_PT_custom_props_metaball,
    #     # )
    #     #
    #     # if __name__ == "__main__":  # only for live edit.
    #     #     from bpy.utils import register_class
    #     #     for cls in classes:
    #     #         register_class(cls)
    #
    #
    # class Armature:
    #
    #
    #     def __init__(self, operator, context):
    #
    #         pass
    #
    #     # # <pep8 compliant>
    #     # import bpy
    #     # from bpy.types import Panel, Menu
    #     # from rna_prop_ui import PropertyPanel
    #     #
    #     #
    #     # class ArmatureButtonsPanel:
    #     #     bl_space_type = 'PROPERTIES'
    #     #     bl_region_type = 'WINDOW'
    #     #     bl_context = "data"
    #     #
    #     #     @classmethod
    #     #     def poll(cls, context):
    #     #         return context.armature
    #     #
    #     #
    #     # class DATA_PT_context_arm(ArmatureButtonsPanel, Panel):
    #     #     bl_label = ""
    #     #     bl_options = {'HIDE_HEADER'}
    #     #
    #     #     def draw(self, context):
    #     #         layout = self.layout
    #     #
    #     #         ob = context.object
    #     #         arm = context.armature
    #     #         space = context.space_data
    #     #
    #     #         if ob:
    #     #             layout.template_ID(ob, "data")
    #     #         elif arm:
    #     #             layout.template_ID(space, "pin_id")
    #     #
    #     #
    #     # class DATA_PT_skeleton(ArmatureButtonsPanel, Panel):
    #     #     bl_label = "Skeleton"
    #     #
    #     #     def draw(self, context):
    #     #         layout = self.layout
    #     #
    #     #         arm = context.armature
    #     #
    #     #         layout.row().prop(arm, "pose_position", expand=True)
    #     #
    #     #         col = layout.column()
    #     #         col.label(text="Layers:")
    #     #         col.prop(arm, "layers", text="")
    #     #         col.label(text="Protected Layers:")
    #     #         col.prop(arm, "layers_protected", text="")
    #     #
    #     #         if context.scene.render.engine == 'BLENDER_GAME':
    #     #             col = layout.column()
    #     #             col.label(text="Deform:")
    #     #             col.prop(arm, "deform_method", expand=True)
    #     #
    #     #
    #     # class DATA_PT_display(ArmatureButtonsPanel, Panel):
    #     #     bl_label = "Display"
    #     #
    #     #     def draw(self, context):
    #     #         layout = self.layout
    #     #
    #     #         ob = context.object
    #     #         arm = context.armature
    #     #
    #     #         layout.row().prop(arm, "draw_type", expand=True)
    #     #
    #     #         split = layout.split()
    #     #
    #     #         col = split.column()
    #     #         col.prop(arm, "show_names", text="Names")
    #     #         col.prop(arm, "show_axes", text="Axes")
    #     #         col.prop(arm, "show_bone_custom_shapes", text="Shapes")
    #     #
    #     #         col = split.column()
    #     #         col.prop(arm, "show_group_colors", text="Colors")
    #     #         if ob:
    #     #             col.prop(ob, "show_x_ray", text="X-Ray")
    #     #         col.prop(arm, "use_deform_delay", text="Delay Refresh")
    #     #
    #     #
    #     # class DATA_PT_bone_group_specials(Menu):
    #     #     bl_label = "Bone Group Specials"
    #     #
    #     #     def draw(self, context):
    #     #         layout = self.layout
    #     #
    #     #         layout.operator("pose.group_sort", icon='SORTALPHA')
    #     #
    #     #
    #     # class DATA_PT_bone_groups(ArmatureButtonsPanel, Panel):
    #     #     bl_label = "Bone Groups"
    #     #
    #     #     @classmethod
    #     #     def poll(cls, context):
    #     #         return (context.object and context.object.type == 'ARMATURE' and context.object.pose)
    #     #
    #     #     def draw(self, context):
    #     #         layout = self.layout
    #     #
    #     #         ob = context.object
    #     #         pose = ob.pose
    #     #         group = pose.bone_groups.active
    #     #
    #     #         row = layout.row()
    #     #
    #     #         rows = 1
    #     #         if group:
    #     #             rows = 4
    #     #         row.template_list("UI_UL_list", "bone_groups", pose, "bone_groups", pose.bone_groups, "active_index", rows=rows)
    #     #
    #     #         col = row.column(align=True)
    #     #         col.active = (ob.proxy is None)
    #     #         col.operator("pose.group_add", icon='ZOOMIN', text="")
    #     #         col.operator("pose.group_remove", icon='ZOOMOUT', text="")
    #     #         col.menu("DATA_PT_bone_group_specials", icon='DOWNARROW_HLT', text="")
    #     #         if group:
    #     #             col.separator()
    #     #             col.operator("pose.group_move", icon='TRIA_UP', text="").direction = 'UP'
    #     #             col.operator("pose.group_move", icon='TRIA_DOWN', text="").direction = 'DOWN'
    #     #
    #     #             split = layout.split()
    #     #             split.active = (ob.proxy is None)
    #     #
    #     #             col = split.column()
    #     #             col.prop(group, "color_set")
    #     #             if group.color_set:
    #     #                 col = split.column()
    #     #                 sub = col.row(align=True)
    #     #                 sub.enabled = group.is_custom_color_set  # only custom colors are editable
    #     #                 sub.prop(group.colors, "normal", text="")
    #     #                 sub.prop(group.colors, "select", text="")
    #     #                 sub.prop(group.colors, "active", text="")
    #     #
    #     #         row = layout.row()
    #     #         row.active = (ob.proxy is None)
    #     #
    #     #         sub = row.row(align=True)
    #     #         sub.operator("pose.group_assign", text="Assign")
    #     #         sub.operator("pose.group_unassign", text="Remove")  # row.operator("pose.bone_group_remove_from", text="Remove")
    #     #
    #     #         sub = row.row(align=True)
    #     #         sub.operator("pose.group_select", text="Select")
    #     #         sub.operator("pose.group_deselect", text="Deselect")
    #     #
    #     #
    #     # class DATA_PT_pose_library(ArmatureButtonsPanel, Panel):
    #     #     bl_label = "Pose Library"
    #     #     bl_options = {'DEFAULT_CLOSED'}
    #     #
    #     #     @classmethod
    #     #     def poll(cls, context):
    #     #         return (context.object and context.object.type == 'ARMATURE' and context.object.pose)
    #     #
    #     #     def draw(self, context):
    #     #         layout = self.layout
    #     #
    #     #         ob = context.object
    #     #         poselib = ob.pose_library
    #     #
    #     #         layout.template_ID(ob, "pose_library", new="poselib.new", unlink="poselib.unlink")
    #     #
    #     #         if poselib:
    #     #             # warning about poselib being in an invalid state
    #     #             if len(poselib.fcurves) > 0 and len(poselib.pose_markers) == 0:
    #     #                 layout.label(icon='ERROR', text="Error: Potentially corrupt library, run 'Sanitize' operator to fix")
    #     #
    #     #             # list of poses in pose library
    #     #             row = layout.row()
    #     #             row.template_list("UI_UL_list", "pose_markers", poselib, "pose_markers",
    #     #                               poselib.pose_markers, "active_index", rows=5)
    #     #
    #     #             # column of operators for active pose
    #     #             # - goes beside list
    #     #             col = row.column(align=True)
    #     #
    #     #             # invoke should still be used for 'add', as it is needed to allow
    #     #             # add/replace options to be used properly
    #     #             col.operator("poselib.pose_add", icon='ZOOMIN', text="")
    #     #
    #     #             col.operator_context = 'EXEC_DEFAULT'  # exec not invoke, so that menu doesn't need showing
    #     #
    #     #             pose_marker_active = poselib.pose_markers.active
    #     #
    #     #             if pose_marker_active is not None:
    #     #                 col.operator("poselib.pose_remove", icon='ZOOMOUT', text="")
    #     #                 col.operator("poselib.apply_pose", icon='ZOOM_SELECTED', text="").pose_index = poselib.pose_markers.active_index
    #     #
    #     #             col.operator("poselib.action_sanitize", icon='HELP', text="")  # kkkkkkkkkkkkkkkkkkXXX: put in menu?
    #     #
    #     #             if pose_marker_active is not None:
    #     #                 col.operator("poselib.pose_move", icon='TRIA_UP', text="").direction = 'UP'
    #     #                 col.operator("poselib.pose_move", icon='TRIA_DOWN', text="").direction = 'DOWN'
    #     #
    #     #
    #     # # TODO: this panel will soon be deprecated too
    #     # class DATA_PT_ghost(ArmatureButtonsPanel, Panel):
    #     #     bl_label = "Ghost"
    #     #
    #     #     def draw(self, context):
    #     #         layout = self.layout
    #     #
    #     #         arm = context.armature
    #     #
    #     #         layout.row().prop(arm, "ghost_type", expand=True)
    #     #
    #     #         split = layout.split()
    #     #
    #     #         col = split.column(align=True)
    #     #
    #     #         if arm.ghost_type == 'RANGE':
    #     #             col.prop(arm, "ghost_frame_start", text="Start")
    #     #             col.prop(arm, "ghost_frame_end", text="End")
    #     #             col.prop(arm, "ghost_size", text="Step")
    #     #         elif arm.ghost_type == 'CURRENT_FRAME':
    #     #             col.prop(arm, "ghost_step", text="Range")
    #     #             col.prop(arm, "ghost_size", text="Step")
    #     #
    #     #         col = split.column()
    #     #         col.label(text="Display:")
    #     #         col.prop(arm, "show_only_ghost_selected", text="Selected Only")
    #     #
    #     #
    #     # class DATA_PT_iksolver_itasc(ArmatureButtonsPanel, Panel):
    #     #     bl_label = "Inverse Kinematics"
    #     #     bl_options = {'DEFAULT_CLOSED'}
    #     #
    #     #     @classmethod
    #     #     def poll(cls, context):
    #     #         ob = context.object
    #     #         return (ob and ob.pose)
    #     #
    #     #     def draw(self, context):
    #     #         layout = self.layout
    #     #
    #     #         ob = context.object
    #     #         itasc = ob.pose.ik_param
    #     #
    #     #         layout.prop(ob.pose, "ik_solver")
    #     #
    #     #         if itasc:
    #     #             layout.row().prop(itasc, "mode", expand=True)
    #     #             simulation = (itasc.mode == 'SIMULATION')
    #     #             if simulation:
    #     #                 layout.label(text="Reiteration:")
    #     #                 layout.row().prop(itasc, "reiteration_method", expand=True)
    #     #
    #     #             row = layout.row()
    #     #             row.active = not simulation or itasc.reiteration_method != 'NEVER'
    #     #             row.prop(itasc, "precision")
    #     #             row.prop(itasc, "iterations")
    #     #
    #     #             if simulation:
    #     #                 layout.prop(itasc, "use_auto_step")
    #     #                 row = layout.row()
    #     #                 if itasc.use_auto_step:
    #     #                     row.prop(itasc, "step_min", text="Min")
    #     #                     row.prop(itasc, "step_max", text="Max")
    #     #                 else:
    #     #                     row.prop(itasc, "step_count")
    #     #
    #     #             layout.prop(itasc, "solver")
    #     #             if simulation:
    #     #                 layout.prop(itasc, "feedback")
    #     #                 layout.prop(itasc, "velocity_max")
    #     #             if itasc.solver == 'DLS':
    #     #                 row = layout.row()
    #     #                 row.prop(itasc, "damping_max", text="Damp", slider=True)
    #     #                 row.prop(itasc, "damping_epsilon", text="Eps", slider=True)
    #     #
    #     # from bl_ui.properties_animviz import (
    #     #         MotionPathButtonsPanel,
    #     #         OnionSkinButtonsPanel,
    #     #         )
    #     #
    #     #
    #     # class DATA_PT_motion_paths(MotionPathButtonsPanel, Panel):
    #     #     #bl_label = "Bones Motion Paths"
    #     #     bl_context = "data"
    #     #
    #     #     @classmethod
    #     #     def poll(cls, context):
    #     #         # XXX: include pose-mode check?
    #     #         return (context.object) and (context.armature)
    #     #
    #     #     def draw(self, context):
    #     #         # layout = self.layout
    #     #
    #     #         ob = context.object
    #     #         avs = ob.pose.animation_visualization
    #     #
    #     #         pchan = context.active_pose_bone
    #     #         mpath = pchan.motion_path if pchan else None
    #     #
    #     #         self.draw_settings(context, avs, mpath, bones=True)
    #     #
    #     #
    #     # class DATA_PT_onion_skinning(OnionSkinButtonsPanel):  # , Panel): # inherit from panel when ready
    #     #     #bl_label = "Bones Onion Skinning"
    #     #     bl_context = "data"
    #     #
    #     #     @classmethod
    #     #     def poll(cls, context):
    #     #         # XXX: include pose-mode check?
    #     #         return (context.object) and (context.armature)
    #     #
    #     #     def draw(self, context):
    #     #         ob = context.object
    #     #
    #     #         self.draw_settings(context, ob.pose.animation_visualization, bones=True)
    #     #
    #     #
    #     # class DATA_PT_custom_props_arm(ArmatureButtonsPanel, PropertyPanel, Panel):
    #     #     COMPAT_ENGINES = {'BLENDER_RENDER', 'BLENDER_GAME'}
    #     #     _context_path = "object.data"
    #     #     _property_type = bpy.types.Armature
    #     #
    #     #
    #     # classes = (
    #     #     DATA_PT_context_arm,
    #     #     DATA_PT_skeleton,
    #     #     DATA_PT_display,
    #     #     DATA_PT_bone_group_specials,
    #     #     DATA_PT_bone_groups,
    #     #     DATA_PT_pose_library,
    #     #     DATA_PT_ghost,
    #     #     DATA_PT_iksolver_itasc,
    #     #     DATA_PT_motion_paths,
    #     #     DATA_PT_custom_props_arm,
    #     # )
    #     #
    #     # if __name__ == "__main__":  # only for live edit.
    #     #     from bpy.utils import register_class
    #     #     for cls in classes:
    #     #         register_class(cls)
    #
    #
    # class Lattice:
    #
    #
    #     def __init__(self, operator, context):
    #
    #         pass
    #
    #     # # <pep8 compliant>
    #     # import bpy
    #     # from bpy.types import Panel
    #     # from rna_prop_ui import PropertyPanel
    #     #
    #     #
    #     # class DataButtonsPanel:
    #     #     bl_space_type = 'PROPERTIES'
    #     #     bl_region_type = 'WINDOW'
    #     #     bl_context = "data"
    #     #
    #     #     @classmethod
    #     #     def poll(cls, context):
    #     #         return context.lattice
    #     #
    #     #
    #     # class DATA_PT_context_lattice(DataButtonsPanel, Panel):
    #     #     bl_label = ""
    #     #     bl_options = {'HIDE_HEADER'}
    #     #
    #     #     def draw(self, context):
    #     #         layout = self.layout
    #     #
    #     #         ob = context.object
    #     #         lat = context.lattice
    #     #         space = context.space_data
    #     #
    #     #         split = layout.split(percentage=0.65)
    #     #         if ob:
    #     #             split.template_ID(ob, "data")
    #     #             split.separator()
    #     #         elif lat:
    #     #             split.template_ID(space, "pin_id")
    #     #             split.separator()
    #     #
    #     #
    #     # class DATA_PT_lattice(DataButtonsPanel, Panel):
    #     #     bl_label = "Lattice"
    #     #
    #     #     def draw(self, context):
    #     #         layout = self.layout
    #     #
    #     #         lat = context.lattice
    #     #
    #     #         row = layout.row()
    #     #         row.prop(lat, "points_u")
    #     #         row.prop(lat, "interpolation_type_u", text="")
    #     #
    #     #         row = layout.row()
    #     #         row.prop(lat, "points_v")
    #     #         row.prop(lat, "interpolation_type_v", text="")
    #     #
    #     #         row = layout.row()
    #     #         row.prop(lat, "points_w")
    #     #         row.prop(lat, "interpolation_type_w", text="")
    #     #
    #     #         row = layout.row()
    #     #         row.prop(lat, "use_outside")
    #     #         row.prop_search(lat, "vertex_group", context.object, "vertex_groups", text="")
    #     #
    #     #
    #     # class DATA_PT_custom_props_lattice(DataButtonsPanel, PropertyPanel, Panel):
    #     #     COMPAT_ENGINES = {'BLENDER_RENDER', 'BLENDER_GAME'}
    #     #     _context_path = "object.data"
    #     #     _property_type = bpy.types.Lattice
    #     #
    #     #
    #     # classes = (
    #     #     DATA_PT_context_lattice,
    #     #     DATA_PT_lattice,
    #     #     DATA_PT_custom_props_lattice,
    #     # )
    #     #
    #     # if __name__ == "__main__":  # only for live edit.
    #     #     from bpy.utils import register_class
    #     #     for cls in classes:
    #     #         register_class(cls)
    #
    #
    # class Empty:
    #
    #
    #     def __init__(self, operator, context):
    #
    #         pass
    #
    #     # import bpy
    #     # from bpy.types import Panel
    #     #
    #     #
    #     # class DataButtonsPanel:
    #     #     bl_space_type = 'PROPERTIES'
    #     #     bl_region_type = 'WINDOW'
    #     #     bl_context = "data"
    #     #
    #     #     @classmethod
    #     #     def poll(cls, context):
    #     #         return (context.object and context.object.type == 'EMPTY')
    #     #
    #     #
    #     # class DATA_PT_empty(DataButtonsPanel, Panel):
    #     #     bl_label = "Empty"
    #     #
    #     #     def draw(self, context):
    #     #         layout = self.layout
    #     #
    #     #         ob = context.object
    #     #
    #     #         layout.prop(ob, "empty_draw_type", text="Display")
    #     #
    #     #         if ob.empty_draw_type == 'IMAGE':
    #     #             layout.template_ID(ob, "data", open="image.open", unlink="object.unlink_data")
    #     #             layout.template_image(ob, "data", ob.image_user, compact=True)
    #     #
    #     #             row = layout.row(align=True)
    #     #             row = layout.row(align=True)
    #     #
    #     #             layout.prop(ob, "color", text="Transparency", index=3, slider=True)
    #     #             row = layout.row(align=True)
    #     #             row.prop(ob, "empty_image_offset", text="Offset X", index=0)
    #     #             row.prop(ob, "empty_image_offset", text="Offset Y", index=1)
    #     #
    #     #         layout.prop(ob, "empty_draw_size", text="Size")
    #     #
    #     #
    #     # classes = (
    #     #     DATA_PT_empty,
    #     # )
    #     #
    #     # if __name__ == "__main__":  # only for live edit.
    #     #     from bpy.utils import register_class
    #     #     for cls in classes:
    #     #         register_class(cls)
    #
    #
    # class Speaker:
    #
    #
    #     def __init__(self, operator, context):
    #
    #         pass
    #
    #     # # <pep8 compliant>
    #     # import bpy
    #     # from bpy.types import Panel
    #     # from rna_prop_ui import PropertyPanel
    #     #
    #     #
    #     # class DataButtonsPanel:
    #     #     bl_space_type = 'PROPERTIES'
    #     #     bl_region_type = 'WINDOW'
    #     #     bl_context = "data"
    #     #
    #     #     @classmethod
    #     #     def poll(cls, context):
    #     #         engine = context.scene.render.engine
    #     #         return context.speaker and (engine in cls.COMPAT_ENGINES)
    #     #
    #     #
    #     # class DATA_PT_context_speaker(DataButtonsPanel, Panel):
    #     #     bl_label = ""
    #     #     bl_options = {'HIDE_HEADER'}
    #     #     COMPAT_ENGINES = {'BLENDER_RENDER', 'BLENDER_GAME'}
    #     #
    #     #     def draw(self, context):
    #     #         layout = self.layout
    #     #
    #     #         ob = context.object
    #     #         speaker = context.speaker
    #     #         space = context.space_data
    #     #
    #     #         split = layout.split(percentage=0.65)
    #     #
    #     #         if ob:
    #     #             split.template_ID(ob, "data")
    #     #         elif speaker:
    #     #             split.template_ID(space, "pin_id")
    #     #
    #     #
    #     # class DATA_PT_speaker(DataButtonsPanel, Panel):
    #     #     bl_label = "Sound"
    #     #     COMPAT_ENGINES = {'BLENDER_RENDER'}
    #     #
    #     #     def draw(self, context):
    #     #         layout = self.layout
    #     #
    #     #         speaker = context.speaker
    #     #
    #     #         split = layout.split(percentage=0.75)
    #     #
    #     #         split.template_ID(speaker, "sound", open="sound.open_mono")
    #     #         split.prop(speaker, "muted")
    #     #
    #     #         row = layout.row()
    #     #         row.prop(speaker, "volume")
    #     #         row.prop(speaker, "pitch")
    #     #
    #     #
    #     # class DATA_PT_distance(DataButtonsPanel, Panel):
    #     #     bl_label = "Distance"
    #     #     COMPAT_ENGINES = {'BLENDER_RENDER'}
    #     #
    #     #     def draw(self, context):
    #     #         layout = self.layout
    #     #
    #     #         speaker = context.speaker
    #     #
    #     #         split = layout.split()
    #     #
    #     #         col = split.column()
    #     #         col.label("Volume:")
    #     #         col.prop(speaker, "volume_min", text="Minimum")
    #     #         col.prop(speaker, "volume_max", text="Maximum")
    #     #         col.prop(speaker, "attenuation")
    #     #
    #     #         col = split.column()
    #     #         col.label("Distance:")
    #     #         col.prop(speaker, "distance_max", text="Maximum")
    #     #         col.prop(speaker, "distance_reference", text="Reference")
    #     #
    #     #
    #     # class DATA_PT_cone(DataButtonsPanel, Panel):
    #     #     bl_label = "Cone"
    #     #     COMPAT_ENGINES = {'BLENDER_RENDER'}
    #     #
    #     #     def draw(self, context):
    #     #         layout = self.layout
    #     #
    #     #         speaker = context.speaker
    #     #
    #     #         split = layout.split()
    #     #
    #     #         col = split.column()
    #     #         col.label("Angle:")
    #     #         col.prop(speaker, "cone_angle_outer", text="Outer")
    #     #         col.prop(speaker, "cone_angle_inner", text="Inner")
    #     #
    #     #         col = split.column()
    #     #         col.label("Volume:")
    #     #         col.prop(speaker, "cone_volume_outer", text="Outer")
    #     #
    #     #
    #     # class DATA_PT_custom_props_speaker(DataButtonsPanel, PropertyPanel, Panel):
    #     #     COMPAT_ENGINES = {'BLENDER_RENDER', 'BLENDER_GAME'}
    #     #     _context_path = "object.data"
    #     #     _property_type = bpy.types.Speaker
    #     #
    #     #
    #     # classes = (
    #     #     DATA_PT_context_speaker,
    #     #     DATA_PT_speaker,
    #     #     DATA_PT_distance,
    #     #     DATA_PT_cone,
    #     #     DATA_PT_custom_props_speaker,
    #     # )
    #     #
    #     # if __name__ == "__main__":  # only for live edit.
    #     #     from bpy.utils import register_class
    #     #     for cls in classes:
    #     #         register_class(cls)
    #
    #
    # class Camera:
    #
    #
    #     def __init__(self, operator, context):
    #
    #         pass
    #
    #     # import bpy
    #     # from bpy.types import Panel, Menu
    #     # from rna_prop_ui import PropertyPanel
    #     #
    #     #
    #     # class CameraButtonsPanel:
    #     #     bl_space_type = 'PROPERTIES'
    #     #     bl_region_type = 'WINDOW'
    #     #     bl_context = "data"
    #     #
    #     #     @classmethod
    #     #     def poll(cls, context):
    #     #         engine = context.scene.render.engine
    #     #         return context.camera and (engine in cls.COMPAT_ENGINES)
    #     #
    #     #
    #     # class CAMERA_MT_presets(Menu):
    #     #     bl_label = "Camera Presets"
    #     #     preset_subdir = "camera"
    #     #     preset_operator = "script.execute_preset"
    #     #     COMPAT_ENGINES = {'BLENDER_RENDER', 'BLENDER_GAME'}
    #     #     draw = Menu.draw_preset
    #     #
    #     #
    #     # class SAFE_AREAS_MT_presets(Menu):
    #     #     bl_label = "Camera Presets"
    #     #     preset_subdir = "safe_areas"
    #     #     preset_operator = "script.execute_preset"
    #     #     COMPAT_ENGINES = {'BLENDER_RENDER', 'BLENDER_GAME'}
    #     #     draw = Menu.draw_preset
    #     #
    #     #
    #     # class DATA_PT_context_camera(CameraButtonsPanel, Panel):
    #     #     bl_label = ""
    #     #     bl_options = {'HIDE_HEADER'}
    #     #     COMPAT_ENGINES = {'BLENDER_RENDER', 'BLENDER_GAME'}
    #     #
    #     #     def draw(self, context):
    #     #         layout = self.layout
    #     #
    #     #         ob = context.object
    #     #         cam = context.camera
    #     #         space = context.space_data
    #     #
    #     #         split = layout.split(percentage=0.65)
    #     #         if ob:
    #     #             split.template_ID(ob, "data")
    #     #             split.separator()
    #     #         elif cam:
    #     #             split.template_ID(space, "pin_id")
    #     #             split.separator()
    #     #
    #     #
    #     # class DATA_PT_lens(CameraButtonsPanel, Panel):
    #     #     bl_label = "Lens"
    #     #     COMPAT_ENGINES = {'BLENDER_RENDER', 'BLENDER_GAME'}
    #     #
    #     #     def draw(self, context):
    #     #         layout = self.layout
    #     #
    #     #         cam = context.camera
    #     #
    #     #         layout.row().prop(cam, "type", expand=True)
    #     #
    #     #         split = layout.split()
    #     #
    #     #         col = split.column()
    #     #         if cam.type == 'PERSP':
    #     #             row = col.row()
    #     #             if cam.lens_unit == 'MILLIMETERS':
    #     #                 row.prop(cam, "lens")
    #     #             elif cam.lens_unit == 'FOV':
    #     #                 row.prop(cam, "angle")
    #     #             row.prop(cam, "lens_unit", text="")
    #     #
    #     #         elif cam.type == 'ORTHO':
    #     #             col.prop(cam, "ortho_scale")
    #     #
    #     #         elif cam.type == 'PANO':
    #     #             engine = context.scene.render.engine
    #     #             if engine == 'CYCLES':
    #     #                 ccam = cam.cycles
    #     #                 col.prop(ccam, "panorama_type", text="Type")
    #     #                 if ccam.panorama_type == 'FISHEYE_EQUIDISTANT':
    #     #                     col.prop(ccam, "fisheye_fov")
    #     #                 elif ccam.panorama_type == 'FISHEYE_EQUISOLID':
    #     #                     row = layout.row()
    #     #                     row.prop(ccam, "fisheye_lens", text="Lens")
    #     #                     row.prop(ccam, "fisheye_fov")
    #     #                 elif ccam.panorama_type == 'EQUIRECTANGULAR':
    #     #                     row = layout.row()
    #     #                     sub = row.column(align=True)
    #     #                     sub.prop(ccam, "latitude_min")
    #     #                     sub.prop(ccam, "latitude_max")
    #     #                     sub = row.column(align=True)
    #     #                     sub.prop(ccam, "longitude_min")
    #     #                     sub.prop(ccam, "longitude_max")
    #     #             elif engine == 'BLENDER_RENDER':
    #     #                 row = col.row()
    #     #                 if cam.lens_unit == 'MILLIMETERS':
    #     #                     row.prop(cam, "lens")
    #     #                 elif cam.lens_unit == 'FOV':
    #     #                     row.prop(cam, "angle")
    #     #                 row.prop(cam, "lens_unit", text="")
    #     #
    #     #         split = layout.split()
    #     #
    #     #         col = split.column(align=True)
    #     #         col.label(text="Shift:")
    #     #         col.prop(cam, "shift_x", text="X")
    #     #         col.prop(cam, "shift_y", text="Y")
    #     #
    #     #         col = split.column(align=True)
    #     #         col.label(text="Clipping:")
    #     #         col.prop(cam, "clip_start", text="Start")
    #     #         col.prop(cam, "clip_end", text="End")
    #     #
    #     #
    #     # class DATA_PT_camera_stereoscopy(CameraButtonsPanel, Panel):
    #     #     bl_label = "Stereoscopy"
    #     #     COMPAT_ENGINES = {'BLENDER_RENDER'}
    #     #
    #     #     @classmethod
    #     #     def poll(cls, context):
    #     #         render = context.scene.render
    #     #         return (super().poll(context) and render.use_multiview and
    #     #                 render.views_format == 'STEREO_3D')
    #     #
    #     #     def draw(self, context):
    #     #         layout = self.layout
    #     #         render = context.scene.render
    #     #         st = context.camera.stereo
    #     #         cam = context.camera
    #     #
    #     #         is_spherical_stereo = cam.type != 'ORTHO' and render.use_spherical_stereo
    #     #         use_spherical_stereo = is_spherical_stereo and st.use_spherical_stereo
    #     #
    #     #         col = layout.column()
    #     #         col.row().prop(st, "convergence_mode", expand=True)
    #     #
    #     #         sub = col.column()
    #     #         sub.active = st.convergence_mode != 'PARALLEL'
    #     #         sub.prop(st, "convergence_distance")
    #     #
    #     #         col.prop(st, "interocular_distance")
    #     #
    #     #         if is_spherical_stereo:
    #     #             col.separator()
    #     #             row = col.row()
    #     #             row.prop(st, "use_spherical_stereo")
    #     #             sub = row.row()
    #     #             sub.active = st.use_spherical_stereo
    #     #             sub.prop(st, "use_pole_merge")
    #     #             row = col.row(align=True)
    #     #             row.active = st.use_pole_merge
    #     #             row.prop(st, "pole_merge_angle_from")
    #     #             row.prop(st, "pole_merge_angle_to")
    #     #
    #     #         col.label(text="Pivot:")
    #     #         row = col.row()
    #     #         row.active = not use_spherical_stereo
    #     #         row.prop(st, "pivot", expand=True)
    #     #
    #     #
    #     # class DATA_PT_camera(CameraButtonsPanel, Panel):
    #     #     bl_label = "Camera"
    #     #     COMPAT_ENGINES = {'BLENDER_RENDER', 'BLENDER_GAME'}
    #     #
    #     #     def draw(self, context):
    #     #         layout = self.layout
    #     #
    #     #         cam = context.camera
    #     #
    #     #         row = layout.row(align=True)
    #     #
    #     #         row.menu("CAMERA_MT_presets", text=bpy.types.CAMERA_MT_presets.bl_label)
    #     #         row.operator("camera.preset_add", text="", icon='ZOOMIN')
    #     #         row.operator("camera.preset_add", text="", icon='ZOOMOUT').remove_active = True
    #     #
    #     #         layout.label(text="Sensor:")
    #     #
    #     #         split = layout.split()
    #     #
    #     #         col = split.column(align=True)
    #     #         if cam.sensor_fit == 'AUTO':
    #     #             col.prop(cam, "sensor_width", text="Size")
    #     #         else:
    #     #             sub = col.column(align=True)
    #     #             sub.active = cam.sensor_fit == 'HORIZONTAL'
    #     #             sub.prop(cam, "sensor_width", text="Width")
    #     #             sub = col.column(align=True)
    #     #             sub.active = cam.sensor_fit == 'VERTICAL'
    #     #             sub.prop(cam, "sensor_height", text="Height")
    #     #
    #     #         col = split.column(align=True)
    #     #         col.prop(cam, "sensor_fit", text="")
    #     #
    #     #
    #     # class DATA_PT_camera_dof(CameraButtonsPanel, Panel):
    #     #     bl_label = "Depth of Field"
    #     #     COMPAT_ENGINES = {'BLENDER_RENDER', 'BLENDER_GAME'}
    #     #
    #     #     def draw(self, context):
    #     #         layout = self.layout
    #     #
    #     #         cam = context.camera
    #     #         dof_options = cam.gpu_dof
    #     #
    #     #         split = layout.split()
    #     #
    #     #         col = split.column()
    #     #         col.label(text="Focus:")
    #     #         col.prop(cam, "dof_object", text="")
    #     #         sub = col.column()
    #     #         sub.active = (cam.dof_object is None)
    #     #         sub.prop(cam, "dof_distance", text="Distance")
    #     #
    #     #         hq_support = dof_options.is_hq_supported
    #     #         col = split.column(align=True)
    #     #         col.label("Viewport:")
    #     #         sub = col.column()
    #     #         sub.active = hq_support
    #     #         sub.prop(dof_options, "use_high_quality")
    #     #         col.prop(dof_options, "fstop")
    #     #         if dof_options.use_high_quality and hq_support:
    #     #             col.prop(dof_options, "blades")
    #     #
    #     #
    #     # class DATA_PT_camera_display(CameraButtonsPanel, Panel):
    #     #     bl_label = "Display"
    #     #     COMPAT_ENGINES = {'BLENDER_RENDER', 'BLENDER_GAME'}
    #     #
    #     #     def draw(self, context):
    #     #         layout = self.layout
    #     #
    #     #         cam = context.camera
    #     #
    #     #         split = layout.split()
    #     #
    #     #         col = split.column()
    #     #         col.prop(cam, "show_limits", text="Limits")
    #     #         col.prop(cam, "show_mist", text="Mist")
    #     #
    #     #         col.prop(cam, "show_sensor", text="Sensor")
    #     #         col.prop(cam, "show_name", text="Name")
    #     #
    #     #         col = split.column()
    #     #         col.prop_menu_enum(cam, "show_guide")
    #     #         col.separator()
    #     #         col.prop(cam, "draw_size", text="Size")
    #     #         col.separator()
    #     #         col.prop(cam, "show_passepartout", text="Passepartout")
    #     #         sub = col.column()
    #     #         sub.active = cam.show_passepartout
    #     #         sub.prop(cam, "passepartout_alpha", text="Alpha", slider=True)
    #     #
    #     #
    #     # class DATA_PT_camera_safe_areas(CameraButtonsPanel, Panel):
    #     #     bl_label = "Safe Areas"
    #     #     bl_options = {'DEFAULT_CLOSED'}
    #     #     COMPAT_ENGINES = {'BLENDER_RENDER', 'BLENDER_GAME'}
    #     #
    #     #     def draw_header(self, context):
    #     #         cam = context.camera
    #     #
    #     #         self.layout.prop(cam, "show_safe_areas", text="")
    #     #
    #     #     def draw(self, context):
    #     #         layout = self.layout
    #     #         safe_data = context.scene.safe_areas
    #     #         camera = context.camera
    #     #
    #     #         draw_display_safe_settings(layout, safe_data, camera)
    #     #
    #     #
    #     # class DATA_PT_custom_props_camera(CameraButtonsPanel, PropertyPanel, Panel):
    #     #     COMPAT_ENGINES = {'BLENDER_RENDER', 'BLENDER_GAME'}
    #     #     _context_path = "object.data"
    #     #     _property_type = bpy.types.Camera
    #     #
    #     #
    #     # def draw_display_safe_settings(layout, safe_data, settings):
    #     #     show_safe_areas = settings.show_safe_areas
    #     #     show_safe_center = settings.show_safe_center
    #     #
    #     #     split = layout.split()
    #     #
    #     #     col = split.column()
    #     #     row = col.row(align=True)
    #     #     row.menu("SAFE_AREAS_MT_presets", text=bpy.types.SAFE_AREAS_MT_presets.bl_label)
    #     #     row.operator("safe_areas.preset_add", text="", icon='ZOOMIN')
    #     #     row.operator("safe_areas.preset_add", text="", icon='ZOOMOUT').remove_active = True
    #     #
    #     #     col = split.column()
    #     #     col.prop(settings, "show_safe_center", text="Center-Cut Safe Areas")
    #     #
    #     #     split = layout.split()
    #     #     col = split.column()
    #     #     col.active = show_safe_areas
    #     #     col.prop(safe_data, "title", slider=True)
    #     #     col.prop(safe_data, "action", slider=True)
    #     #
    #     #     col = split.column()
    #     #     col.active = show_safe_areas and show_safe_center
    #     #     col.prop(safe_data, "title_center", slider=True)
    #     #     col.prop(safe_data, "action_center", slider=True)
    #     #
    #     #
    #     # classes = (
    #     #     CAMERA_MT_presets,
    #     #     SAFE_AREAS_MT_presets,
    #     #     DATA_PT_context_camera,
    #     #     DATA_PT_lens,
    #     #     DATA_PT_camera,
    #     #     DATA_PT_camera_stereoscopy,
    #     #     DATA_PT_camera_dof,
    #     #     DATA_PT_camera_display,
    #     #     DATA_PT_camera_safe_areas,
    #     #     DATA_PT_custom_props_camera,
    #     # )
    #     #
    #     # if __name__ == "__main__":  # only for live edit.
    #     #     from bpy.utils import register_class
    #     #     for cls in classes:
    #     #         register_class(cls)
    #
    #
    # class Lamp:
    #
    #
    #     def __init__(self, operator, context):
    #
    #         pass
    #
    #     # # <pep8 compliant>
    #     # import bpy
    #     # from bpy.types import Menu, Panel
    #     # from rna_prop_ui import PropertyPanel
    #     #
    #     #
    #     # class LAMP_MT_sunsky_presets(Menu):
    #     #     bl_label = "Sun & Sky Presets"
    #     #     preset_subdir = "sunsky"
    #     #     preset_operator = "script.execute_preset"
    #     #     COMPAT_ENGINES = {'BLENDER_RENDER', 'BLENDER_GAME'}
    #     #     draw = Menu.draw_preset
    #     #
    #     #
    #     # class DataButtonsPanel:
    #     #     bl_space_type = 'PROPERTIES'
    #     #     bl_region_type = 'WINDOW'
    #     #     bl_context = "data"
    #     #
    #     #     @classmethod
    #     #     def poll(cls, context):
    #     #         engine = context.scene.render.engine
    #     #         return context.lamp and (engine in cls.COMPAT_ENGINES)
    #     #
    #     #
    #     # class DATA_PT_context_lamp(DataButtonsPanel, Panel):
    #     #     bl_label = ""
    #     #     bl_options = {'HIDE_HEADER'}
    #     #     COMPAT_ENGINES = {'BLENDER_RENDER', 'BLENDER_GAME'}
    #     #
    #     #     def draw(self, context):
    #     #         layout = self.layout
    #     #
    #     #         ob = context.object
    #     #         lamp = context.lamp
    #     #         space = context.space_data
    #     #
    #     #         split = layout.split(percentage=0.65)
    #     #
    #     #         texture_count = len(lamp.texture_slots.keys())
    #     #
    #     #         if ob:
    #     #             split.template_ID(ob, "data")
    #     #         elif lamp:
    #     #             split.template_ID(space, "pin_id")
    #     #
    #     #         if texture_count != 0:
    #     #             split.label(text=str(texture_count), icon='TEXTURE')
    #     #
    #     #
    #     # class DATA_PT_preview(DataButtonsPanel, Panel):
    #     #     bl_label = "Preview"
    #     #     COMPAT_ENGINES = {'BLENDER_RENDER', 'BLENDER_GAME'}
    #     #
    #     #     def draw(self, context):
    #     #         self.layout.template_preview(context.lamp)
    #     #
    #     #
    #     # class DATA_PT_lamp(DataButtonsPanel, Panel):
    #     #     bl_label = "Lamp"
    #     #     COMPAT_ENGINES = {'BLENDER_RENDER', 'BLENDER_GAME'}
    #     #
    #     #     def draw(self, context):
    #     #         layout = self.layout
    #     #
    #     #         lamp = context.lamp
    #     #
    #     #         layout.row().prop(lamp, "type", expand=True)
    #     #
    #     #         split = layout.split()
    #     #
    #     #         col = split.column()
    #     #         sub = col.column()
    #     #         sub.prop(lamp, "color", text="")
    #     #         sub.prop(lamp, "energy")
    #     #
    #     #         if lamp.type in {'POINT', 'SPOT'}:
    #     #             sub.label(text="Falloff:")
    #     #             sub.prop(lamp, "falloff_type", text="")
    #     #             sub.prop(lamp, "distance")
    #     #
    #     #             if lamp.falloff_type == 'LINEAR_QUADRATIC_WEIGHTED':
    #     #                 col.label(text="Attenuation Factors:")
    #     #                 sub = col.column(align=True)
    #     #                 sub.prop(lamp, "linear_attenuation", slider=True, text="Linear")
    #     #                 sub.prop(lamp, "quadratic_attenuation", slider=True, text="Quadratic")
    #     #
    #     #             elif lamp.falloff_type == 'INVERSE_COEFFICIENTS':
    #     #                 col.label(text="Inverse Coefficients:")
    #     #                 sub = col.column(align=True)
    #     #                 sub.prop(lamp, "constant_coefficient", text="Constant")
    #     #                 sub.prop(lamp, "linear_coefficient", text="Linear")
    #     #                 sub.prop(lamp, "quadratic_coefficient", text="Quadratic")
    #     #
    #     #             col.prop(lamp, "use_sphere")
    #     #
    #     #         if lamp.type == 'AREA':
    #     #             col.prop(lamp, "distance")
    #     #             col.prop(lamp, "gamma")
    #     #
    #     #         col = split.column()
    #     #         col.prop(lamp, "use_negative")
    #     #         col.prop(lamp, "use_own_layer", text="This Layer Only")
    #     #         col.prop(lamp, "use_specular")
    #     #         col.prop(lamp, "use_diffuse")
    #     #
    #     #
    #     # class DATA_PT_sunsky(DataButtonsPanel, Panel):
    #     #     bl_label = "Sky & Atmosphere"
    #     #     COMPAT_ENGINES = {'BLENDER_RENDER'}
    #     #
    #     #     @classmethod
    #     #     def poll(cls, context):
    #     #         lamp = context.lamp
    #     #         engine = context.scene.render.engine
    #     #         return (lamp and lamp.type == 'SUN') and (engine in cls.COMPAT_ENGINES)
    #     #
    #     #     def draw(self, context):
    #     #         layout = self.layout
    #     #
    #     #         lamp = context.lamp.sky
    #     #
    #     #         row = layout.row(align=True)
    #     #         row.prop(lamp, "use_sky")
    #     #         row.menu("LAMP_MT_sunsky_presets", text=bpy.types.LAMP_MT_sunsky_presets.bl_label)
    #     #         row.operator("lamp.sunsky_preset_add", text="", icon='ZOOMIN')
    #     #         row.operator("lamp.sunsky_preset_add", text="", icon='ZOOMOUT').remove_active = True
    #     #
    #     #         row = layout.row()
    #     #         row.active = lamp.use_sky or lamp.use_atmosphere
    #     #         row.prop(lamp, "atmosphere_turbidity", text="Turbidity")
    #     #
    #     #         split = layout.split()
    #     #
    #     #         col = split.column()
    #     #         col.active = lamp.use_sky
    #     #         col.label(text="Blending:")
    #     #         sub = col.column()
    #     #         sub.prop(lamp, "sky_blend_type", text="")
    #     #         sub.prop(lamp, "sky_blend", text="Factor")
    #     #
    #     #         col.label(text="Color Space:")
    #     #         sub = col.column()
    #     #         sub.row().prop(lamp, "sky_color_space", expand=True)
    #     #         sub.prop(lamp, "sky_exposure", text="Exposure")
    #     #
    #     #         col = split.column()
    #     #         col.active = lamp.use_sky
    #     #         col.label(text="Horizon:")
    #     #         sub = col.column()
    #     #         sub.prop(lamp, "horizon_brightness", text="Brightness")
    #     #         sub.prop(lamp, "spread", text="Spread")
    #     #
    #     #         col.label(text="Sun:")
    #     #         sub = col.column()
    #     #         sub.prop(lamp, "sun_brightness", text="Brightness")
    #     #         sub.prop(lamp, "sun_size", text="Size")
    #     #         sub.prop(lamp, "backscattered_light", slider=True, text="Back Light")
    #     #
    #     #         layout.separator()
    #     #
    #     #         layout.prop(lamp, "use_atmosphere")
    #     #
    #     #         split = layout.split()
    #     #
    #     #         col = split.column()
    #     #         col.active = lamp.use_atmosphere
    #     #         col.label(text="Intensity:")
    #     #         col.prop(lamp, "sun_intensity", text="Sun")
    #     #         col.prop(lamp, "atmosphere_distance_factor", text="Distance")
    #     #
    #     #         col = split.column()
    #     #         col.active = lamp.use_atmosphere
    #     #         col.label(text="Scattering:")
    #     #         sub = col.column(align=True)
    #     #         sub.prop(lamp, "atmosphere_inscattering", slider=True, text="Inscattering")
    #     #         sub.prop(lamp, "atmosphere_extinction", slider=True, text="Extinction")
    #     #
    #     #
    #     # class DATA_PT_shadow(DataButtonsPanel, Panel):
    #     #     bl_label = "Shadow"
    #     #     COMPAT_ENGINES = {'BLENDER_RENDER'}
    #     #
    #     #     @classmethod
    #     #     def poll(cls, context):
    #     #         lamp = context.lamp
    #     #         engine = context.scene.render.engine
    #     #         return (lamp and lamp.type in {'POINT', 'SUN', 'SPOT', 'AREA'}) and (engine in cls.COMPAT_ENGINES)
    #     #
    #     #     def draw(self, context):
    #     #         layout = self.layout
    #     #
    #     #         lamp = context.lamp
    #     #
    #     #         layout.row().prop(lamp, "shadow_method", expand=True)
    #     #
    #     #         if lamp.shadow_method == 'NOSHADOW' and lamp.type == 'AREA':
    #     #             split = layout.split()
    #     #
    #     #             col = split.column()
    #     #             col.label(text="Form factor sampling:")
    #     #
    #     #             sub = col.row(align=True)
    #     #
    #     #             if lamp.shape == 'SQUARE':
    #     #                 sub.prop(lamp, "shadow_ray_samples_x", text="Samples")
    #     #             elif lamp.shape == 'RECTANGLE':
    #     #                 sub.prop(lamp, "shadow_ray_samples_x", text="Samples X")
    #     #                 sub.prop(lamp, "shadow_ray_samples_y", text="Samples Y")
    #     #
    #     #         if lamp.shadow_method != 'NOSHADOW':
    #     #             split = layout.split()
    #     #
    #     #             col = split.column()
    #     #             col.prop(lamp, "shadow_color", text="")
    #     #
    #     #             col = split.column()
    #     #             col.prop(lamp, "use_shadow_layer", text="This Layer Only")
    #     #             col.prop(lamp, "use_only_shadow")
    #     #
    #     #         if lamp.shadow_method == 'RAY_SHADOW':
    #     #             split = layout.split()
    #     #
    #     #             col = split.column()
    #     #             col.label(text="Sampling:")
    #     #
    #     #             if lamp.type in {'POINT', 'SUN', 'SPOT'}:
    #     #                 sub = col.row()
    #     #
    #     #                 sub.prop(lamp, "shadow_ray_samples", text="Samples")
    #     #                 sub.prop(lamp, "shadow_soft_size", text="Soft Size")
    #     #
    #     #             elif lamp.type == 'AREA':
    #     #                 sub = col.row(align=True)
    #     #
    #     #                 if lamp.shape == 'SQUARE':
    #     #                     sub.prop(lamp, "shadow_ray_samples_x", text="Samples")
    #     #                 elif lamp.shape == 'RECTANGLE':
    #     #                     sub.prop(lamp, "shadow_ray_samples_x", text="Samples X")
    #     #                     sub.prop(lamp, "shadow_ray_samples_y", text="Samples Y")
    #     #
    #     #             col.row().prop(lamp, "shadow_ray_sample_method", expand=True)
    #     #
    #     #             if lamp.shadow_ray_sample_method == 'ADAPTIVE_QMC':
    #     #                 layout.prop(lamp, "shadow_adaptive_threshold", text="Threshold")
    #     #
    #     #             if lamp.type == 'AREA' and lamp.shadow_ray_sample_method == 'CONSTANT_JITTERED':
    #     #                 row = layout.row()
    #     #                 row.prop(lamp, "use_umbra")
    #     #                 row.prop(lamp, "use_dither")
    #     #                 row.prop(lamp, "use_jitter")
    #     #
    #     #         elif lamp.shadow_method == 'BUFFER_SHADOW':
    #     #             col = layout.column()
    #     #             col.label(text="Buffer Type:")
    #     #             col.row().prop(lamp, "shadow_buffer_type", expand=True)
    #     #
    #     #             if lamp.shadow_buffer_type in {'REGULAR', 'HALFWAY', 'DEEP'}:
    #     #                 split = layout.split()
    #     #
    #     #                 col = split.column()
    #     #                 col.label(text="Filter Type:")
    #     #                 col.prop(lamp, "shadow_filter_type", text="")
    #     #                 sub = col.column(align=True)
    #     #                 sub.prop(lamp, "shadow_buffer_soft", text="Soft")
    #     #                 sub.prop(lamp, "shadow_buffer_bias", text="Bias")
    #     #
    #     #                 col = split.column()
    #     #                 col.label(text="Sample Buffers:")
    #     #                 col.prop(lamp, "shadow_sample_buffers", text="")
    #     #                 sub = col.column(align=True)
    #     #                 sub.prop(lamp, "shadow_buffer_size", text="Size")
    #     #                 sub.prop(lamp, "shadow_buffer_samples", text="Samples")
    #     #                 if lamp.shadow_buffer_type == 'DEEP':
    #     #                     col.prop(lamp, "compression_threshold")
    #     #
    #     #             elif lamp.shadow_buffer_type == 'IRREGULAR':
    #     #                 layout.prop(lamp, "shadow_buffer_bias", text="Bias")
    #     #
    #     #             split = layout.split()
    #     #
    #     #             col = split.column()
    #     #             col.prop(lamp, "use_auto_clip_start", text="Autoclip Start")
    #     #             sub = col.column()
    #     #             sub.active = not lamp.use_auto_clip_start
    #     #             sub.prop(lamp, "shadow_buffer_clip_start", text="Clip Start")
    #     #
    #     #             col = split.column()
    #     #             col.prop(lamp, "use_auto_clip_end", text="Autoclip End")
    #     #             sub = col.column()
    #     #             sub.active = not lamp.use_auto_clip_end
    #     #             sub.prop(lamp, "shadow_buffer_clip_end", text=" Clip End")
    #     #
    #     #
    #     # class DATA_PT_area(DataButtonsPanel, Panel):
    #     #     bl_label = "Area Shape"
    #     #     COMPAT_ENGINES = {'BLENDER_RENDER', 'BLENDER_GAME'}
    #     #
    #     #     @classmethod
    #     #     def poll(cls, context):
    #     #         lamp = context.lamp
    #     #         engine = context.scene.render.engine
    #     #         return (lamp and lamp.type == 'AREA') and (engine in cls.COMPAT_ENGINES)
    #     #
    #     #     def draw(self, context):
    #     #         layout = self.layout
    #     #
    #     #         lamp = context.lamp
    #     #
    #     #         col = layout.column()
    #     #         col.row().prop(lamp, "shape", expand=True)
    #     #         sub = col.row(align=True)
    #     #
    #     #         if lamp.shape == 'SQUARE':
    #     #             sub.prop(lamp, "size")
    #     #         elif lamp.shape == 'RECTANGLE':
    #     #             sub.prop(lamp, "size", text="Size X")
    #     #             sub.prop(lamp, "size_y", text="Size Y")
    #     #
    #     #
    #     # class DATA_PT_spot(DataButtonsPanel, Panel):
    #     #     bl_label = "Spot Shape"
    #     #     COMPAT_ENGINES = {'BLENDER_RENDER', 'BLENDER_GAME'}
    #     #
    #     #     @classmethod
    #     #     def poll(cls, context):
    #     #         lamp = context.lamp
    #     #         engine = context.scene.render.engine
    #     #         return (lamp and lamp.type == 'SPOT') and (engine in cls.COMPAT_ENGINES)
    #     #
    #     #     def draw(self, context):
    #     #         layout = self.layout
    #     #
    #     #         lamp = context.lamp
    #     #
    #     #         split = layout.split()
    #     #
    #     #         col = split.column()
    #     #         sub = col.column()
    #     #         sub.prop(lamp, "spot_size", text="Size")
    #     #         sub.prop(lamp, "spot_blend", text="Blend", slider=True)
    #     #         col.prop(lamp, "use_square")
    #     #         col.prop(lamp, "show_cone")
    #     #
    #     #         col = split.column()
    #     #
    #     #         col.active = (lamp.shadow_method != 'BUFFER_SHADOW' or lamp.shadow_buffer_type != 'DEEP')
    #     #         col.prop(lamp, "use_halo")
    #     #         sub = col.column(align=True)
    #     #         sub.active = lamp.use_halo
    #     #         sub.prop(lamp, "halo_intensity", text="Intensity")
    #     #         if lamp.shadow_method == 'BUFFER_SHADOW':
    #     #             sub.prop(lamp, "halo_step", text="Step")
    #     #
    #     #
    #     # class DATA_PT_falloff_curve(DataButtonsPanel, Panel):
    #     #     bl_label = "Falloff Curve"
    #     #     bl_options = {'DEFAULT_CLOSED'}
    #     #     COMPAT_ENGINES = {'BLENDER_RENDER', 'BLENDER_GAME'}
    #     #
    #     #     @classmethod
    #     #     def poll(cls, context):
    #     #         lamp = context.lamp
    #     #         engine = context.scene.render.engine
    #     #
    #     #         return (lamp and lamp.type in {'POINT', 'SPOT'} and lamp.falloff_type == 'CUSTOM_CURVE') and (engine in cls.COMPAT_ENGINES)
    #     #
    #     #     def draw(self, context):
    #     #         lamp = context.lamp
    #     #
    #     #         self.layout.template_curve_mapping(lamp, "falloff_curve", use_negative_slope=True)
    #     #
    #     #
    #     # class DATA_PT_custom_props_lamp(DataButtonsPanel, PropertyPanel, Panel):
    #     #     COMPAT_ENGINES = {'BLENDER_RENDER', 'BLENDER_GAME'}
    #     #     _context_path = "object.data"
    #     #     _property_type = bpy.types.Lamp
    #     #
    #     #
    #     # classes = (
    #     #     LAMP_MT_sunsky_presets,
    #     #     DATA_PT_context_lamp,
    #     #     DATA_PT_preview,
    #     #     DATA_PT_lamp,
    #     #     DATA_PT_sunsky,
    #     #     DATA_PT_shadow,
    #     #     DATA_PT_area,
    #     #     DATA_PT_spot,
    #     #     DATA_PT_falloff_curve,
    #     #     DATA_PT_custom_props_lamp,
    #     # )
    #     #
    #     # if __name__ == "__main__":  # only for live edit.
    #     #     from bpy.utils import register_class
    #     #     for cls in classes:
    #     #         register_class(cls)
    #
    #
    # class Group:
    #
    #
    #     def __init__(self, operator, context):
    #
    #         pass
    #
    #
    # class GreasePencil:
    #
    #
    #     def __init__(self, operator, context):
    #
    #         pass
    #
    #
    # class GPencilLayer:
    #
    #
    #     def __init__(self, operator, context):
    #
    #         pass
    #
    #
    # class Action:
    #
    #
    #     def __init__(self, operator, context):
    #
    #         pass
    #
    #
    # class Constraint:
    #
    #
    #     def __init__(self, operator, context):
    #
    #         pass
    #
    #
    # class Modifier:
    #
    #
    #     def __init__(self, operator, context):
    #
    #         pass
    #
    #
    # class Image:
    #
    #
    #     def __init__(self, operator, context):
    #
    #         pass
    #
    #
    # class BoneGroup:
    #
    #
    #     def __init__(self, operator, context):
    #
    #         pass
    #
    #
    # class PoseBone:
    #
    #
    #     def __init__(self, operator, context):
    #
    #         pass
    #
    #
    # class EditBone:
    #
    #
    #     def __init__(self, operator, context):
    #
    #         pass
    #
    #
    # class VertexGroup:
    #
    #
    #     def __init__(self, operator, context):
    #
    #         pass
    #
    #
    # class ShapeKey:
    #
    #
    #     def __init__(self, operator, context):
    #
    #         pass
    #
    #
    # class MeshTexturePolyLayer:
    #
    #
    #     def __init__(self, operator, context):
    #
    #         pass
    #
    #
    # class MeshLoopColorLayer:
    #
    #
    #     def __init__(self, operator, context):
    #
    #         pass
    #
    #
    # class Material:
    #
    #
    #     def __init__(self, operator, context):
    #
    #         pass
    #
    #
    # class Texture:
    #
    #
    #     def __init__(self, operator, context):
    #
    #         pass
    #
    #
    # class ParticleSystem:
    #
    #
    #     def __init__(self, operator, context):
    #
    #         pass
    #
    #
    # class ParticleSettings:
    #
    #
    #     def __init__(self, operator, context):
    #
    #         pass


class namer:


    def __init__(self, operator, context, specials=False):

        option = get.namer.options(context)

        layout = operator.layout
        column = layout.column()
        split = column.split(percentage=0.15)
        column = split.column()
        column.prop(option, 'mode', expand=True)

        self.set_height(column, 11)

        column = split.column()

        getattr(self, option.mode.lower())(operator, context, option, column)


    @staticmethod
    def set_height(column, separators):

        for _ in range(0, separators): column.separator()


    @staticmethod
    def split_row(column, offset=0.0):

        row = column.row(align=True)
        split = row.split(align=True, percentage=0.275+offset)

        return split


    @staticmethod
    def datablock_buttons(category, option, layout, use_label=True):

        # if category not in {'Objects', 'Objects Data', 'Custom Properties'}:
        if use_label:
            layout.label(text=category + ':')

        row = layout.row(align=True)
        row.scale_x = 5

        if category == 'Objects':

            row.prop(option, 'toggle_objects', text='', icon='RADIOBUT_OFF' if not option.toggle_objects else 'RADIOBUT_ON')

        elif category == 'Objects Data':

            row.prop(option, 'toggle_objects_data', text='', icon='RADIOBUT_OFF' if not option.toggle_objects_data else 'RADIOBUT_ON')

        for target in get.namer.catagories[category]:

            if target not in {'line_sets', 'sensors', 'controllers', 'actuators'}:
                row.prop(option, target, text='', icon=get.icon(target))

            elif target == 'line_sets':
                row.prop(option, target, text='Line Sets', toggle=True)

            else:
                row.prop(option, target, text=target.title(), toggle=True)


    @staticmethod
    def search_specials(operator, context):

        layout = operator.layout

        if get.namer.options(context).mode == 'NAME':

            naming = get.namer.options(context).naming['options']
            option = naming.operations[naming.active_index]

        else:

            option = get.namer.options(context).sorting['options']

        layout.prop(option, 'case_sensitive')
        layout.prop(option, 're')


    @staticmethod
    def move_search_specials(operator, context):

        layout = operator.layout

        naming = get.namer.options(context).naming['options']
        option = naming.operations[naming.active_index]

        layout.prop(option, 'move_case_sensitive')
        layout.prop(option, 'move_re')


    @staticmethod
    def swap_search_specials(operator, context):

        layout = operator.layout

        naming = get.namer.options(context).naming['options']
        option = naming.operations[naming.active_index]

        layout.prop(option, 'swap_case_sensitive')
        layout.prop(option, 'swap_re')



    @staticmethod
    def operation_specials(operator, context):

        layout = operator.layout

        layout.prop(get.preferences(context), 'use_last')
        layout.prop(get.preferences(context), 'auto_name_operations')

        layout.operator('wm.namer_operation_rename_active')
        layout.operator('wm.namer_operation_rename_all')


    class mode_row:
        dual_position = True
        sorting = False
        swap = False
        move = False


        def __init__(self, option, column, active=True, dual_position=True, custom_mode='', sorting=False, swap=False, move=False):

            self.dual_position = True if dual_position else False
            self.sorting = True if sorting else False
            self.swap = True if swap else False
            self.move = True if move else False

            if self.sorting and not custom_mode:
                operation_mode = 'placement'

            else:
                operation_mode = '{}_mode'.format(option.operation_options_mode.lower()) if not custom_mode else custom_mode

            split = namer.split_row(column)
            split.prop(option, operation_mode, text='')

            row = split.row(align=True)
            row.active = active

            mode = getattr(option, operation_mode).lower()
            getattr(self, mode)(option, row)


        @staticmethod
        def search_prop(option, row, prop):

            row.prop(option, prop, text='', icon='VIEWZOOM')


        def search_specials(self, row):

            menu = 'WM_MT_namer_search_specials'
            menu = 'WM_MT_namer_move_search_specials' if self.move else menu
            menu = 'WM_MT_namer_swap_search_specials' if self.swap else menu

            sub = row.row(align=True)
            sub.menu(menu, text='', icon='COLLAPSEMENU')


        def position_prop(self, option, row):

            if self.dual_position:
                begin = 'begin' if not self.swap else 'swap_begin'
                end = 'end' if not self.swap else 'swap_end'

                row.prop(option, begin)
                row.prop(option, end)

                prop = 'outside' if not self.swap else 'swap_outside'
                row = row.row(align=True)
                icon = 'FULLSCREEN_EXIT' if not option.outside else 'FULLSCREEN_ENTER'
                row.prop(option, prop, text='', icon=icon)

            else:
                prop = 'position' if not self.move else 'move_position'
                row.prop(option, prop)


        def all(self, option, row):

            if not self.sorting:
                self.search_prop(option, row, 'find')
                self.search_specials(row)

            else:
                self.position_prop(option, row)


        def find(self, option, row):

            prop = 'find' if not self.swap else 'swap_find'
            self.search_prop(option, row, prop)
            self.search_specials(row)


        def position(self, option, row):

            self.position_prop(option, row)


        def before(self, option, row):

            prop = 'before'
            prop = 'move_before' if self.move else prop
            prop = 'swap_before' if self.swap else prop
            self.search_prop(option, row, prop)
            self.search_specials(row)


        def after(self, option, row):

            prop = 'after'
            prop = 'move_after' if self.move else prop
            prop = 'swap_after' if self.swap else prop
            self.search_prop(option, row, prop)
            self.search_specials(row)


        def between(self, option, row):

            after = 'after'
            after = 'move_after' if self.move else after
            after = 'swap_after' if self.swap else after
            self.search_prop(option, row, after)

            before = 'before'
            before = 'move_before' if self.move else before
            before = 'swap_before' if self.swap else before
            self.search_prop(option, row, 'before')
            self.search_specials(row)


        @staticmethod
        def insert_prop(option, row):

            row.prop(option, 'insert', text='', icon='ZOOMIN')


        @staticmethod
        def separator_prop(option, row):

            row.prop(option, 'separator', text='', icon='ARROW_LEFTRIGHT')


        def prefix(self, option, row):

            if self.sorting:
                self.separator_prop(option, row)

            else:
                self.insert_prop(option, row)


        def suffix(self, option, row):

            if self.sorting:
                self.separator_prop(option, row)

            else:
                self.insert_prop(option, row)


    class target:


        def __init__(self, operator, context, option, layout):

            option = option.targeting['options']

            row = layout.row()
            row.prop(option, 'target_options_mode', expand=True)

            layout.separator()

            layout = layout.column(align=True)

            if option.target_options_mode == 'CONTEXT':

                self.context_area(operator, context, option, layout)

            else:

                namer.datablock_buttons('Objects', option, layout, use_label=False)
                namer.datablock_buttons('Objects Data', option, layout, use_label=False)
                namer.datablock_buttons('Object Related', option, layout)

                layout.separator()

                row = layout.row(align=True)
                row.prop(option, 'display_more')

                if option.display_more:

                    namer.datablock_buttons('Grease Pencil', option, layout)
                    namer.datablock_buttons('Animation', option, layout)
                    namer.datablock_buttons('Node', option, layout)
                    namer.datablock_buttons('Particle', option, layout)
                    namer.datablock_buttons('Freestyle', option, layout)
                    namer.datablock_buttons('Scene', option, layout)
                    namer.datablock_buttons('Image & Brush', option, layout)
                    namer.datablock_buttons('Sequence', option, layout)
                    namer.datablock_buttons('Game Engine', option, layout)
                    namer.datablock_buttons('Misc', option, layout)
                    # namer.datablock_buttons('Custom Properties', option, layout, use_label=False)


        class context_area:

            def __init__(self, operator, context, option, layout):

                getattr(self, operator.area_type.lower())(operator, context, option, layout)


            class properties:


                def __init__(self, operator, context, option, layout):

                    getattr(self, context.space_data.context.lower())(operator, context, option, layout)


                @staticmethod
                def render(operator, context, option, layout):

                    layout.label(text='Nothing specific in the properties render context to target')


                @staticmethod
                def render_layer(operator, context, option, layout):

                    layout.label(text='Properties render layer context is not yet implemented')
                    # render layers
                    # views
                    # freestyle


                @staticmethod
                def scene(operator, context, option, layout):

                    layout.label(text='Properties scene context is not yet implemented')
                    # keying sets
                    # custom properties


                @staticmethod
                def world(operator, context, option, layout):

                    layout.label(text='Properties world context is not yet implemented')
                    # worlds
                    # custom properties


                @staticmethod
                def object(operator, context, option, layout):

                    layout.label(text='Properties object context is not yet implemented')
                    # groups
                    # custom properties


                @staticmethod
                def constraint(operator, context, option, layout):

                    layout.label(text='Properties constraint context is not yet implemented')
                    # constraints


                @staticmethod
                def modifier(operator, context, option, layout):

                    layout.label(text='Properties modifier context is not yet implemented')
                    # modifiers


                @staticmethod
                def data(operator, context, option, layout):

                    layout.label(text='Properties object data context is not yet implemented')
                    # vertex groups
                    # shape keys
                    # uv maps
                    # vertex colors
                    # bone groups
                    # pose library
                    # sound * for speaker
                    # font * for text
                    # custom properties


                @staticmethod
                def bone(operator, context, option, layout):

                    layout.label(text='Properties bone context is not yet implemented')
                    # custom properties


                @staticmethod
                def bone_constraint(operator, context, option, layout):

                    layout.label(text='Properties bone constraint context is not yet implemented')
                    # constraints


                @staticmethod
                def material(operator, context, option, layout):

                    layout.label(text='Properties material context is not yet implemented')
                    # materials
                    # custom properties


                @staticmethod
                def texture(operator, context, option, layout):

                    layout.label(text='Properties texture context is not yet implemented')
                    # image
                    # custom properties


                @staticmethod
                def particle(operator, context, option, layout):

                    layout.label(text='Properties particle context is not yet implemented')
                    # particles
                    # cache
                    # textures
                    # custom properties


                @staticmethod
                def physics(operator, context, option, layout):

                    layout.label(text='Properties physics context is not yet implemented')
                    # cloth cache
                    # dynamic paint cache
                    # dynamic paint canvas
                    # soft body cache


            @staticmethod
            def console(operator, context, option, layout):

                layout.label(text='Nothing specific in the console to target')


            @staticmethod
            def text_editor(operator, context, option, layout):

                # texts
                layout.label(text='Text editor is not yet implemented')


            class dopesheet_editor:


                def __init__(self, operator, context, option, layout):

                    getattr(self, context.space_data.mode.lower())(operator, context, option, layout)


                @staticmethod
                def dopesheet(operator, context, option, layout):

                    # object
                    # action
                    # group
                    layout.label('Dopesheet\'s dopesheet mode is not yet supported')


                @staticmethod
                def action(operator, context, option, layout):

                    # group
                    layout.label('Dopesheet\'s action mode is not yet supported')


                @staticmethod
                def shapekey(operator, context, option, layout):

                    # group
                    layout.label('Dopesheet\'s shapekey mode is not yet supported')


                @staticmethod
                def gpencil(operator, context, option, layout):

                    # g pencil
                    # layers
                    layout.label('Dopesheet\'s grease pencil mode is not yet supported')


                @staticmethod
                def mask(operator, context, option, layout):

                    # mask
                    # layer
                    layout.label('Dopesheet\'s mask file mode is not yet supported')


                @staticmethod
                def cachefile(operator, context, option, layout):

                    layout.label('Dopesheet\'s cache file mode is not yet supported')


            class graph_editor:


                def __init__(self, operator, context, option, layout):

                    getattr(self, context.space_data.mode.lower())(operator, context, option, layout)


                @staticmethod
                def fcurves(operator, context, option, layout):

                    # object
                    # action
                    # action groups
                    layout.label(text='Graph editor\'s fcurve mode is not yet implemented')


                @staticmethod
                def drivers(operator, context, option, layout):

                    # object
                    # driver variables
                    layout.label(text='Graph editor\'s driver mode is not yet implemented')


            @staticmethod
            def view_3d(operator, context, option, layout):

                namer.datablock_buttons('Objects', option, layout, use_label=False)
                namer.datablock_buttons('Objects Data', option, layout, use_label=False)
                row = layout.row(align=True)
                row.prop(option, 'target_mode', expand=True)
                namer.datablock_buttons('Object Related', option, layout)
                # namer.datablock_buttons('Custom Properties', option, layout)


            class image_editor:


                def __init__(self, operator, context, option, layout):

                    getattr(self, context.space_data.mode.lower())(operator, context, option, layout)


                @staticmethod
                def view(operator, context, option, layout):

                    # images
                    # uv's
                    # grease pencil
                    # gp layer
                    # gp pallete
                    # gp brushes
                    layout.label(text='Image editor\'s view mode is not yet implemented')


                @staticmethod
                def paint(operator, context, option, layout):

                    # images
                    # paint curves
                    # pallettes
                    # textures
                    # grease pencil
                    # gp layer
                    # gp pallete
                    # gp brushes
                    layout.label(text='Image editor\'s paint mode is not yet implemented')


                @staticmethod
                def mask(operator, context, option, layout):

                    # images
                    # masks
                    # masks layers
                    # grease pencil
                    # gp layer
                    # gp pallete
                    # gp brushes
                    layout.label(text='Image editor\'s mask mode is not yet implemented')


            @staticmethod
            def node_editor(operator, context, option, layout):

                layout.label(text='Node editor is not yet implemented')
                # nodes & labels
                # objects
                # object related *textures, uv maps, vertex colors
                # images
                # masks
                # worlds
                # scene
                # node input output?


            @staticmethod
            def timeline(operator, context, option, layout):

                layout.label(text='Timeline is not yet implemented')
                # markers


            @staticmethod
            def nla_editor(operator, context, option, layout):

                layout.label(text='NLA editor is not yet implemented')
                # object
                # action
                # tracks
                # strips


            @staticmethod
            def sequence_editor(operator, context, option, layout):

                layout.label(text='Sequence editor is not yet implemented')
                # sequences
                # modifiers
                # grease pencil
                # custom properties


            @staticmethod
            def clip_editor(operator, context, option, layout):

                layout.label(text='Clip editor is not yet implemented')
                # tracks
                # mask layers
                # grease pencil


            @staticmethod
            def logic_editor(operator, context, option, layout):

                layout.label(text='Logic editor is not yet implemented')
                # logic bricks
                # game properties


            @staticmethod
            def outliner(operator, context, option, layout):

                layout.label(text='Outliner is not yet implemented')


            @staticmethod
            def user_preferences(operator, context, option, layout):

                layout.label(text='Nothing specific in user preferences to target')


            @staticmethod
            def info(operator, context, option, layout):

                layout.label(text='Nothing specific in info to target')


            @staticmethod
            def file_browser(operator, context, option, layout):

                layout.label(text='File browser is not yet implemented')


    class name:


        def __init__(self, operator, context, option, layout):

            option = option.naming['options']

            split = layout.split(percentage=0.7)
            column = split.column()

            if not option.operations:
                column.label(text='Add a naming operation {} \N{Rightwards Arrow}'.format(' '*40))

            else:
                self.name_operation(option, column)

            column = split.column(align=True)
            row = column.row(align=True)
            row.template_list('UI_UL_list', 'namer', option, 'operations', option, 'active_index', rows=8)

            column = row.column(align=True)
            column.operator('wm.namer_operation_add', text='', icon='ZOOMIN')
            column.operator('wm.namer_operation_remove', text='', icon='ZOOMOUT')
            column.menu('WM_MT_namer_operation_specials', text='', icon='COLLAPSEMENU')

            column.separator()

            operator = column.operator('wm.namer_operation_move', text='', icon='TRIA_UP')
            operator.up = True

            operator = column.operator('wm.namer_operation_move', text='', icon='TRIA_DOWN')
            operator.up = False


        class name_operation:


            def __init__(self, option, column):

                option = option.operations[option.active_index]

                row = column.row()
                row.prop(option, 'operation_options_mode', expand=True)
                column.separator()

                getattr(self, option.operation_options_mode.lower())(option, column)


            def replace(self, option, column):

                namer.mode_row(option, column, active=option.replace_mode != 'ALL')

                column.label(text='With:')
                column.prop(option, 'replace', text='', icon='FILE_REFRESH')


            def insert(self, option, column):

                namer.mode_row(option, column, dual_position=False)

                if option.insert_mode not in {'PREFIX', 'SUFFIX'}:
                    column.label(text='Insert:')
                    namer.mode_row.insert_prop(option, column.row())


            def convert(self, option, column):

                namer.mode_row(option, column, active=option.convert_mode != 'ALL')

                column.label(text='Case:')

                row = column.row()
                row.prop(option, 'case_mode', text='')

                column.label(text='Separators:')

                if option.separate_mode == 'CUSTOM':
                    row = column.row(align=True)
                    split = row.split(align=True, percentage=0.275)
                    split.prop(option, 'separate_mode', text='')

                    row = split.row(align=True)
                    row.prop(option, 'custom', text='')


                else:
                    row = column.row()
                    row.prop(option, 'separate_mode', text='')


            def move(self, option, column):

                namer.mode_row(option, column)

                column.label(text='To:')

                namer.mode_row(option, column, dual_position=False, custom_mode='move_to', move=True)


            def swap(self, option, column):

                namer.mode_row(option, column)

                column.label(text='With:')

                namer.mode_row(option, column, custom_mode='swap_to', swap=True)


            @staticmethod
            def transfer(option, column):

                column.label(text='Transfering is not yet implemented')


    class sort:


        def __init__(self, operator, context, option, column):

            option = option.sorting['options']

            row = column.row()
            row.prop(option, 'sort_options_mode', expand=True)

            column.separator()

            getattr(self, option.sort_options_mode.lower())(option, column)


        @staticmethod
        def name_slice(option, column):

            pass


        @staticmethod
        def fallback_mode_prop(option, column):

            column.label(text='Fallback:')

            row = column.row(align=True)
            row.prop(option, 'display_options', text='', icon='SETTINGS')
            row.prop(option, 'fallback_mode', expand=True)


        @staticmethod
        def none(option, column):

            column.label(text='No sorting will be performed')


        def ascend(self, option, column):

            if option.sort_mode == 'ALL':
                namer.mode_row(option, column, active=False, custom_mode='sort_mode', sorting=True)

            else:
                namer.mode_row(option, column, custom_mode='sort_mode', sorting=True)


        def descend(self, option, column):

            if option.sort_mode == 'ALL':
                namer.mode_row(option, column, active=False, custom_mode='sort_mode', sorting=True)

            else:
                namer.mode_row(option, column, custom_mode='sort_mode')


        def position(self, option, column): # TODO: orientation? contains, rotation, scale, location modes, from viewport perspective?

            if option.display_options:
                getattr(self, option.fallback_mode.lower())(option, column)

            else:
                split = namer.split_row(column)
                split.prop(option, 'starting_point', text='')

                row = split.row(align=True)
                row.prop(option, 'axis_3d', expand=True)

                if option.starting_point in {'CURSOR', 'CENTER', 'ACTIVE'}:
                    column.separator()

                    if option.axis_3d == 'Z':
                        props = ['top', 'bottom']

                    elif option.axis_3d == 'Y':
                        props = ['front', 'back']

                    else:
                        props = ['left', 'right']

                    split = namer.split_row(column, offset=-0.01)
                    split.label(text=props[0].title() + ':')

                    row = split.row()
                    row.prop(option, props[0], text='')

                    split = namer.split_row(column, offset=-0.01)
                    split.label(text=props[1].title() + ':')

                    row = split.row()
                    row.prop(option, props[1], text='')

                    if option.placement not in {'PREFIX', 'SUFFIX'}:
                        split = namer.split_row(column, offset=-0.01)
                        split.label(text='Separator:')

                        row = split.row()
                        row.prop(option, 'separator', text='', icon='ARROW_LEFTRIGHT')

                    namer.mode_row(option, column, dual_position=False, sorting=True)

            self.fallback_mode_prop(option, column)


        def hierarchy(self, option, column):

            if option.display_options:
                getattr(self, option.fallback_mode.lower())(option, column)

            else:
                row = column.row()
                row.prop(option, 'hierarchy_mode', expand=True)

            self.fallback_mode_prop(option, column)


        def manual(self, option, column):

            column.label(text='Manual sort options have not yet been implemented')


    class count:


        def __init__(self, operator, context, option, column):

            option = option.counting['options']

            row = column.row()
            row.prop(option, 'count_options_mode', expand=True)

            column.separator()

            getattr(self, option.count_options_mode.lower())(operator, context, option, column)


        @staticmethod
        def position_row(operator, context, option, column):

            column.separator()

            row = column.row(align=True)
            row.prop(option, 'placement', expand=True)

            row = row.row(align=True)
            row.enabled = option.placement == 'POSITION'
            row.prop(option, 'position', text='At')


        def common(self, operator, context, option, column):

            column.prop(option, 'separator')

            column.separator()

            row = column.row(align=True)
            row.prop(option, 'start')
            row.prop(option, 'step')

            self.position_row(operator, context, option, column)


        @staticmethod
        def none(operator, context, option, column):

            column.label(text='No counting will be performed')


        def numeric(self, operator, context, option, column):

            row = column.row(align=True)
            split = row.split(percentage=0.25, align=True)
            split.prop(option, 'auto', toggle=True)
            split.prop(option, 'pad')

            column.separator()

            column.prop(option, 'character')

            self.common(operator, context, option, column)


        def alphabetic(self, operator, context, option, column):

            self.common(operator, context, option, column)


        def roman_numeral(self, operator, context, option, column):

            self.common(operator, context, option, column)


    @staticmethod
    def preview(operator, context, options, column):

        column.label('Preview is not yet implemented')


    class options:


        def __init__(self, operator, context, option, column):

            row = column.row()
            row.prop(option, 'options_mode', expand=True)

            column.separator()

            getattr(self, option.options_mode.lower())(operator, context, option, column)


        @staticmethod
        def presets(operator, context, option, column):

            column.label(text='Presets are not yet implemented')


        @staticmethod
        def restore(operator, context, option, column):

            column.label(text='Restore points are not yet implemented')


        @staticmethod
        def importing(operator, context, option, column):

            column.label(text='Importing is not yet implemented')


        @staticmethod
        def exporting(operator, context, option, column):

            column.label(text='Exporting is not yet implemented')


        @staticmethod
        def preferences(operator, context, option, column):

            row = column.row()
            row.prop(get.preferences(context), 'use_last')
            row.prop(get.preferences(context), 'auto_name_operations')

            column.prop(get.preferences(context), 'namer_popup_width')
