import bpy

from bpy.types import Panel

from . import interface
from .utilities import get


class tool_shelf(Panel):
    bl_idname = 'view3d.name_panel_tool_shelf'
    bl_space_type = 'VIEW_3D'
    bl_label = 'Name'
    bl_region_type = 'TOOLS'
    bl_category = 'Name'


    @classmethod
    def poll(cls, context):

        return get.preferences(context).location == 'TOOLS'


    def draw(self, context):

        interface.name_panel(self, context)


class property_shelf(Panel):
    bl_idname = 'view3d.name_panel_property_shelf'
    bl_space_type = 'VIEW_3D'
    bl_label = 'Name'
    bl_region_type = 'UI'


    @classmethod
    def poll(cls, context):

        return get.preferences(context).location == 'UI'


    def draw(self, context):

        interface.name_panel(self, context)
