import bpy

from bpy.types import PropertyGroup
from bpy.props import *

from .utilities import update
from .config import defaults


class filter_options(PropertyGroup):

    default = defaults['panel']['filters']

    mode = EnumProperty(
        name = 'Mode',
        description = 'Mode',
        items = [
            ('FILTERS', 'Filters', ''),
            ('OPTIONS', 'Options', ''),
        ],
        default = default['mode']
    )

    display_mode = EnumProperty(
        name = 'Display Mode',
        description = 'Display mode for object(s) in the name stack',
        items = [
            ('ACTIVE', 'Active', ''),
            ('SELECTED', 'Selected', ''),
            ('VISIBLE', 'Visible', '')
        ],
        default = default['display_mode']
    )

    toggle_all = BoolProperty(
        name = 'Toggle All',
        description = 'Toggle display state of all datablocks',
        update = update.filter_options,
        default = default['toggle_all']
    )

    groups = BoolProperty(
        name = 'Groups',
        description = 'Display object groups',
        default = default['groups']
    )

    grease_pencils = BoolProperty(
        name = 'Grease Pencils',
        description = 'Display object grease pencils',
        default = default['grease_pencils']
    )

    actions = BoolProperty(
        name = 'Actions',
        description = 'Display object actions',
        default = default['actions']
    )

    constraints = BoolProperty(
        name = 'Constraints',
        description = 'Display object constraints',
        default = default['constraints']
    )

    modifiers = BoolProperty(
        name = 'Modifiers',
        description = 'Display object modifiers',
        default = default['modifiers']
    )

    bones = BoolProperty(
        name = 'Bones',
        description = 'Display armature bones',
        default = default['bones']
    )

    bone_groups = BoolProperty(
        name = 'Bone Groups',
        description = 'Display armature bone groups',
        default = default['bone_groups']
    )

    bone_constraints = BoolProperty(
        name = 'Bone Constraints',
        description = 'Display pose bone constraints',
        default = default['bone_constraints']
    )

    shapekeys = BoolProperty(
        name = 'Shapekeys',
        description = 'Display object shapekeys',
        default = default['shapekeys']
    )

    vertex_groups = BoolProperty(
        name = 'Vertex Groups',
        description = 'Display mesh vertex groups',
        default = default['vertex_groups']
    )

    uv_maps = BoolProperty(
        name = 'UV Maps',
        description = 'Display mesh uv maps',
        default = default['uv_maps']
    )

    vertex_colors = BoolProperty(
        name = 'Vertex Colors',
        description = 'Display mesh vertex colors',
        default = default['vertex_colors']
    )

    materials = BoolProperty(
        name = 'Materials',
        description = 'Display object materials',
        default = default['materials']
    )

    textures = BoolProperty(
        name = 'Textures',
        description = 'Display textures',
        default = default['textures']
    )

    images = BoolProperty(
        name = 'Images',
        description = 'Display images',
        default = default ['images']
    )

    particle_systems = BoolProperty(
        name = 'Particle Systems',
        description = 'Display particle systems',
        default = default['particle_systems']
    )


