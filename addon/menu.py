import bpy

from bpy.types import Menu

from .utilities import get


class name_panel_specials(Menu):
    bl_idname = 'view3d.name_panel_specials'
    bl_label = 'Specials'
    bl_description = 'Tools and Options'


    def draw(self, context):

        option = get.panel.options(context)
        layout = self.layout

        layout.label(text='Find & Replace')

        layout.separator()

        layout.prop(option, 'case_sensitive')
        layout.prop(option, 'regex')

        layout.separator()

        layout.label(text='Batch Naming')

        layout.separator()

        # layout.operator('wm.namer', text='Transfer Names')
        # layout.operator('wm.namer', text='Count Names')
        #
        # layout.separator()
        #
        # layout.operator('wm.namer', text='Namer', icon='SORTALPHA')
