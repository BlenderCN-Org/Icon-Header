import bpy

# -----------------------------------------------------------------------------
# Draw UI, use an function to be append into 3D View Header
# -----------------------------------------------------------------------------
def menu_func(self, context):
    layout = self.layout

    layout.operator("view.grid_control", text='', icon='GRID')
    icon = 'LATTICE_DATA'
    layout.operator("object.center_pivot_mesh_obj", text='', icon=icon)
