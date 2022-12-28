import c4d

# A dictionary mapping object types to folder names
folders = {
    c4d.Olight: "Lights",
    c4d.Opolygon: "Geometry",
    c4d.Ocamera: "Cameras",
    c4d.Osphere: "Geometry",
    c4d.Ocube: "Geometry",
}

# A dictionary to store the created folders
created_folders = {}

# Iterate over all objects in the scene
for obj in doc.GetObjects():
    # Check if the object has a folder specified in the folders dictionary
    folder_name = folders.get(obj.GetType())
    if folder_name is None:
        # If no folder is specified, skip the object
        continue

    # Check if the folder has already been created
    folder = created_folders.get(folder_name)
    if folder is None:
        # If the folder has not been created, create it
        folder = c4d.BaseObject(c4d.Onull)
        folder.SetName(folder_name)
        doc.InsertObject(folder)
        created_folders[folder_name] = folder

    # Move the object to the folder
    obj.InsertUnder(folder)

# Update the scene
c4d.EventAdd()