import bpy

from bpy.types import PropertyGroup, AddonPreferences
from bpy.props import *

from . import interface

from .config import defaults
from .utilities import get, update


class render_context(PropertyGroup):

    default = defaults['preferences']['datablock']['render']

    id = StringProperty()

    label = StringProperty(
        name = 'Label',
        description = 'Name to display in the box panel header',
        default = default['label'])

    hidden = BoolProperty(
        name = 'Hide',
        description='Hide this panel in the datablock popup',
        default = default['hidden'])

    collapsed = BoolProperty(
        name = 'Collapse',
        description = 'Callapse this box panel',
        default = default['collapsed'])


class render_layer_context(PropertyGroup):

    default = defaults['preferences']['datablock']['render_layers']

    id = StringProperty()

    label = StringProperty(
        name = 'Label',
        description = 'Name to display in the box panel header',
        default = default['label'])

    hidden = BoolProperty(
        name = 'Hide',
        description='Hide this panel in the datablock popup',
        default = default['hidden'])

    collapsed = BoolProperty(
        name = 'Collapse',
        description = 'Callapse this box panel',
        default = default['collapsed'])


class scene_context(PropertyGroup):

    default = defaults['preferences']['datablock']['scene']

    id = StringProperty()

    label = StringProperty(
        name = 'Label',
        description = 'Name to display in the box panel header',
        default = default['label'])

    hidden = BoolProperty(
        name = 'Hide',
        description='Hide this panel in the datablock popup',
        default = default['hidden'])

    collapsed = BoolProperty(
        name = 'Collapse',
        description = 'Callapse this box panel',
        default = default['collapsed'])


class world_context(PropertyGroup):

    default = defaults['preferences']['datablock']['world']

    id = StringProperty()

    label = StringProperty(
        name = 'Label',
        description = 'Name to display in the box panel header',
        default = default['label'])

    hidden = BoolProperty(
        name = 'Hide',
        description='Hide this panel in the datablock popup',
        default = default['hidden'])

    collapsed = BoolProperty(
        name = 'Collapse',
        description = 'Callapse this box panel',
        default = default['collapsed'])


class object_context(PropertyGroup):

    default = defaults['preferences']['datablock']['object']

    id = StringProperty()

    label = StringProperty(
        name = 'Label',
        description = 'Name to display in the box panel header',
        default = default['label'])

    hidden = BoolProperty(
        name = 'Hide',
        description='Hide this panel in the datablock popup',
        default = default['hidden'])

    collapsed = BoolProperty(
        name = 'Collapse',
        description = 'Callapse this box panel',
        default = default['collapsed'])


class constraint_context(PropertyGroup):

    default = defaults['preferences']['datablock']['constraints']

    id = StringProperty()

    label = StringProperty(
        name = 'Label',
        description = 'Name to display in the box panel header',
        default = default['label'])

    hidden = BoolProperty(
        name = 'Hide',
        description='Hide this panel in the datablock popup',
        default = default['hidden'])

    collapsed = BoolProperty(
        name = 'Collapse',
        description = 'Callapse this box panel',
        default = default['collapsed'])


class modifier_context(PropertyGroup):

    default = defaults['preferences']['datablock']['modifiers']

    id = StringProperty()

    label = StringProperty(
        name = 'Label',
        description = 'Name to display in the box panel header',
        default = default['label'])

    hidden = BoolProperty(
        name = 'Hide',
        description='Hide this panel in the datablock popup',
        default = default['hidden'])

    collapsed = BoolProperty(
        name = 'Collapse',
        description = 'Callapse this box panel',
        default = default['collapsed'])


class data_context(PropertyGroup):

    default = defaults['preferences']['datablock']['data']

    id = StringProperty()

    label = StringProperty(
        name = 'Label',
        description = 'Name to display in the box panel header',
        default = default['label'])

    hidden = BoolProperty(
        name = 'Hide',
        description='Hide this panel in the datablock popup',
        default = default['hidden'])

    collapsed = BoolProperty(
        name = 'Collapse',
        description = 'Callapse this box panel',
        default = default['collapsed'])


