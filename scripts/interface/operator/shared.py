
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

# sort
def sort(layout, option):

  # separator
  layout.separator()

  # row
  row = layout.row(align=True)

  # sub
  sub = row.row(align=True)

  # scale
  sub.scale_x = 0.5

  # sort
  sub.prop(option, 'sort', text='Sort', toggle=True)

  # pad
  row.prop(option, 'pad', text='Pad')

  # start
  row.prop(option, 'start', text='Start')

  # step
  row.prop(option, 'step', text='Step')

  # sub
  sub = row.row(align=True)

  # scale
  sub.scale_x = 0.1

  # separator
  sub.prop(option, 'separator', text='')

  # icon
  icon = 'LINKED' if option.link else 'UNLINKED'

  # link
  row.prop(option, 'link', text='', icon=icon)

  # ignore
  row.prop(option, 'ignore', text='', icon='ZOOM_PREVIOUS')
