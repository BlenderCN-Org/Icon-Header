import bpy
import math


class SmoothShading(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.smooth_shading"
    bl_label = "Advanced Smooth Shading"


    def execute(self, context):
        sltd_obj = context.selected_objects
        data = bpy.data

        for obj in sltd_obj:
            # Activate Smooth Shading
            bpy.ops.object.shade_smooth()
            # Use auto Smooth feature
            data.objects[obj.name].data.use_auto_smooth = True
            # Find Mesh Name
            mesh_name = data.objects[obj.name].data.name
            # Convert degrees to radians
            angle = math.radians(45)
            # Apply angle to smooth Shading
            bpy.data.meshes[mesh_name].auto_smooth_angle = angle

        return {'FINISHED'}


def register():
    bpy.utils.register_class(SmoothShading)


def unregister():
    bpy.utils.unregister_class(SmoothShading)
