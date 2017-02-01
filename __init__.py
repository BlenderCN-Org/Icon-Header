import bpy
from bpy.props import (BoolProperty,
                       PointerProperty,
                       )

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
# Generate a Bool variable to on and Off Grid settings
# -----------------------------------------------------------------------------
class GridData(bpy.types.PropertyGroup):
    grid_data = BoolProperty(
        name = "Show/Hide Grid",
        description = "Bolean to on or off the grid",
        default = False
    )


# -----------------------------------------------------------------------------
# Call operator
# -----------------------------------------------------------------------------

class GridControl(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "view.grid_control"
    bl_label = "Show and Hide Grid"

    def execute(self, context):
        area = None
        for a in bpy.data.window_managers[0].windows[0].screen.areas:
            if a.type == 'VIEW_3D':
                area = a
                break

        if area:
            space = area.spaces[0]
        else:
            space = bpy.context.space_data

        if space.show_floor == True:
            space.show_floor = False
            space.show_axis_x = False
            space.show_axis_y = False
            # space.show_axis_z = False
        else:
            space.show_floor = True
            space.show_axis_x = True
            space.show_axis_y = True
            # space.show_axis_z = True

        return {'FINISHED'}

# -----------------------------------------------------------------------------
# Draw UI, use an function to be append into 3D View Header
# -----------------------------------------------------------------------------
def menu_func(self, context):
    layout = self.layout
    scn = context.scene
    grid = scn.my_tool

    layout.operator("view.grid_control", text='', icon='GRID')
    # layout.prop(grid, "grid_data", text='', icon='GRID', toggle=True)


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
