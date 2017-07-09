import os
import re

import bpy

from bpy.app.handlers import persistent

from .config import defaults


@persistent
def write_config(void):

    preferences = get.preferences(bpy.context)
    panel = get.panel.options(bpy.context)
    filters = panel.filters['options']

    defaults = {
        'preferences': {
            'remove_item': preferences.remove_item,
            'auto_save': preferences.auto_save,
            'popup_width': preferences.popup_width
        },
        'panel': {
            'location': panel.location,
            'find': '',
            'replace': '',
            'case_sensitive': panel.case_sensitive,
            'regex': panel.regex,
            'filters': {
                'mode': filters.mode,
                'display_mode': filters.display_mode,
                'groups': filters.groups,
                'grease_pencils': filters.grease_pencils,
                'actions': filters.actions,
                'constraints': filters.constraints,
                'modifiers': filters.modifiers,
                'bones': filters.bones,
                'bone_groups': filters.bone_groups,
                'bone_constraints': filters.bone_constraints,
                'shapekeys': filters.shapekeys,
                'vertex_groups': filters.vertex_groups,
                'uv_maps': filters.uv_maps,
                'vertex_colors': filters.vertex_colors,
                'materials': filters.materials,
                'textures': filters.textures,
                'images': filters.images,
                'particle_systems': filters.particle_systems,
                'pin_active': filters.pin_active,
            }
        },
        'namer': {
            'mode': 'TARGET',
            'option_mode': 'PRESETS',
            'target': {
                'mode': 'CONTEXT',
                'effect': 'ALL',
                'object_target': 'BOTH',
                'display_more': False,
                'datablocks': {
                    'cameras': False,
                    'scenes': False,
                    'render_layers': False,
                    'views': False,
                    'keying_sets': False,
                    'empties': False,
                    'materials': False,
                    'nodes': False,
                    'node_labels': False,
                    'node_frames': False,
                    'node_groups': False,
                    'meshes': False,
                    'vertex_groups': False,
                    'uv_maps': False,
                    'vertex_colors': False,
                    'lamps': False,
                    'libraries': False,
                    'screens': False,
                    'images': False,
                    'lattices': False,
                    'curves': False,
                    'surfaces': False,
                    'metaballs': False,
                    'text_curves': False,
                    'fonts': False,
                    'textures': False,
                    'brushes': False,
                    'worlds': False,
                    'groups': False,
                    'shapekeys': False,
                    'constraints': False,
                    'modifiers': False,
                    'texts': False,
                    'speakers': False,
                    'sounds': False,
                    'armatures': False,
                    'bones': False,
                    'bone_groups': False,
                    'pose_libraries': False,
                    'pose_markers': False,
                    'bone_constraints': False,
                    'actions': False,
                    'action_groups': False,
                    'tracks': False,
                    'markers': False,
                    'particles': False,
                    'particle_settings': False,
                    'particle_textures': False,
                    'palletes': False,
                    'grease_pencils': False,
                    'grease_pencil_layers': False,
                    'grease_pencil_pallettes': False,
                    'grease_pencil_pallette_colors': False,
                    'movie_clips': False,
                    'masks': False,
                    'line_sets': False,
                    'line_styles': False,
                    'line_style_modifiers': False,
                    'line_style_textures': False,
                    'sequences': False,
                    'sensors': False,
                    'controllers': False,
                    'actuators': False,
                    'custom_properties': False
                },
                'custom_property_path': ''
            },
            'entry': {
                'mode': 'REPLACE',
                'replace_mode': 'FIND',
                'find': '',
                'case_sensitive': False,
                're': False,
                'position': 0,
                'begin': 0,
                'end': 1,
                'outside': False,
                'before': '',
                'after': '',
                'replace': '',
                'insert_mode': 'PREFIX',
                'insert': '',
                'convert_mode': 'ALL',
                'case_mode': 'NONE',
                'separate_mode': 'NONE',
                'custom': '',
                'move_mode': 'FIND',
                'move_to': 'POSITION',
                'move_case_sensitive': False,
                'move_re': False,
                'move_position': 0,
                'move_before': '',
                'move_after': '',
                'swap_mode': 'FIND',
                'swap_to': 'FIND',
                'swap_find': '',
                'swap_case_sensitive': False,
                'swap_re': False,
                'swap_begin': 0,
                'swap_end': 1,
                'swap_outside': False,
                'swap_before': '',
                'swap_after': ''
            },
            'sort': {
                'mode': 'ASCEND',
                'sort_mode': 'ALL',
                'begin': 0,
                'end': 1,
                'outside': False,
                'starting_point': 'CENTER',
                'axis_3d': 'X',
                'camera': False,
                'axis_2d': 'X',
                'left': 'L',
                'right': 'R',
                'front': 'Fr',
                'back': 'Bk',
                'top': 'Top',
                'bottom': 'Bot',
                'positional_placement': 'SUFFIX',
                'separator': '.',
                'before': '',
                'after': '',
                're': False,
                'case_sensitive': False,
                'position': 0,
                'fallback_mode': 'ASCEND',
                'display_options': False,
                'hierarchy_mode': 'PARENT'
            },
            'count': {
                'mode': 'NUMERIC',
                'placement': 'SUFFIX',
                'position': 0,
                'auto': True,
                'pad': 0,
                'character': '0',
                'separator': '.',
                'start': 1,
                'alphabetic_start': 1,
                'roman_numeral_start': 1,
                'step': 1,
                'uppercase': True
            }
        }
    }

    filepath = os.path.abspath(os.path.join(os.path.dirname(__file__), 'config.py'))
    print('Writing config at: {}'.format(filepath))
    # with open(filepath, 'r+') as default:
    #     default.truncate()
    #     default.write('# Written by name_panel.addon.utilities.write_config\n' + 'defaults = ' + str(defaults))


