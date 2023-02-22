"""
             ___        _    _ _       _ 
            / __> ___ _| |_ | | | ___ | |
            \__ \/ ._> | |  | ' || . \|_/
            <___/\___. |_|  `___'|  _/<_>
                                |_|
            Autosorting script for Cinema 4D by object type
            
    Authors:
    
    Thoisoi Three: https://vk.com/lighting.techdirector
    Alexey Golod: https://vk.com/golodvk
    Artem Kondrackii: https://vk.com/artem_kondrackii
"""

import c4d

# For old versions c4d
ICONS_AVAILABLE = c4d.GetC4DVersion() >= 21000

#* A dictionary of folders and object types to folder names
#! To know obj id type 'print(op.GetType())'
FOLDERS = {
    "Geometry": {
        "color": c4d.Vector(0, 0.66667, 1),
        "icon": 13364,
        "ids": [
            c4d.Opolygon,
            c4d.Osphere,
            c4d.Ocube,
            c4d.Onull,
            5163, # Torus
            5167, # Pyramid
            5173, # Relief
            5168, # Plane
            5171, # Capsule
            5161, # Platonic
            1027657, # Guide
            5162, # Cone
            5172, # Oil Tank
            5166, # Figure
            5165, # Tube
            5170, # Cylinder
            5169, # Landscape
            1019268, # Text,
            5120, # Bezier
            1007455, #* Subdivision
            1018544, #* Cloner
            1039861, #* Volume Mesher
            1039859, #* Volume Builder
            5126, #* Instance
            1011010, #* Connect
            1010865, #* Boole
            5116, #* Extrude
            5118, #* Sweep
            5142, #* Symmetry
            1050418, #* Octane ORBX
            1038649, #* RS Proxy
            1054728, #* V-Ray Proxy
            1035544, #* Corona Proxy
            1035792, #* Octane Volume/VDB
            1035961, #* Octane Scatter
            1050417, #* Octane Vectron
            1055637, #* Corona Volume Grid
            1058613, #* Corona Decal
            1058600, #* Corona Pattern
            1058682, #* Chaos Scatter
            1059505, #* V-Ray Particles
            1058532, #* V-Ray Scene
            1057380, #* V-Ray Fur
            1057445, #* V-Ray Clipper
            1059061, #* V-Ray Decal
            1059492, #* V-Ray Enmesh
            1038655, #* RS Volume
            1032509, #* Arnold Procedural
            1033693, #* Arnold Volume
            1055097, #* Arnold Scatter
        ]
    },
    "Light Setup": {
        "color": c4d.Vector(1, 0.83529, 0),
        "icon": 200000031,
        "ids": 
            [
                c4d.Olight,
                1030424, #* Arnold Lights
                1036751, #* Redshift Lights
                1053280, #* Rectangle Light V
                1053281, #* Sphere Light V
                1053277, #* Dome Light V
                1059898, #* Mesh Light V
                1053278, #* IES Light V
                1053287, #* V-Ray Sun V
                1032104, #* Corona Light C
                1032153, #* Corona Sun C
                1053478, #* Corona Sky C
                1036751, #* Redshift Light 
                1036754, #* Redshift Sky 
            ]
    },
    "Cameras": {
        "color": c4d.Vector(1, 0.21961, 0.14902),
        "icon": 18170,
        "ids": [
            c4d.Ocamera,
            1057516, #* Redshift camera    
        ]
    },
    "Trash / Archive": {
        "color": c4d.Vector(0.70196, 0.70196, 0.70196),
        "icon": 440000193,
        "ids": []
    }
}

# Separating the names
FOLDERS_NAMES = list(FOLDERS.keys())

# A dictionary to store the created folders
created_folders = []

# Creating folders to scene
def create_folder(name):
    config = FOLDERS[name]
    
    # Setup object to scene
    folder = c4d.BaseObject(c4d.Onull)
    folder.SetName(name) #folder name
    folder[c4d.NULLOBJECT_DISPLAY] = 14

    if ICONS_AVAILABLE:
        folder[c4d.ID_BASELIST_ICON_COLOR] = config['color'] #icon color
        folder[c4d.ID_BASELIST_ICON_FILE] = str(config['icon']) #icon image
        folder[c4d.ID_BASELIST_ICON_COLORIZE_MODE] = 2
        
    doc.InsertObject(folder)
    # Add object to store
    created_folders.append(folder)

# Getting the names from objects array
def get_names(objects):
    return [obj.GetName() for obj in objects]

def main():
    # Getting objects from scene
    scene_objects = doc.GetObjects()
    
    # If the objects are created before and the script is run again, then we restore the created_dictionary array.
    if len(created_folders) == 0:
        for obj in scene_objects:
            if obj.GetName() in FOLDERS_NAMES:
                created_folders.append(obj)

    # Creating folders if they haven't created before yet. If one of the folders is missing, then we create a missing one
    if FOLDERS_NAMES not in get_names(created_folders):
        for folder_name in FOLDERS_NAMES:
            if folder_name not in get_names(scene_objects):
                create_folder(folder_name)

    for obj in scene_objects:
        obj_name = obj.GetName()
        obj_type = obj.GetType()
        
        # Searching category by object id
        folder_name = next(iter(filter(lambda name: obj_type in FOLDERS[name]['ids'], FOLDERS)), None)
        
        # Limiting duplication of our folders
        if obj_name not in FOLDERS_NAMES:
            if folder_name is not None:
                folder = next(iter(filter(lambda f: f.GetName() == folder_name, created_folders)), None)
            else:
                continue
            
            if folder is not None:
                obj.InsertUnder(folder)
                
    # Update the scene
    c4d.EventAdd()
    # Done message
    c4d.gui.MessageDialog("SetUp is ready!")

if __name__ == "__main__":
    # Compatibility check
    if c4d.GetC4DVersion() >= 16000:
        main()
    else:
        c4d.gui.MessageDialog("SetUp it cannot be run, Cinema 4D R16 or newer is required!")