class operation_options(PropertyGroup):

    default = defaults['namer']['operation']

    operation_options_mode = EnumProperty(
         name = 'Operation Options',
         description = 'Type of operation to perform',
         items = [
            ('REPLACE', 'Replace', 'Replace characters'),
            ('INSERT', 'Insert', 'Insert characters'),
            ('CONVERT', 'Convert', 'Convert characters'),
            ('MOVE', 'Move', 'Move characters'),
            ('SWAP', 'Swap', 'Swap characters'),
            ('TRANSFER', 'Transfer', 'Transfer names'),
         ],
         update = update.operation_name,
         default = default['operation_options_mode']
    )

    replace_mode = EnumProperty(
        name = 'Replace Mode',
        description = 'Type of replace operation',
        items = [
            ('BETWEEN', 'Between', 'Replace the characters between these strings'),
            ('AFTER', 'After', 'Replace characters after this string'),
            ('BEFORE', 'Before', 'Replace the characters before this string'),
            ('POSITION', 'Position', 'Replace text at this position'),
            ('FIND', 'Find', 'Replace this string'),
            ('ALL', 'All', 'Replace entire name'),
        ],
        update = update.operation_name,
        default = default['replace_mode']
    )

    find = StringProperty(
        name = 'Find',
        description = 'Find this string',
        default = default['find']
    )

    case_sensitive = BoolProperty(
        name = 'Case Sensitive',
        description = 'Case sensitive matching',
        default = default['case_sensitive']
    )

    re = BoolProperty(
        name = 'Regular Expressions',
        description = 'Evaluate regular expressions',
        default = default['re']
    )

    position = IntProperty(
        name = 'Positon',
        description = 'The position in number of characters',
        default = default['position']
    )

    begin = IntProperty(
        name = 'Begin',
        description = 'The beginning position to start in number of characters',
        default = default['begin']
    )

    end = IntProperty(
        name = 'End',
        description = 'The ending position to stop in number of characters',
        default = default['end']
    )

    outside = BoolProperty(
        name = 'Outside',
        description = 'Replace outside of this position',
        default = default['outside']
    )

    before = StringProperty(
        name = 'Before',
        description = 'Before this string',
        default = default['before']
    )

    after = StringProperty(
        name = 'After',
        description = 'After this string',
        default = default['after']
    )

    replace = StringProperty(
         name = 'Replace',
         description = 'The replacement string',
         default = default['replace']
    )

    insert_mode = EnumProperty(
        name = 'Insert Mode',
        description = 'Type of insert operation',
        items = [
            ('BETWEEN', 'Between', 'Between strings'),
            ('AFTER', 'After', 'After string'),
            ('BEFORE', 'Before', 'Before string'),
            ('POSITION', 'Position', 'At position'),
            ('SUFFIX', 'Suffix', 'As suffix'),
            ('PREFIX', 'Prefix', 'As prefix'),
        ],
        update = update.operation_name,
        default = default['insert_mode']
    )

    insert = StringProperty(
        name = 'Insert',
        description = 'The string to insert',
        default = default['insert']
    )

    convert_mode = EnumProperty(
        name = 'Convert Mode',
        description = 'Type of conversion operation',
        items = [
            ('BETWEEN', 'Between', 'Convert the characters between these strings'),
            ('AFTER', 'After', 'Convert characters after this string'),
            ('BEFORE', 'Before', 'Convert the characters before this string'),
            ('POSITION', 'Position', 'Convert text at this position'),
            ('FIND', 'Find', 'Convert this string'),
            ('ALL', 'All', 'Convert entire name'),
        ],
        default = default['convert_mode']
    )

    case_mode = EnumProperty(
        name = 'Case Mode',
        description = 'Type of case conversion',
        items = [
            ('DORKIFY', 'DoRkIfY', 'By DoRkIfIeInG the names'),
            ('TITLE', 'Title', 'By capatilizing the first character of each word'),
            ('CAPATILIZE', 'Capatilize', 'By capatilizing the first character of the name'),
            ('SWAP', 'sWAP', 'By swapping the case'),
            ('LOWER', 'lower', 'To lower'),
            ('UPPER', 'UPPER', 'To upper'),
            ('NONE', 'No Conversion', 'By doing nothing'),
        ],
        update = update.operation_name,
        default = default['case_mode']
    )

    separate_mode = EnumProperty(
        name = 'Separate Mode',
        description = 'Type of separator conversion',
        items = [
            ('CUSTOM', 'Custom', 'Into custom character(s)'),
            ('SPACE', 'Space', 'Into spaces'),
            ('DASH', 'Dash', 'Into dashes'),
            ('UNDERSCORE', 'Underscore', 'Into underscores'),
            ('NONE', 'No Conversion', 'By doing nothing'),
        ],
        update = update.operation_name,
        default = default['separate_mode']
    )

    custom = StringProperty(
        name = 'Custom',
        description = 'Custom separator entry',
        default = default['custom']
    )

    move_mode = EnumProperty(
        name = 'Move Mode',
        description = 'What you wish to move',
        items = [
            ('BETWEEN', 'Between', 'Move characters between srings'),
            ('AFTER', 'After', 'Move characters after string'),
            ('BEFORE', 'Before', 'Move characters before string'),
            ('POSITION', 'Position', 'Move string at position'),
            ('FIND', 'Find', 'Find string to move'),
        ],
        update = update.operation_name,
        default = default['move_mode']
    )

    move_to = EnumProperty(
        name = 'Move To',
        description = 'Where you want it to move',
        items = [
            ('BETWEEN', 'Between', 'Move between strings'),
            ('AFTER', 'After', 'Move after string'),
            ('BEFORE', 'Before', 'Move before string'),
            ('POSITION', 'Position', 'Move to posiiton'),
        ],
        update = update.operation_name,
        default = default['move_to']
    )

    move_case_sensitive = BoolProperty(
        name = 'Case Sensitive',
        description = 'Case sensitive matching',
        default = default['move_case_sensitive']
    )

    move_re = BoolProperty(
        name = 'Regular Expressions',
        description = 'Evaluate regular expressions',
        default = default['move_re']
    )

    move_position = IntProperty(
        name = 'Positon',
        description = 'The position to move to, in number of characters',
        default = default['move_position']
    )

    move_before = StringProperty(
        name = 'Before',
        description = 'Before this string',
        default = default['move_before']
    )

    move_after = StringProperty(
        name = 'After',
        description = 'After this string',
        default = default['move_after']
    )

    swap_mode = EnumProperty(
        name = 'Swap Mode',
        description = 'What you wish to swap',
        items = [
            ('BETWEEN', 'Between', 'Text between strings'),
            ('AFTER', 'After', 'Text after string'),
            ('BEFORE', 'Before', 'Text before string'),
            ('POSITION', 'Position', 'Text at position'),
            ('FIND', 'Find', 'Swap with string'),
        ],
        update = update.operation_name,
        default = default['swap_mode']
    )

    swap_to = EnumProperty(
        name = 'Swap To',
        description = 'What you wish to swap with',
        items = [
            ('BETWEEN', 'Between', 'Swap with text between strings'),
            ('AFTER', 'After', 'Swap with text after string'),
            ('BEFORE', 'Before', 'Swap with text before string'),
            ('POSITION', 'Position', 'Swap with text at position'),
            ('FIND', 'Find', 'Swap with string'),
        ],
        update = update.operation_name,
        default = default['swap_to']
    )

    swap_find = StringProperty(
        name = 'Swap Find',
        description = 'Swap with this string',
        default = default['swap_find']
    )

    swap_case_sensitive = BoolProperty(
        name = 'Case Sensitive',
        description = 'Case sensitive matching',
        default = default['swap_case_sensitive']
    )

    swap_re = BoolProperty(
        name = 'Regular Expressions',
        description = 'Evaluate regular expressions',
        default = default['swap_re']
    )

    swap_begin = IntProperty(
        name = 'Begin',
        description = 'The beginning position to swap with, in number of characters',
        default = default['swap_begin']
    )

    swap_end = IntProperty(
        name = 'End',
        description = 'The ending position to swap with, in number of characters',
        default = default['swap_end']
    )

    swap_outside = BoolProperty(
        name = 'Outside',
        description = 'Swap outside of this position',
        default = default['swap_outside']
    )

    swap_before = StringProperty(
        name = 'Before',
        description = 'Before this string',
        default = default['swap_before']
    )

    swap_after = StringProperty(
        name = 'After',
        description = 'After this string',
        default = default['swap_after']
    )


