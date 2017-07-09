from .utilities import get


class panel:


    def __init__(self, Panel, context):

        self.layout = Panel.layout

        self.option = get.panel.options(context)

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

        self.stack = get.panel.name_stack(context)

        # TODO: add display limit
        if self.stack:

            for object in self.stack['datablocks']:

                self.stack_object(self, context, object)

        else:

            self.no_stack()


    class stack_object:


        def __init__(self, panel, context, object):

            self.option = get.panel.options(context).filters['options']
            self.context = context
            self.object = object

            column = panel.layout.column(align=True)

            self.row(panel.stack['objects'], column, self.object, get.icon.object(self.object), emboss=True if self.object.select or self.object == self.context.active_object else False, active=not (self.object == self.context.scene.objects.active and not self.object.select))

            for type in panel.stack['objects'][object.name]['types']:

                getattr(self, type)(panel.stack['objects'][object.name][type], column)

            panel.layout.separator()


        def row(self, location, column, datablock, icon, name_type='name', emboss=False, active=True):

            row = column.row(align=True)
            row.active = location[getattr(datablock, name_type)]['active']

            sub = row.row(align=True if emboss else False)
            sub.scale_x = 1.5 if not emboss else 1.6
            sub.active = active

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

                if 'textures' in location[material.name]:

                    for texture in location[material.name]['textures']['datablocks']:

                        self.row(location[material.name]['textures'], column, texture, get.icon('textures'))


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
