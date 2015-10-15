
# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or modify it
#  under the terms of the GNU General Public License as published by the Free
#  Software Foundation; either version 2 of the License, or (at your option)
#  any later version.
#
#  This program is distributed in the hope that it will be useful, but WITHOUT
#  ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
#  FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for
#  more details.
#
#  You should have received a copy of the GNU General Public License along with
#  this program; if not, write to the Free Software Foundation, Inc.,
#  51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

# imports
import bpy
from bpy.types import PropertyGroup
from bpy.props import EnumProperty, BoolProperty, StringProperty, IntProperty

###########
## LISTS ##
###########

# list
class menuList:
  '''
    Contains Lists;
      objects
      modifiers
      constraints
  '''
  # object
  objects = [
    ('ALL', 'All Objects', '', 'OBJECT_DATA', 0),
    ('MESH', 'Mesh', '', 'OUTLINER_OB_MESH', 1),
    ('CURVE', 'Curve', '', 'OUTLINER_OB_CURVE', 2),
    ('SURFACE', 'Surface', '', 'OUTLINER_OB_SURFACE', 3),
    ('META', 'Meta', '', 'OUTLINER_OB_META', 4),
    ('FONT', 'Text', '', 'OUTLINER_OB_FONT', 5),
    ('ARMATURE', 'Armature', '', 'OUTLINER_OB_ARMATURE', 6),
    ('LATTICE', 'Lattice', '', 'OUTLINER_OB_LATTICE', 7),
    ('EMPTY', 'Empty', '', 'OUTLINER_OB_EMPTY', 8),
    ('SPEAKER', 'Speaker', '', 'OUTLINER_OB_SPEAKER', 9),
    ('CAMERA', 'Camera', '', 'OUTLINER_OB_CAMERA', 10),
    ('LAMP', 'Lamp', '', 'OUTLINER_OB_LAMP', 11)
  ]

  # constraint
  constraints = [
    ('ALL', 'All Constraints', '', 'CONSTRAINT', 0),

    # motion tracking
    ('CAMERA_SOLVER', 'Camera Solver', '', 'CONSTRAINT_DATA', 1),
    ('FOLLOW_TRACK', 'Follow Track', '', 'CONSTRAINT_DATA', 2),
    ('OBJECT_SOLVER', 'Object Solver', '', 'CONSTRAINT_DATA', 3),

    # transform
    ('COPY_LOCATION', 'Copy Location', '', 'CONSTRAINT_DATA', 4),
    ('COPY_ROTATION', 'Copy Rotation', '', 'CONSTRAINT_DATA', 5),
    ('COPY_SCALE', 'Copy Scale', '', 'CONSTRAINT_DATA', 6),
    ('COPY_TRANSFORMS', 'Copy Transforms', '', 'CONSTRAINT_DATA', 7),
    ('LIMIT_DISTANCE', 'Limit Distance', '', 'CONSTRAINT_DATA', 8),
    ('LIMIT_LOCATION', 'Limit Location', '', 'CONSTRAINT_DATA', 9),
    ('LIMIT_ROTATION', 'Limit Rotation', '', 'CONSTRAINT_DATA', 10),
    ('LIMIT_SCALE', 'Limit Scale', '', 'CONSTRAINT_DATA', 11),
    ('MAINTAIN_VOLUME', 'Maintain Volume', '', 'CONSTRAINT_DATA', 12),
    ('TRANSFORM', 'Transformation', '', 'CONSTRAINT_DATA', 13),

    # tracking
    ('CLAMP_TO', 'Clamp To', '', 'CONSTRAINT_DATA', 14),
    ('DAMPED_TRACK', 'Damped Track', '', 'CONSTRAINT_DATA', 15),
    ('IK', 'Inverse Kinematics', '', 'CONSTRAINT_DATA', 16),
    ('LOCKED_TRACK', 'Locked Track', '', 'CONSTRAINT_DATA', 17),
    ('SPLINE_IK', 'Spline IK', '', 'CONSTRAINT_DATA', 18),
    ('STRETCH_TO', 'Stretch To', '', 'CONSTRAINT_DATA', 19),
    ('TRACK_TO', 'Track To', '', 'CONSTRAINT_DATA', 20),

    # relationship
    ('ACTION', 'Action', '', 'CONSTRAINT_DATA', 21),
    ('CHILD_OF', 'Child Of', '', 'CONSTRAINT_DATA', 22),
    ('FLOOR', 'Floor', '', 'CONSTRAINT_DATA', 23),
    ('FOLLOW_PATH', 'Follow Path', '', 'CONSTRAINT_DATA', 24),
    ('PIVOT', 'Pivot', '', 'CONSTRAINT_DATA', 25),
    ('RIGID_BODY_JOINT', 'Rigid Body Joint', '', 'CONSTRAINT_DATA', 26),
    ('SHRINKWRAP', 'Shrinkwrap', '', 'CONSTRAINT_DATA', 27)
  ]

  # modifier
  modifiers = [
    ('ALL', 'All Modifiers', '', 'MODIFIER', 0),

    # modify
    ('DATA_TRANSFER', 'Data Transfer', '', 'MOD_DATA_TRANSFER', 1),
    ('MESH_CACHE', 'Mesh Cache', '', 'MOD_MESHDEFORM', 2),
    ('NORMAL_EDIT', 'Normal Edit', '', 'MOD_NORMALEDIT', 3),
    ('UV_PROJECT', 'UV Project', '', 'MOD_UVPROJECT', 4),
    ('UV_WARP', 'UV Warp', '', 'MOD_UVPROJECT', 5),
    ('VERTEX_WEIGHT_EDIT', 'Vertex Weight Edit', '', 'MOD_VERTEX_WEIGHT', 6),
    ('VERTEX_WEIGHT_MIX', 'Vertex Weight Mix', '', 'MOD_VERTEX_WEIGHT', 7),
    ('VERTEX_WEIGHT_PROXIMITY', 'Vertex Weight Proximity', '', 'MOD_VERTEX_WEIGHT', 8),

    # generate
    ('ARRAY', 'Array', '', 'MOD_ARRAY', 9),
    ('BEVEL', 'Bevel', '', 'MOD_BEVEL', 10),
    ('BOOLEAN', 'Boolean', '', 'MOD_BOOLEAN', 11),
    ('BUILD', 'Build', '', 'MOD_BUILD', 12),
    ('DECIMATE', 'Decimate', '', 'MOD_DECIM', 13),
    ('EDGE_SPLIT', 'Edge Split', '', 'MOD_EDGESPLIT', 14),
    ('MASK', 'Mask', '', 'MOD_MASK', 15),
    ('MIRROR', 'Mirror', '', 'MOD_MIRROR', 16),
    ('MULTIRES', 'Multiresolution', '', 'MOD_MULTIRES', 17),
    ('REMESH', 'Remesh', '', 'MOD_REMESH', 18),
    ('SCREW', 'Screw', '', 'MOD_SCREW', 19),
    ('SKIN', 'Skin', '', 'MOD_SKIN', 20),
    ('SOLIDIFY', 'Solidify', '', 'MOD_SOLIDIFY', 21),
    ('SUBSURF', 'Subdivision Surface', '', 'MOD_SUBSURF', 22),
    ('TRIANGULATE', 'Triangulate', '', 'MOD_TRIANGULATE', 23),
    ('WIREFRAME', 'Wireframe', '', 'MOD_WIREFRAME', 24),

    # deform
    ('ARMATURE', 'Armature', '', 'MOD_ARMATURE', 25),
    ('CAST', 'Cast', '', 'MOD_CAST', 26),
    ('CORRECTIVE_SMOOTH', 'Corrective Smooth', '', 'MOD_SMOOTH', 27),
    ('CURVE', 'Curve', '', 'MOD_CURVE', 28),
    ('DISPLACE', 'Displace', '', 'MOD_DISPLACE', 29),
    ('HOOK', 'Hook', '', 'HOOK', 30),
    ('LAPLACIANSMOOTH', 'Laplacian Smooth', '', 'MOD_SMOOTH', 31),
    ('LAPLACIANDEFORM', 'Laplacian Deform', '', 'MOD_MESHDEFORM', 32),
    ('LATTICE', 'Lattice', '', 'MOD_LATTICE', 33),
    ('MESH_DEFORM', 'Mesh Deform', '', 'MOD_MESHDEFORM', 34),
    ('SHRINKWRAP', 'Shrinkwrap', '', 'MOD_SHRINKWRAP', 35),
    ('SIMPLE_DEFORM', 'Simple Deform', '', 'MOD_SIMPLEDEFORM', 36),
    ('SMOOTH', 'Smooth', '', 'MOD_SMOOTH', 37),
    ('WARP', 'Warp', '', 'MOD_WARP', 38),
    ('WAVE', 'Wave', '', 'MOD_WAVE', 39),

    # simulate
    ('CLOTH', 'Cloth', '', 'MOD_CLOTH', 40),
    ('COLLISION', 'Collision', '', 'MOD_PHYSICS', 41),
    ('DYNAMIC_PAINT', 'Dynamic Paint', '', 'MOD_DYNAMICPAINT', 42),
    ('EXPLODE', 'Explode', '', 'MOD_EXPLODE', 43),
    ('FLUID_SIMULATION', 'Fluid Simulation', '', 'MOD_FLUIDSIM', 44),
    ('OCEAN', 'Ocean', '', 'MOD_OCEAN', 45),
    ('PARTICLE_INSTANCE', 'Particle Instance', '', 'MOD_PARTICLES', 46),
    ('PARTICLE_SYSTEM', 'Particle System', '', 'MOD_PARTICLES', 47),
    ('SMOKE', 'Smoke', '', 'MOD_SMOKE', 48),
    ('SOFT_BODY', 'Soft Body', '', 'MOD_SOFT', 49)
  ]

