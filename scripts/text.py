
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

cheatsheet = r'''
Special Characters

  \        Escape special characters or start a sequence.

  .        Matches any character. ('.*' matches everything in a name.)

  ^        Matches beginning of string.

  $        Matches end of string.

  [3a-c]   Matches any characters '3', 'a', 'b' or 'c'.

  [^3a-c]  Matches any characters except '3', 'a', 'b' or 'c'.

  a|b      matches either a or b.


Quantifiers

  *        0 or more. (append ? for fewest)

  +        1 or more. (append ? for fewest)

  ?        0 or 1. (append ? for fewest)

  {m}      Exactly m occurrences.

  {m, n}   From m to n, m defaults to 0, n defaults to infinity.

  {m, n}?  From m to n, as few as possible.


Special Sequences

  \A       Start of string.

  \b       Matches empty string at word boundary. (between \w and \W)

  \B       Matches empty string not at word boundary.

  \d       A digit.

  \D       A non-digit.

  \s       Whitespace.

  \S       Non-whitespace.

  \w       Alphanumeric, Same as: [0-9a-zA-Z_]

  \W       Non-alphanumeric.

  \Z       End of name.


Groups

  ()             Creates a capture group and indicates precedence.

  \1             Recall first captured group, change accordingly.

  (?P<name>...)  Creates a group with the id of 'name'.

  \g<id>         Matches a previously defined group.

  (?(id)yes|no)  Match 'yes' if group 'id' matched, else 'no'.


Examples

(1) String: Name.001

    Find: \W[0-9]*$

    Result: Name

    This expression will strip any numbers at the tail end of a name up to and
    including any non-alphanumeric character.

    The individual characters used are;

    \W    Non-alphanumeric. (any character other then [0-9a-zA-Z_])

    [0-9] Character class from range 0 through 9.

    *     Anything preceding this symbol will be matched until no other matches
          are found.

    $     Indicates that we want to start from the end of the string.


(2) String: Name.001

    Find: ([A-z]*\.)

    Replace: Changed_\1

    Result: Changed_Name.001

    This expression will create a capture group of any characters and a . (dot)
    replace those characters with 'Changed_' infront of that captured group.

      The individual characters used are;

      (     Start a capture group.

      [A-z] Character class range A-z (upper and lowercase).

      *     Anything preceding this symbol will be matched until no other
            matches are found.

      \.    Used here to escape the character . (dot) which has special
            meaning in regular expressions.

      )     End a capture group.

      \1    Recall first captured group.


(3) String: Name

    Find: ^((?!Name).)*$

    Replace: Not_Name

    Result: Not_Name

  This expression will actually look ahead in the name and determine if there
  is the string 'Name' in it, if there is then it will be skipped, however if it
  is not there then that name will be entirely replaced with Not_Name. This is
  useful in situations where you want to name everything except those names
  with a specific string in it.



Regular expressions are much like a tiny programming language, this cheatsheet
will help get you started.

For a more complete documentation of python related regular expressions;

  https://docs.python.org/3.5/library/re.html
'''

