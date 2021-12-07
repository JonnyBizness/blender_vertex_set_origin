bl_info = {
    "name": "Vertex set origin",
    "blender": (2, 80, 0),
    "category": "Object",
}

import bpy
import bmesh
from mathutils import Vector

addon_keymaps = []


class ObjectSetOrigin(bpy.types.Operator):
    """Object Origin by Vertices"""      # Use this as a tooltip for menu items and buttons.
    bl_idname = "object.vertex_set_origin"        # Unique identifier for buttons and menu items to reference.
    bl_label = "Move objects origin to selected vertices"         # Display name in the interface.
    bl_options = {'REGISTER', 'UNDO'}  # Enable undo for the operator.    

    def execute(self, context):        # execute() is called when running the operator.

        # The original script
        #context = bpy.context #in og script bt not needed now?
        scene = context.scene

        #print('Setting to center')

        if bpy.context.mode == 'EDIT_MESH':
            ##store starting location
            starting_cursor = bpy.context.scene.cursor.location.copy()
            #print('Starting cursor point:', starting_cursor)


            ##move cursor to selected location

            ##vertices
            ob = context.edit_object # RUN IN EDIT MODE
            me = ob.data
            bm = bmesh.from_edit_mesh(me)
            selected_verts = [v for v in bm.verts if v.select]
            #print('Selected Verts', selected_verts)

            n = len(selected_verts)
            #print('Number of selected verts: ', n)


            average_local_location = sum([v.co for v in selected_verts], Vector()) / n
            #print('average local location:', average_local_location)

            new_location = ob.matrix_world @ average_local_location

            print('New location point:', new_location)
            scene.cursor.location = new_location

            ##set origin to cursor new location
            bpy.ops.object.editmode_toggle()
            bpy.ops.object.origin_set(type='ORIGIN_CURSOR', center='MEDIAN')


            ##restore starting cursor location
            bpy.ops.object.editmode_toggle()
            #print('starting_cursor:', starting_cursor)
            scene.cursor.location = starting_cursor
            #print('done')            
        elif bpy.context.mode == 'OBJECT':
            bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY', center='MEDIAN')
        
        return {'FINISHED'}

def menu_func(self, context):
    self.layout.operator(ObjectSetOrigin.bl_idname)

def register():
    bpy.utils.register_class(ObjectSetOrigin)
    bpy.types.VIEW3D_MT_object.append(menu_func)  # Adds the new operator to an existing menu.

    # handle the keymap
    wm = bpy.context.window_manager
    km = wm.keyconfigs.addon.keymaps.new(name='Screen Editing', space_type='EMPTY')
    kmi = km.keymap_items.new(ObjectSetOrigin.bl_idname, 'F5', 'PRESS', ctrl=False, shift=False)
    addon_keymaps.append((km, kmi))

def unregister():
    bpy.utils.unregister_class(ObjectSetOrigin)

    # handle the keymap
    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()