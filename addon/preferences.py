import bpy

from bpy.types import PropertyGroup, AddonPreferences
from bpy.props import *

from .config import defaults
from .utilities import get


class render_options(PropertyGroup):

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


class render_layers_options(PropertyGroup):

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


class scene_options(PropertyGroup):

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


class world_options(PropertyGroup):

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


class object_options(PropertyGroup):

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


class constraints_options(PropertyGroup):

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


class modifiers_options(PropertyGroup):

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


class mesh_options(PropertyGroup):

    default = defaults['preferences']['datablock']['mesh']

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


class curve_options(PropertyGroup):

    default = defaults['preferences']['datablock']['curve']

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


class metaball_options(PropertyGroup):

    default = defaults['preferences']['datablock']['metaball']

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


class armature_options(PropertyGroup):

    default = defaults['preferences']['datablock']['armature']

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


class lattice_options(PropertyGroup):

    default = defaults['preferences']['datablock']['lattice']

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


class empty_options(PropertyGroup):

    default = defaults['preferences']['datablock']['empty']

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


class speaker_options(PropertyGroup):

    default = defaults['preferences']['datablock']['speaker']

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


class camera_options(PropertyGroup):

    default = defaults['preferences']['datablock']['camera']

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


class lamp_options(PropertyGroup):

    default = defaults['preferences']['datablock']['lamp']

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


class material_options(PropertyGroup):

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


class texture_options(PropertyGroup):

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


class particles_options(PropertyGroup):

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


class physics_options(PropertyGroup):

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


class datablock_options(PropertyGroup):

    default = defaults['preferences']['datablock']

    context = EnumProperty(
        name = 'Context',
        description = 'Type of active data to display and edit',
        items = get.datablock.contexts)

    render = CollectionProperty(
        name = 'Render',
        type = render_options)

    render_layers = CollectionProperty(
        name = 'Render Layers',
        type = render_layers_options)

    scene = CollectionProperty(
        name = 'Scene',
        type = scene_options)

    world = CollectionProperty(
        name = 'World',
        type = world_options)

    object = CollectionProperty(
        name = 'Object',
        type = object_options)

    constraints = CollectionProperty(
        name = 'Constraints',
        type = constraints_options)

    modifiers = CollectionProperty(
        name = 'Modifiers',
        type = modifiers_options)

    mesh = CollectionProperty(
        name = 'Mesh',
        type = mesh_options)

    curve = CollectionProperty(
        name = 'Curve',
        type = curve_options)

    metaball = CollectionProperty(
        name = 'Metaball',
        type = metaball_options)

    armature = CollectionProperty(
        name = 'Armature',
        type = armature_options)

    lattice = CollectionProperty(
        name = 'Lattice',
        type = lattice_options)

    empty = CollectionProperty(
        name = 'Empty',
        type = empty_options)

    speaker = CollectionProperty(
        name = 'Speaker',
        type = speaker_options)

    camera = CollectionProperty(
        name = 'Camera',
        type = camera_options)

    lamp = CollectionProperty(
        name = 'Lamp',
        type = lamp_options)

    material = CollectionProperty(
        name = 'Material',
        type = material_options)

    texture = CollectionProperty(
        name = 'Texture',
        type = texture_options)

    particles = CollectionProperty(
        name = 'Particles',
        type = particles_options)

    physics = CollectionProperty(
        name = 'Physics',
        type = physics_options)


class name_panel(AddonPreferences):
    bl_idname = __name__.partition('.')[0]

    default = defaults['preferences']

    mode = EnumProperty(
        name = 'Mode',
        description = 'Mode',
        items = [
            ('GENERAL', 'General', 'Adjust general preferences'),
            ('PANEL', 'Name Panel', 'Adjust preferences related to the name stack'),
            ('NAMER', 'Namer', 'Adjust preferences related to namer')],
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
        description = 'Do not activate the pop-up when clicking a datablock icon',
        default = default['click_through'])

    remove_item = BoolProperty(
        name = 'Remove Item Panel',
        description = 'Remove the item panel from the properties shelf when this addon is active',
        default = default['remove_item'])

    popup_width = IntProperty(
        name = 'Width',
        description = 'Width of the pop-up panels in pixels',
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
        type = datablock_options)


    def draw(self, context):

        web_links = [
            ('Thread', ''),
            ('Blender Market', ''),
            ('Github', ''),
            ('Report Bug', ''),
            ('Donate', '')]

        self.preference = get.preferences(context)

        row = self.layout.row()
        row.prop(self.preference, 'mode', expand=True)

        getattr(self, self.preference.mode.lower())(context)

        row = self.layout.row(align=True)
        row.scale_y = 1.5
        for name, url in web_links:
            row.operator('wm.url_open', text=name).url = url


    def general(self, context):

        box = self.layout.box()

        row = box.row()
        row.prop(self.preference, 'keep_session_settings')


    def panel(self, context):

        box = self.layout.box()

        row = box.row()
        row.label(text='Location:')
        row.prop(self.preference, 'location', expand=True)

        row = box.row()
        row.prop(self.preference, 'pin_active')
        row.prop(self.preference, 'remove_item')

        row = box.row()
        row.prop(self.preference, 'click_through')

        row = box.row()
        row.label(text='Pop-up Width:')
        row.prop(self.preference, 'popup_width', text='')

        row = box.row()
        row.label(text='Separators:')
        row.prop(self.preference, 'separators', text='')


    def namer(self, context):

        box = self.layout.box()

        row = box.row()
        row.prop(self.preference, 'use_last')
        row.prop(self.preference, 'auto_name_operations')

        row = box.row()
        row.label(text='Namer Pop-up Width:')
        row.prop(self.preference, 'namer_popup_width')