class target_options(PropertyGroup):

    default = defaults['namer']['target']

    target_options_mode = EnumProperty(
        name = 'Target Options Mode',
        description = 'Mode',
        items = [
            ('CONTEXT', 'Context', 'Context specific datablock target options'),
            ('GLOBAL', 'Global', 'Generalized datablock target options'),
        ],
        default = default['target_options_mode']
    )

    target_mode = EnumProperty(
        name = 'Target Mode',
        description = 'Mode',
        items = [
            ('ALL', 'All', 'All the designated targets'),
            ('SELECTED', 'Selected', 'The targets that are currently selected when possible'),
            ('SCENE', 'Scene', 'Only targets that are in the current scene when possible'),
            ('VISIBLE', 'Visible', 'The targets that are currently visible when possible'),
        ],
        default = default['target_mode']
    )

    toggle_objects = BoolProperty(
        name = 'Toggle Objects',
        description = 'Enable/Disable all objects',
        update = update.target_options,
        default = default['toggle_objects']
    )


    toggle_objects_data = BoolProperty(
        name = 'Toggle Objects Data',
        description = 'Enable/Disable all objects data',
        update = update.target_options,
        default = default['toggle_objects_data']
    )

    display_more = BoolProperty(
        name = 'More Targets',
        description = 'Display more targets',
        default = default['display_more']
    )

    meshes = BoolProperty(
        name = 'Meshes',
        description = 'Name meshes',
        default = default['datablocks']['meshes']
    )

    meshes_data = BoolProperty(
        name = 'Meshes Data',
        description = 'Name meshes data',
        default = default['datablocks']['meshes_data']
    )

    cameras = BoolProperty(
        name = 'Camera',
        description = 'Name cameras',
        default = default['datablocks']['cameras']
    )

    cameras_data = BoolProperty(
        name = 'Camera Data',
        description = 'Name cameras data',
        default = default['datablocks']['cameras_data']
    )

    scenes = BoolProperty(
        name = 'Scenes',
        description = 'Name scenes',
        default = default['datablocks']['scenes']
    )

    render_layers = BoolProperty(
        name = 'Render Layers',
        description = 'Name render layers',
        default = default['datablocks']['render_layers']
    )

    views = BoolProperty(
        name = 'Views',
        description = 'Name views',
        default = default['datablocks']['views']
    )

    keying_sets = BoolProperty(
        name = 'Keying Sets',
        description = 'Name keying sets',
        default = default['datablocks']['keying_sets']
    )

    empties = BoolProperty(
        name = 'Empties',
        description = 'Name empties',
        default = default['datablocks']['empties']
    )

    empties_data = BoolProperty(
        name = 'Empties Data',
        description = 'Name empties data',
        default = default['datablocks']['empties_data']
    )

    materials = BoolProperty(
        name = 'Materials',
        description = 'Name materials',
        default = default['datablocks']['materials']
    )

    nodes = BoolProperty(
        name = 'Nodes',
        description = 'Name nodes',
        default = default['datablocks']['nodes']
    )

    node_labels = BoolProperty(
        name = 'Node Labels',
        description = 'Name node labels',
        default = default['datablocks']['node_labels']
    )

    node_frames = BoolProperty(
        name = 'Node Frames',
        description = 'Name node frames',
        default = default['datablocks']['node_frames']
    )

    node_groups = BoolProperty(
        name = 'Node Groups',
        description = 'Name node groups',
        default = default['datablocks']['node_groups']
    )

    vertex_groups = BoolProperty(
        name = 'Vertex Groups',
        description = 'Name vertex groups',
        default = default['datablocks']['vertex_groups']
    )

    uv_maps = BoolProperty(
        name = 'UV Maps',
        description = 'Name UV maps',
        default = default['datablocks']['uv_maps']
    )

    vertex_colors = BoolProperty(
        name = 'Vertex Colors',
        description = 'Name vertex colors',
        default = default['datablocks']['vertex_colors']
    )

    lamps = BoolProperty(
        name = 'Lamp',
        description = 'Name lamps',
        default = default['datablocks']['lamps']
    )

    lamps_data = BoolProperty(
        name = 'Lamp Data',
        description = 'Name lamps data',
        default = default['datablocks']['lamps_data']
    )

    libraries = BoolProperty(
        name = 'Libaries',
        description = 'Name libaries',
        default = default['datablocks']['libraries']
    )

    screens = BoolProperty(
        name = 'Screens',
        description = 'Name screens',
        default = default['datablocks']['screens']
    )

    images = BoolProperty(
        name = 'Images',
        description = 'Name images',
        default = default['datablocks']['images']
    )

    lattices = BoolProperty(
        name = 'Lattices',
        description = 'Name lattices',
        default = default['datablocks']['lattices']
    )

    lattices_data = BoolProperty(
        name = 'Lattices Data',
        description = 'Name lattices data',
        default = default['datablocks']['lattices_data']
    )

    curves = BoolProperty(
        name = 'Curves',
        description = 'Name curves',
        default = default['datablocks']['curves']
    )

    curves_data = BoolProperty(
        name = 'Curves Data',
        description = 'Name curves data',
        default = default['datablocks']['curves_data']
    )

    surfaces = BoolProperty(
        name = 'Surfaces',
        description = 'Name surfaces',
        default = default['datablocks']['surfaces']
    )

    surfaces_data = BoolProperty(
        name = 'Surfaces Data',
        description = 'Name surfaces data',
        default = default['datablocks']['surfaces_data']
    )

    metaballs = BoolProperty(
        name = 'Metaballs',
        description = 'Name metaballs',
        default = default['datablocks']['metaballs']
    )

    metaballs_data = BoolProperty(
        name = 'Metaballs Data',
        description = 'Name metaballs data',
        default = default['datablocks']['metaballs_data']
    )

    text_curves = BoolProperty(
        name = 'Text Curves',
        description = 'Name text curves',
        default = default['datablocks']['text_curves']
    )

    text_curves_data = BoolProperty(
        name = 'Text Curves Data',
        description = 'Name text curves data',
        default = default['datablocks']['text_curves_data']
    )

    fonts = BoolProperty(
        name = 'Fonts',
        description = 'Name fonts',
        default = default['datablocks']['fonts']
    )

    textures = BoolProperty(
        name = 'Textures',
        description = 'Name textures',
        default = default['datablocks']['textures']
    )

    brushes = BoolProperty(
        name = 'Brushes',
        description = 'Name brushes',
        default = default['datablocks']['brushes']
    )

    worlds = BoolProperty(
        name = 'Worlds',
        description = 'Name worlds',
        default = default['datablocks']['worlds']
    )

    groups = BoolProperty(
        name = 'Groups',
        description = 'Name groups',
        default = default['datablocks']['groups']
    )

    shapekeys = BoolProperty(
        name = 'Shapekeys',
        description = 'Name shapekeys',
        default = default['datablocks']['shapekeys']
    )

    constraints = BoolProperty(
        name = 'Constraints',
        description = 'Name constraints',
        default = default['datablocks']['constraints']
    )

    modifiers = BoolProperty(
        name = 'Modifiers',
        description = 'Name modifiers',
        default = default['datablocks']['modifiers']
    )

    texts = BoolProperty(
        name = 'Texts',
        description = 'Name texts',
        default = default['datablocks']['texts']
    )

    speakers = BoolProperty(
        name = 'Speakers',
        description = 'Name speakers',
        default = default['datablocks']['speakers']
    )

    speakers_data = BoolProperty(
        name = 'Speakers Data',
        description = 'Name speakers data',
        default = default['datablocks']['speakers_data']
    )

    sounds = BoolProperty(
        name = 'Sounds',
        description = 'Name sounds',
        default = default['datablocks']['sounds']
    )

    armatures = BoolProperty(
        name = 'Armatures',
        description = 'Name armatures',
        default = default['datablocks']['armatures']
    )

    armatures_data = BoolProperty(
        name = 'Armatures Data',
        description = 'Name armatures data',
        default = default['datablocks']['armatures_data']
    )

    bones = BoolProperty(
        name = 'Bones',
        description = 'Name Bones',
        default = default['datablocks']['bones']
    )

    bone_groups = BoolProperty(
        name = 'Bone Groups',
        description = 'Name bone groups',
        default = default['datablocks']['bone_groups']
    )

    pose_libraries = BoolProperty(
        name = 'Pose Libaries',
        description = 'Name pose libraries',
        default = default['datablocks']['pose_libraries']
    )

    pose_markers = BoolProperty(
        name = 'Pose Library Poses',
        description = 'Name pose library poses',
        default = default['datablocks']['pose_markers']
    )

    bone_constraints = BoolProperty(
        name = 'Bone Constraints',
        description = 'Name bone constraints',
        default = default['datablocks']['bone_constraints']
    )

    actions = BoolProperty(
        name = 'Actions',
        description = 'Name actions',
        default = default['datablocks']['actions']
    )

    action_groups = BoolProperty(
        name = 'Action Groups',
        description = 'Name action groups',
        default = default['datablocks']['action_groups']
    )

    tracks = BoolProperty(
        name = 'NLA Tracks',
        description = 'Name NLS tracks',
        default = default['datablocks']['tracks']
    )

    markers = BoolProperty(
        name = 'Timeline Markers',
        description = 'Name timeline markers',
        default = default['datablocks']['markers']
    )

    particle_systems = BoolProperty(
        name = 'Particle Systems',
        description = 'Name particle systems',
        default = default['datablocks']['particle_systems']
    )

    particle_settings = BoolProperty(
        name = 'Particle Settings',
        description = 'Name particle settings',
        default = default['datablocks']['particle_settings']
    )

    particle_textures = BoolProperty(
        name = 'Particle Textures',
        description = 'Name particle textures',
        default = default['datablocks']['particle_textures']
    )

    palletes = BoolProperty(
        name = 'Palletes',
        description = 'Name palletes',
        default = default['datablocks']['palletes']
    )

    grease_pencils = BoolProperty(
        name = 'Grease Pencils',
        description = 'Name grease pencils',
        default = default['datablocks']['grease_pencils']
    )

    grease_pencil_layers = BoolProperty(
        name = 'Grease Pencil Layers',
        description = 'Name grease pencil layers',
        default = default['datablocks']['grease_pencil_layers']
    )

    grease_pencil_pallettes = BoolProperty(
        name = 'Grease Pencil Pallettes',
        description = 'Name grease pencil pallettes',
        default = default['datablocks']['grease_pencil_pallettes']
    )

    grease_pencil_pallette_colors = BoolProperty(
        name = 'Grease Pencil Pallette Colors',
        description = 'Name grease pencil pallette colors',
        default = default['datablocks']['grease_pencil_pallette_colors']
    )

    movie_clips = BoolProperty(
        name = 'Movie Clips',
        description = 'Name movie clips',
        default = default['datablocks']['movie_clips']
    )

    masks = BoolProperty(
        name = 'Masks',
        description = 'Name masks',
        default = default['datablocks']['masks']
    )

    line_sets = BoolProperty(
        name = 'Line Sets',
        description = 'Name line sets',
        default = default['datablocks']['line_sets']
    )

    line_styles = BoolProperty(
        name = 'Line Styles',
        description = 'Name line styles',
        default = default['datablocks']['line_styles']
    )

    line_style_modifiers = BoolProperty(
        name = 'Line Style Modifiers',
        description = 'Name line style modifiers',
        default = default['datablocks']['line_style_modifiers']
    )

    line_style_textures = BoolProperty(
        name = 'Line Style Textures',
        description = 'Name line style textures',
        default = default['datablocks']['line_style_textures']
    )

    sequences = BoolProperty(
        name = 'Sequences',
        description = 'Name sequences',
        default = default['datablocks']['sequences']
    )

    sensors = BoolProperty(
        name = 'Sensors',
        description = 'Name sensors',
        default = default['datablocks']['sensors']
    )

    controllers = BoolProperty(
        name = 'Controllers',
        description = 'Name controllers',
        default = default['datablocks']['controllers']
    )

    actuators = BoolProperty(
        name = 'Actuators',
        description = 'Name actuators',
        default = default['datablocks']['actuators']
    )

    custom_properties = BoolProperty(
        name = 'Custom Properties',
        description = 'Name custom properties',
        default = default['datablocks']['custom_properties']
    )

    custom_property_path = StringProperty(
        name = 'Custom Property Path',
        description = 'RNA path to datablock that is storing the custom properties',
        default = default['custom_property_path']
    )


