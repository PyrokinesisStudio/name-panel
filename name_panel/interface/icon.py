
# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or modify it
#  under the terms of the GNU General Public License as published by the Free
#  Software Foundation; either version 2 of the License, or (at your option)
#  any later version.
#
#  This program is distributed in the hope that it will be useful, but WITHOUT
#  ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
#  this program; if not, write to the Free Software Foundation, Inc.,
#  FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for
#  more details.
#
#  You should have received a copy of the GNU General Public License along with
#  51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

# object icon
def object(object):
  '''
    Returns a icon based on object type.
  '''

  # mesh
  if object.type in 'MESH':
    icon = 'OUTLINER_OB_MESH'

  # curve
  elif object.type in 'CURVE':
    icon = 'OUTLINER_OB_CURVE'

  # surface
  elif object.type in 'SURFACE':
    icon = 'OUTLINER_OB_SURFACE'

  # meta
  elif object.type in 'META':
    icon = 'OUTLINER_OB_META'

  # font
  elif object.type in 'FONT':
    icon = 'OUTLINER_OB_FONT'

  # armature
  elif object.type in 'ARMATURE':
    icon = 'OUTLINER_OB_ARMATURE'

  # lattice
  elif object.type in 'LATTICE':
    icon = 'OUTLINER_OB_LATTICE'

  # empty
  elif object.type in 'EMPTY':
    icon = 'OUTLINER_OB_EMPTY'

  # speaker
  elif object.type in 'SPEAKER':
    icon = 'OUTLINER_OB_SPEAKER'

  # camera
  elif object.type in 'CAMERA':
    icon = 'OUTLINER_OB_CAMERA'

  # lamp
  elif object.type in 'LAMP':
    icon = 'OUTLINER_OB_LAMP'

  # default
  else:
    icon = 'OUTLINER_OB_MESH'
  return icon