def check_re(context, name):

        option = get.panel.options(context)

        if option.find:
            if option.regex:
                if option.case_sensitive:
                    return re.search(option.find, name) != None
                else:
                    return re.search(option.find, name, re.I) != None
            else:
                if option.case_sensitive:
                    return re.search(re.escape(option.find), name) != None
                else:
                    return re.search(re.escape(option.find), name, re.I) != None
        else:
            return True


class get:


    def preferences(context):

        return context.user_preferences.addons[__name__.partition('.')[0]].preferences


    class identifier:


        def __new__(self, datablock):

            self.identifiers = [datablock.rna_type.identifier]

            self.check_bases(self, datablock.rna_type.base)

            if self.identifiers[-1] == 'ID':

                identifier = self.identifiers[-2]

            else:

                identifier = self.identifiers[-1]

            return identifier


        def check_bases(self, base):

            if hasattr(base, 'identifier'):

                self.identifiers.append(base.identifier)

            if hasattr(base, 'base'):

                self.check_bases(self, base.base)


    class icon:


        def __new__(self, type):

            icons = {
                'action'
                'meshes': 'OUTLINER_OB_MESH',
                'curves': 'OUTLINER_OB_CURVE',
                'surfaces': 'OUTLINER_OB_SURFACE',
                'metaballs': 'OUTLINER_OB_META',
                'text_curves': 'OUTLINER_OB_FONT',
                'armatures': 'OUTLINER_OB_ARMATURE',
                'lattices': 'OUTLINER_OB_LATTICE',
                'empties': 'OUTLINER_OB_EMPTY',
                'speakers': 'OUTLINER_OB_SPEAKER',
                'cameras': 'OUTLINER_OB_CAMERA',
                'lamps': 'OUTLINER_OB_LAMP',
                'groups': 'GROUP',
                'grease_pencils': 'GREASEPENCIL',
                'grease_pencil_layers': 'LAYER_USED',
                'grease_pencil_pallettes': 'COLOR',
                'grease_pencil_pallette_colors': 'GROUP_VCOL',
                'actions': 'ACTION',
                'action_groups': 'IPO',
                'constraints': 'CONSTRAINT',
                'modifiers': 'MODIFIER',
                'bones': 'BONE_DATA',
                'bone_groups': 'GROUP_BONE',
                'bone_constraints': 'CONSTRAINT_BONE',
                'keying_sets': 'KEYINGSET',
                'pose_libraries': 'POSE_DATA',
                'pose_markers': 'POSE_HLT',
                'tracks': 'NLA',
                'markers': 'MARKER_HLT',
                'shapekeys': 'SHAPEKEY_DATA',
                'vertex_groups': 'GROUP_VERTEX',
                'uv_maps': 'GROUP_UVS',
                'vertex_colors': 'GROUP_VCOL',
                'materials': 'MATERIAL_DATA',
                'textures': 'TEXTURE_DATA',
                'images': 'IMAGE_DATA',
                'nodes': 'NODE_SEL',
                'node_labels': 'NODE',
                'node_frames': 'FULLSCREEN',
                'node_groups': 'NODETREE',
                'particle_systems': 'PARTICLE_DATA',
                'particle_settings': 'MOD_PARTICLES',
                'particle_textures': 'TEXTURE_DATA',
                'line_styles': 'LINE_DATA',
                'line_style_modifiers': 'MODIFIER',
                'line_style_textures': 'TEXTURE_DATA',
                'scenes': 'SCENE_DATA',
                'render_layers': 'RENDERLAYERS',
                'views': 'RESTRICT_RENDER_OFF',
                'brushes': 'BRUSH_DATA',
                'palletes': 'COLOR',
                'sequences': 'SEQUENCE',
                'movie_clips': 'CLIP',
                'sounds': 'SOUND',
                'worlds': 'WORLD_DATA',
                'screens': 'SPLITSCREEN',
                'masks': 'MOD_MASK',
                'fonts': 'FONT_DATA',
                'texts': 'FILE_TEXT',
                'libraries': 'LIBRARY_DATA_DIRECT',
                'custom_properties': 'RNA_ADD',
                'custom_property_paths': 'RNA'
            }

            return icons[type]


        def object(object):

            icons = {
                'MESH': 'OUTLINER_OB_MESH',
                'CURVE': 'OUTLINER_OB_CURVE',
                'SURFACE': 'OUTLINER_OB_SURFACE',
                'META': 'OUTLINER_OB_META',
                'FONT': 'OUTLINER_OB_FONT',
                'ARMATURE': 'OUTLINER_OB_ARMATURE',
                'LATTICE': 'OUTLINER_OB_LATTICE',
                'EMPTY': 'OUTLINER_OB_EMPTY',
                'SPEAKER': 'OUTLINER_OB_SPEAKER',
                'CAMERA': 'OUTLINER_OB_CAMERA',
                'LAMP': 'OUTLINER_OB_LAMP'
            }

            return icons[object.type]


        def modifier(modifier):

            icons = {
                'DATA_TRANSFER': 'MOD_DATA_TRANSFER',
                'MESH_CACHE': 'MOD_MESHDEFORM',
                'NORMAL_EDIT': 'MOD_NORMALEDIT',
                'UV_PROJECT': 'MOD_UVPROJECT',
                'UV_WARP': 'MOD_UVPROJECT',
                'VERTEX_WEIGHT_EDIT': 'MOD_VERTEX_WEIGHT',
                'VERTEX_WEIGHT_MIX': 'MOD_VERTEX_WEIGHT',
                'VERTEX_WEIGHT_PROXIMITY': 'MOD_VERTEX_WEIGHT',
                'ARRAY': 'MOD_ARRAY',
                'BEVEL': 'MOD_BEVEL',
                'BOOLEAN': 'MOD_BOOLEAN',
                'BUILD': 'MOD_BUILD',
                'DECIMATE': 'MOD_DECIM',
                'EDGE_SPLIT': 'MOD_EDGESPLIT',
                'MASK': 'MOD_MASK',
                'MIRROR': 'MOD_MIRROR',
                'MULTIRES': 'MOD_MULTIRES',
                'REMESH': 'MOD_REMESH',
                'SCREW': 'MOD_SCREW',
                'SKIN': 'MOD_SKIN',
                'SOLIDIFY': 'MOD_SOLIDIFY',
                'SUBSURF': 'MOD_SUBSURF',
                'TRIANGULATE': 'MOD_TRIANGULATE',
                'WIREFRAME': 'MOD_WIREFRAME',
                'ARMATURE': 'MOD_ARMATURE',
                'CAST': 'MOD_CAST',
                'CORRECTIVE_SMOOTH': 'MOD_SMOOTH',
                'CURVE': 'MOD_CURVE',
                'DISPLACE': 'MOD_DISPLACE',
                'HOOK': 'HOOK',
                'LAPLACIANSMOOTH': 'MOD_SMOOTH',
                'LAPLACIANDEFORM': 'MOD_MESHDEFORM',
                'LATTICE': 'MOD_LATTICE',
                'MESH_DEFORM': 'MOD_MESHDEFORM',
                'SHRINKWRAP': 'MOD_SHRINKWRAP',
                'SIMPLE_DEFORM': 'MOD_SIMPLEDEFORM',
                'SMOOTH': 'MOD_SMOOTH',
                'WARP': 'MOD_WARP',
                'WAVE': 'MOD_WAVE',
                'CLOTH': 'MOD_CLOTH',
                'COLLISION': 'MOD_PHYSICS',
                'DYNAMIC_PAINT': 'MOD_DYNAMICPAINT',
                'EXPLODE': 'MOD_EXPLODE',
                'FLUID_SIMULATION': 'MOD_FLUIDSIM',
                'OCEAN': 'MOD_OCEAN',
                'PARTICLE_INSTANCE': 'MOD_PARTICLES',
                'PARTICLE_SYSTEM': 'MOD_PARTICLES',
                'SMOKE': 'MOD_SMOKE',
                'SOFT_BODY': 'MOD_SOFT'
            }

            return icons[modifier.type]


        def object_data(object):

            icons = {
                'MESH': 'MESH_DATA',
                'CURVE': 'CURVE_DATA',
                'SURFACE': 'SURFACE_DATA',
                'META': 'META_DATA',
                'FONT': 'FONT_DATA',
                'ARMATURE': 'ARMATURE_DATA',
                'LATTICE': 'LATTICE_DATA',
                'EMPTY': 'IMAGE_DATA',
                'SPEAKER': 'SPEAKER',
                'CAMERA': 'CAMERA_DATA',
                'LAMP': 'LAMP_DATA',
            }

            return icons[object.type]


        def subtype(type):

            icons = {
                'camera': 'OUTLINER_OB_CAMERA',
                'target': 'OBJECT_DATA',
                'subtarget': 'BONE',
                'depth_object': 'OBJECT_DATA',
                'child': 'OBJECT_DATA',
                'action': 'ACTION',
                'object': 'OBJECT_DATA',
                'object_from': 'OBJECT_DATA',
                'object_to': 'OBJECT_DATA',
                'offset_object': 'OBJECT_DATA',
                'start_cap': 'OBJECT_DATA',
                'end_cap': 'OBJECT_DATA',
                'mirror_object': 'OBJECT_DATA',
                'texture_coords_object': 'OBJECT_DATA',
                'origin': 'OBJECT_DATA',
                'start_position_object': 'OBJECT_DATA',
                'image': 'IMAGE_DATA',
                'uv_layer': 'GROUP_UVS',
                'vertex_group': 'GROUP_VERTEX',
                'vertex_group_a': 'GROUP_VERTEX',
                'vertex_group_b': 'GROUP_VERTEX',
                'mask_vertex_group': 'GROUP_VERTEX',
                'mask_texture': 'TEXTURE_DATA',
                'particle_system': 'PARTICLE_DATA'
            }

            return icons[type]


    class panel:


        def options(context):

            location = context.window_manager.name_panel.panel

            if not location:

                location.add().name = 'options'
                location['options'].filters.add().name = 'options'

            return location['options']


        class name_stack:

            types = [
                'groups',
                'grease_pencils',
                'actions',
                'constraints',
                'modifiers',
                'object_data',
                'bone_groups',
                'bones',
                'vertex_groups',
                'shapekeys',
                'uv_maps',
                'vertex_colors',
                'materials',
            ]


            def __new__(self, context):

                option = get.panel.options(context).filters['options']

                if option.display_mode == 'ACTIVE':

                    if context.active_object:

                        stack = {
                            'objects': {},
                            'datablocks': [context.active_object]
                        }

                    else:

                        stack = {}

                elif option.display_mode == 'SELECTED':

                    if context.selected_objects:

                        stack = {
                            'objects': {},
                            'datablocks': self.objects(context, option, context.selected_objects)
                        }

                    elif context.active_object and option.pin_active:

                        stack = {
                            'objects': {},
                            'datablocks': []
                        }

                    else:

                        stack = {}

                else:

                    if context.visible_objects:

                        stack = {
                            'objects': {},
                            'datablocks': self.objects(context, option, context.visible_objects)
                        }

                    elif context.active_object and option.pin_active:

                        stack = {
                            'objects': {},
                            'datablocks': []
                        }

                    else:

                        stack = {}

                if 'datablocks' in stack:
                    if context.active_object and option.pin_active and option.display_mode != 'ACTIVE':

                        stack['datablocks'].insert(0, context.active_object)

                    for object in stack['datablocks']:

                        stack['objects'][object.name] = {
                            'datablock': object,
                            'active': check_re(context, object.name),
                            'types': []
                        }

                        for type in get.panel.name_stack.types:
                            if type not in {'object_data'}:
                                if getattr(option, type):
                                    if getattr(self, type)(context, object):

                                        stack['objects'][object.name]['types'].append(type)

                                        stack['objects'][object.name][type] = {
                                            'datablocks': getattr(get.panel.name_stack, type)(context, object)
                                        }

                                        for datablock in stack['objects'][object.name][type]['datablocks']:

                                            stack['objects'][object.name][type][datablock.name] = {
                                                'datablock': datablock,
                                                'active': check_re(context, datablock.name)
                                            }

                                            if type in {'grease_pencils', 'modifiers', 'bones', 'materials'}:

                                                self.subtypes(context, option, stack, object, type, datablock)

                            else:
                                if object.type == 'EMPTY':
                                    if object.empty_draw_type == 'IMAGE':
                                        if object.data:

                                            stack['objects'][object.name]['types'].append('object_data')

                                            stack['objects'][object.name]['object_data'] = {
                                                'datablocks': [object.data],
                                                object.data.name: {
                                                    'datablock': object.data,
                                                    'active': check_re(context, object.data.name)
                                                }
                                            }

                                else:

                                    stack['objects'][object.name]['types'].append('object_data')

                                    stack['objects'][object.name]['object_data'] = {
                                        'datablocks': [object.data],
                                        object.data.name: {
                                            'datablock': object.data,
                                            'active': check_re(context, object.data.name)
                                        }
                                    }

                return stack


            def objects(context, option, location):

                return sorted([object for object in location if object != context.active_object], key=lambda object: object.name) if option.pin_active else sorted([object for object in location], key=lambda object: object.name)


            def groups(context, object):

                return [group for group in bpy.data.groups for group_object in group.objects if group_object == object] if bpy.data.groups else []


            def grease_pencils(context, object):

                return [object.grease_pencil] if hasattr(object.grease_pencil, 'name') else []


            def actions(context, object):

                return [object.animation_data.action] if hasattr(object.animation_data, 'action') and hasattr(object.animation_data.action, 'name') else []


            def constraints(context, object):

                return [constraint for constraint in object.constraints]


            def modifiers(context, object):

                return [modifier for modifier in object.modifiers]


            def images(context, object):

                return [object.data] if object.type == 'EMPTY' and object.empty_draw_type == 'IMAGE' and hasattr(object, 'data') else []


            def bone_groups(context, object):

                return [bone_group for bone_group in object.pose.bone_groups] if context.mode == 'POSE' else []


            def bones(context, object):

                bones = []

                if object == context.active_object and object.type == 'ARMATURE':

                    option = get.panel.options(context).filters['options']
                    display_mode = get.panel.options(context).filters['options'].display_mode

                    if context.mode == 'POSE':

                        if option.display_mode == 'ACTIVE':

                            bones = [context.active_pose_bone]

                        elif option.display_mode == 'SELECTED':

                            bones = [pose_bone for pose_bone in context.selected_pose_bones if pose_bone != context.active_pose_bone] if option.pin_active else [pose_bone for pose_bone in context.selected_pose_bones]

                        else:

                            bones = [pose_bone for pose_bone in context.visible_pose_bones if pose_bone != context.active_pose_bone] if option.pin_active else [pose_bone for pose_bone in context.visible_pose_bones]

                        if option.pin_active and option.display_mode != 'ACTIVE':

                            bones.insert(0, context.active_pose_bone)

                    elif context.mode == 'EDIT_ARMATURE':

                        if option.display_mode == 'ACTIVE':

                            bones = [context.active_bone]

                        elif option.display_mode == 'SELECTED':

                            bones = [bone for bone in context.selected_bones if bone != context.active_bone] if option.pin_active else [bone for bone in context.selected_bones]

                        else:

                            bones = [bone for bone in context.visible_bones if bone != context.active_bone] if option.pin_active else [bone for bone in context.visible_bones]

                        if option.pin_active and option.display_mode != 'ACTIVE':

                            bones.insert(0, context.active_bone)


                return bones


            def vertex_groups(context, object):

                return [vertex_group for vertex_group in object.vertex_groups] if hasattr(object, 'vertex_groups') else []


            def shapekeys(context, object):

                return [shape_key for shape_key in object.data.shape_keys.key_blocks] if hasattr(object.data, 'shape_keys') and hasattr(object.data.shape_keys, 'key_blocks') else []


            def uv_maps(context, object):

                return [uv_map for uv_map in object.data.uv_textures] if object.type == 'MESH' else []


            def vertex_colors(context, object):

                return [vertex_color for vertex_color in object.data.vertex_colors] if object.type == 'MESH' else []


            def materials(context, object):

                return [material_slot.material for material_slot in object.material_slots if material_slot != None]


            def subtypes(context, option, stack, object, type, datablock):

                if type == 'grease_pencils':

                    stack['objects'][object.name][type][datablock.name]['grease_pencil_layers'] = {
                        'datablocks': [layer for layer in datablock.layers]
                    }

                    for layer in stack['objects'][object.name][type][datablock.name]['grease_pencil_layers']['datablocks']:

                        stack['objects'][object.name][type][datablock.name]['grease_pencil_layers'][layer.info] = {
                            'datablock': layer,
                            'active': check_re(context, layer.info)
                        }

                if type == 'modifiers':

                    if option.particle_systems:
                        if datablock.type == 'PARTICLE_SYSTEM':

                            stack['objects'][object.name][type][datablock.name]['particle_system'] = {
                                datablock.particle_system.name: {
                                    'datablock': datablock.particle_system,
                                    'active': check_re(context, datablock.particle_system.name)
                                }
                            }

                            stack['objects'][object.name][type][datablock.name]['particle_system'][datablock.particle_system.name]['particle_settings'] = {
                                datablock.particle_system.settings.name: {
                                    'datablock': datablock.particle_system.settings,
                                    'active': check_re(context, datablock.particle_system.settings.name)
                                }
                            }

                            if option.textures and context.scene.render.engine == 'CYCLES':

                                stack['objects'][object.name][type][datablock.name]['particle_system'][datablock.particle_system.name]['particle_settings'][datablock.particle_system.settings.name]['textures'] = {
                                    'datablocks': [texture_slot.texture for texture_slot in datablock.particle_system.settings.texture_slots if texture_slot != None]
                                }

                                for texture in stack['objects'][object.name][type][datablock.name]['particle_system'][datablock.particle_system.name]['particle_settings'][datablock.particle_system.settings.name]['textures']['datablocks']:

                                    stack['objects'][object.name][type][datablock.name]['particle_system'][datablock.particle_system.name]['particle_settings'][datablock.particle_system.settings.name]['textures'][texture.name] = {
                                        'datablock': texture,
                                        'active': check_re(context, texture.name)
                                    }

                if type == 'bones':
                    if option.bones and option.bone_constraints:
                        if object == context.active_object and object.type == 'ARMATURE' and context.mode == 'POSE': # TODO: Account for weight paint

                            stack['objects'][object.name][type][datablock.name]['bone_constraints'] = {
                                'datablocks': [constraint for constraint in datablock.constraints]
                            }

                            for constraint in stack['objects'][object.name][type][datablock.name]['bone_constraints']['datablocks']:

                                stack['objects'][object.name][type][datablock.name]['bone_constraints'][constraint.name] = {
                                    'datablock': constraint,
                                    'active': check_re(context, constraint.name)
                                }

                if type == 'materials':
                    if option.textures and context.scene.render.engine == 'BLENDER_RENDER':

                        stack['objects'][object.name][type][datablock.name]['textures'] = {
                            'datablocks': [texture_slot.texture for texture_slot in datablock.texture_slots if texture_slot != None]
                        }

                        for texture in stack['objects'][object.name][type][datablock.name]['textures']['datablocks']:

                            stack['objects'][object.name][type][datablock.name]['textures'][texture.name] = {
                                'datablock': texture,
                                'active': check_re(context, texture.name)
                            }


        class target:


            def __new__(self, operator, context):

                return getattr(self, operator.identifier)(operator, context)


            def Object(operator, context):

                return bpy.data.objects[operator.target_name]


            def Group(operator, context):

                return bpy.data.groups[operator.target_name]


            def GreasePencil(operator, context):

                return bpy.data.grease_pencils[operator.target_name]


            def GPencilLayer(operator, context):

                return bpy.data.objects[operator.object_name].grease_pencil.layers[operator.target_name]


            def Action(operator, context):

                return bpy.data.actions[operator.target_name]


            def Constraint(operator, context):

                return bpy.data.objects[operator.object_name].constraints[operator.target_name]


            def Modifier(operator, context):

                return bpy.data.objects[operator.object_name].modifiers[operator.target_name]


            def Image(operator, context):

                return bpy.data.images[operator.target_name]


            def BoneGroup(operator, context):

                return bpy.data.objects[operator.object_name].pose.bone_groups[operator.target_name]


            def PoseBone(operator, context):

                return bpy.data.objects[operator.object_name].pose.bones[operator.target_name]


            def EditBone(operator, context):

                return bpy.data.objects[operator.object_name].data.bones[operator.target_name]


            def VertexGroup(operator, context):

                return bpy.data.objects[operator.object_name].vertex_groups[operator.target_name]


            def ShapeKey(operator, context):

                return bpy.data.objects[operator.object_name].shapekeys.key_blocks[operator.target_name]


            def MeshTexturePolyLayer(operator, context):

                return bpy.data.objects[operator.object_name].data.uv_textures[operator.target_name]


            def MeshLoopColorLayer(operator, context):

                return bpy.data.objects[operator.object_name].data.vertex_colors[operator.target_name]


            def Material(operator, context):

                return bpy.data.materials[operator.target_name]


            def Texture(operator, context):

                return bpy.data.textures[operator.texture_name]


            def ParticleSystem(operator, context):

                return bpy.data.objects[operator.object_name].particle_systems.active


            def ParticleSettings(operator, context):

                return bpy.data.particles[operator.target_name]


class update:


    def handlers(remove=False):

        if get.preferences(bpy.context).auto_save:
            if not remove:

                bpy.app.handlers.load_pre.append(write_config)
                bpy.app.handlers.save_post.append(write_config)

            else:

                bpy.app.handlers.load_pre.remove(write_config)
                bpy.app.handlers.save_post.remove(write_config)


    def entry_name(operator, context):

        pass
