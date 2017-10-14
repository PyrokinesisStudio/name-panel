import os
import re
import requests

import bpy
import addon_utils

from bpy.app.handlers import persistent

from .config import default_panels, defaults, remote


@persistent
def keep_session_settings(none):

    preferences = get.preferences(bpy.context)
    panel = get.name_panel.options(bpy.context)
    filters = panel.filters['options']

    defaults['preferences']['location'] = preferences.location
    defaults['preferences']['keep_session_settings'] = preferences.keep_session_settings
    defaults['preferences']['pin_active']= preferences.pin_active
    defaults['preferences']['click_through'] = preferences.click_through
    defaults['preferences']['remove_item_panel'] = preferences.remove_item_panel
    defaults['preferences']['popup_width'] = preferences.popup_width
    defaults['preferences']['separators'] = preferences.separators
    defaults['preferences']['use_last'] = preferences.use_last
    defaults['preferences']['datablock_popup_width'] = preferences.datablock_popup_width
    defaults['preferences']['auto_name_operations'] = preferences.auto_name_operations
    defaults['preferences']['namer_popup_width'] = preferences.namer_popup_width
    defaults['preferences']['update_check'] = preferences.update_check
    defaults['preferences']['update_display_menu'] = preferences.update_display_menu
    defaults['preferences']['update_display_panel'] = preferences.update_display_panel

    defaults['panel']['case_sensitive'] = panel.case_sensitive
    defaults['panel']['regex'] = panel.regex

    defaults['panel']['filters']['mode'] = filters.mode
    defaults['panel']['filters']['display_mode'] = filters.display_mode
    defaults['panel']['filters']['groups'] = filters.groups
    defaults['panel']['filters']['grease_pencils'] = filters.grease_pencils
    defaults['panel']['filters']['actions'] = filters.actions
    defaults['panel']['filters']['constraints'] = filters.constraints
    defaults['panel']['filters']['modifiers'] = filters.modifiers
    defaults['panel']['filters']['bones'] = filters.bones
    defaults['panel']['filters']['bone_groups'] = filters.bone_groups
    defaults['panel']['filters']['bone_constraints'] = filters.bone_constraints
    defaults['panel']['filters']['shapekeys'] = filters.shapekeys
    defaults['panel']['filters']['vertex_groups'] = filters.vertex_groups
    defaults['panel']['filters']['uv_maps'] = filters.uv_maps
    defaults['panel']['filters']['vertex_colors'] = filters.vertex_colors
    defaults['panel']['filters']['materials'] = filters.materials
    defaults['panel']['filters']['textures'] = filters.textures
    defaults['panel']['filters']['images'] = filters.images
    defaults['panel']['filters']['particle_systems'] = filters.particle_systems


class regex:


    def panel_search(context, name):

        option = get.name_panel.options(context)

        if option.find:
            if option.regex:
                if option.case_sensitive: return re.search(option.find, name) != None
                else: return re.search(option.find, name, re.I) != None
            elif option.case_sensitive: return re.search(re.escape(option.find), name) != None
            else: return re.search(re.escape(option.find), name, re.I) != None
        else: return True


