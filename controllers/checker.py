import bpy

def tex_checker():
    # Variables
    pictures = bpy.data.images
    # Settings Textures Checker
    name = "Checker"
    size = 1024

    # Check if a Checker texture are exist.
    if pictures.get(name) is not None:
        state = True

    # Not Create, make a new texture.
    else:
        pictures.new(name, size, size)
        pictures[name].source = 'GENERATED'
        pictures[name].generated_type = 'UV_GRID'
        state = False

    # Activate Checker Texture to your UV active.
    slct_obj = bpy.context.selected_objects
    object = bpy.data.objects[slct_obj[0].name]
    uv_map = object.data.uv_textures.active.data
    for uv_face in uv_map:
        uv_face.image = pictures[name]

    return state



class UVChecker(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "unwrap.uv_checker"
    bl_label = "Activate an UV checker"

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

        if space.show_textured_solid == True:
            space.show_textured_solid = False
            # Check if a Checker as exist

            # Generate a Checker Picture
            # tex_checker()
            print(tex_checker())
        else:
            space.show_textured_solid = True


        return {'FINISHED'}


def register():
    bpy.utils.register_class(UVChecker)


def unregister():
    bpy.utils.unregister_class(UVChecker)
