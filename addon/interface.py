import bpy
import bl_ui
import rna_keymap_ui

from .utilities import get
from .config import remote


class name_panel:


    def __init__(self, panel, context):


        self.layout = panel.layout

        if get.preferences(context).update_display_panel and get.preferences(context).update_ready:

            row = self.layout.row()
            row.alignment = 'CENTER'
            row.scale_y = 2
            row.operator('wm.name_panel_update_info', text='Update Available!', icon='ERROR', emboss=False)


        self.option = get.name_panel.options(context)

        self.find_and_replace(context)

        self.layout.separator()

        self.name_stack(context)


    def find_and_replace(self, context):

        column = self.layout.column(align=True)

        row = column.row(align=True)

        row.prop(self.option, 'find', text='', icon='VIEWZOOM')

        if self.option.find: row.operator('view3d.name_panel_clear_find', text='', icon='X')

        row.operator('view3d.name_panel_options', text='', icon='FILTER')
        row.menu('view3d.name_panel_specials', text='', icon='COLLAPSEMENU')

        if self.option.find:
            row = column.row(align=True)

            row.prop(self.option, 'replace', text='', icon='FILE_REFRESH')

            if self.option.replace: row.operator('view3d.name_panel_clear_replace', text='', icon='X')

            sub = row.row(align=True)
            sub.scale_x = 0.2

            sub.operator('view3d.name_panel_options', text='OK')


    def name_stack(self, context):

        self.stack = get.name_panel.name_stack(context)

        # TODO: add display limit
        if self.stack:
            for object in self.stack['datablocks']: self.stack_object(self, context, object)
        else: self.no_stack()


    def no_stack(self):

        option = self.option.filters['options']

        row = self.layout.row()
        row.alignment = 'CENTER'

        # if self.option.find:
        #
        #     row.label(text='No matches found')

        if option.display_mode == 'ACTIVE': row.label(text='No active object')
        elif option.display_mode == 'SELECTED': row.label(text='No selected objects')
        else: row.label(text='No visible objects')

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

        if get.preferences(context).update_display_menu and get.preferences(context).update_ready:
            layout.separator()

            layout.operator('wm.name_panel_update_info', text='Update Available!', icon='ERROR')


    class stack_object:


        def __init__(self, panel, context, object):

            self.option = get.name_panel.options(context).filters['options']
            self.context = context
            self.object = object

            column = panel.layout.column(align=True)

            self.row(panel.stack['objects'], column, self.object, get.icon.object(self.object), emboss=True if self.object.select or self.object == self.context.active_object else False, active=not (self.object == self.context.scene.objects.active and not self.object.select))

            for type in panel.stack['objects'][object.name]['types']: getattr(self, type)(panel.stack['objects'][object.name][type], column)
            for _ in range(get.preferences(self.context).separators): panel.layout.separator()


        def row(self, location, column, datablock, icon, name_type='name', emboss=False, active=True):

            if datablock:
                row = column.row(align=True)
                row.active = location[getattr(datablock, name_type)]['active']

                sub = row.row(align=True if emboss else False)
                sub.scale_x = 1.5 if not emboss else 1.6
                sub.active = active

                operator = sub.operator('wm.datablock_settings', text='', icon=icon, emboss=emboss)
                operator.click_through = get.preferences(self.context).click_through
                operator.context_override = ''
                operator.object_name = self.object.name
                operator.target_name = getattr(datablock, name_type)
                operator.identifier = get.identifier(datablock)

                row.prop(datablock, name_type, text='')


        def groups(self, location, column):
            for group in location['datablocks']: self.row(location, column, group, get.icon('groups'))


        def grease_pencils(self, location, column):

            self.row(location, column, location['datablocks'][0], get.icon('grease_pencils'))

            for layer in location[location['datablocks'][0].name]['grease_pencil_layers']['datablocks']: self.row(location[location['datablocks'][0].name]['grease_pencil_layers'], column, layer, get.icon('grease_pencil_layers'), name_type='info')


        def actions(self, location, column):
            self.row(location, column, location['datablocks'][0], get.icon('actions'))


        def constraints(self, location, column):
            for constraint in location['datablocks']: self.row(location, column, constraint, get.icon('constraints'))


        def modifiers(self, location, column):

            for modifier in location['datablocks']:
                self.row(location, column, modifier, get.icon.modifier(modifier))

                if 'particle_system' in location[modifier.name]:
                    self.row(location[modifier.name]['particle_system'], column, location[modifier.name]['particle_system'][modifier.particle_system.name]['datablock'], get.icon.subtype('particle_system'))
                    self.row(location[modifier.name]['particle_system'][modifier.particle_system.name]['particle_settings'], column, location[modifier.name]['particle_system'][modifier.particle_system.name]['particle_settings'][modifier.particle_system.settings.name]['datablock'], 'DOT')

                    if 'textures' in location[modifier.name]['particle_system'][modifier.particle_system.name]['particle_settings'][modifier.particle_system.settings.name]:
                        for texture in location[modifier.name]['particle_system'][modifier.particle_system.name]['particle_settings'][modifier.particle_system.settings.name]['textures']['datablocks']: self.row(location[modifier.name]['particle_system'][modifier.particle_system.name]['particle_settings'][modifier.particle_system.settings.name]['textures'], column,  location[modifier.name]['particle_system'][modifier.particle_system.name]['particle_settings'][modifier.particle_system.settings.name]['textures'][texture.name]['datablock'], get.icon('textures'))


        def object_data(self, location, column):
            self.row(location, column, location['datablocks'][0], get.icon.object_data(self.object), emboss=True if self.object.select or self.object == self.context.active_object else False, active=not (self.object == self.context.scene.objects.active and not self.object.select))


        def bone_groups(self, location, column):
            for group in location['datablocks']: self.row(location, column, group, get.icon('bone_groups'))


        def bones(self, location, column): # TODO: implement bones for all armatures in namestack

            if location['datablocks']: column.separator()

            for bone in location['datablocks']:
                active_bone = self.context.active_bone if self.context.mode == 'EDIT_ARMATURE' else self.context.active_pose_bone
                bone_selected = bone.select if self.context.mode == 'EDIT_ARMATURE' else bone.bone.select

                self.row(location, column, bone, get.icon('bones'), emboss=True if bone_selected or bone == active_bone else False, active=not (bone == active_bone and not bone_selected))

                if 'bone_constraints' in location[bone.name]: self.constraints(location[bone.name]['bone_constraints'], column)


        def shapekeys(self, location, column):
            for shapekey in location['datablocks']: self.row(location, column, shapekey, get.icon('shapekeys'))


        def vertex_groups(self, location, column):
            for vertex_group in location['datablocks']: self.row(location, column, vertex_group, get.icon('vertex_groups'))


        def uv_maps(self, location, column):
            for uv_map in location['datablocks']: self.row(location, column, uv_map, get.icon('uv_maps'))


        def vertex_colors(self, location, column):
            for vertex_color in location['datablocks']: self.row(location, column, vertex_color, get.icon('vertex_colors'))


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
                self.filters(context)
                self.display_mode(context)

            else: self.extra_options(context)


        @staticmethod
        def set_height(column, separators):

            for _ in range(0, separators): column.separator()


        def display_mode(self, context):

            row = self.split.row()

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
            row.prop(get.preferences(context), 'pin_active', toggle=True)
            row.prop(get.preferences(context), 'click_through', toggle=True)

            row = self.split.row(align=True)
            row.prop(get.preferences(context), 'location', expand=True)

            row = self.split.row()
            row.prop(get.preferences(context), 'popup_width', text='Pop-up Width')


    class preferences:


        def __init__(self, addon, context):
            addon.preference = get.preferences(context)

            row = addon.layout.row()
            row.scale_y = 2
            row.prop(addon.preference, 'mode', expand=True)

            getattr(self, addon.preference.mode.lower())(addon, context)

            addon.layout.separator()

            row = addon.layout.row(align=True)
            row.scale_y = 1.5
            row.operator('wm.url_open', text='Report a bug').url = remote['bug_report']
            row.operator('wm.url_open', text='Thread').url = remote['thread']
            row.operator('wm.url_open', text='proxeIO').url = remote['proxeIO']
            row.operator('wm.url_open', text='Patreon').url = remote['patreon']
            row.operator('wm.url_open', text='Donate').url = remote['donate']


        def general(self, addon, context):

            box = addon.layout.box()

            row = box.row()
            row.prop(addon.preference, 'keep_session_settings')


        def panel(self, addon, context):

            box = addon.layout.box()

            row = box.row()
            row.label(text='Location:')
            row.prop(addon.preference, 'location', expand=True)

            row = box.row()
            row.prop(addon.preference, 'pin_active')

            row = box.row()
            row.prop(addon.preference, 'remove_item_panel')
            row.prop(addon.preference, 'click_through')

            row = box.row()
            row.label(text='Pop-up Width:')
            row.prop(addon.preference, 'popup_width', text='')

            row = box.row()
            row.label(text='Separators:')
            row.prop(addon.preference, 'separators', text='')


        def datablock(self, addon, context):

            box = addon.layout.box()

            row = box.row()
            row.label(text='Pop-up Width:')
            row.prop(addon.preference, 'datablock_popup_width', text='')


        def namer(self, addon, context):

            box = addon.layout.box()

            row = box.row()
            row.prop(addon.preference, 'use_last')
            row.prop(addon.preference, 'auto_name_operations')

            row = box.row()
            row.label(text='Pop-up Width:')
            row.prop(addon.preference, 'namer_popup_width')


        def hotkey(self, addon, context):

            layout = addon.layout
            column = layout.column()

            keyconfig = context.window_manager.keyconfigs.addon
            keymap = keyconfig.keymaps['Window']

            if 'wm.datablock_settings' in keymap.keymap_items:
                keymapitem = keymap.keymap_items['wm.datablock_settings']
                column.context_pointer_set("keymap", keymap)
                rna_keymap_ui.draw_kmi([], keyconfig, keymap, keymapitem, column, 0)

            if 'wm.namer' in keymap.keymap_items:
                keymapitem = keymap.keymap_items['wm.namer']
                column.context_pointer_set("keymap", keymap)
                rna_keymap_ui.draw_kmi([], keyconfig, keymap, keymapitem, column, 0)


        def updates(self, addon, context):

            box = addon.layout.box()

            row = box.row()
            row.prop(addon, 'update_check')

            row = box.row()
            row.prop(addon, 'update_display_menu')
            row.prop(addon, 'update_display_panel')