class get:


    @classmethod
    def item_panel_poll(cls, context): return (context.space_data and context.active_object)


    @classmethod
    def item_panel_poll_override(cls, context):

        preferences = get.preferences(context)

        return (context.space_data and context.active_object) and not (preferences.location == 'UI' and preferences.remove_item_panel)


    def preferences(context):

        return context.user_preferences.addons[__name__.partition('.')[0]].preferences


    class version:


        def string(bl_info): return '{}.{}'.format(str(bl_info['version'][0]), bl_info['version'][1])


        def remote_string():

            # get remote raw
            # https://raw.githubusercontent.com/proxeIO/name-panel/master/__init__.py
            init_text = requests.get('{}{}/{}/{}/__init__.py'.format(remote['raw'], remote['user'], remote['repo'], remote['branch'])).text

            # get version
            version = re.search(r'\'version\': [ ,\':()1-9A-z]*', init_text).group()
            version = version.split('(')[1][:-2]
            version = version.split(',')[0] + '.' + version.split(',')[1][2:-1]

            return version


        def remote_info(): return requests.get('{}{}/{}/{}/update_info'.format(remote['raw'], remote['user'], remote['repo'], remote['branch'])).text


    class identifier:


        def __new__(self, datablock):

            self.identifiers = [datablock.rna_type.identifier]

            self.check_bases(self, datablock.rna_type.base)

            if self.identifiers[-1] == 'ID': identifier = self.identifiers[-2]
            else: identifier = self.identifiers[-1]
            return identifier


        def check_bases(self, base):

            if hasattr(base, 'identifier'): self.identifiers.append(base.identifier)
            if hasattr(base, 'base'): self.check_bases(self, base.base)


    class icon:


        def __new__(self, type):

            icons = {
                'meshes': 'OUTLINER_OB_MESH',
                'meshes_data': 'OUTLINER_DATA_MESH',
                'curves': 'OUTLINER_OB_CURVE',
                'curves_data': 'OUTLINER_DATA_CURVE',
                'surfaces': 'OUTLINER_OB_SURFACE',
                'surfaces_data': 'OUTLINER_DATA_SURFACE',
                'metaballs': 'OUTLINER_OB_META',
                'metaballs_data': 'OUTLINER_DATA_META',
                'text_curves': 'OUTLINER_OB_FONT',
                'text_curves_data': 'OUTLINER_DATA_FONT',
                'armatures': 'OUTLINER_OB_ARMATURE',
                'armatures_data': 'OUTLINER_DATA_ARMATURE',
                'lattices': 'OUTLINER_OB_LATTICE',
                'lattices_data': 'OUTLINER_DATA_LATTICE',
                'empties': 'OUTLINER_OB_EMPTY',
                'empties_data': 'OUTLINER_DATA_EMPTY',
                'speakers': 'OUTLINER_OB_SPEAKER',
                'speakers_data': 'OUTLINER_DATA_SPEAKER',
                'cameras': 'OUTLINER_OB_CAMERA',
                'cameras_data': 'OUTLINER_DATA_CAMERA',
                'lamps': 'OUTLINER_OB_LAMP',
                'lamps_data': 'OUTLINER_DATA_LAMP',
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
                'line_sets': 'OOPS',
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
                'sensors': 'NONE',
                'actuators': 'NONE',
                'controllers': 'NONE',
                'worlds': 'WORLD_DATA',
                'screens': 'SPLITSCREEN',
                'masks': 'MOD_MASK',
                'fonts': 'FONT_DATA',
                'texts': 'FILE_TEXT',
                'libraries': 'LIBRARY_DATA_DIRECT',
                'custom_properties': 'RNA_ADD',
                'custom_property_path': 'RNA'}

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
                'LAMP': 'OUTLINER_OB_LAMP'}

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
                'SOFT_BODY': 'MOD_SOFT'}

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
                'LAMP': 'LAMP_DATA'}

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
                'particle_system': 'PARTICLE_DATA'}

            return icons[type]


    class name_panel:


        def options(context):

            location = context.window_manager.name_panel.panel

            if not 'options' in location:
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
                'materials']


            def __new__(self, context):

                option = get.name_panel.options(context).filters['options']

                if option.display_mode == 'ACTIVE':
                    if context.active_object:
                        stack = {
                            'objects': {},
                            'datablocks': [context.active_object]}

                    else:
                        stack = {}

                elif option.display_mode == 'SELECTED':
                    if context.selected_objects:
                        stack = {
                            'objects': {},
                            'datablocks': self.objects(context, option, context.selected_objects)}

                    elif context.active_object and get.preferences(context).pin_active:
                        stack = {
                            'objects': {},
                            'datablocks': []}

                    else:
                        stack = {}

                else:
                    if context.visible_objects:
                        stack = {
                            'objects': {},
                            'datablocks': self.objects(context, option, context.visible_objects)}

                    elif context.active_object and get.preferences(context).pin_active:
                        stack = {
                            'objects': {},
                            'datablocks': []}

                    else:
                        stack = {}

                if 'datablocks' in stack:
                    if context.active_object and get.preferences(context).pin_active and option.display_mode != 'ACTIVE': stack['datablocks'].insert(0, context.active_object)
                    for object in stack['datablocks']:
                        stack['objects'][object.name] = {
                            'datablock': object,
                            'active': regex.panel_search(context, object.name),
                            'types': []}

                        for type in get.name_panel.name_stack.types:
                            if type != 'object_data':
                                if getattr(option, type):
                                    if getattr(self, type)(context, object):
                                        stack['objects'][object.name]['types'].append(type)

                                        stack['objects'][object.name][type] = {
                                            'datablocks': getattr(get.name_panel.name_stack, type)(context, object)}

                                        for datablock in stack['objects'][object.name][type]['datablocks']:
                                            if datablock:
                                                stack['objects'][object.name][type][datablock.name] = {
                                                    'datablock': datablock,
                                                    'active': regex.panel_search(context, datablock.name)}

                                                if type in {'grease_pencils', 'modifiers', 'bones', 'materials'}: self.subtypes(context, option, stack, object, type, datablock)

                            elif object.type == 'EMPTY':
                                if object.empty_draw_type == 'IMAGE':
                                    if object.data:
                                        stack['objects'][object.name]['types'].append('object_data')

                                        stack['objects'][object.name]['object_data'] = {
                                            'datablocks': [object.data],
                                            object.data.name: {
                                                'datablock': object.data,
                                                'active': regex.panel_search(context, object.data.name)}}

                            else:
                                stack['objects'][object.name]['types'].append('object_data')

                                stack['objects'][object.name]['object_data'] = {
                                    'datablocks': [object.data],
                                    object.data.name: {
                                        'datablock': object.data,
                                        'active': regex.panel_search(context, object.data.name)}}

                return stack


            def objects(context, option, location): return sorted([object for object in location if object != context.active_object], key=lambda object: object.name) if get.preferences(context).pin_active else sorted([object for object in location], key=lambda object: object.name)


            def groups(context, object): return [group for group in bpy.data.groups for group_object in group.objects if group_object == object] if bpy.data.groups else []


            def grease_pencils(context, object): return [object.grease_pencil] if hasattr(object.grease_pencil, 'name') else []


            def actions(context, object): return [object.animation_data.action] if hasattr(object.animation_data, 'action') and hasattr(object.animation_data.action, 'name') else []


            def constraints(context, object): return [constraint for constraint in object.constraints]


            def modifiers(context, object): return [modifier for modifier in object.modifiers]


            def images(context, object): return [object.data] if object.type == 'EMPTY' and object.empty_draw_type == 'IMAGE' and hasattr(object, 'data') else []


            def bone_groups(context, object):

                if object.type == 'ARMATURE':
                    object = context.active_object if object == context.active_object else object

                    return [bone_group for bone_group in object.pose.bone_groups]

                else: return []


            def bones(context, object):

                bones = []

                if object == context.active_object and object.type == 'ARMATURE':
                    option = get.name_panel.options(context).filters['options']
                    display_mode = get.name_panel.options(context).filters['options'].display_mode

                    if context.mode == 'POSE':
                        if option.display_mode == 'ACTIVE':
                            bones = [context.active_pose_bone]

                        elif option.display_mode == 'SELECTED':
                            bones = [pose_bone for pose_bone in context.selected_pose_bones if pose_bone != context.active_pose_bone] if get.preferences(context).pin_active else [pose_bone for pose_bone in context.selected_pose_bones]

                        else:
                            bones = [pose_bone for pose_bone in context.visible_pose_bones if pose_bone != context.active_pose_bone] if get.preferences(context).pin_active else [pose_bone for pose_bone in context.visible_pose_bones]

                        if get.preferences(context).pin_active and option.display_mode != 'ACTIVE':
                            bones.insert(0, context.active_pose_bone)

                    elif context.mode == 'EDIT_ARMATURE':
                        if option.display_mode == 'ACTIVE':
                            bones = [context.active_bone]

                        elif option.display_mode == 'SELECTED':
                            bones = [bone for bone in context.selected_bones if bone != context.active_bone] if get.preferences(context).pin_active else [bone for bone in context.selected_bones]

                        else:
                            bones = [bone for bone in context.visible_bones if bone != context.active_bone] if get.preferences(context).pin_active else [bone for bone in context.visible_bones]

                        if get.preferences(context).pin_active and option.display_mode != 'ACTIVE':
                            bones.insert(0, context.active_bone)

                return bones


            def vertex_groups(context, object): return [vertex_group for vertex_group in object.vertex_groups] if hasattr(object, 'vertex_groups') else []


            def shapekeys(context, object): return [shape_key for shape_key in object.data.shape_keys.key_blocks] if hasattr(object.data, 'shape_keys') and hasattr(object.data.shape_keys, 'key_blocks') else []


            def uv_maps(context, object): return [uv_map for uv_map in object.data.uv_textures] if object.type == 'MESH' else []


            def vertex_colors(context, object): return [vertex_color for vertex_color in object.data.vertex_colors] if object.type == 'MESH' else []


            def materials(context, object): return [material_slot.material for material_slot in object.material_slots if material_slot != None]


            def subtypes(context, option, stack, object, type, datablock):

                if type == 'grease_pencils':
                    stack['objects'][object.name][type][datablock.name]['grease_pencil_layers'] = {
                        'datablocks': [layer for layer in datablock.layers]}

                    for layer in stack['objects'][object.name][type][datablock.name]['grease_pencil_layers']['datablocks']:
                        stack['objects'][object.name][type][datablock.name]['grease_pencil_layers'][layer.info] = {
                            'datablock': layer,
                            'active': regex.panel_search(context, layer.info)}

                if type == 'modifiers':
                    if option.particle_systems:
                        if datablock.type == 'PARTICLE_SYSTEM':
                            stack['objects'][object.name][type][datablock.name]['particle_system'] = {
                                datablock.particle_system.name: {
                                    'datablock': datablock.particle_system,
                                    'active': regex.panel_search(context, datablock.particle_system.name)}}

                            stack['objects'][object.name][type][datablock.name]['particle_system'][datablock.particle_system.name]['particle_settings'] = {
                                datablock.particle_system.settings.name: {
                                    'datablock': datablock.particle_system.settings,
                                    'active': regex.panel_search(context, datablock.particle_system.settings.name)}}

                            if option.textures and context.scene.render.engine == 'CYCLES':
                                stack['objects'][object.name][type][datablock.name]['particle_system'][datablock.particle_system.name]['particle_settings'][datablock.particle_system.settings.name]['textures'] = {
                                    'datablocks': [texture_slot.texture for texture_slot in datablock.particle_system.settings.texture_slots if texture_slot != None]}

                                for texture in stack['objects'][object.name][type][datablock.name]['particle_system'][datablock.particle_system.name]['particle_settings'][datablock.particle_system.settings.name]['textures']['datablocks']:

                                    stack['objects'][object.name][type][datablock.name]['particle_system'][datablock.particle_system.name]['particle_settings'][datablock.particle_system.settings.name]['textures'][texture.name] = {
                                        'datablock': texture,
                                        'active': regex.panel_search(context, texture.name)}

                if type == 'bones':
                    if option.bones and option.bone_constraints:
                        if object == context.active_object and object.type == 'ARMATURE' and context.mode == 'POSE': # TODO: account for weight paint mode and and any active pose bone in it

                            stack['objects'][object.name][type][datablock.name]['bone_constraints'] = {
                                'datablocks': [constraint for constraint in datablock.constraints]}

                            for constraint in stack['objects'][object.name][type][datablock.name]['bone_constraints']['datablocks']:
                                stack['objects'][object.name][type][datablock.name]['bone_constraints'][constraint.name] = {
                                    'datablock': constraint,
                                    'active': regex.panel_search(context, constraint.name)}

                if type == 'materials':
                    if option.textures and context.scene.render.engine == 'BLENDER_RENDER':
                        stack['objects'][object.name][type][datablock.name]['textures'] = {
                            'datablocks': [texture_slot.texture for texture_slot in datablock.texture_slots if texture_slot != None]}

                        for texture in stack['objects'][object.name][type][datablock.name]['textures']['datablocks']:
                            stack['objects'][object.name][type][datablock.name]['textures'][texture.name] = {
                                'datablock': texture,
                                'active': regex.panel_search(context, texture.name)}


        class target:


            def __new__(self, operator, context): return getattr(self, operator.identifier)(operator, context)


            def Object(operator, context): return context.active_object


            def Mesh(operator, context): return context.active_object.data


            def Curve(operator, context): return context.active_object.data


            def MetaBall(operator, context): return context.active_object.data


            def Armature(operator, context): return context.active_object.data


            def Lattice(operator, context): return context.active_object.data


            def Empty(operator, context): return context.active_object.data


            def Speaker(operator, context): return context.active_object.data


            def Camera(operator, context): return context.active_object.data


            def Lamp(operator, context): return context.active_object.data


            def Group(operator, context): return bpy.data.groups[operator.target_name]


            def GreasePencil(operator, context): return context.active_object.grease_pencil


            def GPencilLayer(operator, context): return context.active_object.grease_pencil.layers[operator.target_name]


            def Action(operator, context): return context.active_object.animation_data.action


            def Constraint(operator, context): return context.active_object.constraints[operator.target_name]


            def Modifier(operator, context): return context.active_object.modifiers[operator.target_name]


            def Image(operator, context): return context.active_object.data


            def BoneGroup(operator, context): return context.active_object.pose.bone_groups[operator.target_name]


            def PoseBone(operator, context): return context.active_pose_bone


            def EditBone(operator, context): return context.active_bone


            def VertexGroup(operator, context): return context.active_object.vertex_groups[operator.target_name]


            def ShapeKey(operator, context): return context.active_object.data.shape_keys.key_blocks[operator.target_name]


            def MeshTexturePolyLayer(operator, context): return context.active_object.data.uv_textures[operator.target_name]


            def MeshLoopColorLayer(operator, context): return context.active_object.data.vertex_colors[operator.target_name]


            def Material(operator, context): return context.active_object.materials[operator.target_name]


            def Texture(operator, context): return bpy.data.textures[operator.texture_name]


            def ParticleSystem(operator, context): return context.active_object.particle_systems[operator.target_name]


            def ParticleSettings(operator, context): return bpy.data.particles[operator.target_name]


    class namer:

        catagories = {
            'Objects': [
                'meshes',
                'curves',
                'surfaces',
                'metaballs',
                'text_curves',
                'armatures',
                'lattices',
                'empties',
                'speakers',
                'cameras',
                'lamps'],
            'Objects Data': [
                'meshes_data',
                'curves_data',
                'surfaces_data',
                'metaballs_data',
                'text_curves_data',
                'armatures_data',
                'lattices_data',
                'empties_data',
                'speakers_data',
                'cameras_data',
                'lamps_data'],
            'Object Related': [
                'groups',
                'constraints',
                'modifiers',
                'vertex_groups',
                'uv_maps',
                'vertex_colors',
                'shapekeys',
                'bones',
                'bone_groups',
                'bone_constraints',
                'materials'],
            'Grease Pencil': [
                'grease_pencils',
                'grease_pencil_layers',
                'grease_pencil_pallettes',
                'grease_pencil_pallette_colors'],
            'Animation': [
                'actions',
                'action_groups',
                'keying_sets',
                'pose_libraries',
                'pose_markers',
                'tracks',
                'markers'],
            'Node': [
                'nodes',
                'node_labels',
                'node_frames',
                'node_groups'],
            'Particle': [
                'particle_systems',
                'particle_settings'],
            'Freestyle': [
                'line_sets',
                'line_styles',
                'line_style_modifiers'],
            'Scene': [
                'scenes',
                'render_layers',
                'views'],
            'Image & Brush': [
                'images',
                'brushes',
                'textures',
                'palletes'],
            'Sequence': [
                'sequences',
                'movie_clips',
                'sounds'],
            'Game Engine': [
                'sensors',
                'controllers',
                'actuators'],
            'Misc': [
                'worlds',
                'screens',
                'masks',
                'fonts',
                'texts',
                'libraries']}
            # 'Custom Properties': [
            #     'custom_properties',
            #     'custom_property_path',
            # ]


        def options(context):

            location = context.window_manager.name_panel.namer

            if not 'options' in location:
                location.add().name = 'options'
                location['options'].targeting.add().name = 'options'
                location['options'].naming.add().name = 'options'
                location['options'].sorting.add().name = 'options'
                location['options'].counting.add().name = 'options'

            if not location['options'].naming['options'].operations: location['options'].naming['options'].operations.add().name = 'Default'
            return location['options']


        def operation_name(operation):

            if operation.operation_options_mode not in {'CONVERT', 'TRANSFER'}:
                mode = '{}_mode'.format(operation.operation_options_mode.lower())
                filler = ' at ' if mode == 'insert_mode' and operation.insert_mode == 'POSITION' else ' '

                if mode in {'replace_mode', 'move_mode', 'swap_mode'} and getattr(operation, mode) == 'FIND': secondary = filler + 'Found'
                else: secondary = filler + getattr(operation, mode).title()
            elif operation.operation_options_mode == 'CONVERT':

                secondary = ''

                if operation.case_mode != 'NONE': secondary = ' Case'
                if operation.separate_mode != 'NONE':
                    if secondary != '': secondary += ' & Separators'
                    else: secondary = ' Separators'
            else: secondary = ''
            return operation.operation_options_mode.title() + secondary


    class datablock:


        def options(context):

            location = get.preferences(context).datablock

            if not 'panel' in location:
                location.add().name = 'panel'

                for panel in default_panels:
                    collection = getattr(location['panel'], panel[0].lower())
                    bl_label = getattr(bpy.types, panel[1]).bl_label
                    collection.add().name = panel[1]
                    collection[panel[1]].id = panel[1]
                    collection[panel[1]].label = bl_label
                    collection[panel[1]].hidden = False
                    collection[panel[1]].collapsed = True


            return location['panel']


        def contexts(scene, context):

            items = [
                ('RENDER', 'Render', '', 'SCENE', 0),
                ('RENDER_LAYER', 'Render layers', '', 'RENDERLAYERS', 1),
                ('SCENE', 'Scene', '', 'SCENE_DATA', 2),
                ('WORLD', 'World', '', 'WORLD_DATA', 3)]

            if context.active_object:

                items.append(('OBJECT', 'Object', '', 'OBJECT_DATA', 4))
                items.append(('CONSTRAINT', 'Constraint', '', 'CONSTRAINT', 5))

                if context.active_object.type in {'CURVE', 'LATTICE', 'MESH', 'SURFACE', 'FONT'}: items.append(('MODIFIER', 'Modifier', '', 'MODIFIER', 6))
                if context.active_object.type in {'CURVE', 'SURFACE', 'FONT'}: items.append(('DATA', 'Data', '', 'CURVE_DATA', 7))
                else: items.append(('DATA', 'Data', '', '{}_DATA'.format(context.active_object.type), 7))
                if context.active_object.type in {'CURVE', 'MESH', 'META', 'SURFACE', 'FONT'}: items.append(('MATERIAL', 'Material', '', 'MATERIAL_DATA', 8))

            items.append(('TEXTURE', 'Texture', '', 'TEXTURE_DATA', 9))

            if context.active_object:
                if context.active_object.type == 'MESH': items.append(('PARTICLES', 'Particles', '', 'PARTICLE_DATA', 10))

                items.append(('PHYSICS', 'Physics', '', 'PHYSICS', 11))

            return items


