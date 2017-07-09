import bpy

from bpy.types import Operator
from bpy.props import StringProperty

from .utilities import get


class name_panel_clear_find(Operator):
    bl_idname = 'view3d.name_panel_clear_find'
    bl_label = 'Clear Find'
    bl_description = 'Clear the find field'


    def execute(self, context):

        get.panel.options(context).find = ''

        return {'FINISHED'}


class name_panel_clear_replace(Operator):
    bl_idname = 'view3d.name_panel_clear_replace'
    bl_label = 'Clear Replace'
    bl_description = 'Clear the replace field'


    def execute(self, context):

        get.panel.options(context).replace = ''

        return {'FINISHED'}


class name_panel_options(Operator):
    bl_idname = 'view3d.name_panel_options'
    bl_label = 'Display Options'
    bl_description = 'Adjust display options for the name stack'


    @staticmethod
    def set_height(column, separators):

        for _ in range(0, separators):

            column.separator()


    def check(self, context):

        return True


    def draw(self, context):

        self.option = get.panel.options(context).filters['options']

        split = self.layout.column().split(percentage=0.15)
        column = split.column()
        column.prop(self.option, 'mode', expand=True)

        self.set_height(column, 4)

        self.split = split.column()

        if self.option.mode == 'FILTERS':

            self.display_mode(context)
            self.filters(context)

        else:

            self.extra_options(context)


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
        row.prop(get.panel.options(context), 'location', expand=True)

        row = self.split.row()
        row.prop(self.option, 'pin_active')

        row = self.split.row()
        row.label(text='Panel Width:')
        row.prop(get.preferences(context), 'popup_width', text='')


    def invoke(self, context, event):

        context.window_manager.invoke_popup(self, width=get.preferences(context).popup_width)

        return {'RUNNING_MODAL'}


    def execute(self, context):

        return {'FINISHED'}


class datablock(Operator):
    bl_idname = 'view3d.name_panel_datablock'
    bl_label = 'Datablock Settings'
    bl_description = 'Update the selection\n  Ctrl \N{Rightwards Arrow} Adjust datablock settings\n  Alt \N{Rightwards Arrow} Center view on selected\n  Shift \N{Rightwards Arrow} Add/Remove selection'
    bl_options = {'REGISTER', 'UNDO'}

    object_name = StringProperty()
    target_name = StringProperty()
    identifier = StringProperty()


    def check(self, context):

        return True


    def draw(self, context):

        self.settings(self, context)


    def invoke(self, context, event):

        self.update_selection(context, event)

        self.object = {self.object_name: bpy.data.objects[self.object_name]}
        self.target = {self.target_name: get.panel.target(self, context)}

        if event.alt:
            bpy.ops.view3d.view_selected()

        if event.ctrl:

            context.window_manager.invoke_popup(self, width=get.preferences(context).popup_width)

            return {'RUNNING_MODAL'}

        else:

            return {'FINISHED'}


    def execute(self, context):

        return {'FINISHED'}


    def update_selection(self, context, event):

        option = get.panel.options(context).filters['options']

        objects = context.scene.objects
        object_selected = True if not objects[self.object_name].select else False


        if objects[self.object_name] != objects.active:

            objects.active = objects[self.object_name]
            objects[self.object_name].select = object_selected if event.shift and self.identifier not in {'PoseBone', 'EditBone'} else True

        else:

            objects[self.object_name].select = object_selected if event.shift and self.identifier not in {'PoseBone', 'EditBone'} else True

        if self.identifier not in {'PoseBone', 'EditBone'}:

            if self.identifier == 'ParticleSystem':

                location = objects[self.object_name].particle_system

                if location[self.target_name] != location.active:

                    location.active_index = 0

                    while location[self.target_name] != location.active:

                        location.active_index += 1

            if not event.shift:
                for object in context.visible_objects:
                    if object != objects[self.object_name]:

                        object.select = False

            bpy.ops.object.mode_set(mode='OBJECT')

        elif self.identifier == 'PoseBone':

            bones = objects.active.data.bones
            bone_selected = True if not bones[self.target].select else False

            if bones[self.target] != bones.active:

                bones.active = bones[self.target]
                bones[self.target].select = bone_selected if event.shift else True

            else:

                bones.active.select = bone_selected if event.shift else True

            if not event.shift:
                for bone in context.visible_pose_bones:
                    if bones[bone.name] != bones[self.target]:

                        bone.bone.select = False

        elif self.identifier == 'EditBone':

            bones = objects.active.data.edit_bones
            bone_selected = True if not bones[self.target].select else False

            if bones[self.target] != bones.active:

                bones.active = bones[self.target]
                bones[self.target].select = bone_selected if event.shift else True
                bones[self.target].select_head = bone_selected if event.shift else True
                bones[self.target].select_tail = bone_selected if event.shift else True

            else:

                bones[self.target].select = bone_selected if event.shift else True
                bones[self.target].select_head = bone_selected if event.shift else True
                bones[self.target].select_tail = bone_selected if event.shift else True


            if not event.shift:
                for bone in context.visible_bones:
                    if bone != bones[self.target]:

                        bone.select = False
                        bone.select_head = False
                        bone.select_tail = False


    class settings:


        def __init__(self, operator, context):

            layout = operator.layout

            layout.prop(operator.object[operator.target_name], 'name')

            # getattr(self, operator.type)()


class batch_name(Operator):
    bl_idname = 'wm.batch_name'
    bl_label = 'Batch Name'
    bl_description = 'Batch name datablocks'


    def check(self, context):

        return True


    def draw(self, context):

        pass


    def invoke(self, context, event):

        context.window_manager.invoke_props_dialog(self, width=250)

        return {'RUNNING_MODAL'}


    def execute(self, context):

        return {'FINISHED'}
