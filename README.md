# blender_vertex_set_origin
Simple Blender addon to set the origin of an object to the average position of selected vertices

# install
Regular install
Clone this repo or download the vertex_set_origin.py file
Edit -> Preferences -> Add-ons -> Install...
Navigate to and find 'vertex_set_origin.py'
Select 'Install addon'
Search for 'Vertex set origin' and Ensure Add-on is enabled.

# use
Hotkey in use: F5

In Edit mode:
Select any number of vertices and press F5, will set the origin to the geometric center of the selected vertices
-What it essentially does:
Sets the 3d cursor to the average of the selected vertices
Changes to Object mode and sets origin to the 3d cursor
Changes back to edit mode and puts the 3d cursor back where it was

In Object mode:
Select object and press F5, will set origin to the objects geometric center
-What it essentially does:
Right click -> Set Origin -> Origin to Geometry




# todo:
1. Allow change of hotkey to be whatever the installer wants.
2. Remove added stuff that was part of the tutorial that i didn't really understand...no need for that total 4 stuff... 
