import bpy


class UVChecker(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "unwrap.uv_checker"
    bl_label = "Activate an UV checker"

    def execute(self, context):
        print("UV Checker")
        return {'FINISHED'}


def register():
    bpy.utils.register_class(UVChecker)


def unregister():
    bpy.utils.unregister_class(UVChecker)