class bone_context(PropertyGroup):

    default = defaults['preferences']['datablock']['data']

    id = StringProperty()

    label = StringProperty(
        name = 'Label',
        description = 'Name to display in the box panel header',
        default = default['label'])

    hidden = BoolProperty(
        name = 'Hide',
        description='Hide this panel in the datablock popup',
        default = default['hidden'])

    collapsed = BoolProperty(
        name = 'Collapse',
        description = 'Callapse this box panel',
        default = default['collapsed'])


class bone_constraint_context(PropertyGroup):

    default = defaults['preferences']['datablock']['data']

    id = StringProperty()

    label = StringProperty(
        name = 'Label',
        description = 'Name to display in the box panel header',
        default = default['label'])

    hidden = BoolProperty(
        name = 'Hide',
        description='Hide this panel in the datablock popup',
        default = default['hidden'])

    collapsed = BoolProperty(
        name = 'Collapse',
        description = 'Callapse this box panel',
        default = default['collapsed'])


class material_context(PropertyGroup):

    default = defaults['preferences']['datablock']['material']

    id = StringProperty()

    label = StringProperty(
        name = 'Label',
        description = 'Name to display in the box panel header',
        default = default['label'])

    hidden = BoolProperty(
        name = 'Hide',
        description='Hide this panel in the datablock popup',
        default = default['hidden'])

    collapsed = BoolProperty(
        name = 'Collapse',
        description = 'Callapse this box panel',
        default = default['collapsed'])


class texture_context(PropertyGroup):

    default = defaults['preferences']['datablock']['texture']

    id = StringProperty()

    label = StringProperty(
        name = 'Label',
        description = 'Name to display in the box panel header',
        default = default['label'])

    hidden = BoolProperty(
        name = 'Hide',
        description='Hide this panel in the datablock popup',
        default = default['hidden'])

    collapsed = BoolProperty(
        name = 'Collapse',
        description = 'Callapse this box panel',
        default = default['collapsed'])


class particles_context(PropertyGroup):

    default = defaults['preferences']['datablock']['particles']

    id = StringProperty()

    label = StringProperty(
        name = 'Label',
        description = 'Name to display in the box panel header',
        default = default['label'])

    hidden = BoolProperty(
        name = 'Hide',
        description='Hide this panel in the datablock popup',
        default = default['hidden'])

    collapsed = BoolProperty(
        name = 'Collapse',
        description = 'Callapse this box panel',
        default = default['collapsed'])


class physics_context(PropertyGroup):

    default = defaults['preferences']['datablock']['physics']

    id = StringProperty()

    label = StringProperty(
        name = 'Label',
        description = 'Name to display in the box panel header',
        default = default['label'])

    hidden = BoolProperty(
        name = 'Hide',
        description='Hide this panel in the datablock popup',
        default = default['hidden'])

    collapsed = BoolProperty(
        name = 'Collapse',
        description = 'Callapse this box panel',
        default = default['collapsed'])


class datablock_settings(PropertyGroup):

    default = defaults['preferences']['datablock']

    context = EnumProperty(
        name = 'Context',
        description = 'Type of active data to display and edit',
        items = get.datablock.contexts)

    render = CollectionProperty(
        name = 'Render',
        type = render_context)

    render_layer = CollectionProperty(
        name = 'Render Layer',
        type = render_layer_context)

    scene = CollectionProperty(
        name = 'Scene',
        type = scene_context)

    world = CollectionProperty(
        name = 'World',
        type = world_context)

    object = CollectionProperty(
        name = 'Object',
        type = object_context)

    constraint = CollectionProperty(
        name = 'Constraint',
        type = constraint_context)

    modifier = CollectionProperty(
        name = 'Modifier',
        type = modifier_context)

    data = CollectionProperty(
        name = 'Data',
        type = data_context)

    bone = CollectionProperty(
        name = 'Bone',
        type = bone_context)

    bone_constraint = CollectionProperty(
        name = 'Bone Constraint',
        type = bone_constraint_context)

    material = CollectionProperty(
        name = 'Material',
        type = material_context)

    texture = CollectionProperty(
        name = 'Texture',
        type = texture_context)

    particles = CollectionProperty(
        name = 'Particles',
        type = particles_context)

    physics = CollectionProperty(
        name = 'Physics',
        type = physics_context)


