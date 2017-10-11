import bpy

from bpy.types import Operator
from bpy.props import StringProperty, BoolProperty, EnumProperty

from . import interface
from .utilities import get, update
from .config import defaults


class clear_find(Operator):
    bl_idname = 'view3d.name_panel_clear_find'
    bl_label = 'Clear Find'
    bl_description = 'Clear the find field'


    def execute(self, context):

        get.name_panel.options(context).find = ''

        return {'FINISHED'}


class clear_replace(Operator):
    bl_idname = 'view3d.name_panel_clear_replace'
    bl_label = 'Clear Replace'
    bl_description = 'Clear the replace field'


    def execute(self, context):

        get.name_panel.options(context).replace = ''

        return {'FINISHED'}


class options(Operator):
    bl_idname = 'view3d.name_panel_options'
    bl_label = 'Display Options'
    bl_description = 'Adjust display options for the name stack'


    def check(self, context):
        return True


    def draw(self, context):
        interface.name_panel.options(self, context)


    def invoke(self, context, event):

        context.window_manager.invoke_popup(self, width=get.preferences(context).popup_width)

        return {'RUNNING_MODAL'}


    def execute(self, context):
        return {'FINISHED'}


class datablock_settings(Operator):
    bl_idname = 'wm.datablock_settings'
    bl_label = 'Datablock Settings'
    bl_description = 'Adjust datablock settings\n  Ctrl \N{Rightwards Arrow} Display pop-up\n  Alt \N{Rightwards Arrow} Center view on selected\n  Shift \N{Rightwards Arrow} Add/Remove selection'
    bl_options = {'REGISTER', 'UNDO'}

    click_through = BoolProperty(
        name = 'Click Through',
        description = 'Do not activate the pop-up when clicking',
        default = False)

    context_override = StringProperty(
        name = 'Context',
        description = 'Context to load',
        default = 'render')

    object_name = StringProperty(
        name = 'Object',
        description = 'Base object',
        default = '')

    target_name = StringProperty(
        name = 'Target',
        description = 'Target datablock',
        default = '')

    identifier = StringProperty(
        name = 'Identifier',
        description = 'RNA type identifier for the target datablock',
        default = '')


    def check(self, context):
        return True


    def draw(self, context):
        interface.datablock(self, context)


    def invoke(self, context, event):

        if self.object_name:
            update.selection(self, context, event)

            if event.alt:
                bpy.ops.view3d.view_selected()

            if self.click_through:
                self.click_through = False
                if event.ctrl:
                    context.window_manager.invoke_popup(self, width=get.preferences(context).datablock_popup_width)
                    return {'RUNNING_MODAL'}
                else: return {'FINISHED'}
            elif event.ctrl: return {'FINISHED'}
            else:
                context.window_manager.invoke_popup(self, width=get.preferences(context).datablock_popup_width)
                return {'RUNNING_MODAL'}

        else:
            context.window_manager.invoke_popup(self, width=get.preferences(context).datablock_popup_width)
        return {'RUNNING_MODAL'}


    def execute(self, context):
        return {'FINISHED'}


class namer(Operator):
    bl_idname = 'wm.namer'
    bl_label = 'Namer'
    bl_description = 'Batch name datablocks'


    def check(self, context):
        return True


    def draw(self, context):
        interface.namer(self, context)


    def invoke(self, context, event):

        self.area_type = context.area.type

        context.window_manager.invoke_props_dialog(self, width=get.preferences(context).namer_popup_width)

        return {'RUNNING_MODAL'}


    def execute(self, context):
        return {'FINISHED'}


class operation_add(Operator):
    bl_idname = 'wm.namer_operation_add'
    bl_label = 'Add'
    bl_description = 'Add another name operation to the list'
    bl_options = {'INTERNAL'}


    def execute(self, context):

        naming = get.namer.options(context).naming['options']

        if naming.operations:
            prior_operation = naming.operations[naming.active_index]
            active_index = len(naming.operations) - 1

            prior_operation.name = get.namer.operation_name(prior_operation)
            naming.operations.add().name = get.namer.operation_name(prior_operation)

            active_index += 1

            if get.preferences(context).use_last:
                options = [option for option in defaults['namer']['operation']]

                for option in options:
                    setattr(naming.operations[active_index], option, getattr(prior_operation, option))

            else:
                naming.operations[active_index].name = 'Default'

            naming.active_index = active_index

        else:
            naming.operations.add().name = 'Default'
            naming.active_index = 0

        return {'FINISHED'}


class operation_remove(Operator):
    bl_idname = 'wm.namer_operation_remove'
    bl_label = 'Remove'
    bl_description = 'Remove active name operation from the list\n  Alt \N{Rightwards Arrow} to clear all)'
    bl_options = {'INTERNAL'}

    all = BoolProperty()


    def invoke(self, context, event):

        self.all = True if event.alt else False
        self.execute(context)

        return {'FINISHED'}


    def execute(self, context):

        naming = get.namer.options(context).naming['options']

        if len(naming.operations):
            if not self.all:
                naming.operations.remove(naming.active_index)
                naming.active_index -= 1 if naming.active_index != 0 else 0

            else:
                naming.active_index = 0
                naming.operations.clear()


class operation_rename_active(Operator):
    bl_idname = 'wm.namer_operation_rename_active'
    bl_label = 'Rename Active'
    bl_description = 'Automatically rename active name operation'
    bl_options = {'INTERNAL'}


    def execute(self, context):

        naming = get.namer.options(context).naming['options']
        operation = naming.operations[naming.active_index]

        operation.name = get.namer.operation_name(operation)

        return {'FINISHED'}


class operation_rename_all(Operator):
    bl_idname = 'wm.namer_operation_rename_all'
    bl_label = 'Rename All'
    bl_description = 'Automatically rename all name operations'
    bl_options = {'INTERNAL'}


    def execute(self, context):

        naming = get.namer.options(context).naming['options']

        for operation in naming.operations: operation.name = get.namer.operation_name(operation)
        return {'FINISHED'}


class operation_move(Operator):
    bl_idname = 'wm.namer_operation_move'
    bl_label = 'Move'
    bl_description = 'Move active name operation'
    bl_options = {'INTERNAL'}

    up = BoolProperty()


    def execute(self, context):

        naming = get.namer.options(context).naming['options']

        if self.up:
            naming.operations.move(naming.active_index, naming.active_index - 1)
            naming.active_index -= 1 if naming.active_index > 0 else 0

        else:
            naming.operations.move(naming.active_index, naming.active_index + 1)
            naming.active_index += 1 if naming.active_index < len(naming.operations) - 1 else 0

        return {'FINISHED'}
