import bpy
import struct
import array

def export_raw_stuff(filenamepathetc):

    ob=bpy.context.active_object
    mesh=ob.to_mesh(bpy.context.scene,True,"PREVIEW")

    fp=open(filenamepathetc,"wb")


    num=0

    for poly in mesh.polygons:
        if len(poly.loop_indices) != 3: 
            raise RuntimeError("Number of points in polygon is not three, consider triangulate faces or triangulate modifier")		

        for ind in poly.loop_indices:
            num+=1
            vind=ind-poly.loop_start
            vx=poly.vertices[vind]
            v=mesh.vertices[vx].co
            vc=mesh.vertex_colors[0].data[ind].color
            #print ((v,vc))
            array.array("d",[v.x,v.y,v.z]).tofile(fp)
            if num<2: print(("vector:",num,v))
            #array.array("d",[vc.r,vc.g,vc.b]).tofile(fp)

    num=0

    for poly in mesh.polygons:
        for ind in poly.loop_indices:
            num+=1
            vind=ind-poly.loop_start
            vx=poly.vertices[vind]
            v=mesh.vertices[vx].co
            vc=mesh.vertex_colors[0].data[ind].color
            #print ((v,vc))
            #array.array("d",[v.x,v.y,v.z]).tofile(fp)
            array.array("d",[vc.r,vc.g,vc.b]).tofile(fp)
            if num<2: print(("colour:",num,vc))

    print ((num))
    fp.close()




bl_info = {
    "name": "Raw Faces and Vertex Colours format (.dat)",
    "author": "Robin Potter",
    "version": (0, 1),
    "blender": (2, 74, 0),
    "location": "File > Import-Export > Export Raw Faces/Vertex (.dat) ",
    "description": "Export Raw Faces",
    "warning": "",
    "wiki_url": "",
    "category": "Import-Export",
}


from bpy.props import StringProperty, BoolProperty
from bpy_extras.io_utils import ExportHelper


class RobinExporter(bpy.types.Operator, ExportHelper):
    """Save Raw triangle mesh data"""
    bl_idname = "export_mesh_colours.dat"
    bl_label = "Export RAW/Vertex Cols"

    filename_ext = ".dat"
    filter_glob = StringProperty(default="*.dat", options={'HIDDEN'})

    def execute(self, context):        
        export_raw_stuff(self.filepath)
        return {'FINISHED'}



def menu_export(self, context):
    self.layout.operator(RobinExporter.bl_idname, text="Raw Faces and Vertex Colours (.dat)")


def register():
    bpy.utils.register_module(__name__)
    bpy.types.INFO_MT_file_export.append(menu_export)


def unregister():
    bpy.utils.unregister_module(__name__)
    bpy.types.INFO_MT_file_export.remove(menu_export)

if __name__ == "__main__":
    register()



