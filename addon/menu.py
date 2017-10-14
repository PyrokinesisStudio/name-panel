import bpy

from bpy.types import Menu

from . import interface
from .utilities import get


class name_panel_specials(Menu):
    bl_idname = 'view3d.name_panel_specials'
    bl_label = 'Specials'
    bl_description = 'Tools and Options'


    def draw(self, context): interface.name_panel.specials(self, context)


class namer_search_specials(Menu):
    bl_idname = 'WM_MT_namer_search_specials'
    bl_label = 'Search Options'


    def draw(self, context): interface.namer.search_specials(self, context)


class move_search_specials(Menu):
    bl_idname = 'WM_MT_namer_move_search_specials'
    bl_label = 'Search Options'


    def draw(self, context): interface.namer.move_search_specials(self, context)


class swap_search_specials(Menu):
    bl_idname = 'WM_MT_namer_swap_search_specials'
    bl_label = 'Search Options'


    def draw(self, context): interface.namer.swap_search_specials(self, context)


class operation_specials(Menu):
    bl_idname = 'WM_MT_namer_operation_specials'
    bl_label = 'Name Operation Specials'


    def draw(self, context): interface.namer.operation_specials(self, context)