#####################
## PROPERTY GROUPS ##
#####################

# panel
class panel(PropertyGroup):
  '''
    Properties that effect how item panel displays the datablocks within the users current selection.
  '''

  # filters
  filters = BoolProperty(
    name = 'Filters',
    description = 'Show options for whether datablock names are displayed.',
    default = False
  )

  # options
  options = BoolProperty(
    name = 'Options',
    description = 'Show shortcut options next to datablock names.',
    default = False
  )

  # selected
  selected = BoolProperty(
    name = 'Selected',
    description = 'Display all possible object related datablock names within your current selection inside the item panel.',
    default = False
  )

  # groups
  groups = BoolProperty(
    name = 'Groups',
    description = 'Display group name.',
    default = False
  )

  # action
  action = BoolProperty(
    name = 'Action',
    description = 'Display action name.',
    default = False
  )

  # grease pencil
  greasePencil = BoolProperty(
    name = 'Grease Pencil',
    description = 'Display grease pencil and layer names',
    default = False
  )

  # constraints
  constraints = BoolProperty(
    name = 'Constraints',
    description = 'Display constraint names.',
    default = False
  )

  # modifiers
  modifiers = BoolProperty(
    name = 'Modifiers',
    description = 'Display modifier names.',
    default = False
  )

  # bone groups
  boneGroups = BoolProperty(
    name = 'Bone Groups',
    description = 'Display bone group names.',
    default = False
  )

  # bone constraints
  boneConstraints = BoolProperty(
    name = 'Bone Constraints',
    description = 'Display bone constraint names.',
    default = False
  )

  # vertex groups
  vertexGroups = BoolProperty(
    name = 'Vertex Groups',
    description = 'Display vertex group names.',
    default = False
  )

  # shapekeys
  shapekeys = BoolProperty(
    name = 'Shapekeys',
    description = 'Display shapekey names.',
    default = False
  )

  # uvs
  uvs = BoolProperty(
    name = 'UV\'s',
    description = 'Display uv names.',
    default = False
  )

  # vertex color
  vertexColors = BoolProperty(
    name = 'Vertex Colors',
    description = 'Display vertex color names.',
    default = False
  )

  # materials
  materials = BoolProperty(
    name = 'Materials',
    description = 'Display material names.',
    default = False
  )

  # textures
  textures = BoolProperty(
    name = 'Textures.',
    description = 'Display material texture names.',
    default = False
  )

  # particle systems
  particleSystems = BoolProperty(
    name = 'Particle Systems',
    description = 'Display the particle system and setting names. (Modifier filter must be active)',
    default = False
  )

  # selected bones
  selectedBones = BoolProperty(
    name = 'Selected',
    description = 'Display selected bone names.',
    default = False
  )