class name_options(PropertyGroup):

    operations = CollectionProperty(
        type = operation_options,
        name = 'Operations'
    )

    active_index = IntProperty(
        name = 'Active Index'
    )


class sort_options(PropertyGroup):

    default = defaults['namer']['sort']

    sort_options_mode = EnumProperty(
        name = 'Sort Options Mode',
        description = 'Type of sorting to perform',
        items = [
            ('NONE', 'No Sorting', 'Do not sort the names'),
            ('ASCEND', 'Ascending', 'In ascending order'),
            ('DESCEND', 'Descending', 'In descending order'),
            ('POSITION', 'Positional', 'In positional order'),
            ('HIERARCHY', 'Hierarchy', 'In hierarchical order'),
            ('MANUAL', 'Manual', 'By defining the order')
        ],
        default = default['sort_options_mode']
    )

    sort_mode = EnumProperty(
        name = 'Sort Mode',
        description = 'How to sort',
        items = [
            ('ALL', 'Full Name', 'Sort using entire name'),
            ('POSITION', 'Section', 'Sort using a section of the name')
        ],
        default = default['sort_mode']
    )

    begin = IntProperty(
        name = 'Begin',
        description = 'The beginning of the section',
        default = default['begin']
    )

    end = IntProperty(
        name = 'End',
        description = 'The ending of the section',
        default = default['end']
    )

    outside = BoolProperty(
        name = 'Outside',
        description = 'Sort outside of this section',
        default = default['outside']
    )

    axis_3d = EnumProperty(
        name = 'Axis',
        description = 'The primary axis to sort with',
        items = [
            ('X', 'X', 'The X axis'),
            ('Y', 'Y', 'The Y axis'),
            ('Z', 'Z', 'The Z axis'),
        ],
        default = default['axis_3d']
    )

    camera = BoolProperty(
        name = 'Use Camera',
        description = 'Sort using the camera axis orientation',
        default = default['camera']
    )

    axis_2d = EnumProperty(
        name = 'Axis',
        description = 'The primary axis to sort with',
        items = [
            ('X', 'X', 'The X axis'),
            ('Y', 'Y', 'The Y axis'),
        ],
        default = default['axis_2d']
    )

    starting_point = EnumProperty(
        name = 'Starting Point',
        description = 'The position to begin counting',
        items = [
            ('POSITIVE', 'Positive', 'Start from the furthest positive item on the axis'),
            ('NEGATIVE', 'Negative', 'Start from the furthest negative item on the axis'),
            ('ACTIVE', 'Active', 'Start from the active element'),
            ('CENTER', 'Center', 'Start from the view\'s center'),
            ('CURSOR', 'Cursor', 'Start from the cursor'),
        ],
        default = default['starting_point']
    )

    top = StringProperty(
        name = 'Top',
        description = 'The positional tag to use for items in the +Z axis',
        default = default['top']
    )

    bottom = StringProperty(
        name = 'Bottom',
        description = 'The positional tag to use for items in the -Z axis',
        default = default['bottom']
    )

    front = StringProperty(
        name = 'Front',
        description = 'The positional tag to use for items in the +Y axis',
        default = default['front']
    )

    back = StringProperty(
        name = 'back',
        description = 'The positional tag to use for items in the -Y axis',
        default = default['back']
    )

    left = StringProperty(
        name = 'Left',
        description = 'The positional tag to use for items in the +X axis',
        default = default['left']
    )

    right = StringProperty(
        name = 'Right',
        description = 'The positional tag to use for items in the -X axis',
        default = default['right']
    )

    placement = EnumProperty(
        name = 'Placement',
        description = 'Where to place the position tag',
        items = [
            ('PREFIX', 'Prefix', 'As a prefix'),
            ('SUFFIX', 'Suffix', 'As a suffix'),
            ('POSITION', 'Position', 'At this position'),
        ],
        default = default['placement']
    )

    separator = StringProperty(
        name = 'Separator',
        description = 'The separator to use between the name and the positional tag',
        default = default['separator']
    )

    position = IntProperty(
        name = 'Positon',
        description = 'The position in number of characters',
        default = default['position']
    )

    before = StringProperty(
        name = 'Before',
        description = 'Before this string',
        default = default['before']
    )

    after = StringProperty(
        name = 'After',
        description = 'After this string',
        default = default['after']
    )

    re = BoolProperty(
        name = 'Regular Expressions',
        description = 'Evaluate Regular Expressions',
        default = default['re']
    )

    case_sensitive = BoolProperty(
        name = 'Case Sensitive',
        description = 'Case sensitive matching',
        default = default['case_sensitive']
    )

    fallback_mode = EnumProperty(
        name = 'Fallback Mode',
        description = 'Fallback mode where position or hierarchy cannot be detected',
        items = [
            ('NONE', 'No Sorting', 'Do not sort the names'),
            ('ASCEND', 'Ascending', 'In ascending order'),
            ('DESCEND', 'Descending', 'In descending order'),
            ('MANUAL', 'Manual', 'Manually adjust the order'),
        ],
        default = default['fallback_mode']
    )

    display_options = BoolProperty(
        name = 'Display Fallback Options',
        description = 'Display the options for the fallback method',
        default = default['display_options']
    )

    hierarchy_mode = EnumProperty(
        name = 'Hierarchy Mode',
        description = 'The hierarchy order to sort in',
        items = [
            ('PARENT', 'Parent First', 'sort the parent before the child'),
            ('CHILD', 'Child First', 'sort the parent before the child'),
        ],
        default = default['hierarchy_mode']
    )


