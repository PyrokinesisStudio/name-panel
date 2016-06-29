
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

# addon
addon = bpy.context.user_preferences.addons.get(__name__.partition('.')[0])

# reset
def reset(context, panel, auto, names, name, copy):
  '''
    Resets the property values for the name panel add-on.
  '''

  # panel
  if panel:

    # name panel option
    namePanelOption = context.scene.NamePanel

    # pin active object
    namePanelOption.pinActiveObject = False

    # hide search
    namePanelOption.hideSearch = True

    # filters
    namePanelOption.filters = False

    # options
    namePanelOption.options = False

    # selected
    namePanelOption.displayNames = False

    # mode
    namePanelOption.mode = 'SELECTED'

    # search
    namePanelOption.search = ''

    # regex
    namePanelOption.regex = False

    # groups
    namePanelOption.groups = False

    # action
    namePanelOption.action = False

    # grease pencil
    namePanelOption.greasePencil = False

    # constraints
    namePanelOption.constraints = False

    # modifiers
    namePanelOption.modifiers = False

    # bone groups
    namePanelOption.boneGroups = False

    # bone constraints
    namePanelOption.boneConstraints = False

    # vertex groups
    namePanelOption.vertexGroups = False

    # shapekeys
    namePanelOption.shapekeys = False

    # uvs
    namePanelOption.uvs = False

    # vertex colors
    namePanelOption.vertexColors = False

    # materials
    namePanelOption.materials = False

    # textures
    namePanelOption.textures = False

    # particle systems
    namePanelOption.particleSystems = False

    # display bones
    namePanelOption.displayBones = False

    # bone mode
    namePanelOption.boneMode = 'SELECTED'

  # auto
  if auto:

    # default
    default = defaults['auto name']

    # auto name option
    batchAutoNameOption = context.scene.BatchAutoName

    # mode
    batchAutoNameOption.mode = default['mode']

    # objects
    batchAutoNameOption.objects = default['objects']

    # constraints
    batchAutoNameOption.constraints = default['constraints']

    # modifiers
    batchAutoNameOption.modifiers = default['modifiers']

    # object data
    batchAutoNameOption.objectData = default['object data']

    # bone constraints
    batchAutoNameOption.boneConstraints = default['bone constraints']

    # object type
    batchAutoNameOption.objectType = default['object type']

    # constraint type
    batchAutoNameOption.constraintType = default['constraint type']

    # modifier type
    batchAutoNameOption.modifierType = default['modifier type']

  # names
  if names:

    # default
    default = defaults['auto name']['object names']

    # object name
    objectName = context.scene.BatchAutoName_ObjectNames

    # prefix
    objectName.prefix = default['prefix']

    # mesh
    objectName.mesh = default['mesh']

    # curve
    objectName.curve = default['curve']

    # surface
    objectName.surface = default['surface']

    # meta
    objectName.meta = default['meta']

    # font
    objectName.font = default['font']

    # armature
    objectName.armature = default['armature']

    # lattice
    objectName.lattice = default['lattice']

    # empty
    objectName.empty = default['empty']

    # speaker
    objectName.speaker = default['speaker']

    # camera
    objectName.camera = default['camera']

    # lamp
    objectName.lamp = default['lamp']

    # default
    default = defaults['auto name']['constraint names']

    # constraint name
    constraintName = context.scene.BatchAutoName_ConstraintNames

    # prefix
    constraintName.prefix = default['prefix']

    # camera solver
    constraintName.cameraSolver = default['camera solver']

    # follow track
    constraintName.followTrack = default['follow track']

    # object solver
    constraintName.objectSolver = default['object solver']

    # copy location
    constraintName.copyLocation = default['copy location']

    # copy rotation
    constraintName.copyRotation = default['copy rotation']

    # copy scale
    constraintName.copyScale = default['copy scale']

    # copy transforms
    constraintName.copyTransforms = default['copy transforms']

    # limit distance
    constraintName.limitDistance = default['limit distance']

    # limit location
    constraintName.limitLocation = default['limit location']

    # limit rotation
    constraintName.limitRotation = default['limit rotation']

    # limit scale
    constraintName.limitScale = default['limit scale']

    # maintain volume
    constraintName.maintainVolume = default['maintain volume']

    # transform
    constraintName.transform = default['transform']

    # clamp to
    constraintName.clampTo = default['clamp to']

    # damped track
    constraintName.dampedTrack = default['damped track']

    # inverse kinematics
    constraintName.inverseKinematics = default['inverse kinematics']

    # locked track
    constraintName.lockedTrack = default['locked track']

    # spline inverse kinematics
    constraintName.splineInverseKinematics = default['spline inverse kinematics']

    # stretch to
    constraintName.stretchTo = default['stretch to']

    # track to
    constraintName.trackTo = default['track to']

    # action
    constraintName.action = default['action']

    # child of
    constraintName.childOf = default['child of']

    # floor
    constraintName.floor = default['floor']

    # follow path
    constraintName.followPath = default['follow path']

    # pivot
    constraintName.pivot = default['pivot']

    # rigid body joint
    constraintName.rigidBodyJoint = default['rigid body joint']

    # shrinkwrap
    constraintName.shrinkwrap = default['shrinkwrap']

    # default
    default = defaults['auto name']['modifier names']

    # modifier name
    modifierName = context.scene.BatchAutoName_ModifierNames

    # prefix
    modifierName.prefix = default['prefix']

    # data transfer
    modifierName.dataTransfer = default['data transfer']

    # mesh cache
    modifierName.meshCache = default['mesh cache']

    # normal edit
    modifierName.normalEdit = default['normal edit']

    # uv project
    modifierName.uvProject = default['uv project']

    # uv warp
    modifierName.uvWarp = default['uv warp']

    # vertex weight edit
    modifierName.vertexWeightEdit = default['vertex weight edit']

    # vertex weight mix
    modifierName.vertexWeightMix = default['vertex weight mix']

    # vertex weight proximity
    modifierName.vertexWeightProximity = default['vertex weight proximity']

    # array
    modifierName.array = default['array']

    # bevel
    modifierName.bevel = default['bevel']

    # boolean
    modifierName.boolean = default['boolean']

    # build
    modifierName.build = default['build']

    # decimate
    modifierName.decimate = default['decimate']

    # edge split
    modifierName.edgeSplit = default['edge split']

    # mask
    modifierName.mask = default['mask']

    # mirror
    modifierName.mirror = default['mirror']

    # multiresolution
    modifierName.multiresolution = default['multiresolution']

    # remesh
    modifierName.remesh = default['remesh']

    # screw
    modifierName.screw = default['screw']

    # skin
    modifierName.skin = default['skin']

    # solidify
    modifierName.solidify = default['solidify']

    # subdivision surface
    modifierName.subdivisionSurface = default['subdivision surface']

    # triangulate
    modifierName.triangulate = default['triangulate']

    # wireframe
    modifierName.wireframe = default['wireframe']

    # armature
    modifierName.armature = default['armature']

    # cast
    modifierName.cast = default['cast']

    # corrective smooth
    modifierName.correctiveSmooth = default['corrective smooth']

    # curve
    modifierName.curve = default['curve']

    # displace
    modifierName.displace = default['displace']

    # hook
    modifierName.hook = default['hook']

    # laplacian smooth
    modifierName.laplacianSmooth = default['laplacian smooth']

    # laplacian deform
    modifierName.laplacianDeform = default['laplacian deform']

    # lattice
    modifierName.lattice = default['lattice']

    # mesh deform
    modifierName.meshDeform = default['mesh deform']

    # shrinkwrap
    modifierName.shrinkwrap = default['shrinkwrap']

    # simple deform
    modifierName.simpleDeform = default['simple deform']

    # smooth
    modifierName.smooth = default['smooth']

    # warp
    modifierName.warp = default['warp']

    # wave
    modifierName.wave = default['wave']

    # cloth
    modifierName.cloth = default['cloth']

    # collision
    modifierName.collision = default['collision']

    # dynamic paint
    modifierName.dynamicPaint = default['dynamic paint']

    # explode
    modifierName.explode = default['explode']

    # fluid simulation
    modifierName.fluidSimulation = default['fluid simulation']

    # ocean
    modifierName.ocean = default['ocean']

    # particle instance
    modifierName.particleInstance = default['particle instance']

    # particle system
    modifierName.particleSystem = default['particle system']

    # smoke
    modifierName.smoke = default['smoke']

    # soft body
    modifierName.softBody = default['soft body']

    # default
    default = defaults['auto name']['object data names']

    # object data name
    objectDataName = context.scene.BatchAutoName_ObjectDataNames

    # prefix
    objectDataName.prefix = default['prefix']

    # mesh
    objectDataName.mesh = default['mesh']

    # curve
    objectDataName.curve = default['curve']

    # surface
    objectDataName.surface = default['surface']

    # meta
    objectDataName.meta = default['meta']

    # font
    objectDataName.font = default['font']

    # armature
    objectDataName.armature = default['armature']

    # lattice
    objectDataName.lattice = default['lattice']

    # speaker
    objectDataName.speaker = default['speaker']

    # camera
    objectDataName.camera = default['camera']

    # lamp
    objectDataName.lamp = default['lamp']

  # name
  if name:

    # default
    default = defaults['batch name']

    # name option
    batchNameOption = context.scene.BatchName

    # mode
    batchNameOption.mode = default['mode']

    # actions
    batchNameOption.actions = default['actions']

    # action groups
    batchNameOption.actionGroups = default['action groups']

    # grease pencil
    batchNameOption.greasePencil = default['grease pencil']

    # pencil layers
    batchNameOption.pencilLayers = default['pencil layers']

    # objects
    batchNameOption.objects = default['objects']

    # groups
    batchNameOption.groups = default['groups']

    # constraints
    batchNameOption.constraints = default['constraints']

    # modifiers
    batchNameOption.modifiers = default['modifiers']

    # object data
    batchNameOption.objectData = default['object data']

    # bone groups
    batchNameOption.boneGroups = default['bone groups']

    # bones
    batchNameOption.bones = default['bones']

    # bone constraints
    batchNameOption.boneConstraints = default['bone constraints']

    # vertex groups
    batchNameOption.vertexGroups = default['vertex groups']

    # shapekeys
    batchNameOption.shapekeys = default['shapekeys']

    # uvs
    batchNameOption.uvs = default['uvs']

    # vertex colors
    batchNameOption.vertexColors = default['vertex colors']

    # materials
    batchNameOption.materials = default['materials']

    # textures
    batchNameOption.textures = default['textures']

    # particle systems
    batchNameOption.particleSystems = default['particle systems']

    # particle settings
    batchNameOption.particleSettings = default['particle settings']

    # object type
    batchNameOption.objectType = default['object type']

    # constraint type
    batchNameOption.constraintType = default['constraint type']

    # modifier type
    batchNameOption.modifierType = default['modifier type']

    # sensors
    batchNameOption.sensors = default['sensors']

    # controllers
    batchNameOption.controllers = default['controllers']

    # actuators
    batchNameOption.actuators = default['actuators']

    # line sets
    batchNameOption.lineSets = default['line sets']

    # linestyles
    batchNameOption.linestyles = default['linestyles']

    # linestyle modifiers
    batchNameOption.linestyleModifiers = default['linestyle modifiers']

    # linestyle modifier type
    batchNameOption.linestyleModifierType = default['linestyle modifier type']

    # scenes
    batchNameOption.scenes = default['scenes']

    # render layers
    batchNameOption.renderLayers = default['render layers']

    # worlds
    batchNameOption.worlds = default['worlds']

    # libraries
    batchNameOption.libraries = default['libraries']

    # images
    batchNameOption.images = default['images']

    # masks
    batchNameOption.masks = default['masks']

    # sequences
    batchNameOption.sequences = default['sequences']

    # movie clips
    batchNameOption.movieClips = default['movie clips']

    # sounds
    batchNameOption.sounds = default['sounds']

    # screens
    batchNameOption.screens = default['screens']

    # keying sets
    batchNameOption.keyingSets = default['keying sets']

    # palettes
    batchNameOption.palettes = default['palettes']

    # brushes
    batchNameOption.brushes = default['brushes']

    # nodes
    batchNameOption.nodes = default['nodes']

    # node labels
    batchNameOption.nodeLabels = default['node labels']

    # frame nodes
    batchNameOption.frameNodes = default['frame nodes']

    # node groups
    batchNameOption.nodeGroups = default['node groups']

    # texts
    batchNameOption.texts = default['texts']

    # ignore action
    batchNameOption.ignoreAction = default['ignore action']

    # ignore grease pencil
    batchNameOption.ignoreGreasePencil = default['ignore grease pencil']

    # ignore object
    batchNameOption.ignoreObject = default['ignore object']

    # ignore group
    batchNameOption.ignoreGroup = default['ignore group']

    # ignore constraint
    batchNameOption.ignoreConstraint = default['ignore constraint']

    # ignore modifier
    batchNameOption.ignoreModifier = default['ignore modifier']

    # ignore bone
    batchNameOption.ignoreBone = default['ignore bone']

    # ignore bone group
    batchNameOption.ignoreBoneGroup = default['ignore bone group']

    # ignore bone constraint
    batchNameOption.ignoreBoneConstraint = default['ignore bone constraint']

    # ignore object data
    batchNameOption.ignoreObjectData = default['ignore object data']

    # ignore vertex group
    batchNameOption.ignoreVertexGroup = default['ignore vertex group']

    # ignore shapekey
    batchNameOption.ignoreShapekey = default['ignore shapekey']

    # ignore uv
    batchNameOption.ignoreUV = default['ignore uv']

    # ignore vertex color
    batchNameOption.ignoreVertexColor = default['ignore vertex color']

    # ignore material
    batchNameOption.ignoreMaterial = default['ignore material']

    # ignore texture
    batchNameOption.ignoreTexture = default['ignore texture']

    # ignore particle system
    batchNameOption.ignoreParticleSystem = default['ignore particle system']

    # ignore particle setting
    batchNameOption.ignoreParticleSetting = default['ignore particle setting']

    # custom name
    batchNameOption.customName = default['custom name']

    # find
    batchNameOption.find = default['find']

    # regex
    batchNameOption.regex = default['regex']

    # replace
    batchNameOption.replace = default['replace']

    # prefix
    batchNameOption.prefix = default['prefix']

    # suffix
    batchNameOption.suffix = default['suffix']

    # suffix last
    batchNameOption.suffixLast = default['suffix last']

    # trim start
    batchNameOption.trimStart = default['trim start']

    # trim end
    batchNameOption.trimEnd = default['trim end']

    # sort
    batchNameOption.sort = default['sort']

    # start
    batchNameOption.start = default['start']

    # padding
    batchNameOption.padding = default['padding']

    # separator
    batchNameOption.separator = default['separator']

    # sort only
    batchNameOption.sortOnly = default['sort only']

    # link
    batchNameOption.link = default['link']

    # ignore position
    batchNameOption.ignorePosition = default['ignore position']

  # copy
  if copy:

    # default
    default = defaults['copy name']

    # copy option
    batchCopyOption = context.scene.BatchCopyName

    # mode
    batchCopyOption.mode = default['mode']

    # source
    batchCopyOption.source = default['source']

    # objects
    batchCopyOption.objects = default['objects']

    # object data
    batchCopyOption.objectData = default['object data']

    # materials
    batchCopyOption.materials = default['materials']

    # textures
    batchCopyOption.textures = default['textures']

    # particle systems
    batchCopyOption.particleSystems = default['particle systems']

    # particle settings
    batchCopyOption.particleSettings = default['particle settings']

    # use active object
    batchCopyOption.useActiveObject = default['use active object']