class batch:
  '''
    Contains Classes;
      auto
      name (PropertyGroup)
      copy (PropertyGroup)
  '''
  # auto
  class auto:
    '''
      Contains Classes;
        name (PropertyGroup)
        objects (PropertyGroup)
        constraints (PropertyGroup)
        modifiers (PropertyGroup)
        objectData (PropertyGroup)
    '''
    # options
    class name(PropertyGroup):
      '''
        Main properties that effect how the batch auto name operator is performed.
      '''

      # batch type
      batchType = EnumProperty(
        name = 'Batch Type',
        description = '',
        items = [
          ('SELECTED', 'Selected', 'Batch auto name will only effect the object related datablock names within the current selection.'),
          ('OBJECTS', 'All Objects', 'Batch auto name will effect all object related datablock names in the file.')
        ],
        default = 'SELECTED'
      )

      # objects
      objects = BoolProperty(
        name = 'Objects',
        description = 'Name objects.',
        default = False
      )

      # constraints
      constraints = BoolProperty(
        name = 'Constraints',
        description = 'Name constraints.',
        default = False
      )

      # modifiers
      modifiers = BoolProperty(
        name = 'Modifiers',
        description = 'Name modifiers.',
        default = False
      )

      # objectData
      objectData = BoolProperty(
        name = 'Object Data',
        description = 'Name object data.',
        default = False
      )

      # bone Constraints
      boneConstraints = BoolProperty(
        name = 'Bone Constraints',
        description = 'Name bone constraints.'
      )

      # object type
      objectType = EnumProperty(
        name = 'Object Type',
        description = 'Type of objects to be effected.',
        items = menuList.objects,
        default = 'ALL'
      )

      # constraint type
      constraintType = EnumProperty(
        name = 'Constraint Type',
        description = 'Type of constraints to be effected.',
        items = menuList.constraints,
        default = 'ALL'
      )

      # modifier type
      modifierType = EnumProperty(
        name = 'Modifier Type',
        description = 'Type of modifiers to be effected.',
        items = menuList.modifiers,
        default = 'ALL'
      )

    # object
    class objects(PropertyGroup):
      '''
        Properties that effect the names used when auto naming objects.
      '''
      # mesh
      mesh = StringProperty(
        name = 'Mesh',
        description = 'Name used for mesh objects.',
        default = 'Mesh'
      )

      # curve
      curve = StringProperty(
        name = 'Curve',
        description = 'Name used for curve objects.',
        default = 'Curve'
      )

      # surface
      surface = StringProperty(
        name = 'Surface',
        description = 'Name used for surface objects.',
        default = 'Surface'
      )

      # meta
      meta = StringProperty(
        name = 'Meta',
        description = 'Name used for meta objects.',
        default = 'Meta'
      )

      # font
      font = StringProperty(
        name = 'Text',
        description = 'Name used for font objects.',
        default = 'Text'
      )

      # armature
      armature = StringProperty(
        name = 'Armature',
        description = 'Name used for armature objects.',
        default = 'Armature'
      )

      # lattice
      lattice = StringProperty(
        name = 'Lattice',
        description = 'Name used for lattice objects.',
        default = 'Lattice'
      )

      # empty
      empty = StringProperty(
        name = 'Empty',
        description = 'Name used for empty objects.',
        default = 'Empty'
      )

      # speaker
      speaker = StringProperty(
        name = 'Speaker',
        description = 'Name used for speaker objects.',
        default = 'Speaker'
      )

      # camera
      camera = StringProperty(
        name = 'Camera',
        description = 'Name used for camera objects.',
        default = 'Camera'
      )

      # lamp
      lamp = StringProperty(
        name = 'Lamp',
        description = 'Name used for lamp objects.',
        default = 'Lamp'
      )

    # constraint
    class constraints(PropertyGroup):
      '''
        Properties that effect the names used when auto naming constraints.
      '''

      # camera solver
      cameraSolver = StringProperty(
        name = 'Camera Solver',
        description = 'Name used for camera solver constraints.',
        default = 'Camera Solver'
      )

      # follow track
      followTrack = StringProperty(
        name = 'Follow Track',
        description = 'Name used for follow track constraints.',
        default = 'Follow Track'
      )

      # object solver
      objectSolver = StringProperty(
        name = 'Object Solver',
        description = 'Name used for object solver constraints.',
        default = 'Object Solver'
      )

      # copy location
      copyLocation = StringProperty(
        name = 'Copy Location',
        description = 'Name used for copy location constraints.',
        default = 'Copy Location'
      )

      # copy rotation
      copyRotation = StringProperty(
        name = 'Copy Rotation',
        description = 'Name used for copy rotation constraints.',
        default = 'Copy Rotation'
      )

      # copy scale
      copyScale = StringProperty(
        name = 'Copy Scale',
        description = 'Name used for copy scale constraints.',
        default = 'Copy Scale'
      )

      # copy transforms
      copyTransforms = StringProperty(
        name = 'Copy Transforms',
        description = 'Name used for copy transforms constraints.',
        default = 'Copy Transforms'
      )

      # limit distance
      limitDistance = StringProperty(
        name = 'Limit Distance',
        description = 'Name used for limit distance constraints.',
        default = 'Limit Distance'
      )

      # limit location
      limitLocation = StringProperty(
        name = 'Limit Location',
        description = 'Name used for limit location constraints.',
        default = 'Limit Location'
      )

      # limit rotation
      limitRotation = StringProperty(
        name = 'Limit Rotation',
        description = 'Name used for limit rotation constraints.',
        default = 'Limit Rotation'
      )

      # limit scale
      limitScale = StringProperty(
        name = 'Limit Scale',
        description = 'Name used for limit scale constraints.',
        default = 'Limit Scale'
      )

      # maintain volume
      maintainVolume = StringProperty(
        name = 'Maintain Volume',
        description = 'Name used for maintain volume constraints.',
        default = 'Maintain Volume'
      )

      # transform
      transform = StringProperty(
        name = 'Transform',
        description = 'Name used for transform constraints.',
        default = 'Transform'
      )

      # clamp to
      clampTo = StringProperty(
        name = 'Clamp To',
        description = 'Name used for clamp to constraints.',
        default = 'Clamp To'
      )

      # damped track
      dampedTrack = StringProperty(
        name = 'Damped Track',
        description = 'Name used for damped track constraints.',
        default = 'Damped Track'
      )

      # inverse kinematics
      inverseKinematics = StringProperty(
        name = 'Inverse Kinematics',
        description = 'Name used for inverse kinematics constraints.',
        default = 'Inverse Kinematics'
      )

      # locked track
      lockedTrack = StringProperty(
         name = 'Locked Track',
         description = 'Name used for locked track constraints.',
         default = 'Locked Track'
      )

      # spline inverse kinematics
      splineInverseKinematics = StringProperty(
         name = 'Spline Inverse Kinematics',
         description = 'Name used for spline inverse kinematics constraints.',
         default = 'Spline Inverse Kinematics'
      )

      # stretch to
      stretchTo = StringProperty(
         name = 'Stretch To',
         description = 'Name used for stretch to constraints.',
         default = 'Stretch To'
      )

      # track to
      trackTo = StringProperty(
         name = 'Track To',
         description = 'Name used for track to constraints.',
         default = 'Track To'
      )

      # action
      action = StringProperty(
         name = 'Action',
         description = 'Name used for action constraints.',
         default = 'Action'
      )

      # child of
      childOf = StringProperty(
         name = 'Child Of',
         description = 'Name used for child of constraints.',
         default = 'Child Of'
      )

      # floor
      floor = StringProperty(
         name = 'Floor',
         description = 'Name used for floor constraints.',
         default = 'Floor'
      )

      # follow path
      followPath = StringProperty(
         name = 'Follow Path',
         description = 'Name used for follow path constraints.',
         default = 'Follow Path'
      )

      # pivot
      pivot = StringProperty(
         name = 'Pivot',
         description = 'Name used for pivot constraints.',
         default = 'Pivot'
      )

      # rigid body joint
      rigidBodyJoint = StringProperty(
         name = 'Rigid Body Joint',
         description = 'Name used for rigid body joint constraints.',
         default = 'Rigid Body Joint'
      )

      # shrinkwrap
      shrinkwrap = StringProperty(
         name = 'Shrinkwrap',
         description = 'Name used for shrinkwrap constraints.',
         default = 'Shrinkwrap'
      )

    # modifier
    class modifiers(PropertyGroup):
      '''
        Properties that effect the names used when auto naming modifiers.
      '''
      # data transfer
      dataTransfer = StringProperty(
        name = 'Data Transfer',
        description = 'Name used for data transfer modifiers.',
        default = 'Data Transfer'
      )

      # mesh cache
      meshCache = StringProperty(
        name = 'Mesh Cache',
        description = 'Name used for mesh cache modifiers.',
        default = 'Mesh Cache'
      )

      # normal edit
      normalEdit = StringProperty(
        name = 'Normal Edit',
        description = 'Name used for normal edit modifiers.',
        default = 'Normal Edit'
      )

      # uv project
      uvProject = StringProperty(
        name = 'UV Project',
        description = 'Name used for uv project modifiers.',
        default = 'UV Project'
      )

      # uv warp
      uvWarp = StringProperty(
        name = 'UV Warp',
        description = 'Name used for uv warp modifiers.',
        default = 'UV Warp'
      )

      # vertex weight edit
      vertexWeightEdit = StringProperty(
        name = 'Vertex Weight Edit',
        description = 'Name used for vertex weight edit modifiers.',
        default = 'Vertex Weight Edit'
      )

      # vertex weight mix
      vertexWeightMix = StringProperty(
        name = 'Vertex Weight Mix',
        description = 'Name used for vertex weight mix modifiers.',
        default = 'Vertex Weight Mix'
      )

      # vertex weight proximity
      vertexWeightProximity = StringProperty(
        name = 'Vertex Weight Proximity',
        description = 'Name used for vertex weight proximity modifiers.',
        default = 'Vertex Weight Proximity'
      )

      # array
      array = StringProperty(
        name = 'Array',
        description = 'Name used for array modifiers.',
        default = 'Array'
      )

      # bevel
      bevel = StringProperty(
        name = 'Bevel',
        description = 'Name used for bevel modifiers.',
        default = 'Bevel'
      )

      # boolean
      boolean = StringProperty(
        name = 'Boolean',
        description = 'Name used for boolean modifiers.',
        default = 'Boolean'
      )

      # build
      build = StringProperty(
        name = 'Build',
        description = 'Name used for build modifiers.',
        default = 'Build'
      )

      # decimate
      decimate = StringProperty(
        name = 'Decimate',
        description = 'Name used for decimate modifiers.',
        default = 'Decimate'
      )

      # edge split
      edgeSplit = StringProperty(
        name = 'Edge Split',
        description = 'Name used for edge split modifiers.',
        default = 'Edge Split'
      )

      # mask
      mask = StringProperty(
        name = 'Mask',
        description = 'Name used for mask modifiers.',
        default = 'Mask'
      )

      # mirror
      mirror = StringProperty(
        name = 'Mirror',
        description = 'Name used for mirror modifiers.',
        default = 'Mirror'
      )

      # multiresolution
      multiresolution = StringProperty(
        name = 'Multiresolution',
        description = 'Name used for multiresolution modifiers.',
        default = 'Multiresolution'
      )

      # remesh
      remesh = StringProperty(
        name = 'Remesh',
        description = 'Name used for remesh modifiers.',
        default = 'Remesh'
      )

      # screw
      screw = StringProperty(
        name = 'Screw',
        description = 'Name used for screw modifiers.',
        default = 'Screw'
      )

      # skin
      skin = StringProperty(
        name = 'Skin',
        description = 'Name used for skin modifiers.',
        default = 'Skin'
      )

      # solidify
      solidify = StringProperty(
        name = 'Solidify',
        description = 'Name used for solidify modifiers.',
        default = 'Solidify'
      )

      # subdivision surface
      subdivisionSurface = StringProperty(
        name = 'Subdivision Surface',
        description = 'Name used for subdivision surface modifiers.',
        default = 'Subdivision Surface'
      )

      # triangulate
      triangulate = StringProperty(
        name = 'Triangulate',
        description = 'Name used for triangulate modifiers.',
        default = 'Triangulate'
      )

      # wireframe
      wireframe = StringProperty(
        name = 'Wireframe',
        description = 'Name used for wireframe modifiers.',
        default = 'Wireframe'
      )

      # armature
      armature = StringProperty(
        name = 'Armature',
        description = 'Name used for armature modifiers.',
        default = 'Armature'
      )

      # cast
      cast = StringProperty(
        name = 'Cast',
        description = 'Name used for cast modifiers.',
        default = 'Cast'
      )

      # corrective smooth
      correctiveSmooth = StringProperty(
        name = 'Corrective Smooth',
        description = 'Name used for corrective smooth modifiers.',
        default = 'Corrective Smooth'
      )

      # curve
      curve = StringProperty(
        name = 'Curve',
        description = 'Name used for curve modifiers.',
        default = 'Curve'
      )

      # displace
      displace = StringProperty(
        name = 'Displace',
        description = 'Name used for displace modifiers.',
        default = 'Displace'
      )

      # hook
      hook = StringProperty(
        name = 'Hook',
        description = 'Name used for hook modifiers.',
        default = 'Hook'
      )

      # laplacian smooth
      laplacianSmooth = StringProperty(
        name = 'Laplacian Smooth',
        description = 'Name used for laplacian smooth modifiers.',
        default = 'Laplacian Smooth'
      )

      # laplacian deform
      laplacianDeform = StringProperty(
        name = 'Laplacian Deform',
        description = 'Name used for laplacian deform modifiers.',
        default = 'Laplacian Deform'
      )

      # lattice
      lattice = StringProperty(
        name = 'Lattice',
        description = 'Name used for lattice modifiers.',
        default = 'Lattice'
      )

      # mesh deform
      meshDeform = StringProperty(
        name = 'Mesh Deform',
        description = 'Name used for mesh deform modifiers.',
        default = 'Mesh Deform'
      )

      # shrinkwrap
      shrinkwrap = StringProperty(
        name = 'Shrinkwrap',
        description = 'Name used for shrinkwrap modifiers.',
        default = 'Shrinkwrap'
      )

      # simple deform
      simpleDeform = StringProperty(
        name = 'Simple Deform',
        description = 'Name used for simple deform modifiers.',
        default = 'Simple Deform'
      )

      # smooth
      smooth = StringProperty(
        name = 'Smooth',
        description = 'Name used for smooth modifiers.',
        default = 'Smooth'
      )

      # warp
      warp = StringProperty(
        name = 'Warp',
        description = 'Name used for warp modifiers.',
        default = 'Warp'
      )

      # wave
      wave = StringProperty(
        name = 'Wave',
        description = 'Name used for wave modifiers.',
        default = 'Wave'
      )

      # cloth
      cloth = StringProperty(
        name = 'Cloth',
        description = 'Name used for cloth modifiers.',
        default = 'Cloth'
      )

      # collision
      collision = StringProperty(
        name = 'Collision',
        description = 'Name used for collision modifiers.',
        default = 'Collision'
      )

      # dynamic paint
      dynamicPaint = StringProperty(
        name = 'Dynamic Paint',
        description = 'Name used for dynamic paint modifiers.',
        default = 'Dynamic Paint'
      )

      # explode
      explode = StringProperty(
        name = 'Explode',
        description = 'Name used for explode modifiers.',
        default = 'Explode'
      )

      # fluid simulation
      fluidSimulation = StringProperty(
        name = 'Fluid Simulation',
        description = 'Name used for fluid simulation modifiers.',
        default = 'Fluid Simulation'
      )

      # ocean
      ocean = StringProperty(
        name = 'Ocean',
        description = 'Name used for ocean modifiers.',
        default = 'Ocean'
      )

      # particle instance
      particleInstance = StringProperty(
        name = 'Particle Instance',
        description = 'Name used for particle instance modifiers.',
        default = 'Particle Instance'
      )

      # particle system
      particleSystem = StringProperty(
        name = 'Particle System',
        description = 'Name used for particle system modifiers.',
        default = 'Particle System'
      )

      # smoke
      smoke = StringProperty(
        name = 'Smoke',
        description = 'Name used for smoke modifiers.',
        default = 'Smoke'
      )

      # soft body
      softBody = StringProperty(
        name = 'Soft Body',
        description = 'Name used for soft body modifiers.',
        default = 'Soft Body'
      )

    # object data
    class objectData(PropertyGroup):
      '''
        Properties that effect the names used when auto naming objects.
      '''
      # mesh
      mesh = StringProperty(
        name = 'Mesh',
        description = 'Name used for mesh objects.',
        default = 'Mesh'
      )

      # curve
      curve = StringProperty(
        name = 'Curve',
        description = 'Name used for curve objects.',
        default = 'Curve'
      )

      # surface
      surface = StringProperty(
        name = 'Surface',
        description = 'Name used for surface objects.',
        default = 'Surface'
      )

      # meta
      meta = StringProperty(
        name = 'Meta',
        description = 'Name used for meta objects.',
        default = 'Meta'
      )

      # font
      font = StringProperty(
        name = 'Text',
        description = 'Name used for font objects.',
        default = 'Text'
      )

      # armature
      armature = StringProperty(
        name = 'Armature',
        description = 'Name used for armature objects.',
        default = 'Armature'
      )

      # lattice
      lattice = StringProperty(
        name = 'Lattice',
        description = 'Name used for lattice objects.',
        default = 'Lattice'
      )

      # empty
      empty = StringProperty(
        name = 'Empty',
        description = 'Name used for empty objects.',
        default = 'Empty'
      )

      # speaker
      speaker = StringProperty(
        name = 'Speaker',
        description = 'Name used for speaker objects.',
        default = 'Speaker'
      )

      # camera
      camera = StringProperty(
        name = 'Camera',
        description = 'Name used for camera objects.',
        default = 'Camera'
      )

      # lamp
      lamp = StringProperty(
        name = 'Lamp',
        description = 'Name used for lamp objects.',
        default = 'Lamp'
      )

  # name
  class name(PropertyGroup):
    '''
      Properties that effect how the batch name operation is performed.
    '''

    # tag
    tag = BoolProperty(
      name = 'Tag',
      description = 'Used by batch name internally. (keep it off)',
      default = False
    )

    # batch type
    batchType = EnumProperty(
      name = 'Batch Type',
      description = '',
      items = [
        ('SELECTED', 'Selected', 'Batch name will only effect the object related datablock names within the current selection.'),
        ('OBJECTS', 'All Objects', 'Batch name will effect all object related datablock names in the file.'),
        ('GLOBAL', 'Global', 'Batch name will effect all datablocks in the file. (Disables type filter menus.)')
      ],
      default = 'SELECTED'
    )

    # objects
    objects = BoolProperty(
      name = 'Objects',
      description = 'Name objects.',
      default = False
    )

    # groups
    groups = BoolProperty(
      name = 'Groups',
      description = 'Name groups.',
      default = False
    )

    # actions
    actions = BoolProperty(
      name = 'Actions',
      description = 'Name actions.',
      default = False
    )

    # grease pencil
    greasePencil = BoolProperty(
      name = 'Grease Pencil',
      description = 'Name grease pencils and layers.',
      default = False
    )

    # constraints
    constraints = BoolProperty(
      name = 'Object Constraints',
      description = 'Name constraints.',
      default = False
    )

    # modifiers
    modifiers = BoolProperty(
      name = 'Modifiers',
      description = 'Name modifiers.',
      default = False
    )

    # object data
    objectData = BoolProperty(
      name = 'Object Data',
      description = 'Name object data.',
      default = False
    )

    # bone groups
    boneGroups = BoolProperty(
      name = 'Bone Groups',
      description = 'Name bone groups.',
      default = False
    )

    # bones
    bones = BoolProperty(
      name = 'Bones',
      description = 'Name bones.',
      default = False
    )

    # bone constraints
    boneConstraints = BoolProperty(
      name = 'Bone Constraints',
      description = 'Name bone constraints.',
      default = False
    )

    # vertex groups
    vertexGroups = BoolProperty(
      name = 'Vertex Groups',
      description = 'Name vertex groups.',
      default = False
    )

    # shapekeys
    shapekeys = BoolProperty(
      name = 'Shapekeys',
      description = 'Name shapekeys.',
      default = False
    )

    # uvs
    uvs = BoolProperty(
      name = 'UV Maps',
      description = 'Name uv maps.',
      default = False
    )

    # vertex colors
    vertexColors = BoolProperty(
      name = 'Vertex Colors',
      description = 'Name vertex colors.',
      default = False
    )

    # materials
    materials = BoolProperty(
      name = 'Materials',
      description = 'Name materials.',
      default = False
    )

    # textures
    textures = BoolProperty(
      name = 'Textures',
      description = 'Name material textures.',
      default = False
    )

    # particle systems
    particleSystems = BoolProperty(
      name = 'Particle Systems',
      description = 'Name particle systems.',
      default = False
    )

    # particle settings
    particleSettings = BoolProperty(
      name = 'Particle Settings',
      description = 'Name particle settings.',
      default = False
    )

    # object type
    objectType = EnumProperty(
      name = 'Object Type',
      description = 'Type of objects to be effected.',
      items = menuList.objects,
      default = 'ALL'
    )

    # constraint type
    constraintType = EnumProperty(
      name = 'Constraint Type',
      description = 'Type of constraints to be effected.',
      items = menuList.constraints,
      default = 'ALL'
    )

    # modifier type
    modifierType = EnumProperty(
      name = 'Modifier Type',
      description = 'Type of modifiers to be effected.',
      items = menuList.modifiers,
      default = 'ALL'
    )

    # scenes
    scenes = BoolProperty(
      name = 'scenes',
      description = 'Name scenes. (Must use \'Global\' batch type option)',
      default = False
    )

    # render layers
    renderLayers = BoolProperty(
      name = 'Render Layers',
      description = 'Name render layers. (Must use \'Global\' batch type option)',
      default = False
    )

    # worlds
    worlds = BoolProperty(
      name = 'Worlds',
      description = 'Name worlds. (Must use \'Global\' batch type option)',
      default = False
    )

    # libraries
    libraries = BoolProperty(
      name = 'Libraries',
      description = 'Name libraries. (Must use \'Global\' batch type option)',
      default = False
    )

    # images
    images = BoolProperty(
      name = 'Images',
      description = 'Name images. (Must use \'Global\' batch type option)',
      default = False
    )

    # masks
    masks = BoolProperty(
      name = 'Masks',
      description = 'Name masks. (Must use \'Global\' batch type option)',
      default = False
    )

    # sequences
    sequences = BoolProperty(
      name = 'Sequences',
      description = 'Name sequences. (Must use \'Global\' batch type option)',
      default = False
    )

    # movie clips
    movieClips = BoolProperty(
      name = 'Movie Clips',
      description = 'Name movie clips. (Must use \'Global\' batch type option)',
      default = False
    )

    # sounds
    sounds = BoolProperty(
      name = 'Sounds',
      description = 'Name sounds. (Must use \'Global\' batch type option)',
      default = False
    )

    # screens
    screens = BoolProperty(
      name = 'Screens',
      description = 'Name screens. (Must use \'Global\' batch type option)',
      default = False
    )

    # keying sets
    keyingSets = BoolProperty(
      name = 'Keying Sets',
      description = 'Name keying sets. (Must use \'Global\' batch type option)',
      default = False
    )

    # palettes
    palettes = BoolProperty(
      name = 'Palettes',
      description = 'Name color palettes. (Must use \'Global\' batch type option)',
      default = False
    )

    # brushes
    brushes = BoolProperty(
      name = 'Brushes',
      description = 'Name brushes. (Must use \'Global\' batch type option)',
      default = False
    )

    # linestyles
    linestyles = BoolProperty(
      name = 'Linestyles',
      description = 'Name linestyles. (Must use \'Global\' batch type option)',
      default = False
    )

    # nodes
    nodes = BoolProperty(
      name = 'Nodes',
      description = 'Name nodes. (Must use \'Global\' batch type option)',
      default = False
    )

    # node labels
    nodeLabels = BoolProperty(
      name = 'Node Labels',
      description = 'Name node labels. (Must use \'Global\' batch type option)',
      default = False
    )

    # node groups
    nodeGroups = BoolProperty(
      name = 'Node Groups',
      description = 'Name node groups. (Must use \'Global\' batch type option)',
      default = False
    )

    # texts
    texts = BoolProperty(
      name = 'Texts',
      description = 'Name text documents. (Must use \'Global\' batch type option)',
      default = False
    )

    # custom name
    customName = StringProperty(
      name = 'Custom Name',
      description = 'Designate a new name.'
    )

    # find
    find = StringProperty(
      name = 'Find',
      description = 'Find this string in the datablock name and remove it.'
    )

    # regex
    regex = BoolProperty(
      name = 'Regular Expressions',
      description = 'Use regular expressions.',
      default = False
    )

    # replace
    replace = StringProperty(
      name = 'Replace',
      description = 'Replace found string with the string entered here.'
    )

    # prefix
    prefix = StringProperty(
      name = 'Prefix',
      description = 'Place this string at the beginning of the name.'
    )

    # suffix
    suffix = StringProperty(
      name = 'Suffix',
      description = 'Place this string at the end of the name.'
    )

    # trim start
    trimStart = IntProperty(
      name = 'Trim Start',
      description = 'Trim the beginning of the name.',
      min = 0,
      max = 50,
      default = 0
    )

    # trim end
    trimEnd = IntProperty(
      name = 'Trim End',
      description = 'Trim the ending of the name.',
      min = 0,
      max = 50,
      default = 0
    )

  # copy
  class copy(PropertyGroup):
    '''
      Properties that effect how the batch copy name operation is performed.
    '''

    # batch type
    batchType = EnumProperty(
      name = 'Batch Type',
      description = '',
      items = [
        ('SELECTED', 'Selected', 'Batch name copy will only effect the object related datablock names within the current selection.'),
        ('OBJECTS', 'All Objects', 'Batch name copy will effect all object related datablock names in the file.')
      ],
      default = 'SELECTED'
    )

    # source
    source = EnumProperty(
      name = 'Copy',
      description = 'Type of datablock to copy the name from.',
      items = [
        ('OBJECT', 'Object', 'Use the name from the object.', 'OBJECT_DATA', 0),
        ('DATA', 'Object Data', 'Use the name from the object\'s data.', 'MESH_DATA', 1),
        ('MATERIAL', 'Material', 'Use the name from the active material of the object.', 'MATERIAL', 2),
        ('TEXTURE', 'Texture', 'Use the name from the active material\'s active texture of the object.', 'TEXTURE', 3),
        ('PARTICLE_SYSTEM', 'Particle System', 'Use the name from the active particle system of the object.', 'PARTICLES', 4),
        ('PARTICLE_SETTINGS', 'Particle Settings', 'Use the name from the active particle system\'s settings of the object.', 'MOD_PARTICLES', 5)
      ],
      default = 'OBJECT'
    )

    # objects
    objects = BoolProperty(
      name = 'Object',
      description = 'Paste to objects.',
      default = False
    )

    # object data
    objectData = BoolProperty(
      name = 'Object Data',
      description = 'Paste to object data.',
      default = False
    )

    # materials
    materials = BoolProperty(
      name = 'Material',
      description = 'Paste to materials.',
      default = False
    )

    # textures
    textures = BoolProperty(
      name = 'Texture',
      description = 'Paste to textures.',
      default = False
    )

    # particle systems
    particleSystems = BoolProperty(
      name = 'Particle System',
      description = 'Paste to particle systems.',
      default = False
    )

    # particle settings
    particleSettings = BoolProperty(
      name = 'Particle Settings',
      description = 'Paste to particle settings.',
      default = False
    )

    # use active object
    useActiveObject = BoolProperty(
      name = 'Use active object',
      description = 'Use the names available from the active object to paste to the other datablock names.',
      default = False
    )