class count_options(PropertyGroup):

    default = defaults['namer']['count']

    count_options_mode = EnumProperty(
        name = 'Count Options Mode',
        description = 'Type of counting to perform',
        items = [
            ('NONE', 'No Counting', 'Do not count the names'),
            ('NUMERIC', 'Numeric', 'Numbers'),
            ('ALPHABETIC', 'Alphabetic', 'Alphabetics'),
            ('ROMAN_NUMERAL', 'Roman Numeral', 'Roman numerals'),
        ],
        default = default['count_options_mode']
    )

    placement = EnumProperty(
        name = 'Placement',
        description = 'Where to place the count',
        items = [
            ('PREFIX', 'Prefix', 'The beginning of the name'),
            ('SUFFIX', 'Suffix', 'The end of the name'),
            ('POSITION', 'Position', 'A custom position')
        ],
        default = default['placement']
    )

    position = IntProperty(
        name = 'Position',
        description  = 'The position to place the count',
        default = default['position']
    )

    auto = BoolProperty(
        name = 'Auto Pad',
        description = 'Automatically pad the numbering',
        default = default['auto']
    )

    pad = IntProperty(
        name = 'Minimum Padding',
        description = 'The smallest number of pad characters before the count number',
        default = default['pad']
    )

    character = StringProperty(
        name = 'Pad Character',
        description = 'The character to use for padding',
        default = default['character']
    )

    separator = StringProperty(
        name = 'Separator',
        description = 'Separator to use between the name and the count',
        default = default['separator']
    )

    start = IntProperty(
        name = 'Start',
        description = 'Start the count at this value',
        default = default['start']
    )

    step = IntProperty(
        name = 'Step',
        description = 'Step the count by this amount',
        default = default['step']
    )

    uppercase = BoolProperty(
        name = 'Uppercase',
        description = 'Use uppercase characters',
        default = default['uppercase']
    )


