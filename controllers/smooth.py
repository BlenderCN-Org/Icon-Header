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
            if obj.type == "MESH":
                bpy.ops.object.shade_smooth()
                data.objects[obj.name].data.use_auto_smooth = True
                mesh_name = data.objects[obj.name].data.name
                angle = math.radians(45)
                bpy.data.meshes[mesh_name].auto_smooth_angle = angle

        return {'FINISHED'}


def register():
    bpy.utils.register_class(SmoothShading)


def unregister():
    bpy.utils.unregister_class(SmoothShading)
