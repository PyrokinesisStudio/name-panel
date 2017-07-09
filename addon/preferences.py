import bpy

from bpy.types import AddonPreferences
from bpy.props import *

from .config import defaults
from .utilities import get


class name_panel(AddonPreferences):
    bl_idname = __name__.partition('.')[0]

    default = defaults['preferences']

    remove_item = BoolProperty(
        name = 'Remove Item Panel',
        description = 'Remove the item panel from the properties shelf when this addon is active',
        default = default['remove_item']
    )

    auto_save = BoolProperty(
        name = 'Auto Save Config',
        description = 'Automatically save name panel\'s config file to maintain consistent behavior\nThis is performed when loading and saving blend files\nNote: This does not effect these preferences',
        default = default['auto_save']
    )

    popup_width = IntProperty(
        name = 'Pop-up Width',
        description = 'Width of the pop-up panel in pixels\nYou must save user preferences for this value to be stored',
        min = 200,
        max = 1000,
        subtype = 'PIXEL',
        default = default['popup_width']
    )


    def draw(self, context):

        layout = self.layout

        option = get.preferences(context)

        row = layout.row()
        row.prop(option, 'remove_item')
        row.prop(option, 'auto_save')

        row = layout.row()
        row.label(text='Pop-up Width')
        row.prop(option, 'popup_width')