defaults = r'''
# Modified by scripts.function.preferences.generate.main
defaults = {
  'name panel': {
    'location': 'TOOLS',
    'pin active object': True,
    'pin active bone': True,
    'hide find & replace': True,
    'filters': False,
    'shortcuts': False,
    'display names': False,
    'search': '',
    'regex': False,
    'mode': 'SELECTED',
    'groups': False,
    'action': False,
    'grease pencil': False,
    'constraints': False,
    'modifiers': False,
    'bone groups': False,
    'bone constraints': False,
    'vertex groups': False,
    'shapekeys': False,
    'uvs': False,
    'vertex colors': False,
    'materials': False,
    'textures': False,
    'particle systems': False,
    'bone mode': 'SELECTED',
    'display bones': False,
  },

  'Properties Panel': {
    'location': 'TOOLS'
  },

  'shared': {
    'large popups': False,
    'sort': False,
    'type': 'ALPHABETICAL',
    'axis': 'X',
    'invert': False,
    'count': False,
    'link': False,
    'pad': 0,
    'start': 1,
    'step': 1,
    'separator': '.',
    'ignore': False
  },

  'auto name': {
    'mode': 'SELECTED',
    'objects': False,
    'constraints': False,
    'modifiers': False,
    'object data': False,
    'bone constraints': False,
    'object type': 'ALL',
    'constraint type': 'ALL',
    'modifier type': 'ALL',

    'object names': {
      'prefix': False,
      'mesh': 'Mesh',
      'curve': 'Curve',
      'surface': 'Surface',
      'meta': 'Meta',
      'font': 'Text',
      'armature': 'Armature',
      'lattice': 'Lattice',
      'empty': 'Empty',
      'speaker': 'Speaker',
      'camera': 'Camera',
      'lamp': 'Lamp',
    },

    'constraint names': {
      'prefix': False,
      'camera solver': 'Camera Solver',
      'follow track': 'Follow Track',
      'object solver': 'Object Solver',
      'copy location': 'Copy Location',
      'copy rotation': 'Copy Rotation',
      'copy scale': 'Copy Scale',
      'copy transforms': 'Copy Transforms',
      'limit distance': 'Limit Distance',
      'limit location': 'Limit Location',
      'limit rotation': 'Limit Rotation',
      'limit scale': 'Limit Scale',
      'maintain volume': 'Maintain Volume',
      'transform': 'Transform',
      'clamp to': 'Clamp To',
      'damped track': 'Damped Track',
      'inverse kinematics': 'Inverse Kinematics',
      'locked track': 'Locked Track',
      'spline inverse kinematics': 'Spline Inverse Kinematics',
      'stretch to': 'Stretch To',
      'track to': 'Track To',
      'action': 'Action',
      'child of': 'Child Of',
      'floor': 'Floor',
      'follow path': 'Follow Path',
      'pivot': 'Pivot',
      'rigid body joint': 'Rigid Body Joint',
      'shrinkwrap': 'Shrinkwrap',
    },

    'modifier names': {
      'prefix': False,
      'data transfer': 'Data Transfer',
      'mesh cache': 'Mesh Cache',
      'normal edit': 'Normal Edit',
      'uv project': 'UV Project',
      'uv warp': 'UV Warp',
      'vertex weight edit': 'Vertex Weight Edit',
      'vertex weight mix': 'Vertex Weight Mix',
      'vertex weight proximity': 'Vertex Weight Proximity',
      'array': 'Array',
      'bevel': 'Bevel',
      'boolean': 'Boolean',
      'build': 'Build',
      'decimate': 'Decimate',
      'edge split': 'Edge Split',
      'mask': 'Mask',
      'mirror': 'Mirror',
      'multiresolution': 'Multiresolution',
      'remesh': 'Remesh',
      'screw': 'Screw',
      'skin': 'Skin',
      'solidify': 'Solidify',
      'subdivision surface': 'Subdivision Surface',
      'triangulate': 'Triangulate',
      'wireframe': 'Wireframe',
      'armature': 'Armature',
      'cast': 'Cast',
      'corrective smooth': 'Corrective Smooth',
      'curve': 'Curve',
      'displace': 'Displace',
      'hook': 'Hook',
      'laplacian smooth': 'Laplacian Smooth',
      'laplacian deform': 'Laplacian Deform',
      'lattice': 'Lattice',
      'mesh deform': 'Mesh Deform',
      'shrinkwrap': 'Shrinkwrap',
      'simple deform': 'Simple Deform',
      'smooth': 'Smooth',
      'warp': 'Warp',
      'wave': 'Wave',
      'cloth': 'Cloth',
      'collision': 'Collision',
      'dynamic paint': 'Dynamic Paint',
      'explode': 'Explode',
      'fluid simulation': 'Fluid Simulation',
      'ocean': 'Ocean',
      'particle instance': 'Particle Instance',
      'particle system': 'Particle System',
      'smoke': 'Smoke',
      'soft body': 'Soft Body',
    },

    'object data names': {
      'prefix': False,
      'mesh': 'Mesh',
      'curve': 'Curve',
      'surface': 'Surface',
      'meta': 'Meta',
      'font': 'Text',
      'armature': 'Armature',
      'lattice': 'Lattice',
      'empty': 'Empty',
      'speaker': 'Speaker',
      'camera': 'Camera',
      'lamp': 'Lamp',
    },
  },

  'batch name': {
    'mode': 'SELECTED',
    'actions': False,
    'action groups': False,
    'grease pencil': False,
    'pencil layers': False,
    'objects': False,
    'groups': False,
    'constraints': False,
    'modifiers': False,
    'object data': False,
    'bone groups': False,
    'bones': False,
    'bone constraints': False,
    'vertex groups': False,
    'shapekeys': False,
    'uvs': False,
    'vertex colors': False,
    'materials': False,
    'textures': False,
    'particle systems': False,
    'particle settings': False,
    'object type': 'ALL',
    'constraint type': 'ALL',
    'modifier type': 'ALL',
    'sensors': False,
    'controllers': False,
    'actuators': False,
    'line sets': False,
    'linestyles': False,
    'linestyle modifiers': False,
    'linestyle modifier type': 'ALL',
    'scenes': False,
    'render layers': False,
    'worlds': False,
    'libraries': False,
    'images': False,
    'masks': False,
    'sequences': False,
    'movie clips': False,
    'sounds': False,
    'screens': False,
    'keying sets': False,
    'palettes': False,
    'brushes': False,
    'nodes': False,
    'node labels': False,
    'frame nodes': False,
    'node groups': False,
    'texts': False,
    'ignore action': False,
    'ignore grease pencil': False,
    'ignore object': False,
    'ignore group': False,
    'ignore constraint': False,
    'ignore modifier': False,
    'ignore bone': False,
    'ignore bone group': False,
    'ignore bone constraint': False,
    'ignore object data': False,
    'ignore vertex group': False,
    'ignore shapekey': False,
    'ignore uv': False,
    'ignore vertex color': False,
    'ignore material': False,
    'ignore texture': False,
    'ignore particle system': False,
    'ignore particle setting': False,
    'custom': '',
    'insert': False,
    'insert at': 0,
    'find': '',
    'regex': False,
    'replace': '',
    'prefix': '',
    'suffix': '',
    'suffix last': False,
    'trim start': 0,
    'trim end': 0,
    'cut start': 0,
    'cut amount': 0,
  },

  'copy name': {
    'mode': 'SELECTED',
    'source': 'OBJECT',
    'objects': False,
    'object data': False,
    'materials': False,
    'textures': False,
    'particle systems': False,
    'particle settings': False,
    'use active object': False,
  },
}
'''
