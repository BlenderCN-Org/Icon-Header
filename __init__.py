import bpy

from .controllers.grid import GridControl
from .controllers.location import CenterPivotMeshObj

# -----------------------------------------------------------------------------
# MetaData Add-On Blender
# -----------------------------------------------------------------------------
bl_info = {
    "name": "Grid Control",
    "author": "stilobique",
    "version": (1, 0, 0),
    "blender": (2, 78),
    "location": "3D View > Header",
    "description": "Show or Hide your grid.",
    "warning": "",
    "wiki_url": "https://github.com/stilobique/Grid/wiki",
    "category": "3D View",
    "tracker_url": "https://github.com/stilobique/Grid/issues",
}

# -----------------------------------------------------------------------------
# Draw UI, use an function to be append into 3D View Header
# -----------------------------------------------------------------------------
def menu_func(self, context):
    layout = self.layout

    layout.operator("view.grid_control", text='', icon='GRID')
    icon = 'LATTICE_DATA'
    layout.operator("object.center_pivot_mesh_obj", text='', icon=icon)


# -----------------------------------------------------------------------------
# Register all module and append UI in 3D View Header
# -----------------------------------------------------------------------------
def register():
    bpy.utils.register_module(__name__)
    bpy.types.VIEW3D_HT_header.append(menu_func)

def unregister():
    bpy.utils.unregister_module(__name__)
    bpy.types.VIEW3D_HT_header.remove(menu_func)

if __name__ == "__main__":
    register()
