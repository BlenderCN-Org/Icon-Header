import sys
import importlib

modulesNames = [
    # Views
    'views.header',
    # Controllers
    'controllers.grid',
    'controllers.location',
    ]

modulesFullNames = []
for currentModule in modulesNames:
    modulesFullNames.append('{}.{}'.format(__name__, currentModule))

for currentModule in modulesFullNames:
    if currentModule in sys.modules:
        importlib.reload(sys.modules[currentModule])
    else:
        globals()[currentModule] = importlib.import_module(currentModule)

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
# Register all module and append UI in 3D View Header
# -----------------------------------------------------------------------------
# def register():
#     bpy.utils.register_module(__name__)
#     bpy.types.VIEW3D_HT_header.append(menu_func)
#
# def unregister():
#     bpy.utils.unregister_module(__name__)
#     bpy.types.VIEW3D_HT_header.remove(menu_func)

# -----------------------------------------------------------------------------
# Update register all methods to this addons
# -----------------------------------------------------------------------------
def register():
    for currentModule in modulesFullNames:
        if currentModule in sys.modules:
            if hasattr(sys.modules[currentModule], 'register'):
                sys.modules[currentModule].register()


# -----------------------------------------------------------------------------
# Delete register
# -----------------------------------------------------------------------------
def unregister():
    for currentModule in modulesFullNames:
        if currentModule in sys.modules:
            if hasattr(sys.modules[currentModule], 'unregister'):
                sys.modules[currentModule].unregister()


if __name__ == "__main__":
    register()