class panel_options(PropertyGroup):

    default = defaults['panel']

    user_count = BoolProperty(
        name = 'User Count',
        description = 'Number of times this datablock is referenced',
        default = False
    )

    find = StringProperty(
        name = 'Find',
        description = 'Search filter for the name stack',
        default = default['find']
    )

    replace = StringProperty(
        name = 'Replace',
        description = 'Replace the found text',
        default = default['replace']
    )

    case_sensitive = BoolProperty(
        name = 'Case Sensitive',
        description = 'Enable case sensitive searching',
        default = default['case_sensitive']
    )

    regex = BoolProperty(
        name = 'Regular Expressions',
        description = 'Enable regular expressions',
        default = default['regex']
    )

    filters = CollectionProperty(
        name = 'Filter Options',
        type = filter_options
    )


class namer_options(PropertyGroup):

    default = defaults['namer']

    mode = EnumProperty(
        name = 'Namer Mode',
        description = 'Mode',
        items = [
            ('TARGET', 'Target', 'Choose the targets you wish to name'),
            ('NAME', 'Name', 'Perform naming operations'),
            ('SORT', 'Sort', 'Sorting options'),
            ('COUNT', 'Count', 'Counting options'),
            ('OPTIONS', 'Options', 'Presets and preferences'),
        ],
        default = default['mode']
    )

    options_mode = EnumProperty(
        name = 'Options Mode',
        description = 'Mode',
        items = [
            ('PRESETS', 'Presets', 'Namer presets'),
            ('PREFERENCES', 'Preferences', 'Addon preferences'),
        ],
        default = default['options_mode']
    )

    targeting = CollectionProperty(
        name = 'Targeting',
        type = target_options
    )

    naming = CollectionProperty(
        name = 'Naming',
        type = name_options
    )

    sorting = CollectionProperty(
        name = 'Sorting',
        type = sort_options
    )

    counting = CollectionProperty(
        name = 'Counting',
        type = count_options
    )


class name_panel(PropertyGroup):

        panel = CollectionProperty(
            name = 'Panel',
            type = panel_options
        )

        namer = CollectionProperty(
            name = 'Name',
            type = namer_options
        )