# transfer
def transfer(context, panel, auto, names, name, copy):
  '''
    Resets the property values for the name panel add-on.
  '''

  # panel settings
  if panel:
    for scene in bpy.data.scenes[:]:
      if scene != context.scene:

        # name panel option
        namePanelOption = context.scene.NamePanel

        # pin active object
        scene.NamePanel.pinActiveObject = namePanelOption.pinActiveObject

        # hide search
        scene.NamePanel.hideSearch = namePanelOption.hideSearch

        # filters
        scene.NamePanel.filters = namePanelOption.filters

        # options
        scene.NamePanel.options = namePanelOption.options

        # display names
        scene.NamePanel.displayNames = namePanelOption.displayNames

        # mode
        scene.NamePanel.mode = namePanelOption.mode

        # search
        scene.NamePanel.search = namePanelOption.search

        # regex
        scene.NamePanel.regex = namePanelOption.regex

        # groups
        scene.NamePanel.groups = namePanelOption.groups

        # action
        scene.NamePanel.action = namePanelOption.action

        # grease pencil
        scene.NamePanel.greasePencil = namePanelOption.greasePencil

        # constraint
        scene.NamePanel.constraints = namePanelOption.constraints

        # modifiers
        scene.NamePanel.modifiers = namePanelOption.modifiers

        # bone groups
        scene.NamePanel.boneGroups = namePanelOption.boneGroups

        # bone constraints
        scene.NamePanel.boneConstraints = namePanelOption.boneConstraints

        # vertex groups
        scene.NamePanel.vertexGroups = namePanelOption.vertexGroups

        # shapekeys
        scene.NamePanel.shapekeys = namePanelOption.shapekeys

        # uvs
        scene.NamePanel.uvs = namePanelOption.uvs

        # vertex colors
        scene.NamePanel.vertexColors = namePanelOption.vertexColors

        # materials
        scene.NamePanel.materials = namePanelOption.materials

        # textures
        scene.NamePanel.textures = namePanelOption.textures

        # particels systems
        scene.NamePanel.particleSystems = namePanelOption.particleSystems

        # display bones
        scene.NamePanel.displayBones = namePanelOption.displayBones

        # bone mode
        scene.NamePanel.boneMode = namePanelOption.boneMode

  # auto
  if auto:
    for scene in bpy.data.scenes[:]:
      if scene != context.scene:

        # auto name option
        batchAutoNameOption = context.scene.BatchAutoName

        # type
        scene.BatchAutoName.mode = batchAutoNameOption.mode

        # objects
        scene.BatchAutoName.objects = batchAutoNameOption.objects

        # constraints
        scene.BatchAutoName.constraints = batchAutoNameOption.constraints

        # modifiers
        scene.BatchAutoName.modifiers = batchAutoNameOption.modifiers

        # objectData
        scene.BatchAutoName.objectData = batchAutoNameOption.objectData

        # bone Constraints
        scene.BatchAutoName.boneConstraints = batchAutoNameOption.boneConstraints

        # object type
        scene.BatchAutoName.objectType = batchAutoNameOption.objectType

        # constraint type
        scene.BatchAutoName.constraintType = batchAutoNameOption.constraintType

        # modifier type
        scene.BatchAutoName.modifierType = batchAutoNameOption.modifierType

  # names
  if names:
    for scene in bpy.data.scenes[:]:
      if scene != context.scene:

        # object name
        objectName = context.scene.BatchAutoName_ObjectNames

        # prefix
        scene.BatchAutoName_ObjectNames.prefix = objectName.prefix

        # mesh
        scene.BatchAutoName_ObjectNames.mesh = objectName.mesh

        # curve
        scene.BatchAutoName_ObjectNames.curve = objectName.curve

        # surface
        scene.BatchAutoName_ObjectNames.surface = objectName.surface

        # meta
        scene.BatchAutoName_ObjectNames.meta = objectName.meta

        # font
        scene.BatchAutoName_ObjectNames.font = objectName.font

        # armature
        scene.BatchAutoName_ObjectNames.armature = objectName.armature

        # lattice
        scene.BatchAutoName_ObjectNames.lattice = objectName.lattice

        # empty
        scene.BatchAutoName_ObjectNames.empty = objectName.empty

        # speaker
        scene.BatchAutoName_ObjectNames.speaker = objectName.speaker

        # camera
        scene.BatchAutoName_ObjectNames.camera = objectName.camera

        # lamp
        scene.BatchAutoName_ObjectNames.lamp = objectName.lamp

        # constraint name
        constraintName = context.scene.BatchAutoName_ConstraintNames

        # prefix
        scene.BatchAutoName_ConstraintNames.prefix = constraintName.prefix

        # camera solver
        scene.BatchAutoName_ConstraintNames.cameraSolver = constraintName.cameraSolver

        # follow track
        scene.BatchAutoName_ConstraintNames.followTrack = constraintName.followTrack

        # object solver
        scene.BatchAutoName_ConstraintNames.objectSolver = constraintName.objectSolver

        # copy location
        scene.BatchAutoName_ConstraintNames.copyLocation = constraintName.copyLocation

        # copy rotation
        scene.BatchAutoName_ConstraintNames.copyRotation = constraintName.copyRotation

        # copy scale
        scene.BatchAutoName_ConstraintNames.copyScale = constraintName.copyScale

        # copy transforms
        scene.BatchAutoName_ConstraintNames.copyTransforms = constraintName.copyTransforms

        # limit distance
        scene.BatchAutoName_ConstraintNames.limitDistance = constraintName.limitDistance

        # limit location
        scene.BatchAutoName_ConstraintNames.limitLocation = constraintName.limitLocation

        # limit rotation
        scene.BatchAutoName_ConstraintNames.limitRotation = constraintName.limitRotation

        # limit scale
        scene.BatchAutoName_ConstraintNames.limitScale = constraintName.limitScale

        # maintain volume
        scene.BatchAutoName_ConstraintNames.maintainVolume = constraintName.maintainVolume

        # transform
        scene.BatchAutoName_ConstraintNames.transform = constraintName.transform

        # clamp to
        scene.BatchAutoName_ConstraintNames.clampTo = constraintName.clampTo

        # damped track
        scene.BatchAutoName_ConstraintNames.dampedTrack = constraintName.dampedTrack

        # inverse kinematics
        scene.BatchAutoName_ConstraintNames.inverseKinematics = constraintName.inverseKinematics

        # locked track
        scene.BatchAutoName_ConstraintNames.lockedTrack = constraintName.lockedTrack

        # spline inverse kinematics
        scene.BatchAutoName_ConstraintNames.splineInverseKinematics = constraintName.splineInverseKinematics

        # stretch to
        scene.BatchAutoName_ConstraintNames.stretchTo = constraintName.stretchTo

        # track to
        scene.BatchAutoName_ConstraintNames.trackTo = constraintName.trackTo

        # action
        scene.BatchAutoName_ConstraintNames.action = constraintName.action

        # child of
        scene.BatchAutoName_ConstraintNames.childOf = constraintName.childOf

        # floor
        scene.BatchAutoName_ConstraintNames.floor = constraintName.floor

        # follow path
        scene.BatchAutoName_ConstraintNames.followPath = constraintName.followPath

        # pivot
        scene.BatchAutoName_ConstraintNames.pivot = constraintName.pivot

        # rigid body joint
        scene.BatchAutoName_ConstraintNames.rigidBodyJoint = constraintName.rigidBodyJoint

        # shrinkwrap
        scene.BatchAutoName_ConstraintNames.shrinkwrap = constraintName.shrinkwrap

        # modifier name
        modifierName = context.scene.BatchAutoName_ModifierNames

        # prefix
        scene.BatchAutoName_ModifierNames.prefix = modifierName.prefix

        # data transfer
        scene.BatchAutoName_ModifierNames.dataTransfer = modifierName.dataTransfer

        # mesh cache
        scene.BatchAutoName_ModifierNames.meshCache = modifierName.meshCache

        # normal edit
        scene.BatchAutoName_ModifierNames.normalEdit = modifierName.normalEdit

        # uv project
        scene.BatchAutoName_ModifierNames.uvProject = modifierName.uvProject

        # uv warp
        scene.BatchAutoName_ModifierNames.uvWarp = modifierName.uvWarp

        # vertex weight edit
        scene.BatchAutoName_ModifierNames.vertexWeightEdit = modifierName.vertexWeightEdit

        # vertex weight mix
        scene.BatchAutoName_ModifierNames.vertexWeightMix = modifierName.vertexWeightMix

        # vertex weight proximity
        scene.BatchAutoName_ModifierNames.vertexWeightProximity = modifierName.vertexWeightProximity

        # array
        scene.BatchAutoName_ModifierNames.array = modifierName.array

        # bevel
        scene.BatchAutoName_ModifierNames.bevel = modifierName.bevel

        # boolean
        scene.BatchAutoName_ModifierNames.boolean = modifierName.boolean

        # build
        scene.BatchAutoName_ModifierNames.build = modifierName.build

        # decimate
        scene.BatchAutoName_ModifierNames.decimate = modifierName.decimate

        # edge split
        scene.BatchAutoName_ModifierNames.edgeSplit = modifierName.edgeSplit

        # mask
        scene.BatchAutoName_ModifierNames.mask = modifierName.mask

        # mirror
        scene.BatchAutoName_ModifierNames.mirror = modifierName.mirror

        # multiresolution
        scene.BatchAutoName_ModifierNames.multiresolution = modifierName.multiresolution

        # remesh
        scene.BatchAutoName_ModifierNames.remesh = modifierName.remesh

        # screw
        scene.BatchAutoName_ModifierNames.screw = modifierName.screw

        # skin
        scene.BatchAutoName_ModifierNames.skin = modifierName.skin

        # solidify
        scene.BatchAutoName_ModifierNames.solidify = modifierName.solidify

        # subdivision surface
        scene.BatchAutoName_ModifierNames.subdivisionSurface = modifierName.subdivisionSurface

        # triangulate
        scene.BatchAutoName_ModifierNames.triangulate = modifierName.triangulate

        # wireframe
        scene.BatchAutoName_ModifierNames.wireframe = modifierName.wireframe

        # armature
        scene.BatchAutoName_ModifierNames.armature = modifierName.armature

        # cast
        scene.BatchAutoName_ModifierNames.cast = modifierName.cast

        # corrective smooth
        scene.BatchAutoName_ModifierNames.correctiveSmooth = modifierName.correctiveSmooth

        # curve
        scene.BatchAutoName_ModifierNames.curve = modifierName.curve

        # displace
        scene.BatchAutoName_ModifierNames.displace = modifierName.displace

        # hook
        scene.BatchAutoName_ModifierNames.hook = modifierName.hook

        # laplacian smooth
        scene.BatchAutoName_ModifierNames.laplacianSmooth = modifierName.laplacianSmooth

        # laplacian deform
        scene.BatchAutoName_ModifierNames.laplacianDeform = modifierName.laplacianDeform

        # lattice
        scene.BatchAutoName_ModifierNames.lattice = modifierName.lattice

        # mesh deform
        scene.BatchAutoName_ModifierNames.meshDeform = modifierName.meshDeform

        # shrinkwrap
        scene.BatchAutoName_ModifierNames.shrinkwrap = modifierName.shrinkwrap

        # simple deform
        scene.BatchAutoName_ModifierNames.simpleDeform = modifierName.simpleDeform

        # smooth
        scene.BatchAutoName_ModifierNames.smooth = modifierName.smooth

        # warp
        scene.BatchAutoName_ModifierNames.warp = modifierName.warp

        # wave
        scene.BatchAutoName_ModifierNames.wave = modifierName.wave

        # cloth
        scene.BatchAutoName_ModifierNames.cloth = modifierName.cloth

        # collision
        scene.BatchAutoName_ModifierNames.collision = modifierName.collision

        # dynamic paint
        scene.BatchAutoName_ModifierNames.dynamicPaint = modifierName.dynamicPaint

        # explode
        scene.BatchAutoName_ModifierNames.explode = modifierName.explode

        # fluid simulation
        scene.BatchAutoName_ModifierNames.fluidSimulation = modifierName.fluidSimulation

        # ocean
        scene.BatchAutoName_ModifierNames.ocean = modifierName.ocean

        # particle instance
        scene.BatchAutoName_ModifierNames.particleInstance = modifierName.particleInstance

        # particle system
        scene.BatchAutoName_ModifierNames.particleSystem = modifierName.particleSystem

        # smoke
        scene.BatchAutoName_ModifierNames.smoke = modifierName.smoke

        # soft body
        scene.BatchAutoName_ModifierNames.softBody = modifierName.softBody

        # object data name
        objectDataName = context.scene.BatchAutoName_ObjectDataNames

        # prefix
        scene.BatchAutoName_ObjectDataNames.prefix = objectDataName.prefix

        # mesh
        scene.BatchAutoName_ObjectDataNames.mesh = objectDataName.mesh

        # curve
        scene.BatchAutoName_ObjectDataNames.curve = objectDataName.curve

        # surface
        scene.BatchAutoName_ObjectDataNames.surface = objectDataName.surface

        # meta
        scene.BatchAutoName_ObjectDataNames.meta = objectDataName.meta

        # font
        scene.BatchAutoName_ObjectDataNames.font = objectDataName.font

        # armature
        scene.BatchAutoName_ObjectDataNames.armature = objectDataName.armature

        # lattice
        scene.BatchAutoName_ObjectDataNames.lattice = objectDataName.lattice

        # speaker
        scene.BatchAutoName_ObjectDataNames.speaker = objectDataName.speaker

        # camera
        scene.BatchAutoName_ObjectDataNames.camera = objectDataName.camera

        # lamp
        scene.BatchAutoName_ObjectDataNames.lamp = objectDataName.lamp

  # name
  if name:
    for scene in bpy.data.scenes:
      if scene != context.scene:

        # name option
        batchNameOption = context.scene.BatchName

        # batch type
        scene.BatchName.mode = batchNameOption.mode

        # actions
        scene.BatchName.actions = batchNameOption.actions

        # action groups
        scene.BatchName.actionGroups = batchNameOption.actionGroups

        # grease pencil
        scene.BatchName.greasePencil = batchNameOption.greasePencil

        # pencil layers
        scene.BatchName.pencilLayers = batchNameOption.pencilLayers

        # objects
        scene.BatchName.objects = batchNameOption.objects

        # groups
        scene.BatchName.groups = batchNameOption.groups

        # constraints
        scene.BatchName.constraints = batchNameOption.constraints

        # modifiers
        scene.BatchName.modifiers = batchNameOption.modifiers

        # object data
        scene.BatchName.objectData = batchNameOption.objectData

        # bone groups
        scene.BatchName.boneGroups = batchNameOption.boneGroups

        # bones
        scene.BatchName.bones = batchNameOption.bones

        # bone constraints
        scene.BatchName.boneConstraints = batchNameOption.boneConstraints

        # vertex groups
        scene.BatchName.vertexGroups = batchNameOption.vertexGroups

        # shapekeys
        scene.BatchName.shapekeys = batchNameOption.shapekeys

        # uvs
        scene.BatchName.uvs = batchNameOption.uvs

        # vertex colors
        scene.BatchName.vertexColors = batchNameOption.vertexColors

        # materials
        scene.BatchName.materials = batchNameOption.materials

        # textures
        scene.BatchName.textures = batchNameOption.textures

        # particle systems
        scene.BatchName.particleSystems = batchNameOption.particleSystems

        # particle settings
        scene.BatchName.particleSettings = batchNameOption.particleSettings

        # object type
        scene.BatchName.objectType = batchNameOption.objectType

        # constraint type
        scene.BatchName.constraintType = batchNameOption.constraintType

        # modifier type
        scene.BatchName.modifierType = batchNameOption.modifierType

        # sensors
        scene.BatchName.sensors = batchNameOption.sensors

        # controllers
        scene.BatchName.controllers = batchNameOption.controllers

        # actuators
        scene.BatchName.actuators = batchNameOption.actuators

        # line sets
        scene.BatchName.lineSets = batchNameOption.lineSets

        # linestyles
        scene.BatchName.linestyles = batchNameOption.linestyles

        # linestyle modifiers
        scene.BatchName.linestyleModifiers = batchNameOption.linestyleModifiers

        # linestyle modifier type
        scene.BatchName.linestyleModifierType = batchNameOption.linestyleModifierType

        # scenes
        scene.BatchName.scenes = batchNameOption.scenes

        # render layers
        scene.BatchName.renderLayers = batchNameOption.renderLayers

        # worlds
        scene.BatchName.worlds = batchNameOption.worlds

        # libraries
        scene.BatchName.libraries = batchNameOption.libraries

        # images
        scene.BatchName.images = batchNameOption.images

        # masks
        scene.BatchName.masks = batchNameOption.masks

        # sequences
        scene.BatchName.sequences = batchNameOption.sequences

        # movie clips
        scene.BatchName.movieClips = batchNameOption.movieClips

        # sounds
        scene.BatchName.sounds = batchNameOption.sounds

        # screens
        scene.BatchName.screens = batchNameOption.screens

        # keying sets
        scene.BatchName.keyingSets = batchNameOption.keyingSets

        # palettes
        scene.BatchName.palettes = batchNameOption.palettes

        # brushes
        scene.BatchName.brushes = batchNameOption.brushes

        # linestyles
        scene.BatchName.linestyles = batchNameOption.linestyles

        # nodes
        scene.BatchName.nodes = batchNameOption.nodes

        # node labels
        scene.BatchName.nodeLabels = batchNameOption.nodeLabels

        # frame nodes
        scene.BatchName.frameNodes = batchNameOption.frameNodes

        # node groups
        scene.BatchName.nodeGroups = batchNameOption.nodeGroups

        # texts
        scene.BatchName.texts = batchNameOption.texts

        # ignore action
        scene.BatchName.ignoreAction = batchNameOption.ignoreAction

        # ignore grease pencil
        scene.BatchName.ignoreGreasePencil = batchNameOption.ignoreGreasePencil

        # ignore object
        scene.BatchName.ignoreObject = batchNameOption.ignoreObject

        # ignore group
        scene.BatchName.ignoreGroup = batchNameOption.ignoreGroup

        # ignore constraint
        scene.BatchName.ignoreConstraint = batchNameOption.ignoreConstraint

        # ignore modifier
        scene.BatchName.ignoreModifier = batchNameOption.ignoreModifier

        # ignore bone
        scene.BatchName.ignoreBone = batchNameOption.ignoreBone

        # ignore bone group
        scene.BatchName.ignoreBoneGroup = batchNameOption.ignoreBoneGroup

        # ignore bone constraint
        scene.BatchName.ignoreBoneConstraint = batchNameOption.ignoreBoneConstraint

        # ignore object data
        scene.BatchName.ignoreObjectData = batchNameOption.ignoreObjectData

        # ignore vertex group
        scene.BatchName.ignoreVertexGroup = batchNameOption.ignoreVertexGroup

        # ignore shapekey
        scene.BatchName.ignoreShapekey = batchNameOption.ignoreShapekey

        # ignore uv
        scene.BatchName.ignoreUV = batchNameOption.ignoreUV

        # ignore vertex color
        scene.BatchName.ignoreVertexColor = batchNameOption.ignoreVertexColor

        # ignore material
        scene.BatchName.ignoreMaterial = batchNameOption.ignoreMaterial

        # ignore texture
        scene.BatchName.ignoreTexture = batchNameOption.ignoreTexture

        # ignore particle system
        scene.BatchName.ignoreParticleSystem = batchNameOption.ignoreParticleSystem

        # ignore particle setting
        scene.BatchName.ignoreParticleSetting = batchNameOption.ignoreParticleSetting

        # custom name
        scene.BatchName.customName = batchNameOption.customName

        # find
        scene.BatchName.find = batchNameOption.find

        # regex
        scene.BatchName.regex = batchNameOption.regex

        # replace
        scene.BatchName.replace = batchNameOption.replace

        # prefix
        scene.BatchName.prefix = batchNameOption.prefix

        # suffix
        scene.BatchName.suffix = batchNameOption.suffix

        # suffix last
        scene.BatchName.suffixLast = batchNameOption.suffixLast

        # trim start
        scene.BatchName.trimStart = batchNameOption.trimStart

        # trim end
        scene.BatchName.trimEnd = batchNameOption.trimEnd

        # sort
        scene.BatchName.sort = batchNameOption.sort

        # start
        scene.BatchName.start = batchNameOption.start

        # padding
        scene.BatchName.padding = batchNameOption.padding

        # separator
        scene.BatchName.separator = batchNameOption.separator

        # sort only
        scene.BatchName.sortOnly = batchNameOption.sortOnly

        # link
        scene.BatchName.link = batchNameOption.link

        # ignore position
        scene.BatchName.ignorePosition = batchNameOption.ignorePosition

  # copy
  if copy:
    for scene in bpy.data.scenes[:]:
      if scene != context.scene:

        # copy option
        batchCopyOption = context.scene.BatchCopyName

        # type
        scene.BatchCopyName.mode = batchCopyOption.mode

        # source
        scene.BatchCopyName.source = batchCopyOption.source

        # objects
        scene.BatchCopyName.objects = batchCopyOption.objects

        # object datas
        scene.BatchCopyName.objectData = batchCopyOption.objectData

        # materials
        scene.BatchCopyName.materials = batchCopyOption.materials

        # textures
        scene.BatchCopyName.textures = batchCopyOption.textures

        # particle systems
        scene.BatchCopyName.particleSystems = batchCopyOption.particleSystems

        # particle settings
        scene.BatchCopyName.particleSettings = batchCopyOption.particleSettings

        # use active object
        scene.BatchCopyName.useActiveObject = batchCopyOption.useActiveObject
