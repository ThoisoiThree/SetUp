import c4d

def main():
    
    #! Authors:
    #! Thoisoi Three: https://vk.com/lighting.techdirector
    #! Alexey Golod: https://vk.com/golodvk

    #* A dictionary mapping object types to folder names
    #! To know obj id type 'print(op.GetType())'
    folders = {
        c4d.Olight: "Light Setup",
        c4d.Opolygon: "Geometry",
        c4d.Ocamera: "Cameras",
        c4d.Osphere: "Geometry",
        c4d.Ocube: "Geometry",
        1030424: "Light Setup", #* Arnold Lights
        1036751: "Light Setup", #* Redshift Lights
        1007455: "Geometry", #* Subdivision
        1018544: "Geometry", #* Cloner
        1039861: "Geometry", #* Volume Mesher
        1039859: "Geometry", #* Volume Builder
        5126: "Geometry", #* Instance
        1011010: "Geometry", #* Connect
        1010865: "Geometry", #* Boole
        5116: "Geometry", #* Extrude
        5118: "Geometry", #* Sweep
        5142: "Geometry", #* Symmetry
        1050418: "Geometry", #* Octane ORBX
        1038649: "Geometry", #* RS Proxy
        1054728: "Geometry", #* V-Ray Proxy
        1035544: "Geometry", #* Corona Proxy
        1035792: "Geometry", #* Octane Volume/VDB
        1035961: "Geometry", #* Octane Scatter
        1050417: "Geometry", #* Octane Vectron
        1055637: "Geometry", #* Corona Volume Grid
        1058613: "Geometry", #* Corona Decal
        1058600: "Geometry", #* Corona Pattern
        1058682: "Geometry", #* Chaos Scatter
        1059505: "Geometry", #* V-Ray Particles
        1058532: "Geometry", #* V-Ray Scene
        1057380: "Geometry", #* V-Ray Fur
        1057445: "Geometry", #* V-Ray Clipper
        1059061: "Geometry", #* V-Ray Decal
        1059492: "Geometry", #* V-Ray Enmesh
        1038655: "Geometry", #* RS Volume
        1032509: "Geometry", #* Arnold Procedural
        1033693: "Geometry", #* Arnold Volume
        1055097: "Geometry", #* Arnold Scatter
        1053280: "Light Setup", #* Rectangle Light V
        1053281: "Light Setup", #* Sphere Light V
        1053277: "Light Setup", #* Dome Light V
        1059898: "Light Setup", #* Mesh Light V
        1053278: "Light Setup", #* IES Light V
        1053287: "Light Setup", #* V-Ray Sun V
        1032104: "Light Setup", #* Corona Light C
        1032153: "Light Setup", #* Corona Sun C
        1053478: "Light Setup", #* Corona Sky C
    }

    #* A dictionary to store the created folders
    created_folders = {}
    #* Iterate over all objects in the scene
    for obj in doc.GetObjects():

        #* Check if the object has a folder specified in the folders dictionary
        folder_name = folders.get(obj.GetType())
        if folder_name is None:
            # If no folder is specified, skip the object
            continue

        #* Check if the folder has already been created
        folder = created_folders.get(folder_name)

        if folder is None:
            #* If the folder has not been created, create it
            folder = c4d.BaseObject(c4d.Onull)
            folder.SetName(folder_name)
            doc.InsertObject(folder)
            created_folders[folder_name] = folder

            if folder_name == "Geometry":
                folder[c4d.ID_BASELIST_ICON_COLORIZE_MODE] = 2
                folder[c4d.ID_BASELIST_ICON_COLOR] = c4d.Vector(0, 0.66667, 1) #*icon color
                folder[c4d.ID_BASELIST_ICON_FILE] = str(13364)
                folder[c4d.NULLOBJECT_DISPLAY] = 14
            if folder_name == "Light Setup":
                folder[c4d.ID_BASELIST_ICON_COLORIZE_MODE] = 2
                folder[c4d.ID_BASELIST_ICON_COLOR] = c4d.Vector(1, 0.83529, 0) #*icon color
                folder[c4d.ID_BASELIST_ICON_FILE] = str(200000031)
                folder[c4d.NULLOBJECT_DISPLAY] = 14
            if folder_name == "Cameras":
                folder[c4d.ID_BASELIST_ICON_COLORIZE_MODE] = 2
                folder[c4d.ID_BASELIST_ICON_COLOR] = c4d.Vector(1, 0.21961, 0.14902) #*icon color
                folder[c4d.ID_BASELIST_ICON_FILE] = str(18170)
                folder[c4d.NULLOBJECT_DISPLAY] = 14

        # Move the object to the folder
        obj.InsertUnder(folder)

    if "Light Setup" not in created_folders:
        #*lights setup
        light = c4d.BaseObject(c4d.Onull)
        doc.InsertObject(light)
        light.SetName('Light Setup') #folder name
        light[c4d.ID_BASELIST_ICON_COLORIZE_MODE] = 2
        light[c4d.ID_BASELIST_ICON_COLOR] = c4d.Vector(1, 0.83529, 0) #icon color
        light[c4d.ID_BASELIST_ICON_FILE] = str(200000031)
        light[c4d.NULLOBJECT_DISPLAY] = 14

    if "Cameras" not in created_folders:
        #*cams setup
        cam = c4d.BaseObject(c4d.Onull)
        doc.InsertObject(cam)
        cam.SetName('Cameras') #folder name
        cam[c4d.ID_BASELIST_ICON_COLORIZE_MODE] = 2
        cam[c4d.ID_BASELIST_ICON_COLOR] = c4d.Vector(1, 0.21961, 0.14902) #icon color
        cam[c4d.ID_BASELIST_ICON_FILE] = str(18170)
        cam[c4d.NULLOBJECT_DISPLAY] = 14

    if "Geometry" not in created_folders:
        #*geometry setup
        geometry = c4d.BaseObject(c4d.Onull)
        doc.InsertObject(geometry)
        geometry.SetName('Geometry') #folder name
        geometry[c4d.ID_BASELIST_ICON_COLORIZE_MODE] = 2
        geometry[c4d.ID_BASELIST_ICON_COLOR] = c4d.Vector(0, 0.66667, 1) #icon color
        geometry[c4d.ID_BASELIST_ICON_FILE] = str(13364)
        geometry[c4d.NULLOBJECT_DISPLAY] = 14

    if "Trash / Archive" not in created_folders:
        trash = c4d.BaseObject(c4d.Onull)
        doc.InsertObject(trash)
        trash.SetName('Trash / Archive') #folder name
        trash[c4d.ID_BASELIST_ICON_COLORIZE_MODE] = 2
        trash[c4d.ID_BASELIST_ICON_COLOR] = c4d.Vector(0.70196, 0.70196, 0.70196) #icon color
        trash[c4d.ID_BASELIST_ICON_FILE] = str(440000193)
        trash[c4d.NULLOBJECT_DISPLAY] = 14
    
    #* Update the scene
    c4d.EventAdd()

    text = """
    SetUp is ready!
    
    If the scene is empty just add an object!
    """
    c4d.gui.MessageDialog(text)

if __name__ == '__main__':
    main()
