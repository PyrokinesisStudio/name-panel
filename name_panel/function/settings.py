
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

# reset
def reset(context, panel, auto, names, name, copy):
  '''
    Resets the property values for the name panel add-on.
  '''

  # panel
  if panel:

    # name panel option
    namePanelOption = context.scene.namePanelSettings

    # filters
    namePanelOption.filters = False

    # options
    namePanelOption.options = False

    # selected
    namePanelOption.selected = False

    # pin active object
    namePanelOption.pinActiveObject = True

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

    # selected bones
    namePanelOption.selectedBones = False

  # auto
  if auto:

    # batch auto name option
    batchAutoNameOption = context.scene.batchAutoNameSettings

    # batch type
    batchAutoNameOption.batchType = 'SELECTED'

    # objects
    batchAutoNameOption.objects = False

    # constraints
    batchAutoNameOption.constraints = False

    # modifiers
    batchAutoNameOption.modifiers = False

    # objectData
    batchAutoNameOption.objectData = False

    # bone Constraints
    batchAutoNameOption.boneConstraints = False

    # object type
    batchAutoNameOption.objectType = 'ALL'

    # constraint type
    batchAutoNameOption.constraintType = 'ALL'

    # modifier type
    batchAutoNameOption.modifierType = 'ALL'

  # names
  if names:

    # object name
    objectName = context.scene.batchAutoNameObjectNames

    # mesh
    objectName.mesh = 'Mesh'

    # curve
    objectName.curve = 'Curve'

    # surface
    objectName.surface = 'Surface'

    # meta
    objectName.meta = 'Meta'

    # font
    objectName.font = 'Text'

    # armature
    objectName.armature = 'Armature'

    # lattice
    objectName.lattice = 'Lattice'

    # empty
    objectName.empty = 'Empty'

    # speaker
    objectName.speaker = 'Speaker'

    # camera
    objectName.camera = 'Camera'

    # lamp
    objectName.lamp = 'Lamp'

    # constraint name
    constraintName = context.scene.batchAutoNameConstraintNames

    # camera solver
    constraintName.cameraSolver = 'Camera Solver'

    # follow track
    constraintName.followTrack = 'Follow Track'

    # object solver
    constraintName.objectSolver = 'Object Solver'

    # copy location
    constraintName.copyLocation = 'Copy Location'

    # copy rotation
    constraintName.copyRotation = 'Copy Rotation'

    # copy scale
    constraintName.copyScale = 'Copy Scale'

    # copy transforms
    constraintName.copyTransforms = 'Copy Transforms'

    # limit distance
    constraintName.limitDistance = 'Limit Distance'

    # limit location
    constraintName.limitLocation = 'Limit Location'

    # limit rotation
    constraintName.limitRotation = 'Limit Rotation'

    # limit scale
    constraintName.limitScale = 'Limit Scale'

    # maintain volume
    constraintName.maintainVolume = 'Maintain Volume'

    # transform
    constraintName.transform = 'Transform'

    # clamp to
    constraintName.clampTo = 'Clamp To'

    # damped track
    constraintName.dampedTrack = 'Damped Track'

    # inverse kinematics
    constraintName.inverseKinematics = 'Inverse Kinematics'

    # locked track
    constraintName.lockedTrack = 'Locked Track'

    # spline inverse kinematics
    constraintName.splineInverseKinematics = 'Spline Inverse Kinematics'

    # stretch to
    constraintName.stretchTo = 'Stretch To'

    # track to
    constraintName.trackTo = 'Track To'

    # action
    constraintName.action = 'Action'

    # child of
    constraintName.childOf = 'Child Of'

    # floor
    constraintName.floor = 'Floor'

    # follow path
    constraintName.followPath = 'Follow Path'

    # pivot
    constraintName.pivot = 'Pivot'

    # rigid body joint
    constraintName.rigidBodyJoint = 'Rigid Body Joint'

    # shrinkwrap
    constraintName.shrinkwrap = 'Shrinkwrap'

    # modifier name
    modifierName = context.scene.batchAutoNameModifierNames

    # data transfer
    modifierName.dataTransfer = 'Data Transfer'

    # mesh cache
    modifierName.meshCache = 'Mesh Cache'

    # normal edit
    modifierName.normalEdit = 'Normal Edit'

    # uv project
    modifierName.uvProject = 'UV Project'

    # uv warp
    modifierName.uvWarp = 'UV Warp'

    # vertex weight edit
    modifierName.vertexWeightEdit = 'Vertex Weight Edit'

    # vertex weight mix
    modifierName.vertexWeightMix = 'Vertex Weight Mix'

    # vertex weight proximity
    modifierName.vertexWeightProximity = 'Vertex Weight Proximity'

    # array
    modifierName.array = 'Array'

    # bevel
    modifierName.bevel = 'Bevel'

    # boolean
    modifierName.boolean = 'Boolean'

    # build
    modifierName.build = 'Build'

    # decimate
    modifierName.decimate = 'Decimate'

    # edge split
    modifierName.edgeSplit = 'Edge Split'

    # mask
    modifierName.mask = 'Mask'

    # mirror
    modifierName.mirror = 'Mirror'

    # multiresolution
    modifierName.multiresolution = 'Multiresolution'

    # remesh
    modifierName.remesh = 'Remesh'

    # screw
    modifierName.screw = 'Screw'

    # skin
    modifierName.skin = 'Skin'

    # solidify
    modifierName.solidify = 'Solidify'

    # subdivision surface
    modifierName.subdivisionSurface = 'Subdivision Surface'

    # triangulate
    modifierName.triangulate = 'Triangulate'

    # wireframe
    modifierName.wireframe = 'Wireframe'

    # armature
    modifierName.armature = 'Armature'

    # cast
    modifierName.cast = 'Cast'

    # corrective smooth
    modifierName.correctiveSmooth = 'Corrective Smooth'

    # curve
    modifierName.curve = 'Curve'

    # displace
    modifierName.displace = 'Displace'

    # hook
    modifierName.hook = 'Hook'

    # laplacian smooth
    modifierName.laplacianSmooth = 'Laplacian Smooth'

    # laplacian deform
    modifierName.laplacianDeform = 'Laplacian Deform'

    # lattice
    modifierName.lattice = 'Lattice'

    # mesh deform
    modifierName.meshDeform = 'Mesh Deform'

    # shrinkwrap
    modifierName.shrinkwrap = 'Shrinkwrap'

    # simple deform
    modifierName.simpleDeform = 'Simple Deform'

    # smooth
    modifierName.smooth = 'Smooth'

    # warp
    modifierName.warp = 'Warp'

    # wave
    modifierName.wave = 'Wave'

    # cloth
    modifierName.cloth = 'Cloth'

    # collision
    modifierName.collision = 'Collision'

    # dynamic paint
    modifierName.dynamicPaint = 'Dynamic Paint'

    # explode
    modifierName.explode = 'Explode'

    # fluid simulation
    modifierName.fluidSimulation = 'Fluid Simulation'

    # ocean
    modifierName.ocean = 'Ocean'

    # particle instance
    modifierName.particleInstance = 'Particle Instance'

    # particle system
    modifierName.particleSystem = 'Particle System'

    # smoke
    modifierName.smoke = 'Smoke'

    # soft body
    modifierName.softBody = 'Soft Body'

    # object data names

    # mesh
    modifierName.mesh = 'Mesh'

    # curve
    modifierName.curve = 'Curve'

    # surface
    modifierName.surface = 'Surface'

    # meta
    modifierName.meta = 'Meta'

    # font
    modifierName.font = 'Text'

    # armature
    modifierName.armature = 'Armature'

    # lattice
    modifierName.lattice = 'Lattice'

    # empty
    modifierName.empty = 'Empty'

    # speaker
    modifierName.speaker = 'Speaker'

    # camera
    modifierName.camera = 'Camera'

    # lamp
    modifierName.lamp = 'Lamp'

    # object data name
    objectDataName = context.scene.batchAutoNameObjectDataNames

    # mesh
    objectDataName.mesh = 'Mesh'

    # curve
    objectDataName.curve = 'Curve'

    # surface
    objectDataName.surface = 'Surface'

    # meta
    objectDataName.meta = 'Meta'

    # font
    objectDataName.font = 'Text'

    # armature
    objectDataName.armature = 'Armature'

    # lattice
    objectDataName.lattice = 'Lattice'

    # speaker
    objectDataName.speaker = 'Speaker'

    # camera
    objectDataName.camera = 'Camera'

    # lamp
    objectDataName.lamp = 'Lamp'

  # name
  if name:

    # batch name option
    batchNameOption = context.scene.batchNameSettings

    # batch type
    batchNameOption.batchType = 'SELECTED'

    # batch objects
    batchNameOption.objects = False

    # batch groups
    batchNameOption.groups = False

    # batch actions
    batchNameOption.actions = False

    # batch grease pencil
    batchNameOption.greasePencil = False

    # batch object constraints
    batchNameOption.constraints = False

    # batch modifiers
    batchNameOption.modifiers = False

    # batch object data
    batchNameOption.objectData = False

    # batch bones
    batchNameOption.bones = False

    # batch bone constraints
    batchNameOption.boneConstraints = False

    # batch materials
    batchNameOption.materials = False

    # batch textures
    batchNameOption.textures = False

    # batch particle systems
    batchNameOption.particleSystems = False

    # batch particle settings
    batchNameOption.particleSettings = False

    # batch vertex groups
    batchNameOption.vertexGroups = False

    # batch shape keys
    batchNameOption.shapekeys = False

    # batch uvs
    batchNameOption.uvs = False

    # batch vertex colors
    batchNameOption.vertexColors = False

    # batch bone groups
    batchNameOption.boneGroups = False

    # object type
    batchNameOption.objectType = 'ALL'

    # constraint type
    batchNameOption.constraintType = 'ALL'

    # modifier type
    batchNameOption.modifierType = 'ALL'

    # scenes
    batchNameOption.scenes = False

    # render layers
    batchNameOption.renderLayers = False

    # worlds
    batchNameOption.worlds = False

    # libraries
    batchNameOption.libraries = False

    # images
    batchNameOption.images = False

    # masks
    batchNameOption.masks = False

    # sequences
    batchNameOption.sequences = False

    # movie clips
    batchNameOption.movieClips = False

    # sounds
    batchNameOption.sounds = False

    # layouts
    batchNameOption.screens = False

    # keying sets
    batchNameOption.keyingSets = False

    # palettes
    batchNameOption.palettes = False

    # brushes
    batchNameOption.brushes = False

    # linestyles
    batchNameOption.linestyles = False

    # nodes
    batchNameOption.nodes = False

    # node labels
    batchNameOption.nodeLabels = False

    # node groups
    batchNameOption.nodeGroups = False

    # texts
    batchNameOption.texts = False

    # custom name
    batchNameOption.customName = ''

    # find
    batchNameOption.find = ''

    # regex
    batchNameOption.regex = False

    # replace
    batchNameOption.replace = ''

    # prefix
    batchNameOption.prefix = ''

    # suffix
    batchNameOption.suffix = ''

    # trim start
    batchNameOption.trimStart = 0

    # trim end
    batchNameOption.trimEnd = 0

    # process
    batchNameOption.sort = False

    # padding
    batchNameOption.padding = 0

    # start
    batchNameOption.start = 1

    # separator
    batchNameOption.separator = '.'

    # process only
    batchNameOption.sortOnly = False

  # copy
  if copy:

    # batch copy option
    batchCopyOption = context.scene.batchCopySettings

    # batch type
    batchCopyOption.batchType = 'SELECTED'

    # source
    batchCopyOption.source = 'OBJECT'

    # objects
    batchCopyOption.objects = False

    # object datas
    batchCopyOption.objectData = False

    # materials
    batchCopyOption.materials = False

    # textures
    batchCopyOption.textures = False

    # particle systems
    batchCopyOption.particleSystems = False

    # particle settings
    batchCopyOption.particleSettings = False

    # use active object
    batchCopyOption.useActiveObject = False

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
        namePanelOption = context.scene.namePanelSettings

        # filters
        scene.namePanelSettings.filters = namePanelOption.filters

        # options
        scene.namePanelSettings.options = namePanelOption.options

        # selected
        scene.namePanelSettings.selected = namePanelOption.selected

        # pin active object
        scene.namePanelSettings.pinActiveObject = namePanelOption.pinActiveObject

        # groups
        scene.namePanelSettings.groups = namePanelOption.groups

        # action
        scene.namePanelSettings.action = namePanelOption.action

        # grease pencil
        scene.namePanelSettings.greasePencil = namePanelOption.greasePencil

        # constraint
        scene.namePanelSettings.constraints = namePanelOption.constraints

        # modifiers
        scene.namePanelSettings.modifiers = namePanelOption.modifiers

        # bone groups
        scene.namePanelSettings.boneGroups = namePanelOption.boneGroups

        # bone constraints
        scene.namePanelSettings.boneConstraints = namePanelOption.boneConstraints

        # vertex groups
        scene.namePanelSettings.vertexGroups = namePanelOption.vertexGroups

        # shapekeys
        scene.namePanelSettings.shapekeys = namePanelOption.shapekeys

        # uvs
        scene.namePanelSettings.uvs = namePanelOption.uvs

        # vertex colors
        scene.namePanelSettings.vertexColors = namePanelOption.vertexColors

        # materials
        scene.namePanelSettings.materials = namePanelOption.materials

        # textures
        scene.namePanelSettings.textures = namePanelOption.textures

        # particels systems
        scene.namePanelSettings.particleSystems = namePanelOption.particleSystems

        # selected bones
        scene.namePanelSettings.selectedBones = namePanelOption.selectedBones

  # auto
  if auto:
    for scene in bpy.data.scenes[:]:
      if scene != context.scene:

        # auto name option
        batchAutoNameOption = context.scene.batchAutoNameSettings

        # batch type
        scene.batchAutoNameSettings.batchType = batchAutoNameOption.batchType

        # objects
        scene.batchAutoNameSettings.objects = batchAutoNameOption.objects

        # constraints
        scene.batchAutoNameSettings.constraints = batchAutoNameOption.constraints

        # modifiers
        scene.batchAutoNameSettings.modifiers = batchAutoNameOption.modifiers

        # objectData
        scene.batchAutoNameSettings.objectData = batchAutoNameOption.objectData

        # bone Constraints
        scene.batchAutoNameSettings.boneConstraints = batchAutoNameOption.boneConstraints

        # object type
        scene.batchAutoNameSettings.objectType = batchAutoNameOption.objectType

        # constraint type
        scene.batchAutoNameSettings.constraintType = batchAutoNameOption.constraintType

        # modifier type
        scene.batchAutoNameSettings.modifierType = batchAutoNameOption.modifierType

  # names
  if names:
    for scene in bpy.data.scenes[:]:
      if scene != context.scene:

        # object name
        objectName = context.scene.batchAutoNameObjectNames

        # mesh
        scene.batchAutoNameObjectNames.mesh = objectName.mesh

        # curve
        scene.batchAutoNameObjectNames.curve = objectName.curve

        # surface
        scene.batchAutoNameObjectNames.surface = objectName.surface

        # meta
        scene.batchAutoNameObjectNames.meta = objectName.meta

        # font
        scene.batchAutoNameObjectNames.font = objectName.font

        # armature
        scene.batchAutoNameObjectNames.armature = objectName.armature

        # lattice
        scene.batchAutoNameObjectNames.lattice = objectName.lattice

        # empty
        scene.batchAutoNameObjectNames.empty = objectName.empty

        # speaker
        scene.batchAutoNameObjectNames.speaker = objectName.speaker

        # camera
        scene.batchAutoNameObjectNames.camera = objectName.camera

        # lamp
        scene.batchAutoNameObjectNames.lamp = objectName.lamp

        # constraint name
        constraintName = context.scene.batchAutoNameConstraintNames

        # camera solver
        scene.batchAutoNameConstraintNames.cameraSolver = constraintName.cameraSolver

        # follow track
        scene.batchAutoNameConstraintNames.followTrack = constraintName.followTrack

        # object solver
        scene.batchAutoNameConstraintNames.objectSolver = constraintName.objectSolver

        # copy location
        scene.batchAutoNameConstraintNames.copyLocation = constraintName.copyLocation

        # copy rotation
        scene.batchAutoNameConstraintNames.copyRotation = constraintName.copyRotation

        # copy scale
        scene.batchAutoNameConstraintNames.copyScale = constraintName.copyScale

        # copy transforms
        scene.batchAutoNameConstraintNames.copyTransforms = constraintName.copyTransforms

        # limit distance
        scene.batchAutoNameConstraintNames.limitDistance = constraintName.limitDistance

        # limit location
        scene.batchAutoNameConstraintNames.limitLocation = constraintName.limitLocation

        # limit rotation
        scene.batchAutoNameConstraintNames.limitRotation = constraintName.limitRotation

        # limit scale
        scene.batchAutoNameConstraintNames.limitScale = constraintName.limitScale

        # maintain volume
        scene.batchAutoNameConstraintNames.maintainVolume = constraintName.maintainVolume

        # transform
        scene.batchAutoNameConstraintNames.transform = constraintName.transform

        # clamp to
        scene.batchAutoNameConstraintNames.clampTo = constraintName.clampTo

        # damped track
        scene.batchAutoNameConstraintNames.dampedTrack = constraintName.dampedTrack

        # inverse kinematics
        scene.batchAutoNameConstraintNames.inverseKinematics = constraintName.inverseKinematics

        # locked track
        scene.batchAutoNameConstraintNames.lockedTrack = constraintName.lockedTrack

        # spline inverse kinematics
        scene.batchAutoNameConstraintNames.splineInverseKinematics = constraintName.splineInverseKinematics

        # stretch to
        scene.batchAutoNameConstraintNames.stretchTo = constraintName.stretchTo

        # track to
        scene.batchAutoNameConstraintNames.trackTo = constraintName.trackTo

        # action
        scene.batchAutoNameConstraintNames.action = constraintName.action

        # child of
        scene.batchAutoNameConstraintNames.childOf = constraintName.childOf

        # floor
        scene.batchAutoNameConstraintNames.floor = constraintName.floor

        # follow path
        scene.batchAutoNameConstraintNames.followPath = constraintName.followPath

        # pivot
        scene.batchAutoNameConstraintNames.pivot = constraintName.pivot

        # rigid body joint
        scene.batchAutoNameConstraintNames.rigidBodyJoint = constraintName.rigidBodyJoint

        # shrinkwrap
        scene.batchAutoNameConstraintNames.shrinkwrap = constraintName.shrinkwrap

        # modifier name
        modifierName = context.scene.batchAutoNameModifierNames

        # data transfer
        scene.batchAutoNameModifierNames.dataTransfer = modifierName.dataTransfer

        # mesh cache
        scene.batchAutoNameModifierNames.meshCache = modifierName.meshCache

        # normal edit
        scene.batchAutoNameModifierNames.normalEdit = modifierName.normalEdit

        # uv project
        scene.batchAutoNameModifierNames.uvProject = modifierName.uvProject

        # uv warp
        scene.batchAutoNameModifierNames.uvWarp = modifierName.uvWarp

        # vertex weight edit
        scene.batchAutoNameModifierNames.vertexWeightEdit = modifierName.vertexWeightEdit

        # vertex weight mix
        scene.batchAutoNameModifierNames.vertexWeightMix = modifierName.vertexWeightMix

        # vertex weight proximity
        scene.batchAutoNameModifierNames.vertexWeightProximity = modifierName.vertexWeightProximity

        # array
        scene.batchAutoNameModifierNames.array = modifierName.array

        # bevel
        scene.batchAutoNameModifierNames.bevel = modifierName.bevel

        # boolean
        scene.batchAutoNameModifierNames.boolean = modifierName.boolean

        # build
        scene.batchAutoNameModifierNames.build = modifierName.build

        # decimate
        scene.batchAutoNameModifierNames.decimate = modifierName.decimate

        # edge split
        scene.batchAutoNameModifierNames.edgeSplit = modifierName.edgeSplit

        # mask
        scene.batchAutoNameModifierNames.mask = modifierName.mask

        # mirror
        scene.batchAutoNameModifierNames.mirror = modifierName.mirror

        # multiresolution
        scene.batchAutoNameModifierNames.multiresolution = modifierName.multiresolution

        # remesh
        scene.batchAutoNameModifierNames.remesh = modifierName.remesh

        # screw
        scene.batchAutoNameModifierNames.screw = modifierName.screw

        # skin
        scene.batchAutoNameModifierNames.skin = modifierName.skin

        # solidify
        scene.batchAutoNameModifierNames.solidify = modifierName.solidify

        # subdivision surface
        scene.batchAutoNameModifierNames.subdivisionSurface = modifierName.subdivisionSurface

        # triangulate
        scene.batchAutoNameModifierNames.triangulate = modifierName.triangulate

        # wireframe
        scene.batchAutoNameModifierNames.wireframe = modifierName.wireframe

        # armature
        scene.batchAutoNameModifierNames.armature = modifierName.armature

        # cast
        scene.batchAutoNameModifierNames.cast = modifierName.cast

        # corrective smooth
        scene.batchAutoNameModifierNames.correctiveSmooth = modifierName.correctiveSmooth

        # curve
        scene.batchAutoNameModifierNames.curve = modifierName.curve

        # displace
        scene.batchAutoNameModifierNames.displace = modifierName.displace

        # hook
        scene.batchAutoNameModifierNames.hook = modifierName.hook

        # laplacian smooth
        scene.batchAutoNameModifierNames.laplacianSmooth = modifierName.laplacianSmooth

        # laplacian deform
        scene.batchAutoNameModifierNames.laplacianDeform = modifierName.laplacianDeform

        # lattice
        scene.batchAutoNameModifierNames.lattice = modifierName.lattice

        # mesh deform
        scene.batchAutoNameModifierNames.meshDeform = modifierName.meshDeform

        # shrinkwrap
        scene.batchAutoNameModifierNames.shrinkwrap = modifierName.shrinkwrap

        # simple deform
        scene.batchAutoNameModifierNames.simpleDeform = modifierName.simpleDeform

        # smooth
        scene.batchAutoNameModifierNames.smooth = modifierName.smooth

        # warp
        scene.batchAutoNameModifierNames.warp = modifierName.warp

        # wave
        scene.batchAutoNameModifierNames.wave = modifierName.wave

        # cloth
        scene.batchAutoNameModifierNames.cloth = modifierName.cloth

        # collision
        scene.batchAutoNameModifierNames.collision = modifierName.collision

        # dynamic paint
        scene.batchAutoNameModifierNames.dynamicPaint = modifierName.dynamicPaint

        # explode
        scene.batchAutoNameModifierNames.explode = modifierName.explode

        # fluid simulation
        scene.batchAutoNameModifierNames.fluidSimulation = modifierName.fluidSimulation

        # ocean
        scene.batchAutoNameModifierNames.ocean = modifierName.ocean

        # particle instance
        scene.batchAutoNameModifierNames.particleInstance = modifierName.particleInstance

        # particle system
        scene.batchAutoNameModifierNames.particleSystem = modifierName.particleSystem

        # smoke
        scene.batchAutoNameModifierNames.smoke = modifierName.smoke

        # soft body
        scene.batchAutoNameModifierNames.softBody = modifierName.softBody

        # object data name
        objectDataName = context.scene.batchAutoNameObjectDataNames

        # mesh
        scene.batchAutoNameObjectDataNames.mesh = objectDataName.mesh

        # curve
        scene.batchAutoNameObjectDataNames.curve = objectDataName.curve

        # surface
        scene.batchAutoNameObjectDataNames.surface = objectDataName.surface

        # meta
        scene.batchAutoNameObjectDataNames.meta = objectDataName.meta

        # font
        scene.batchAutoNameObjectDataNames.font = objectDataName.font

        # armature
        scene.batchAutoNameObjectDataNames.armature = objectDataName.armature

        # lattice
        scene.batchAutoNameObjectDataNames.lattice = objectDataName.lattice

        # speaker
        scene.batchAutoNameObjectDataNames.speaker = objectDataName.speaker

        # camera
        scene.batchAutoNameObjectDataNames.camera = objectDataName.camera

        # lamp
        scene.batchAutoNameObjectDataNames.lamp = objectDataName.lamp

  # name
  if name:
    for scene in bpy.data.scenes:
      if scene != context.scene:

        # batch name option
        batchNameOption = context.scene.batchNameSettings

        # batch type
        scene.batchNameSettings.batchType = batchNameOption.batchType

        # batch objects
        scene.batchNameSettings.objects = batchNameOption.objects

        # batch object constraints
        scene.batchNameSettings.constraints = batchNameOption.constraints

        # batch modifiers
        scene.batchNameSettings.modifiers = batchNameOption.modifiers

        # batch object data
        scene.batchNameSettings.objectData = batchNameOption.objectData

        # batch bones
        scene.batchNameSettings.bones = batchNameOption.bones

        # batch bone constraints
        scene.batchNameSettings.boneConstraints = batchNameOption.boneConstraints

        # batch materials
        scene.batchNameSettings.materials = batchNameOption.materials

        # batch textures
        scene.batchNameSettings.textures = batchNameOption.textures

        # batch particle systems
        scene.batchNameSettings.particleSystems = batchNameOption.particleSystems

        # batch particle settings
        scene.batchNameSettings.particleSettings = batchNameOption.particleSettings

        # batch groups
        scene.batchNameSettings.groups = batchNameOption.groups

        # batch vertex groups
        scene.batchNameSettings.vertexGroups = batchNameOption.vertexGroups

        # batch shape keys
        scene.batchNameSettings.shapekeys = batchNameOption.shapekeys

        # batch uvs
        scene.batchNameSettings.uvs = batchNameOption.uvs

        # batch vertex colors
        scene.batchNameSettings.vertexColors = batchNameOption.vertexColors

        # batch bone groups
        scene.batchNameSettings.boneGroups = batchNameOption.boneGroups

        # object type
        scene.batchNameSettings.objectType = batchNameOption.objectType

        # constraint type
        scene.batchNameSettings.constraintType = batchNameOption.constraintType

        # modifier type
        scene.batchNameSettings.modifierType = batchNameOption.modifierType

        # scenes
        scene.batchNameSettings.scenes = batchNameOption.scenes

        # render layers
        scene.batchNameSettings.renderLayers = batchNameOption.renderLayers

        # worlds
        scene.batchNameSettings.worlds = batchNameOption.worlds

        # libraries
        scene.batchNameSettings.libraries = batchNameOption.libraries

        # images
        scene.batchNameSettings.images = batchNameOption.images

        # masks
        scene.batchNameSettings.masks = batchNameOption.masks

        # sequences
        scene.batchNameSettings.sequences = batchNameOption.sequences

        # movie clips
        scene.batchNameSettings.movieClips = batchNameOption.movieClips

        # sounds
        scene.batchNameSettings.sounds = batchNameOption.sounds

        # screens
        scene.batchNameSettings.screens = batchNameOption.screens

        # keying sets
        scene.batchNameSettings.keyingSets = batchNameOption.keyingSets

        # palettes
        scene.batchNameSettings.palettes = batchNameOption.palettes

        # brushes
        scene.batchNameSettings.brushes = batchNameOption.brushes

        # linestyles
        scene.batchNameSettings.linestyles = batchNameOption.linestyles

        # nodes
        scene.batchNameSettings.nodes = batchNameOption.nodes

        # node labels
        scene.batchNameSettings.nodeLabels = batchNameOption.nodeLabels

        # node groups
        scene.batchNameSettings.nodeGroups = batchNameOption.nodeGroups

        # texts
        scene.batchNameSettings.texts = batchNameOption.texts

        # name
        scene.batchNameSettings.customName = batchNameOption.customName

        # find
        scene.batchNameSettings.find = batchNameOption.find

        # regex
        scene.batchNameSettings.regex = batchNameOption.regex

        # replace
        scene.batchNameSettings.replace = batchNameOption.replace

        # prefix
        scene.batchNameSettings.prefix = batchNameOption.prefix

        # suffix
        scene.batchNameSettings.suffix = batchNameOption.suffix

        # trim start
        scene.batchNameSettings.trimStart = batchNameOption.trimStart

        # trim end
        scene.batchNameSettings.trimEnd = batchNameOption.trimEnd

        # process
        scene.batchNameSettings.sort = batchNameOption.sort

        # padding
        scene.batchNameSettings.padding = batchNameOption.padding

        # start
        scene.batchNameSettings.start = batchNameOption.start

        # separator
        scene.batchNameSettings.separator = batchNameOption.separator

        # process only
        scene.batchNameSettings.sortOnly = batchNameOption.sortOnly

  # copy
  if copy:
    for scene in bpy.data.scenes[:]:
      if scene != context.scene:

        # batch copy option
        batchCopyOption = context.scene.batchCopySettings

        # batch type
        scene.batchCopySettings.batchType = batchCopyOption.batchType

        # source
        scene.batchCopySettings.source = batchCopyOption.source

        # objects
        scene.batchCopySettings.objects = batchCopyOption.objects

        # object datas
        scene.batchCopySettings.objectData = batchCopyOption.objectData

        # materials
        scene.batchCopySettings.materials = batchCopyOption.materials

        # textures
        scene.batchCopySettings.textures = batchCopyOption.textures

        # particle systems
        scene.batchCopySettings.particleSystems = batchCopyOption.particleSystems

        # particle settings
        scene.batchCopySettings.particleSettings = batchCopyOption.particleSettings

        # use active object
        scene.batchCopySettings.useActiveObject = batchCopyOption.useActiveObject
