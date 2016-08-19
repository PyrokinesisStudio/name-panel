
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
from .. import storage
from ..defaults import defaults

# reset
def reset(context, panel, auto, names, name, copy):
  '''
    Resets the property values for the name panel add-on.
  '''

  # panel
  if panel:

    # defaults
    default = defaults['name panel']

    # name panel option
    option = context.window_manager.NamePanel

    # pin active object
    option.pinActiveObject = default['pin active object']

    # pin active bone
    option.pinActiveBone = default['pin active bone']

    # hide find & replace
    option.hideFindReplace = default['hide find & replace']

    # filters
    option.filters = default['filters']

    # shortcuts
    option.shortcuts = default['shortcuts']

    # display names
    option.displayNames = default['display names']

    # mode
    option.mode = default['mode']

    # search
    option.search = default['search']

    # regex
    option.regex = default['regex']

    # groups
    option.groups = default['groups']

    # action
    option.action = default['action']

    # grease pencil
    option.greasePencil = default['grease pencil']

    # constraints
    option.constraints = default['constraints']

    # modifiers
    option.modifiers = default['modifiers']

    # bone groups
    option.boneGroups = default['bone groups']

    # bone constraints
    option.boneConstraints = default['bone constraints']

    # vertex groups
    option.vertexGroups = default['vertex groups']

    # shapekeys
    option.shapekeys = default['shapekeys']

    # uvs
    option.uvs = default['uvs']

    # vertex colors
    option.vertexColors = default['vertex colors']

    # materials
    option.materials = default['materials']

    # textures
    option.textures = default['textures']

    # particle systems
    option.particleSystems = default['particle systems']

    # display bones
    option.displayBones = default['display bones']

    # bone mode
    option.boneMode = default['bone mode']

  # auto
  if auto:

    # default
    default = defaults['auto name']

    # auto name option
    option = context.window_manager.AutoName

    # mode
    option.mode = default['mode']

    # objects
    option.objects = default['objects']

    # constraints
    option.constraints = default['constraints']

    # modifiers
    option.modifiers = default['modifiers']

    # object data
    option.objectData = default['object data']

    # bone constraints
    option.boneConstraints = default['bone constraints']

    # object type
    option.objectType = default['object type']

    # constraint type
    option.constraintType = default['constraint type']

    # modifier type
    option.modifierType = default['modifier type']

    # option
    option = context.window_manager.BatchShared

    # default
    default = defaults['shared']

    # sort
    option.sort = default['sort']

    # padding
    option.pad = default['pad']

    # start
    option.start = default['start']

    # step
    option.step = default['step']

    # separate
    option.separator = default['separator']

    # link
    option.link = default['link']

    # ignore ignore
    option.ignore = default['ignore']

  # names
  if names:

    # default
    default = defaults['auto name']['object names']

    # object name
    option = context.window_manager.ObjectNames

    # prefix
    option.prefix = default['prefix']

    # mesh
    option.mesh = default['mesh']

    # curve
    option.curve = default['curve']

    # surface
    option.surface = default['surface']

    # meta
    option.meta = default['meta']

    # font
    option.font = default['font']

    # armature
    option.armature = default['armature']

    # lattice
    option.lattice = default['lattice']

    # empty
    option.empty = default['empty']

    # speaker
    option.speaker = default['speaker']

    # camera
    option.camera = default['camera']

    # lamp
    option.lamp = default['lamp']

    # default
    default = defaults['auto name']['constraint names']

    # constraint name
    option = context.window_manager.ConstraintNames

    # prefix
    option.prefix = default['prefix']

    # camera solver
    option.cameraSolver = default['camera solver']

    # follow track
    option.followTrack = default['follow track']

    # object solver
    option.objectSolver = default['object solver']

    # copy location
    option.copyLocation = default['copy location']

    # copy rotation
    option.copyRotation = default['copy rotation']

    # copy scale
    option.copyScale = default['copy scale']

    # copy transforms
    option.copyTransforms = default['copy transforms']

    # limit distance
    option.limitDistance = default['limit distance']

    # limit location
    option.limitLocation = default['limit location']

    # limit rotation
    option.limitRotation = default['limit rotation']

    # limit scale
    option.limitScale = default['limit scale']

    # maintain volume
    option.maintainVolume = default['maintain volume']

    # transform
    option.transform = default['transform']

    # clamp to
    option.clampTo = default['clamp to']

    # damped track
    option.dampedTrack = default['damped track']

    # inverse kinematics
    option.inverseKinematics = default['inverse kinematics']

    # locked track
    option.lockedTrack = default['locked track']

    # spline inverse kinematics
    option.splineInverseKinematics = default['spline inverse kinematics']

    # stretch to
    option.stretchTo = default['stretch to']

    # track to
    option.trackTo = default['track to']

    # action
    option.action = default['action']

    # child of
    option.childOf = default['child of']

    # floor
    option.floor = default['floor']

    # follow path
    option.followPath = default['follow path']

    # pivot
    option.pivot = default['pivot']

    # rigid body joint
    option.rigidBodyJoint = default['rigid body joint']

    # shrinkwrap
    option.shrinkwrap = default['shrinkwrap']

    # default
    default = defaults['auto name']['modifier names']

    # modifier name
    option = context.window_manager.ModifierNames

    # prefix
    option.prefix = default['prefix']

    # data transfer
    option.dataTransfer = default['data transfer']

    # mesh cache
    option.meshCache = default['mesh cache']

    # normal edit
    option.normalEdit = default['normal edit']

    # uv project
    option.uvProject = default['uv project']

    # uv warp
    option.uvWarp = default['uv warp']

    # vertex weight edit
    option.vertexWeightEdit = default['vertex weight edit']

    # vertex weight mix
    option.vertexWeightMix = default['vertex weight mix']

    # vertex weight proximity
    option.vertexWeightProximity = default['vertex weight proximity']

    # array
    option.array = default['array']

    # bevel
    option.bevel = default['bevel']

    # boolean
    option.boolean = default['boolean']

    # build
    option.build = default['build']

    # decimate
    option.decimate = default['decimate']

    # edge split
    option.edgeSplit = default['edge split']

    # mask
    option.mask = default['mask']

    # mirror
    option.mirror = default['mirror']

    # multiresolution
    option.multiresolution = default['multiresolution']

    # remesh
    option.remesh = default['remesh']

    # screw
    option.screw = default['screw']

    # skin
    option.skin = default['skin']

    # solidify
    option.solidify = default['solidify']

    # subdivision surface
    option.subdivisionSurface = default['subdivision surface']

    # triangulate
    option.triangulate = default['triangulate']

    # wireframe
    option.wireframe = default['wireframe']

    # armature
    option.armature = default['armature']

    # cast
    option.cast = default['cast']

    # corrective smooth
    option.correctiveSmooth = default['corrective smooth']

    # curve
    option.curve = default['curve']

    # displace
    option.displace = default['displace']

    # hook
    option.hook = default['hook']

    # laplacian smooth
    option.laplacianSmooth = default['laplacian smooth']

    # laplacian deform
    option.laplacianDeform = default['laplacian deform']

    # lattice
    option.lattice = default['lattice']

    # mesh deform
    option.meshDeform = default['mesh deform']

    # shrinkwrap
    option.shrinkwrap = default['shrinkwrap']

    # simple deform
    option.simpleDeform = default['simple deform']

    # smooth
    option.smooth = default['smooth']

    # warp
    option.warp = default['warp']

    # wave
    option.wave = default['wave']

    # cloth
    option.cloth = default['cloth']

    # collision
    option.collision = default['collision']

    # dynamic paint
    option.dynamicPaint = default['dynamic paint']

    # explode
    option.explode = default['explode']

    # fluid simulation
    option.fluidSimulation = default['fluid simulation']

    # ocean
    option.ocean = default['ocean']

    # particle instance
    option.particleInstance = default['particle instance']

    # particle system
    option.particleSystem = default['particle system']

    # smoke
    option.smoke = default['smoke']

    # soft body
    option.softBody = default['soft body']

    # default
    default = defaults['auto name']['object data names']

    # object data name
    option = context.window_manager.ObjectDataNames

    # prefix
    option.prefix = default['prefix']

    # mesh
    option.mesh = default['mesh']

    # curve
    option.curve = default['curve']

    # surface
    option.surface = default['surface']

    # meta
    option.meta = default['meta']

    # font
    option.font = default['font']

    # armature
    option.armature = default['armature']

    # lattice
    option.lattice = default['lattice']

    # speaker
    option.speaker = default['speaker']

    # camera
    option.camera = default['camera']

    # lamp
    option.lamp = default['lamp']

  # name
  if name:

    # default
    default = defaults['batch name']

    # name option
    option = context.window_manager.BatchName

    # mode
    option.mode = default['mode']

    # actions
    option.actions = default['actions']

    # action groups
    option.actionGroups = default['action groups']

    # grease pencil
    option.greasePencil = default['grease pencil']

    # pencil layers
    option.pencilLayers = default['pencil layers']

    # objects
    option.objects = default['objects']

    # groups
    option.groups = default['groups']

    # constraints
    option.constraints = default['constraints']

    # modifiers
    option.modifiers = default['modifiers']

    # object data
    option.objectData = default['object data']

    # bone groups
    option.boneGroups = default['bone groups']

    # bones
    option.bones = default['bones']

    # bone constraints
    option.boneConstraints = default['bone constraints']

    # vertex groups
    option.vertexGroups = default['vertex groups']

    # shapekeys
    option.shapekeys = default['shapekeys']

    # uvs
    option.uvs = default['uvs']

    # vertex colors
    option.vertexColors = default['vertex colors']

    # materials
    option.materials = default['materials']

    # textures
    option.textures = default['textures']

    # particle systems
    option.particleSystems = default['particle systems']

    # particle settings
    option.particleSettings = default['particle settings']

    # object type
    option.objectType = default['object type']

    # constraint type
    option.constraintType = default['constraint type']

    # modifier type
    option.modifierType = default['modifier type']

    # sensors
    option.sensors = default['sensors']

    # controllers
    option.controllers = default['controllers']

    # actuators
    option.actuators = default['actuators']

    # line sets
    option.lineSets = default['line sets']

    # linestyles
    option.linestyles = default['linestyles']

    # linestyle modifiers
    option.linestyleModifiers = default['linestyle modifiers']

    # linestyle modifier type
    option.linestyleModifierType = default['linestyle modifier type']

    # scenes
    option.scenes = default['scenes']

    # render layers
    option.renderLayers = default['render layers']

    # worlds
    option.worlds = default['worlds']

    # libraries
    option.libraries = default['libraries']

    # images
    option.images = default['images']

    # masks
    option.masks = default['masks']

    # sequences
    option.sequences = default['sequences']

    # movie clips
    option.movieClips = default['movie clips']

    # sounds
    option.sounds = default['sounds']

    # screens
    option.screens = default['screens']

    # keying sets
    option.keyingSets = default['keying sets']

    # palettes
    option.palettes = default['palettes']

    # brushes
    option.brushes = default['brushes']

    # nodes
    option.nodes = default['nodes']

    # node labels
    option.nodeLabels = default['node labels']

    # frame nodes
    option.frameNodes = default['frame nodes']

    # node groups
    option.nodeGroups = default['node groups']

    # texts
    option.texts = default['texts']

    # ignore action
    option.ignoreAction = default['ignore action']

    # ignore grease pencil
    option.ignoreGreasePencil = default['ignore grease pencil']

    # ignore object
    option.ignoreObject = default['ignore object']

    # ignore group
    option.ignoreGroup = default['ignore group']

    # ignore constraint
    option.ignoreConstraint = default['ignore constraint']

    # ignore modifier
    option.ignoreModifier = default['ignore modifier']

    # ignore bone
    option.ignoreBone = default['ignore bone']

    # ignore bone group
    option.ignoreBoneGroup = default['ignore bone group']

    # ignore bone constraint
    option.ignoreBoneConstraint = default['ignore bone constraint']

    # ignore object data
    option.ignoreObjectData = default['ignore object data']

    # ignore vertex group
    option.ignoreVertexGroup = default['ignore vertex group']

    # ignore shapekey
    option.ignoreShapekey = default['ignore shapekey']

    # ignore uv
    option.ignoreUV = default['ignore uv']

    # ignore vertex color
    option.ignoreVertexColor = default['ignore vertex color']

    # ignore material
    option.ignoreMaterial = default['ignore material']

    # ignore texture
    option.ignoreTexture = default['ignore texture']

    # ignore particle system
    option.ignoreParticleSystem = default['ignore particle system']

    # ignore particle setting
    option.ignoreParticleSetting = default['ignore particle setting']

    # custom
    option.custom = default['custom']

    # insert
    option.insert = default['insert']

    # insert at
    option.insertAt = default['insert at']

    # find
    option.find = default['find']

    # regex
    option.regex = default['regex']

    # replace
    option.replace = default['replace']

    # prefix
    option.prefix = default['prefix']

    # suffix
    option.suffix = default['suffix']

    # suffix last
    option.suffixLast = default['suffix last']

    # trim start
    option.trimStart = default['trim start']

    # trim end
    option.trimEnd = default['trim end']

    # start
    option.cutStart = default['cut start']

    # end
    option.cutAmount = default['cut amount']

    # default
    default = defaults['shared']

    # option
    option = context.window_manager.BatchShared

    # sort
    option.sort = default['sort']

    # type
    option.type = default['type']

    # axis
    option.axis = default['axis']

    # invert
    option.invert = default['invert']

    # count
    option.count = default['count']

    # link
    option.link = default['link']

    # padding
    option.pad = default['pad']

    # start
    option.start = default['start']

    # step
    option.step = default['step']

    # separator
    option.separator = default['separator']

    # ignore
    option.ignore = default['ignore']

  # copy
  if copy:

    # default
    default = defaults['copy name']

    # copy option
    option = context.window_manager.CopyName

    # mode
    option.mode = default['mode']

    # source
    option.source = default['source']

    # objects
    option.objects = default['objects']

    # object data
    option.objectData = default['object data']

    # materials
    option.materials = default['materials']

    # textures
    option.textures = default['textures']

    # particle systems
    option.particleSystems = default['particle systems']

    # particle settings
    option.particleSettings = default['particle settings']

    # use active object
    option.useActiveObject = default['use active object']