class update:


    class check:


        def __init__(self, bl_info):

            current_version = get.version.string(bl_info)

            if self.connection():
                if current_version != self.version(bl_info):
                    get.preferences(bpy.context).update_ready = True
                    # update
                    pass
                else:
                    # dont update
                    pass
            else:
                # cannot get update info
                pass


        @staticmethod
        def version(bl_info):
            current = get.version.string(bl_info)
            latest = get.version.remote_string()

            if current == latest: return current
            return latest


        @staticmethod
        def connection():

            try:
                requests.get(remote['api'])
                return True
            except Exception as e:
                # debug
                print('')
                print(e)
                print('')
                return False


    def handlers(remove=False):

        if get.preferences(bpy.context).keep_session_settings:
            if not remove:
                bpy.app.handlers.load_pre.append(keep_session_settings)
                bpy.app.handlers.save_post.append(keep_session_settings)

            else:
                bpy.app.handlers.load_pre.remove(keep_session_settings)
                bpy.app.handlers.save_post.remove(keep_session_settings)


    def item_panel_poll(restore=False):

        if restore: bpy.types.VIEW3D_PT_view3d_name.poll = get.item_panel_poll
        else: bpy.types.VIEW3D_PT_view3d_name.poll = get.item_panel_poll_override


    def prop_item_panel_poll(scene, context):

        if get.preferences(context).remove_item_panel: bpy.types.VIEW3D_PT_view3d_name.poll = get.item_panel_poll_override
        else: bpy.types.VIEW3D_PT_view3d_name.poll = get.item_panel_poll


    def selection(operator, context, event):

        option = get.name_panel.options(context).filters['options']

        objects = context.scene.objects

        if operator.identifier not in {'PoseBone', 'EditBone'}:
            object_selected = True if not objects[operator.object_name].select else False

            if objects[operator.object_name] != objects.active:
                objects.active = objects[operator.object_name]
                objects[operator.object_name].select = object_selected if event.shift else True

                bpy.ops.object.mode_set(mode='OBJECT')

            else: objects[operator.object_name].select = object_selected if event.shift else True

            if not event.shift:
                for object in objects:
                    if object != objects[operator.object_name]:
                        object.select = False

        if operator.identifier == 'PoseBone':
            bones = objects.active.data.bones
            bone_selected = True if not bones[operator.target_name].select else False

            if bones[operator.target_name] != bones.active:
                bones.active = bones[operator.target_name]
                bones[operator.target_name].select = bone_selected if event.shift else True

            else: bones.active.select = bone_selected if event.shift else True
            if not event.shift:
                for bone in context.visible_pose_bones:
                    if bones[bone.name] != bones[operator.target_name]:
                        bone.bone.select = False

        elif operator.identifier == 'EditBone':
            bones = objects.active.data.edit_bones
            bone_selected = True if not bones[operator.target_name].select else False

            if bones[operator.target_name] != bones.active:
                bones.active = bones[operator.target_name]
                bones[operator.target_name].select = bone_selected if event.shift else True
                bones[operator.target_name].select_head = bone_selected if event.shift else True
                bones[operator.target_name].select_tail = bone_selected if event.shift else True

            else:
                bones[operator.target_name].select = bone_selected if event.shift else True
                bones[operator.target_name].select_head = bone_selected if event.shift else True
                bones[operator.target_name].select_tail = bone_selected if event.shift else True

            if not event.shift:
                for bone in context.visible_bones:
                    if bone != bones[operator.target_name]:
                        bone.select = False
                        bone.select_head = False
                        bone.select_tail = False


    def operation_name(operator, context):

        naming = get.namer.options(context).naming['options']
        active_operation = naming.operations[naming.active_index]
        active_operation.name = get.namer.operation_name(active_operation)


    def filter_options(operator, context):

        option = get.name_panel.options(context).filters['options']

        toggles = [
            'groups',
            'grease_pencils',
            'actions',
            'constraints',
            'modifiers',
            'bones',
            'bone_groups',
            'bone_constraints',
            'shapekeys',
            'vertex_groups',
            'uv_maps',
            'vertex_colors',
            'materials',
            'textures',
            'images',
            'particle_systems']

        if option.toggle_all:
            for toggle in toggles: setattr(option, toggle, True)
        else:
            for toggle in toggles: setattr(option, toggle, False)


    def target_options(operator, context):

        option = get.namer.options(context).targeting['options']

        if option.toggle_objects:
            for target in get.namer.catagories['Objects']: setattr(option, target, True)
        else:
            for target in get.namer.catagories['Objects']: setattr(option, target, False)
        if option.toggle_objects_data:
            for target in get.namer.catagories['Objects Data']: setattr(option, target, True)
        else:
            for target in get.namer.catagories['Objects Data']: setattr(option, target, False)