class name_panel(AddonPreferences):
    bl_idname = __name__.partition('.')[0]

    default = defaults['preferences']

    mode = EnumProperty(
        name = 'Mode',
        description = 'Adjust preferences',
        items = [
            ('GENERAL', 'General', ''),
            ('PANEL', 'Panel', ''),
            ('DATABLOCK', 'Properties', ''),
            ('NAMER', 'Namer', ''),
            ('HOTKEY', 'Hotkeys', ''),
            ('UPDATES', 'Updates', '')],
        default = default['mode'])

    keep_session_settings = BoolProperty(
        name = 'Keep Session Settings',
        description = 'Keep common settings values related to this addon consistent across blend files\n  Note: resets on exit',
        default = default['keep_session_settings'])

    location = EnumProperty(
        name = 'Location',
        description = 'The 3D view shelf to use for the name panel',
        items = [
            ('TOOLS', 'Tool Shelf', 'Places the name panel in the tool shelf under the tab labeled \'Name\''),
            ('UI', 'Property Shelf', 'Places the name panel in the property shelf')],
        default = default['location'])

    pin_active = BoolProperty(
        name = 'Pin Active',
        description = 'Keep the active object/bone at the top of the name stack',
        default = default['pin_active'])

    click_through = BoolProperty(
        name = 'Click Through',
        description = 'Do not activate the pop-up when clicking a name stack icon',
        default = default['click_through'])

    remove_item_panel = BoolProperty(
        name = 'Remove Item Panel',
        description = 'Remove the item panel from the properties shelf when the name panel is there',
        update = update.prop_item_panel_poll,
        default = default['remove_item_panel'])

    popup_width = IntProperty(
        name = 'Width',
        description = 'Width of the filters pop-up panel in pixels',
        min = 200,
        max = 1000,
        subtype = 'PIXEL',
        default = default['popup_width'])

    separators = IntProperty(
        name = 'Separators',
        description = 'Number of separators between objects in the name stack',
        min = 0,
        max = 10,
        default = default['separators'])

    use_last = BoolProperty(
        name = 'Use Last Settings',
        description = 'When adding a naming operation use the previous settings',
        default = default['use_last'])

    datablock_popup_width = IntProperty(
        name = 'Width',
        description = 'Width of the datablock properties pop-up panel in pixels',
        min = 200,
        max = 1000,
        subtype = 'PIXEL',
        default = default['datablock_popup_width'])

    auto_name_operations = BoolProperty(
        name = 'Auto Name Operations',
        description = 'Automatically name operation entries based on operation modes',
        default = default['auto_name_operations'])

    namer_popup_width = IntProperty(
        name = 'Width',
        description = 'Width of the pop-up panel in pixels',
        min = 200,
        max = 1000,
        subtype = 'PIXEL',
        default = default['namer_popup_width'])

    datablock = CollectionProperty(
        name = 'Datablock',
        type = datablock_settings)

    update_check = BoolProperty(
        name = 'Check at startup',
        description = 'Check at blender startup for updates',
        default = default['update_check'])

    update_display_menu = BoolProperty(
        name = 'Display menu notification',
        description = 'Display update information in the name panel specials menu',
        default = default['update_display_menu'])

    update_display_panel = BoolProperty(
        name = 'Display panel notification',
        description = 'Display update information in the name panel',
        default = default['update_display_panel'])

    update_ready = BoolProperty(
        name = 'update_ready',
        description = 'Used internally to determine if an update is ready',
        default = False)

    def draw(self, context):

        interface.name_panel.preferences(self, context)