# transfer
def transfer(context, panel, auto, names, name, copy):
  '''
    Resets the property values for the name panel add-on.
  '''

  # panel settings
  if panel:
    for scene in bpy.data.scenes:
      if scene != context.scene:

        # name panel option
        option = context.window_manager.NamePanel

        # pin active object
        scene.NamePanel.pinActiveObject = option.pinActiveObject

        # pin active bone
        scene.NamePanel.pinActiveBone = option.pinActiveBone

        # hide find and replace
        scene.NamePanel.hideFindReplace = option.hideFindReplace

        # filters
        scene.NamePanel.filters = option.filters

        # shortcuts
        scene.NamePanel.shortcuts = option.shortcuts

        # display names
        scene.NamePanel.displayNames = option.displayNames

        # mode
        scene.NamePanel.mode = option.mode

        # search
        scene.NamePanel.search = option.search

        # regex
        scene.NamePanel.regex = option.regex

        # groups
        scene.NamePanel.groups = option.groups

        # action
        scene.NamePanel.action = option.action

        # grease pencil
        scene.NamePanel.greasePencil = option.greasePencil

        # constraint
        scene.NamePanel.constraints = option.constraints

        # modifiers
        scene.NamePanel.modifiers = option.modifiers

        # bone groups
        scene.NamePanel.boneGroups = option.boneGroups

        # bone constraints
        scene.NamePanel.boneConstraints = option.boneConstraints

        # vertex groups
        scene.NamePanel.vertexGroups = option.vertexGroups

        # shapekeys
        scene.NamePanel.shapekeys = option.shapekeys

        # uvs
        scene.NamePanel.uvs = option.uvs

        # vertex colors
        scene.NamePanel.vertexColors = option.vertexColors

        # materials
        scene.NamePanel.materials = option.materials

        # textures
        scene.NamePanel.textures = option.textures

        # particels systems
        scene.NamePanel.particleSystems = option.particleSystems

        # display bones
        scene.NamePanel.displayBones = option.displayBones

        # bone mode
        scene.NamePanel.boneMode = option.boneMode

  # auto
  if auto:
    for scene in bpy.data.scenes:
      if scene != context.scene:

        # auto name option
        option = context.window_manager.AutoName

        # type
        scene.AutoName.mode = option.mode

        # objects
        scene.AutoName.objects = option.objects

        # constraints
        scene.AutoName.constraints = option.constraints

        # modifiers
        scene.AutoName.modifiers = option.modifiers

        # objectData
        scene.AutoName.objectData = option.objectData

        # bone Constraints
        scene.AutoName.boneConstraints = option.boneConstraints

        # object type
        scene.AutoName.objectType = option.objectType

        # constraint type
        scene.AutoName.constraintType = option.constraintType

        # modifier type
        scene.AutoName.modifierType = option.modifierType

        # batch shared option
        option = context.window_manager.BatchShared

        # sort
        scene.BatchShared.sort = option.sort

        # padding
        scene.BatchShared.pad = option.pad

        # start
        scene.BatchShared.start = option.start

        # step
        scene.BatchShared.step = option.step

        # separate
        scene.BatchShared.separator = option.separator

        # link
        scene.BatchShared.link = option.link

        # ignore
        scene.BatchShared.ignore = option.ignore

  # names
  if names:
    for scene in bpy.data.scenes:
      if scene != context.scene:

        # object name
        option = context.window_manager.ObjectNames

        # prefix
        scene.ObjectNames.prefix = option.prefix

        # mesh
        scene.ObjectNames.mesh = option.mesh

        # curve
        scene.ObjectNames.curve = option.curve

        # surface
        scene.ObjectNames.surface = option.surface

        # meta
        scene.ObjectNames.meta = option.meta

        # font
        scene.ObjectNames.font = option.font

        # armature
        scene.ObjectNames.armature = option.armature

        # lattice
        scene.ObjectNames.lattice = option.lattice

        # empty
        scene.ObjectNames.empty = option.empty

        # speaker
        scene.ObjectNames.speaker = option.speaker

        # camera
        scene.ObjectNames.camera = option.camera

        # lamp
        scene.ObjectNames.lamp = option.lamp

        # constraint name
        option = context.window_manager.ConstraintNames

        # prefix
        scene.ConstraintNames.prefix = option.prefix

        # camera solver
        scene.ConstraintNames.cameraSolver = option.cameraSolver

        # follow track
        scene.ConstraintNames.followTrack = option.followTrack

        # object solver
        scene.ConstraintNames.objectSolver = option.objectSolver

        # copy location
        scene.ConstraintNames.copyLocation = option.copyLocation

        # copy rotation
        scene.ConstraintNames.copyRotation = option.copyRotation

        # copy scale
        scene.ConstraintNames.copyScale = option.copyScale

        # copy transforms
        scene.ConstraintNames.copyTransforms = option.copyTransforms

        # limit distance
        scene.ConstraintNames.limitDistance = option.limitDistance

        # limit location
        scene.ConstraintNames.limitLocation = option.limitLocation

        # limit rotation
        scene.ConstraintNames.limitRotation = option.limitRotation

        # limit scale
        scene.ConstraintNames.limitScale = option.limitScale

        # maintain volume
        scene.ConstraintNames.maintainVolume = option.maintainVolume

        # transform
        scene.ConstraintNames.transform = option.transform

        # clamp to
        scene.ConstraintNames.clampTo = option.clampTo

        # damped track
        scene.ConstraintNames.dampedTrack = option.dampedTrack

        # inverse kinematics
        scene.ConstraintNames.inverseKinematics = option.inverseKinematics

        # locked track
        scene.ConstraintNames.lockedTrack = option.lockedTrack

        # spline inverse kinematics
        scene.ConstraintNames.splineInverseKinematics = option.splineInverseKinematics

        # stretch to
        scene.ConstraintNames.stretchTo = option.stretchTo

        # track to
        scene.ConstraintNames.trackTo = option.trackTo

        # action
        scene.ConstraintNames.action = option.action

        # child of
        scene.ConstraintNames.childOf = option.childOf

        # floor
        scene.ConstraintNames.floor = option.floor

        # follow path
        scene.ConstraintNames.followPath = option.followPath

        # pivot
        scene.ConstraintNames.pivot = option.pivot

        # rigid body joint
        scene.ConstraintNames.rigidBodyJoint = option.rigidBodyJoint

        # shrinkwrap
        scene.ConstraintNames.shrinkwrap = option.shrinkwrap

        # modifier name
        option = context.window_manager.ModifierNames

        # prefix
        scene.ModifierNames.prefix = option.prefix

        # data transfer
        scene.ModifierNames.dataTransfer = option.dataTransfer

        # mesh cache
        scene.ModifierNames.meshCache = option.meshCache

        # normal edit
        scene.ModifierNames.normalEdit = option.normalEdit

        # uv project
        scene.ModifierNames.uvProject = option.uvProject

        # uv warp
        scene.ModifierNames.uvWarp = option.uvWarp

        # vertex weight edit
        scene.ModifierNames.vertexWeightEdit = option.vertexWeightEdit

        # vertex weight mix
        scene.ModifierNames.vertexWeightMix = option.vertexWeightMix

        # vertex weight proximity
        scene.ModifierNames.vertexWeightProximity = option.vertexWeightProximity

        # array
        scene.ModifierNames.array = option.array

        # bevel
        scene.ModifierNames.bevel = option.bevel

        # boolean
        scene.ModifierNames.boolean = option.boolean

        # build
        scene.ModifierNames.build = option.build

        # decimate
        scene.ModifierNames.decimate = option.decimate

        # edge split
        scene.ModifierNames.edgeSplit = option.edgeSplit

        # mask
        scene.ModifierNames.mask = option.mask

        # mirror
        scene.ModifierNames.mirror = option.mirror

        # multiresolution
        scene.ModifierNames.multiresolution = option.multiresolution

        # remesh
        scene.ModifierNames.remesh = option.remesh

        # screw
        scene.ModifierNames.screw = option.screw

        # skin
        scene.ModifierNames.skin = option.skin

        # solidify
        scene.ModifierNames.solidify = option.solidify

        # subdivision surface
        scene.ModifierNames.subdivisionSurface = option.subdivisionSurface

        # triangulate
        scene.ModifierNames.triangulate = option.triangulate

        # wireframe
        scene.ModifierNames.wireframe = option.wireframe

        # armature
        scene.ModifierNames.armature = option.armature

        # cast
        scene.ModifierNames.cast = option.cast

        # corrective smooth
        scene.ModifierNames.correctiveSmooth = option.correctiveSmooth

        # curve
        scene.ModifierNames.curve = option.curve

        # displace
        scene.ModifierNames.displace = option.displace

        # hook
        scene.ModifierNames.hook = option.hook

        # laplacian smooth
        scene.ModifierNames.laplacianSmooth = option.laplacianSmooth

        # laplacian deform
        scene.ModifierNames.laplacianDeform = option.laplacianDeform

        # lattice
        scene.ModifierNames.lattice = option.lattice

        # mesh deform
        scene.ModifierNames.meshDeform = option.meshDeform

        # shrinkwrap
        scene.ModifierNames.shrinkwrap = option.shrinkwrap

        # simple deform
        scene.ModifierNames.simpleDeform = option.simpleDeform

        # smooth
        scene.ModifierNames.smooth = option.smooth

        # warp
        scene.ModifierNames.warp = option.warp

        # wave
        scene.ModifierNames.wave = option.wave

        # cloth
        scene.ModifierNames.cloth = option.cloth

        # collision
        scene.ModifierNames.collision = option.collision

        # dynamic paint
        scene.ModifierNames.dynamicPaint = option.dynamicPaint

        # explode
        scene.ModifierNames.explode = option.explode

        # fluid simulation
        scene.ModifierNames.fluidSimulation = option.fluidSimulation

        # ocean
        scene.ModifierNames.ocean = option.ocean

        # particle instance
        scene.ModifierNames.particleInstance = option.particleInstance

        # particle system
        scene.ModifierNames.particleSystem = option.particleSystem

        # smoke
        scene.ModifierNames.smoke = option.smoke

        # soft body
        scene.ModifierNames.softBody = option.softBody

        # object data name
        option = context.window_manager.ObjectDataNames

        # prefix
        scene.ObjectDataNames.prefix = option.prefix

        # mesh
        scene.ObjectDataNames.mesh = option.mesh

        # curve
        scene.ObjectDataNames.curve = option.curve

        # surface
        scene.ObjectDataNames.surface = option.surface

        # meta
        scene.ObjectDataNames.meta = option.meta

        # font
        scene.ObjectDataNames.font = option.font

        # armature
        scene.ObjectDataNames.armature = option.armature

        # lattice
        scene.ObjectDataNames.lattice = option.lattice

        # speaker
        scene.ObjectDataNames.speaker = option.speaker

        # camera
        scene.ObjectDataNames.camera = option.camera

        # lamp
        scene.ObjectDataNames.lamp = option.lamp

  # name
  if name:
    for scene in bpy.data.scenes:
      if scene != context.scene:

        # name option
        option = context.window_manager.BatchName

        # batch type
        scene.BatchName.mode = option.mode

        # actions
        scene.BatchName.actions = option.actions

        # action groups
        scene.BatchName.actionGroups = option.actionGroups

        # grease pencil
        scene.BatchName.greasePencil = option.greasePencil

        # pencil layers
        scene.BatchName.pencilLayers = option.pencilLayers

        # objects
        scene.BatchName.objects = option.objects

        # groups
        scene.BatchName.groups = option.groups

        # constraints
        scene.BatchName.constraints = option.constraints

        # modifiers
        scene.BatchName.modifiers = option.modifiers

        # object data
        scene.BatchName.objectData = option.objectData

        # bone groups
        scene.BatchName.boneGroups = option.boneGroups

        # bones
        scene.BatchName.bones = option.bones

        # bone constraints
        scene.BatchName.boneConstraints = option.boneConstraints

        # vertex groups
        scene.BatchName.vertexGroups = option.vertexGroups

        # shapekeys
        scene.BatchName.shapekeys = option.shapekeys

        # uvs
        scene.BatchName.uvs = option.uvs

        # vertex colors
        scene.BatchName.vertexColors = option.vertexColors

        # materials
        scene.BatchName.materials = option.materials

        # textures
        scene.BatchName.textures = option.textures

        # particle systems
        scene.BatchName.particleSystems = option.particleSystems

        # particle settings
        scene.BatchName.particleSettings = option.particleSettings

        # object type
        scene.BatchName.objectType = option.objectType

        # constraint type
        scene.BatchName.constraintType = option.constraintType

        # modifier type
        scene.BatchName.modifierType = option.modifierType

        # sensors
        scene.BatchName.sensors = option.sensors

        # controllers
        scene.BatchName.controllers = option.controllers

        # actuators
        scene.BatchName.actuators = option.actuators

        # line sets
        scene.BatchName.lineSets = option.lineSets

        # linestyles
        scene.BatchName.linestyles = option.linestyles

        # linestyle modifiers
        scene.BatchName.linestyleModifiers = option.linestyleModifiers

        # linestyle modifier type
        scene.BatchName.linestyleModifierType = option.linestyleModifierType

        # scenes
        scene.BatchName.scenes = option.scenes

        # render layers
        scene.BatchName.renderLayers = option.renderLayers

        # worlds
        scene.BatchName.worlds = option.worlds

        # libraries
        scene.BatchName.libraries = option.libraries

        # images
        scene.BatchName.images = option.images

        # masks
        scene.BatchName.masks = option.masks

        # sequences
        scene.BatchName.sequences = option.sequences

        # movie clips
        scene.BatchName.movieClips = option.movieClips

        # sounds
        scene.BatchName.sounds = option.sounds

        # screens
        scene.BatchName.screens = option.screens

        # keying sets
        scene.BatchName.keyingSets = option.keyingSets

        # palettes
        scene.BatchName.palettes = option.palettes

        # brushes
        scene.BatchName.brushes = option.brushes

        # linestyles
        scene.BatchName.linestyles = option.linestyles

        # nodes
        scene.BatchName.nodes = option.nodes

        # node labels
        scene.BatchName.nodeLabels = option.nodeLabels

        # frame nodes
        scene.BatchName.frameNodes = option.frameNodes

        # node groups
        scene.BatchName.nodeGroups = option.nodeGroups

        # texts
        scene.BatchName.texts = option.texts

        # ignore action
        scene.BatchName.ignoreAction = option.ignoreAction

        # ignore grease pencil
        scene.BatchName.ignoreGreasePencil = option.ignoreGreasePencil

        # ignore object
        scene.BatchName.ignoreObject = option.ignoreObject

        # ignore group
        scene.BatchName.ignoreGroup = option.ignoreGroup

        # ignore constraint
        scene.BatchName.ignoreConstraint = option.ignoreConstraint

        # ignore modifier
        scene.BatchName.ignoreModifier = option.ignoreModifier

        # ignore bone
        scene.BatchName.ignoreBone = option.ignoreBone

        # ignore bone group
        scene.BatchName.ignoreBoneGroup = option.ignoreBoneGroup

        # ignore bone constraint
        scene.BatchName.ignoreBoneConstraint = option.ignoreBoneConstraint

        # ignore object data
        scene.BatchName.ignoreObjectData = option.ignoreObjectData

        # ignore vertex group
        scene.BatchName.ignoreVertexGroup = option.ignoreVertexGroup

        # ignore shapekey
        scene.BatchName.ignoreShapekey = option.ignoreShapekey

        # ignore uv
        scene.BatchName.ignoreUV = option.ignoreUV

        # ignore vertex color
        scene.BatchName.ignoreVertexColor = option.ignoreVertexColor

        # ignore material
        scene.BatchName.ignoreMaterial = option.ignoreMaterial

        # ignore texture
        scene.BatchName.ignoreTexture = option.ignoreTexture

        # ignore particle system
        scene.BatchName.ignoreParticleSystem = option.ignoreParticleSystem

        # ignore particle setting
        scene.BatchName.ignoreParticleSetting = option.ignoreParticleSetting

        # custom
        scene.BatchName.custom = option.custom

        # insert
        scene.BatchName.insert = option.insert

        # insert at
        scene.BatchName.insertAt = option.insertAt

        # find
        scene.BatchName.find = option.find

        # regex
        scene.BatchName.regex = option.regex

        # replace
        scene.BatchName.replace = option.replace

        # prefix
        scene.BatchName.prefix = option.prefix

        # suffix
        scene.BatchName.suffix = option.suffix

        # suffix last
        scene.BatchName.suffixLast = option.suffixLast

        # trim start
        scene.BatchName.trimStart = option.trimStart

        # trim end
        scene.BatchName.trimEnd = option.trimEnd

        # start
        scene.BatchName.cutStart = option.cutStart

        # end
        scene.BatchName.cutAmount = option.cutAmount

        # batch shared option
        option = context.window_manager.BatchShared

        # sort
        scene.BatchShared.sort = option.sort

        # type
        scene.BatchShared.type = option.type

        # axis
        scene.BatchShared.axis = option.axis

        # invert
        scene.BatchShared.invert = option.invert

        # count
        scene.BatchShared.count = option.count

        # padding
        scene.BatchShared.pad = option.pad

        # start
        scene.BatchShared.start = option.start

        # step
        scene.BatchShared.step = option.step

        # separate
        scene.BatchShared.separator = option.separator

        # link
        scene.BatchShared.link = option.link

        # ignore
        scene.BatchShared.ignore = option.ignore

  # copy
  if copy:
    for scene in bpy.data.scenes:
      if scene != context.scene:

        # copy option
        option = context.window_manager.CopyName

        # type
        scene.CopyName.mode = option.mode

        # source
        scene.CopyName.source = option.source

        # objects
        scene.CopyName.objects = option.objects

        # object datas
        scene.CopyName.objectData = option.objectData

        # materials
        scene.CopyName.materials = option.materials

        # textures
        scene.CopyName.textures = option.textures

        # particle systems
        scene.CopyName.particleSystems = option.particleSystems

        # particle settings
        scene.CopyName.particleSettings = option.particleSettings

        # use active object
        scene.CopyName.useActiveObject = option.useActiveObject
