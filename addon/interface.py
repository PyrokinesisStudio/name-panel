from .utilities import get


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

            panel.layout.separator()


        def row(self, location, column, datablock, icon, name_type='name', emboss=False, active=True):

            if datablock:

                row = column.row(align=True)
                row.active = location[getattr(datablock, name_type)]['active']

                sub = row.row(align=True if emboss else False)
                sub.scale_x = 1.5 if not emboss else 1.6
                sub.active = active

                op_prop = 'view3d.name_panel_datablock_click_through' if get.preferences(self.context).click_through else 'view3d.name_panel_datablock'
                op = sub.operator('view3d.name_panel_datablock', text='', icon=icon, emboss=emboss)
                op.object_name = self.object.name
                op.target_name = getattr(datablock, name_type)
                op.identifier = get.identifier(datablock)

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


        def bones(self, location, column):

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

        self.set_height(column, 4)

        self.split = split.column()

        if self.option.mode == 'FILTERS':

            self.display_mode(context)
            self.filters(context)

        else:

            self.extra_options(context)


    @staticmethod
    def set_height(column, separators):

        for _ in range(0, separators):

            column.separator()


    def display_mode(self, context):

        row = self.split.row(align=True)

        row.prop(self.option, 'display_mode', expand=True)


    def filters(self, context):

        column = self.split.column(align=True)

        row = column.row(align=True)
        row.scale_x = 10 # Forced to fit
        row.prop(self.option, 'groups', text='', icon=get.icon('groups'))
        row.prop(self.option, 'grease_pencils', text='', icon=get.icon('grease_pencils'))
        row.prop(self.option, 'actions', text='', icon=get.icon('actions'))
        row.prop(self.option, 'constraints', text='', icon=get.icon('constraints'))
        row.prop(self.option, 'modifiers', text='', icon=get.icon('modifiers'))
        # sounds
        row.prop(self.option, 'bones', text='', icon=get.icon('bones'))
        row.prop(self.option, 'bone_groups', text='', icon=get.icon('bone_groups'))
        row.prop(self.option, 'bone_constraints', text='', icon=get.icon('bone_constraints'))

        row = column.row(align=True)
        row.scale_x = 10
        row.prop(self.option, 'shapekeys', text='', icon=get.icon('shapekeys'))
        row.prop(self.option, 'vertex_groups', text='', icon=get.icon('vertex_groups'))
        row.prop(self.option, 'uv_maps', text='', icon=get.icon('uv_maps'))
        row.prop(self.option, 'vertex_colors', text='', icon=get.icon('vertex_colors'))
        row.prop(self.option, 'materials', text='', icon=get.icon('materials'))
        row.prop(self.option, 'textures', text='', icon=get.icon('textures'))
        row.prop(self.option, 'images', text='', icon=get.icon('images'))
        row.prop(self.option, 'particle_systems', text='', icon=get.icon('particle_systems'))


    def extra_options(self, context):

        row = self.split.row()
        row.prop(get.preferences(context), 'location', expand=True)

        row = self.split.row()
        row.prop(get.preferences(context), 'pin_active')
        row.prop(get.preferences(context), 'click_through')

        row = self.split.row()
        row.label(text='Pop-up Width:')
        row.prop(get.preferences(context), 'popup_width', text='')


class datablock:


    def __init__(self, operator, context):

        layout = operator.layout

        layout.prop(operator.object[operator.object_name], 'name')

        # getattr(self, operator.type)()


