import bpy

# -----------------------------------------------------------------------------
# Draw UI, use an function to be append into 3D View Header
# -----------------------------------------------------------------------------
def menu_func(self, context):
    layout = self.layout
    row = layout.row(align=True)

    row.operator("view.grid_control", text='', icon='GRID')
    icon = 'CURSOR'
    row.operator("object.center_pivot_mesh_obj", text='', icon=icon)
    icon = 'SMOOTH'
    row.operator("object.smooth_shading", text='', icon=icon)


def register():
    bpy.types.VIEW3D_HT_header.append(menu_func)

def unregister():
    bpy.types.VIEW3D_HT_header.remove(menu_func)
