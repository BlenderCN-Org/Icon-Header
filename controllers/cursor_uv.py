import bpy


class ResetCursor(bpy.types.Operator):
    """Insert a simple description"""
    bl_idname = "unwrap.reset_cursor"
    bl_label = "Simple Object Operator"

    def execute(self, context):
        bpy.context.space_data.cursor_location[0] = 0
        bpy.context.space_data.cursor_location[1] = 0

        return {'FINISHED'}


def register():
    bpy.utils.register_class(ResetCursor)


def unregister():
    bpy.utils.unregister_class(ResetCursor)


if __name__ == "__main__":
    register()