# modifier icon
def modifier(modifier):
  '''
    Returns a icon based on modifier type.
  '''

  # data transfer
  if modifier.type in 'DATA_TRANSFER':
    icon = 'MOD_DATA_TRANSFER'

  # mesh cache
  elif modifier.type in 'MESH_CACHE':
    icon = 'MOD_MESHDEFORM'

  # normal edit
  elif modifier.type in 'NORMAL_EDIT':
    icon = 'MOD_NORMALEDIT'

  # uvs project
  elif modifier.type in 'UV_PROJECT':
    icon = 'MOD_UVPROJECT'

  # uvs warp
  elif modifier.type in 'UV_WARP':
    icon = 'MOD_UVPROJECT'

  # vertex weight edit
  elif modifier.type in 'VERTEX_WEIGHT_EDIT':
    icon = 'MOD_VERTEX_WEIGHT'

  # vertex weight mix
  elif modifier.type in 'VERTEX_WEIGHT_MIX':
    icon = 'MOD_VERTEX_WEIGHT'

  # vertex weight proximity
  elif modifier.type in 'VERTEX_WEIGHT_PROXIMITY':
    icon = 'MOD_VERTEX_WEIGHT'

  # array
  elif modifier.type in 'ARRAY':
    icon = 'MOD_ARRAY'

  # bevel
  elif modifier.type in 'BEVEL':
    icon = 'MOD_BEVEL'

  # bolean
  elif modifier.type in 'BOOLEAN':
    icon = 'MOD_BOOLEAN'

  # boptionld
  elif modifier.type in 'BUILD':
    icon = 'MOD_BUILD'

  # decimate
  elif modifier.type in 'DECIMATE':
    icon = 'MOD_DECIM'

  # edge split
  elif modifier.type in 'EDGE_SPLIT':
    icon = 'MOD_EDGESPLIT'

  # mask
  elif modifier.type in 'MASK':
    icon = 'MOD_MASK'

  # mirror
  elif modifier.type in 'MIRROR':
    icon = 'MOD_MIRROR'

  # multires
  elif modifier.type in 'MULTIRES':
    icon = 'MOD_MULTIRES'

  # remesh
  elif modifier.type in 'REMESH':
    icon = 'MOD_REMESH'

  # screw
  elif modifier.type in 'SCREW':
    icon = 'MOD_SCREW'

  # skin
  elif modifier.type in 'SKIN':
    icon = 'MOD_SKIN'

  # solidify
  elif modifier.type in 'SOLIDIFY':
    icon = 'MOD_SOLIDIFY'

  # subsurf
  elif modifier.type in 'SUBSURF':
    icon = 'MOD_SUBSURF'

  # triangulate
  elif modifier.type in 'TRIANGULATE':
    icon = 'MOD_TRIANGULATE'

  # wireframe
  elif modifier.type in 'WIREFRAME':
    icon = 'MOD_WIREFRAME'

  # armature
  elif modifier.type in 'ARMATURE':
    icon = 'MOD_ARMATURE'

  # cast
  elif modifier.type in 'CAST':
    icon = 'MOD_CAST'

  # corrective smooth
  elif modifier.type in 'CORRECTIVE_SMOOTH':
    icon = 'MOD_SMOOTH'

  # curve
  elif modifier.type in 'CURVE':
    icon = 'MOD_CURVE'

  # displace
  elif modifier.type in 'DISPLACE':
    icon = 'MOD_DISPLACE'

  # hook
  elif modifier.type in 'HOOK':
    icon = 'HOOK'

  # laplacian smooth
  elif modifier.type in 'LAPLACIANSMOOTH':
    icon = 'MOD_SMOOTH'

  # laplacian deform
  elif modifier.type in 'LAPLACIANDEFORM':
    icon = 'MOD_MESHDEFORM'

  # lattice
  elif modifier.type in 'LATTICE':
    icon = 'MOD_LATTICE'

  # mesh deform
  elif modifier.type in 'MESH_DEFORM':
    icon = 'MOD_MESHDEFORM'

  # shrinkwrap
  elif modifier.type in 'SHRINKWRAP':
    icon = 'MOD_SHRINKWRAP'

  # simple deform
  elif modifier.type in 'SIMPLE_DEFORM':
    icon = 'MOD_SIMPLEDEFORM'

  # smooth
  elif modifier.type in 'SMOOTH':
    icon = 'MOD_SMOOTH'

  # warp
  elif modifier.type in 'WARP':
    icon = 'MOD_WARP'

  # wave
  elif modifier.type in 'WAVE':
    icon = 'MOD_WAVE'

  # cloth
  elif modifier.type in 'CLOTH':
    icon = 'MOD_CLOTH'

  # collision
  elif modifier.type in 'COLLISION':
    icon = 'MOD_PHYSICS'

  # dynamic paint
  elif modifier.type in 'DYNAMIC_PAINT':
    icon = 'MOD_DYNAMICPAINT'

  # explode
  elif modifier.type in 'EXPLODE':
    icon = 'MOD_EXPLODE'

  # floptiond simulation
  elif modifier.type in 'FLUID_SIMULATION':
    icon = 'MOD_FLUIDSIM'

  # ocean
  elif modifier.type in 'OCEAN':
    icon = 'MOD_OCEAN'

  # particle instance
  elif modifier.type in 'PARTICLE_INSTANCE':
    icon = 'MOD_PARTICLES'

  # particle system
  elif modifier.type in 'PARTICLE_SYSTEM':
    icon = 'MOD_PARTICLES'

  # smoke
  elif modifier.type in 'SMOKE':
    icon = 'MOD_SMOKE'

  # soft body
  elif modifier.type in 'SOFT_BODY':
    icon = 'MOD_SOFT'

  # default
  else:
    icon = 'MODIFIER'
  return icon

# object data icon
def objectData(object):
  '''
    Returns a icon based on object type.
  '''

  # mesh
  if object.type in 'MESH':
    icon = 'MESH_DATA'

  # curve
  elif object.type in 'CURVE':
    icon = 'CURVE_DATA'

  # surface
  elif object.type in 'SURFACE':
    icon = 'SURFACE_DATA'

  # meta
  elif object.type in 'META':
    icon = 'META_DATA'

  # font
  elif object.type in 'FONT':
    icon = 'FONT_DATA'

  # armature
  elif object.type in 'ARMATURE':
    icon = 'ARMATURE_DATA'

  # lattice
  elif object.type in 'LATTICE':
    icon = 'LATTICE_DATA'

  # speaker
  elif object.type in 'SPEAKER':
    icon = 'SPEAKER'

  # camera
  elif object.type in 'CAMERA':
    icon = 'CAMERA_DATA'

  # lamp
  elif object.type in 'LAMP':
    icon = 'LAMP_DATA'

  # default
  else:
    icon = 'MESH_DATA'
  return icon