class namer:


    def __init__(self, operator, context, specials=False):

        option = get.namer.options(context)

        layout = operator.layout
        column = layout.column()
        split = column.split(percentage=0.15)
        column = split.column()
        column.prop(option, 'mode', expand=True)

        for _ in range(0, 9):
            column.separator()

        column = split.column()

        getattr(self, option.mode.lower())(operator, context, option, column)


    @staticmethod
    def split_row(column, offset=0.0):

        row = column.row(align=True)
        split = row.split(align=True, percentage=0.275+offset)

        return split


    @staticmethod
    def datablock_buttons(category, option, layout):

        targets = {
            'Objects': [
                'meshes',
                'curves',
                'surfaces',
                'metaballs',
                'text_curves',
                'armatures',
                'lattices',
                'empties',
                'speakers',
                'cameras',
                'lamps',
            ],
            'Object Related': [
                'groups',
                'constraints',
                'modifiers',
                'vertex_groups',
                'uv_maps',
                'vertex_colors',
                'shapekeys',
                'bones',
                'bone_groups',
                'bone_constraints',
                'materials',
            ],
            'Grease Pencil': [
                'grease_pencils',
                'grease_pencil_layers',
                'grease_pencil_pallettes',
                'grease_pencil_pallette_colors',
            ],
            'Animation': [
                'actions',
                'action_groups',
                'keying_sets',
                'pose_librarys',
                'pose_markers',
                'tracks',
                'markers',
            ],
            'Node': [
                'nodes',
                'node_labels',
                'node_frames',
                'node_groups',
            ],
            'Particle': [
                'particle_systems',
                'particle_settings',
                'particle_textures',
            ],
            'Freestyle': [
                'line_sets',
                'line_styles',
                'line_style_modifiers',
                'line_style_textures',
            ],
            'Scene': [
                'scenes',
                'render_layers',
                'views',
            ],
            'Image & Brush': [
                'images',
                'brushes',
                'palletes',
            ],
            'Sequence': [
                'sequences',
                'movie_clips',
                'sounds',
            ],
            'Game Engine': [
                'sensors',
                'controllers',
                'actuators',
            ],
            'Misc': [
                'worlds',
                'screens',
                'textures',
                'masks',
                'fonts',
                'texts',
                'librarys',
            ],
            'Custom Property': [
                'custom_properties',
                'custom_property_paths',
            ]
        }

        if category not in {'Objects', 'Custom Property'}:
            layout.label(text=category + ':')

        row = layout.row(align=True)
        row.scale_x = 5

        for target in targets[category]:

            if target not in {'line_set', 'sensor', 'controller', 'actuator'}:
                row.prop(option, target, text='', icon=get.icon(target))

            elif target == 'line_set':
                row.prop(option, target, text='Line Sets', toggle=True)

            else:
                row.prop(option, target, text=target.title() + 's', toggle=True)

        if category == 'Objects':
            row = layout.row()
            row.prop(option, 'object_target', expand=True)


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
                operation_mode = 'positional_placement'

            else:
                operation_mode = '{}_mode'.format(option.mode.lower()) if not custom_mode else custom_mode

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
            row.prop(option, 'mode', expand=True)

            layout.separator()

            if option.mode == 'CONTEXT':
                self.context_area(operator, context, option, layout)

            else:
                namer.datablock_buttons('Objects', option, layout)
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
                    namer.datablock_buttons('Custom Property', option, layout)


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

                row = layout.row()
                row.prop(option, 'effect', expand=True)
                namer.datablock_buttons('Objects', option, layout)
                namer.datablock_buttons('Object Related', option, layout)

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

            op = column.operator('wm.namer_operation_move', text='', icon='TRIA_UP')
            op.up = True

            op = column.operator('wm.namer_operation_move', text='', icon='TRIA_DOWN')
            op.up = False


        class name_operation:


            def __init__(self, option, column):

                option = option.operations[option.active_index]

                row = column.row()
                row.prop(option, 'mode', expand=True)
                column.separator()

                getattr(self, option.mode.lower())(option, column)


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
            row.prop(option, 'mode', expand=True)

            column.separator()

            getattr(self, option.mode.lower())(option, column)


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


        def position(self, option, column): # orientation? contains, rotation, scale, location modes...

            if option.display_options:
                getattr(self, option.fallback_mode.lower())(option, column)

            else:
                split = namer.split_row(column)
                split.prop(option, 'starting_point', text='')

                row = split.row(align=True)
                row.prop(option, 'axis_3D', expand=True)

                if option.starting_point in {'CURSOR', 'CENTER', 'ACTIVE'}:
                    column.separator()

                    if option.axis_3D == 'Z':
                        props = ['top', 'bottom']

                    elif option.axis_3D == 'Y':
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

                    if option.positional_placement not in {'PREFIX', 'SUFFIX'}:
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
            row.prop(option, 'mode', expand=True)

            column.separator()

            getattr(self, option.mode.lower())(operator, context, option, column)


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
            row.prop(option, 'option_mode', expand=True)

            column.separator()

            getattr(self, option.option_mode.lower())(operator, context, option, column)


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