class datablock:

    # TODO: hide extra settings for these datablock types if there is a target and context override in datablock oeprator
    # target object
    # target mesh
    # target curve
    # target metaball
    # target armature
    # target lattice
    # target empty
    # target speaker
    # target camera
    # target lamp
    # target material
    # target texture
    # target particles
    # target group
    # target grease pencil
    # target grease pencil layer
    # target action
    # target constraint
    # target modifier
    # target image
    # target bone group
    # target pose bone
    # target edit bone
    # target vertex group
    # target shapekey
    # target uv map (MeshTexturePolyLayer)
    # target vertex color (MeshLoopColorLayer)
    # target material
    # target texture
    # target particle system
    # target particle settings

    # TODO: pin id, name panel needs to override but not replace pin state if it is called from name stack
        # this should work with the individual states too such as modifier, if a modifier is pinned after being called from name stack, unless the operator is called again from the stack only show the last pin state, otherwise show the new datablock target and maintain the old pin state
        #XXX: add pin history navigation
    # TODO: Create a properties pop-up that behaves the same as the properties window place it on the search row, right after filters
    def __init__(self, operator, context):
        self.override = False

        layout = operator.layout

        option = get.datablock.options(context)

        row = layout.row(align=True)
        row.prop(get.datablock.options(context), 'context', text='', expand=True)
        row.menu('view3d.name_panel_specials', text='', icon='COLLAPSEMENU') # TODO: make datablock pop-up specials menu

        box_column = layout.column(align=True)

        panels = getattr(option, option.context.lower())

        getattr(self, option.context.lower())(context)

        if not self.override: self.draw_panels(context, panels, box_column)


    def render(self, context):
        self._frame_rate_args_prev = None
        self._preset_class = None
        RENDER_PT_dimensions = bpy.types.RENDER_PT_dimensions
        self._draw_framerate_label = bpy.types.RENDER_PT_dimensions._draw_framerate_label
        self.draw_framerate = bpy.types.RENDER_PT_dimensions.draw_framerate


    def render_layer(self, context):
        self.draw_pass_type_buttons = bpy.types.RENDERLAYER_PT_layer_passes.draw_pass_type_buttons
        self.draw_edge_type_buttons = bpy.types.RENDERLAYER_PT_freestyle_lineset.draw_edge_type_buttons
        self.draw_modifier_box_header = bpy.types.RENDERLAYER_PT_freestyle_linestyle.draw_modifier_box_header
        self.draw_modifier_common = bpy.types.RENDERLAYER_PT_freestyle_linestyle.draw_modifier_common
        self.draw_modifier_box_error = bpy.types.RENDERLAYER_PT_freestyle_linestyle.draw_modifier_box_error
        self.draw_modifier_color_ramp_common = bpy.types.RENDERLAYER_PT_freestyle_linestyle.draw_modifier_color_ramp_common
        self.draw_modifier_curve_common = bpy.types.RENDERLAYER_PT_freestyle_linestyle.draw_modifier_curve_common


    def scene(self, context): pass


    def world(self, context): pass


    def object(self, context): pass


    def constraint(self, context): pass


    def modifier(self, context):
        self.ARMATURE = bpy.types.DATA_PT_modifiers.ARMATURE
        self.ARRAY = bpy.types.DATA_PT_modifiers.ARRAY
        self.BEVEL = bpy.types.DATA_PT_modifiers.BEVEL
        self.BOOLEAN = bpy.types.DATA_PT_modifiers.BOOLEAN
        self.BUILD = bpy.types.DATA_PT_modifiers.BUILD
        self.MESH_CACHE = bpy.types.DATA_PT_modifiers.MESH_CACHE
        self.MESH_SEQUENCE_CACHE = bpy.types.DATA_PT_modifiers.MESH_SEQUENCE_CACHE
        self.CAST = bpy.types.DATA_PT_modifiers.CAST
        self.CLOTH = bpy.types.DATA_PT_modifiers.CLOTH
        self.COLLISION = bpy.types.DATA_PT_modifiers.COLLISION
        self.CURVE = bpy.types.DATA_PT_modifiers.CURVE
        self.DECIMATE = bpy.types.DATA_PT_modifiers.DECIMATE
        self.DISPLACE = bpy.types.DATA_PT_modifiers.DISPLACE
        self.DYNAMIC_PAINT = bpy.types.DATA_PT_modifiers.DYNAMIC_PAINT
        self.EDGE_SPLIT = bpy.types.DATA_PT_modifiers.EDGE_SPLIT
        self.EXPLODE = bpy.types.DATA_PT_modifiers.EXPLODE
        self.FLUID_SIMULATION = bpy.types.DATA_PT_modifiers.FLUID_SIMULATION
        self.HOOK = bpy.types.DATA_PT_modifiers.HOOK
        self.LAPLACIANDEFORM = bpy.types.DATA_PT_modifiers.LAPLACIANDEFORM
        self.LAPLACIANSMOOTH = bpy.types.DATA_PT_modifiers.LAPLACIANSMOOTH
        self.LATTICE = bpy.types.DATA_PT_modifiers.LATTICE
        self.MASK = bpy.types.DATA_PT_modifiers.MASK
        self.MESH_DEFORM = bpy.types.DATA_PT_modifiers.MESH_DEFORM
        self.MIRROR = bpy.types.DATA_PT_modifiers.MIRROR
        self.MULTIRES = bpy.types.DATA_PT_modifiers.MULTIRES
        self.OCEAN = bpy.types.DATA_PT_modifiers.OCEAN
        self.PARTICLE_INSTANCE = bpy.types.DATA_PT_modifiers.PARTICLE_INSTANCE
        self.PARTICLE_SYSTEM = bpy.types.DATA_PT_modifiers.PARTICLE_SYSTEM
        self.SCREW = bpy.types.DATA_PT_modifiers.SCREW
        self.SHRINKWRAP = bpy.types.DATA_PT_modifiers.SHRINKWRAP
        self.SIMPLE_DEFORM = bpy.types.DATA_PT_modifiers.SIMPLE_DEFORM
        self.SMOKE = bpy.types.DATA_PT_modifiers.SMOKE
        self.SMOOTH = bpy.types.DATA_PT_modifiers.SMOOTH
        self.SOFT_BODY = bpy.types.DATA_PT_modifiers.SOFT_BODY
        self.SOLIDIFY = bpy.types.DATA_PT_modifiers.SOLIDIFY
        self.SUBSURF = bpy.types.DATA_PT_modifiers.SUBSURF
        self.SURFACE = bpy.types.DATA_PT_modifiers.SURFACE
        self.SURFACE_DEFORM = bpy.types.DATA_PT_modifiers.SURFACE_DEFORM
        self.UV_PROJECT = bpy.types.DATA_PT_modifiers.UV_PROJECT
        self.WARP = bpy.types.DATA_PT_modifiers.WARP
        self.WAVE = bpy.types.DATA_PT_modifiers.WAVE
        self.REMESH = bpy.types.DATA_PT_modifiers.REMESH
        self.vertex_weight_mask = bpy.types.DATA_PT_modifiers.vertex_weight_mask
        self.VERTEX_WEIGHT_EDIT = bpy.types.DATA_PT_modifiers.VERTEX_WEIGHT_EDIT
        self.VERTEX_WEIGHT_MIX = bpy.types.DATA_PT_modifiers.VERTEX_WEIGHT_MIX
        self.VERTEX_WEIGHT_PROXIMITY = bpy.types.DATA_PT_modifiers.VERTEX_WEIGHT_PROXIMITY
        self.SKIN = bpy.types.DATA_PT_modifiers.SKIN
        self.TRIANGULATE = bpy.types.DATA_PT_modifiers.TRIANGULATE
        self.UV_WARP = bpy.types.DATA_PT_modifiers.UV_WARP
        self.WIREFRAME = bpy.types.DATA_PT_modifiers.WIREFRAME
        self.DATA_TRANSFER = bpy.types.DATA_PT_modifiers.DATA_TRANSFER
        self.NORMAL_EDIT = bpy.types.DATA_PT_modifiers.NORMAL_EDIT
        self.CORRECTIVE_SMOOTH = bpy.types.DATA_PT_modifiers.CORRECTIVE_SMOOTH


        def modifiers_draw(self, context):

            layout = self.layout

            ob = context.active_object

            layout.operator_menu_enum("object.modifier_add", "type")

            for md in ob.modifiers:
                box = layout.template_modifier(md)
                if box:
                    # match enum type to our functions, avoids a lookup table.
                    getattr(self, md.type)(self, box, ob, md)

        self.layout = layout.column()
        modifiers_draw(self, context)


    def data(self, context): pass


    def bone(self, context): pass


    def bone_constraint(self, context): pass


    def material(self, context): pass


    def texture(self, context): pass


    def particles(self, context): pass


    def physics(self, context): pass


    def draw_panels(self, context, panels, box_column):
        for panel in panels:
            type = getattr(bpy.types, panel.id)
            if hasattr(type, 'COMPAT_ENGINES'):
                if context.scene.render.engine in type.COMPAT_ENGINES:
                    if hasattr(type, 'poll'):
                        if type.poll(context):
                            draw_header_overrides = [
                                '',
                            ]
                            draw_overrides = [
                                'RENDERLAYER_PT_freestyle_lineset',
                                'WORLD_PT_context_world',
                            ]
                            self.draw_box(context, box_column, panel, type)
                    else: self.draw_box(context, box_column, panel, type)
            elif hasattr(type, 'poll'):
                if type.poll(context): self.draw_box(context, box_column, panel, type)
            else: self.draw_box(context, box_column, panel, type)

        for panel in panels:
            type = getattr(bpy.types, panel.id)
            if hasattr(type, 'COMPAT_ENGINES'):
                if context.scene.render.engine in type.COMPAT_ENGINES:
                    if hasattr(type, 'poll'):
                        if type.poll(context):
                            if panel.id == 'RENDERLAYER_PT_freestyle_lineset': self.draw_box(context, box_column, panel, type, draw=self.freestyle_lineset_draw)
                            else: self.draw_box(context, box_column, panel, type)
                    else: self.draw_box(context, box_column, panel, type)
            elif hasattr(type, 'poll'):
                if type.poll(context): self.draw_box(context, box_column, panel, type)
            else: self.draw_box(context, box_column, panel, type)

        for panel in panels:
            type = getattr(bpy.types, panel.id)
            if hasattr(type, 'COMPAT_ENGINES'):
                if context.scene.render.engine in type.COMPAT_ENGINES:
                    if self.poll_context_world(context):
                        if panel.id == 'WORLD_PT_context_world': self.draw_box(context, box_column, panel, type, draw=self.draw_context_world)
                        else: self.draw_box(context, box_column, panel, type)
                    else: self.draw_box(context, box_column, panel, type)
            elif hasattr(type, 'poll'):
                if type.poll(context): self.draw_box(context, box_column, panel, type)
            else: self.draw_box(context, box_column, panel, type)        pass


    # main
    def draw_box(self, context, box_column, panel, type, draw_header=False, draw=False):

        if hasattr(type, 'bl_options'):
            if 'HIDE_HEADER' in getattr(type, 'bl_options'): hidden_header = True
            else: hidden_header = False
        else: hidden_header = False

        if not hidden_header:
            box = box_column.box()
            row = box.row(align=True)
            row.alignment = 'LEFT'

            sub = row.row(align=True)
            sub.scale_x = 0.5
            sub.prop(panel, 'collapsed', text='', icon='TRIA_DOWN' if not panel.collapsed else 'TRIA_RIGHT', emboss=False)

            if hasattr(type, 'draw_header'):
                sub = row.row(align=True)
                sub.scale_x = 0.8
                self.layout = sub
                if draw_header: draw_header(context)
                else: type.draw_header(self, context)

            row.prop(panel, 'collapsed', text=panel.label, toggle=True, emboss=False) # TODO: Run this as a collapse operator, catch event and emulate panel behavior

            sub = row.row(align=True)
            sub.prop(panel, 'collapsed', text=' ', toggle=True, emboss=False)

            if not panel.collapsed:
                box = box_column.box()
                column = box.column()

                self.layout = column
                if draw: draw(context)
                else: type.draw(self, context)

        else:
            column = box_column

            self.layout = column
            if draw: draw(context)
            else: type.draw(self, context)

        box_column.separator()


    # render


    # render layer
    def freestyle_lineset_draw(self, context):
        layout = self.layout

        rd = context.scene.render
        rl = rd.layers.active
        freestyle = rl.freestyle_settings
        lineset = freestyle.linesets.active

        layout.active = rl.use_freestyle

        row = layout.row()
        rows = 4 if lineset else 2
        row.template_list("RENDERLAYER_UL_linesets", "", freestyle, "linesets", freestyle.linesets, "active_index", rows=rows)

        sub = row.column(align=True)
        sub.operator("scene.freestyle_lineset_add", icon='ZOOMIN', text="")
        sub.operator("scene.freestyle_lineset_remove", icon='ZOOMOUT', text="")
        sub.menu("RENDER_MT_lineset_specials", icon='DOWNARROW_HLT', text="")
        if lineset:
            sub.separator()
            sub.separator()
            sub.operator("scene.freestyle_lineset_move", icon='TRIA_UP', text="").direction = 'UP'
            sub.operator("scene.freestyle_lineset_move", icon='TRIA_DOWN', text="").direction = 'DOWN'

            col = layout.column()
            col.label(text="Selection By:")
            row = col.row(align=True)
            row.prop(lineset, "select_by_visibility", text="Visibility", toggle=True)
            row.prop(lineset, "select_by_edge_types", text="Edge Types", toggle=True)
            row.prop(lineset, "select_by_face_marks", text="Face Marks", toggle=True)
            row.prop(lineset, "select_by_group", text="Group", toggle=True)
            row.prop(lineset, "select_by_image_border", text="Image Border", toggle=True)

            if lineset.select_by_visibility:
                col.label(text="Visibility:")
                row = col.row(align=True)
                row.prop(lineset, "visibility", expand=True)
                if lineset.visibility == 'RANGE':
                    row = col.row(align=True)
                    row.prop(lineset, "qi_start")
                    row.prop(lineset, "qi_end")

            if lineset.select_by_edge_types:
                col.label(text="Edge Types:")
                row = col.row()
                row.prop(lineset, "edge_type_negation", expand=True)
                row.prop(lineset, "edge_type_combination", expand=True)

                split = col.split()

                sub = split.column()
                self.draw_edge_type_buttons(self, sub, lineset, "silhouette")
                self.draw_edge_type_buttons(self, sub, lineset, "border")
                self.draw_edge_type_buttons(self, sub, lineset, "contour")
                self.draw_edge_type_buttons(self, sub, lineset, "suggestive_contour")
                self.draw_edge_type_buttons(self, sub, lineset, "ridge_valley")

                sub = split.column()
                self.draw_edge_type_buttons(self, sub, lineset, "crease")
                self.draw_edge_type_buttons(self, sub, lineset, "edge_mark")
                self.draw_edge_type_buttons(self, sub, lineset, "external_contour")
                self.draw_edge_type_buttons(self, sub, lineset, "material_boundary")

            if lineset.select_by_face_marks:
                col.label(text="Face Marks:")
                row = col.row()
                row.prop(lineset, "face_mark_negation", expand=True)
                row.prop(lineset, "face_mark_condition", expand=True)

            if lineset.select_by_group:
                col.label(text="Group:")
                row = col.row()
                row.prop(lineset, "group", text="")
                row.prop(lineset, "group_negation", expand=True)


    def draw_color_modifier(self, context, modifier):
        layout = self.layout

        col = layout.column(align=True)
        self.draw_modifier_box_header(self, col.box(), modifier)
        if modifier.expanded:
            box = col.box()
            self.draw_modifier_common(self, box, modifier)

            if modifier.type == 'ALONG_STROKE':
                self.draw_modifier_color_ramp_common(self, box, modifier, False)

            elif modifier.type == 'DISTANCE_FROM_OBJECT':
                box.prop(modifier, "target")
                self.draw_modifier_color_ramp_common(self, box, modifier, True)
                prop = box.operator("scene.freestyle_fill_range_by_selection")
                prop.type = 'COLOR'
                prop.name = modifier.name

            elif modifier.type == 'DISTANCE_FROM_CAMERA':
                self.draw_modifier_color_ramp_common(self, box, modifier, True)
                prop = box.operator("scene.freestyle_fill_range_by_selection")
                prop.type = 'COLOR'
                prop.name = modifier.name

            elif modifier.type == 'MATERIAL':
                row = box.row()
                row.prop(modifier, "material_attribute", text="")
                sub = row.column()
                sub.prop(modifier, "use_ramp")
                if modifier.material_attribute in {'LINE', 'DIFF', 'SPEC'}:
                    sub.active = True
                    show_ramp = modifier.use_ramp
                else:
                    sub.active = False
                    show_ramp = True
                if show_ramp:
                    self.draw_modifier_color_ramp_common(self, box, modifier, False)

            elif modifier.type == 'TANGENT':
                self.draw_modifier_color_ramp_common(self, box, modifier, False)

            elif modifier.type == 'NOISE':
                self.draw_modifier_color_ramp_common(self, box, modifier, False)
                row = box.row(align=False)
                row.prop(modifier, "amplitude")
                row.prop(modifier, "period")
                row.prop(modifier, "seed")

            elif modifier.type == 'CREASE_ANGLE':
                self.draw_modifier_color_ramp_common(self, box, modifier, False)
                row = box.row(align=True)
                row.prop(modifier, "angle_min")
                row.prop(modifier, "angle_max")

            elif modifier.type == 'CURVATURE_3D':
                self.draw_modifier_color_ramp_common(self, box, modifier, False)
                row = box.row(align=True)
                row.prop(modifier, "curvature_min")
                row.prop(modifier, "curvature_max")
                freestyle = context.scene.render.layers.active.freestyle_settings
                if not freestyle.use_smoothness:
                    message = "Enable Face Smoothness to use this modifier"
                    self.draw_modifier_box_error(self, col.box(), modifier, message)


    def draw_alpha_modifier(self, context, modifier):
        layout = self.layout

        col = layout.column(align=True)
        self.draw_modifier_box_header(self, col.box(), modifier)
        if modifier.expanded:
            box = col.box()
            self.draw_modifier_common(self, box, modifier)

            if modifier.type == 'ALONG_STROKE':
                self.draw_modifier_curve_common(self, box, modifier, False, False)

            elif modifier.type == 'DISTANCE_FROM_OBJECT':
                box.prop(modifier, "target")
                self.draw_modifier_curve_common(self, box, modifier, True, False)
                prop = box.operator("scene.freestyle_fill_range_by_selection")
                prop.type = 'ALPHA'
                prop.name = modifier.name

            elif modifier.type == 'DISTANCE_FROM_CAMERA':
                self.draw_modifier_curve_common(self, box, modifier, True, False)
                prop = box.operator("scene.freestyle_fill_range_by_selection")
                prop.type = 'ALPHA'
                prop.name = modifier.name

            elif modifier.type == 'MATERIAL':
                box.prop(modifier, "material_attribute", text="")
                self.draw_modifier_curve_common(self, box, modifier, False, False)

            elif modifier.type == 'TANGENT':
                self.draw_modifier_curve_common(self, box, modifier, False, False)

            elif modifier.type == 'NOISE':
                self.draw_modifier_curve_common(self, box, modifier, False, False)
                row = box.row(align=False)
                row.prop(modifier, "amplitude")
                row.prop(modifier, "period")
                row.prop(modifier, "seed")

            elif modifier.type == 'CREASE_ANGLE':
                self.draw_modifier_curve_common(self, box, modifier, False, False)
                row = box.row(align=True)
                row.prop(modifier, "angle_min")
                row.prop(modifier, "angle_max")

            elif modifier.type == 'CURVATURE_3D':
                self.draw_modifier_curve_common(self, box, modifier, False, False)
                row = box.row(align=True)
                row.prop(modifier, "curvature_min")
                row.prop(modifier, "curvature_max")
                freestyle = context.scene.render.layers.active.freestyle_settings
                if not freestyle.use_smoothness:
                    message = "Enable Face Smoothness to use this modifier"
                    self.draw_modifier_box_error(self, col.box(), modifier, message)


    def draw_thickness_modifier(self, context, modifier):
        layout = self.layout

        col = layout.column(align=True)
        self.draw_modifier_box_header(self, col.box(), modifier)
        if modifier.expanded:
            box = col.box()
            self.draw_modifier_common(self, box, modifier)

            if modifier.type == 'ALONG_STROKE':
                self.draw_modifier_curve_common(self, box, modifier, False, True)

            elif modifier.type == 'DISTANCE_FROM_OBJECT':
                box.prop(modifier, "target")
                self.draw_modifier_curve_common(self, box, modifier, True, True)
                prop = box.operator("scene.freestyle_fill_range_by_selection")
                prop.type = 'THICKNESS'
                prop.name = modifier.name

            elif modifier.type == 'DISTANCE_FROM_CAMERA':
                self.draw_modifier_curve_common(self, box, modifier, True, True)
                prop = box.operator("scene.freestyle_fill_range_by_selection")
                prop.type = 'THICKNESS'
                prop.name = modifier.name

            elif modifier.type == 'MATERIAL':
                box.prop(modifier, "material_attribute", text="")
                self.draw_modifier_curve_common(self, box, modifier, False, True)

            elif modifier.type == 'CALLIGRAPHY':
                box.prop(modifier, "orientation")
                row = box.row(align=True)
                row.prop(modifier, "thickness_min")
                row.prop(modifier, "thickness_max")

            elif modifier.type == 'TANGENT':
                self.draw_modifier_curve_common(self, box, modifier, False, False)
                self.mapping = 'CURVE'
                row = box.row(align=True)
                row.prop(modifier, "thickness_min")
                row.prop(modifier, "thickness_max")

            elif modifier.type == 'NOISE':
                row = box.row(align=False)
                row.prop(modifier, "amplitude")
                row.prop(modifier, "period")
                row = box.row(align=False)
                row.prop(modifier, "seed")
                row.prop(modifier, "use_asymmetric")

            elif modifier.type == 'CREASE_ANGLE':
                self.draw_modifier_curve_common(self, box, modifier, False, False)
                row = box.row(align=True)
                row.prop(modifier, "thickness_min")
                row.prop(modifier, "thickness_max")
                row = box.row(align=True)
                row.prop(modifier, "angle_min")
                row.prop(modifier, "angle_max")

            elif modifier.type == 'CURVATURE_3D':
                self.draw_modifier_curve_common(self, box, modifier, False, False)
                row = box.row(align=True)
                row.prop(modifier, "thickness_min")
                row.prop(modifier, "thickness_max")
                row = box.row(align=True)
                row.prop(modifier, "curvature_min")
                row.prop(modifier, "curvature_max")
                freestyle = context.scene.render.layers.active.freestyle_settings
                if not freestyle.use_smoothness:
                    message = "Enable Face Smoothness to use this modifier"
                    self.draw_modifier_box_error(self, col.box(), modifier, message)


    def draw_geometry_modifier(self, context, modifier):
        layout = self.layout

        col = layout.column(align=True)
        self.draw_modifier_box_header(self, col.box(), modifier)
        if modifier.expanded:
            box = col.box()

            if modifier.type == 'SAMPLING':
                box.prop(modifier, "sampling")

            elif modifier.type == 'BEZIER_CURVE':
                box.prop(modifier, "error")

            elif modifier.type == 'SINUS_DISPLACEMENT':
                split = box.split()
                col = split.column()
                col.prop(modifier, "wavelength")
                col.prop(modifier, "amplitude")
                col = split.column()
                col.prop(modifier, "phase")

            elif modifier.type == 'SPATIAL_NOISE':
                split = box.split()
                col = split.column()
                col.prop(modifier, "amplitude")
                col.prop(modifier, "scale")
                col.prop(modifier, "octaves")
                col = split.column()
                col.prop(modifier, "smooth")
                col.prop(modifier, "use_pure_random")

            elif modifier.type == 'PERLIN_NOISE_1D':
                split = box.split()
                col = split.column()
                col.prop(modifier, "frequency")
                col.prop(modifier, "amplitude")
                col.prop(modifier, "seed")
                col = split.column()
                col.prop(modifier, "octaves")
                col.prop(modifier, "angle")

            elif modifier.type == 'PERLIN_NOISE_2D':
                split = box.split()
                col = split.column()
                col.prop(modifier, "frequency")
                col.prop(modifier, "amplitude")
                col.prop(modifier, "seed")
                col = split.column()
                col.prop(modifier, "octaves")
                col.prop(modifier, "angle")

            elif modifier.type == 'BACKBONE_STRETCHER':
                box.prop(modifier, "backbone_length")

            elif modifier.type == 'TIP_REMOVER':
                box.prop(modifier, "tip_length")

            elif modifier.type == 'POLYGONIZATION':
                box.prop(modifier, "error")

            elif modifier.type == 'GUIDING_LINES':
                box.prop(modifier, "offset")

            elif modifier.type == 'BLUEPRINT':
                row = box.row()
                row.prop(modifier, "shape", expand=True)
                box.prop(modifier, "rounds")
                row = box.row()
                if modifier.shape in {'CIRCLES', 'ELLIPSES'}:
                    row.prop(modifier, "random_radius")
                    row.prop(modifier, "random_center")
                elif modifier.shape == 'SQUARES':
                    row.prop(modifier, "backbone_length")
                    row.prop(modifier, "random_backbone")

            elif modifier.type == '2D_OFFSET':
                row = box.row(align=True)
                row.prop(modifier, "start")
                row.prop(modifier, "end")
                row = box.row(align=True)
                row.prop(modifier, "x")
                row.prop(modifier, "y")

            elif modifier.type == '2D_TRANSFORM':
                box.prop(modifier, "pivot")
                if modifier.pivot == 'PARAM':
                    box.prop(modifier, "pivot_u")
                elif modifier.pivot == 'ABSOLUTE':
                    row = box.row(align=True)
                    row.prop(modifier, "pivot_x")
                    row.prop(modifier, "pivot_y")
                row = box.row(align=True)
                row.prop(modifier, "scale_x")
                row.prop(modifier, "scale_y")
                box.prop(modifier, "angle")

            elif modifier.type == 'SIMPLIFICATION':
                box.prop(modifier, "tolerance")


    # scene
    @staticmethod
    def draw_keyframing_settings(context, layout, ks, ksp):
        datablock._draw_keyframing_setting(
                context, layout, ks, ksp, "Needed",
                "use_insertkey_override_needed", "use_insertkey_needed",
                userpref_fallback="use_keyframe_insert_needed")

        datablock._draw_keyframing_setting(
                context, layout, ks, ksp, "Visual",
                "use_insertkey_override_visual", "use_insertkey_visual",
                userpref_fallback="use_visual_keying")

        datablock._draw_keyframing_setting(
                context, layout, ks, ksp, "XYZ to RGB",
                "use_insertkey_override_xyz_to_rgb", "use_insertkey_xyz_to_rgb")


    @staticmethod
    def _draw_keyframing_setting(context, layout, ks, ksp, label, toggle_prop, prop, userpref_fallback=None):
        if ksp:
            item = ksp

            if getattr(ks, toggle_prop):
                owner = ks
                propname = prop
            else:
                owner = context.user_preferences.edit
                if userpref_fallback:
                    propname = userpref_fallback
                else:
                    propname = prop
        else:
            item = ks

            owner = context.user_preferences.edit
            if userpref_fallback:
                propname = userpref_fallback
            else:
                propname = prop

        row = layout.row(align=True)
        row.prop(item, toggle_prop, text="", icon='STYLUS_PRESSURE', toggle=True)  # XXX: needs dedicated icon

        subrow = row.row()
        subrow.active = getattr(item, toggle_prop)
        if subrow.active:
            subrow.prop(item, prop, text=label)
        else:
            subrow.prop(owner, propname, text=label)


    # world
    @staticmethod
    def poll_context_world(context):
        return context.scene.world


    def draw_context_world(self, context):
        layout = self.layout

        scene = context.scene
        world = scene.world
        texture_count = world and len(world.texture_slots.keys())
        split = layout.split(percentage=0.85)
        if scene: split.template_ID(scene, "world", new="world.new")
        if texture_count: split.label(text=str(texture_count), icon='TEXTURE')


    @staticmethod
    def poll_cycles_world_volume(context):
        return context.scene.world.node_tree


    @staticmethod
    def poll_cycles_world_mist(context):
        for layer in context.scene.render.layers:
            if layer.use_pass_mist:
                return True



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

        if category == 'Objects': row.prop(option, 'toggle_objects', text='', icon='RADIOBUT_OFF' if not option.toggle_objects else 'RADIOBUT_ON')
        elif category == 'Objects Data': row.prop(option, 'toggle_objects_data', text='', icon='RADIOBUT_OFF' if not option.toggle_objects_data else 'RADIOBUT_ON')
        for target in get.namer.catagories[category]:
            if target not in {'line_sets', 'sensors', 'controllers', 'actuators'}: row.prop(option, target, text='', icon=get.icon(target))
            elif target == 'line_sets': row.prop(option, target, text='Line Sets', toggle=True)
            else: row.prop(option, target, text=target.title(), toggle=True)


    @staticmethod
    def search_specials(operator, context):

        layout = operator.layout

        if get.namer.options(context).mode == 'NAME':
            naming = get.namer.options(context).naming['options']
            option = naming.operations[naming.active_index]

        else: option = get.namer.options(context).sorting['options']

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

            if self.sorting and not custom_mode: operation_mode = 'placement'
            else: operation_mode = '{}_mode'.format(option.operation_options_mode.lower()) if not custom_mode else custom_mode

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

            else: self.position_prop(option, row)


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

            if self.sorting: self.separator_prop(option, row)
            else: self.insert_prop(option, row)


        def suffix(self, option, row):

            if self.sorting: self.separator_prop(option, row)
            else: self.insert_prop(option, row)


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
                    layout.label(text='Dopesheet\'s dopesheet mode is not yet supported')


                @staticmethod
                def action(operator, context, option, layout):

                    # group
                    layout.label(text='Dopesheet\'s action mode is not yet supported')


                @staticmethod
                def shapekey(operator, context, option, layout):

                    # group
                    layout.label(text='Dopesheet\'s shapekey mode is not yet supported')


                @staticmethod
                def gpencil(operator, context, option, layout):

                    # g pencil
                    # layers
                    layout.label(text='Dopesheet\'s grease pencil mode is not yet supported')


                @staticmethod
                def mask(operator, context, option, layout):

                    # mask
                    # layer
                    layout.label(text='Dopesheet\'s mask file mode is not yet supported')


                @staticmethod
                def cachefile(operator, context, option, layout):

                    layout.label(text='Dopesheet\'s cache file mode is not yet supported')


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
        def name_slice(option, column): pass


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

            if option.sort_mode == 'ALL': namer.mode_row(option, column, active=False, custom_mode='sort_mode', sorting=True)
            else: namer.mode_row(option, column, custom_mode='sort_mode', sorting=True)


        def descend(self, option, column):

            if option.sort_mode == 'ALL': namer.mode_row(option, column, active=False, custom_mode='sort_mode', sorting=True)
            else: namer.mode_row(option, column, custom_mode='sort_mode')


        def position(self, option, column): # TODO: orientation? contains, rotation, scale, location modes, from viewport perspective?

            if option.display_options: getattr(self, option.fallback_mode.lower())(option, column)
            else:
                split = namer.split_row(column)
                split.prop(option, 'starting_point', text='')

                row = split.row(align=True)
                row.prop(option, 'axis_3d', expand=True)

                if option.starting_point in {'CURSOR', 'CENTER', 'ACTIVE'}:
                    column.separator()

                    if option.axis_3d == 'Z': props = ['top', 'bottom']
                    elif option.axis_3d == 'Y': props = ['front', 'back']
                    else: props = ['left', 'right']

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

            if option.display_options: getattr(self, option.fallback_mode.lower())(option, column)
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

        column.label(text='Preview is not yet implemented')


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
