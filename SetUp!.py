from typing import Optional
import c4d

def main():
    
    #Code by Thoisoi Three https://vk.com/lighting.techdirector
    #Logo by Alexey Golod https://vk.com/golodvk

    #trash setup
    trash = c4d.BaseObject(c4d.Onull)
    doc.InsertObject(trash)
    trash.SetName('Trash / Archive') #folder name
    trash[c4d.ID_BASELIST_ICON_COLORIZE_MODE] = 2
    trash[c4d.ID_BASELIST_ICON_COLOR] = c4d.Vector(0.18824, 0.70196, 0.74902) #icon color
    trash[c4d.ID_BASELIST_ICON_FILE] = str(440000193)
    trash[c4d.NULLOBJECT_DISPLAY] = 14
    trash[c4d.NULLOBJECT_ORIENTATION] = 3

    #geometry setup
    geometry = c4d.BaseObject(c4d.Onull)
    doc.InsertObject(geometry)
    geometry.SetName('Geometry') #folder name
    geometry[c4d.ID_BASELIST_ICON_COLORIZE_MODE] = 2
    geometry[c4d.ID_BASELIST_ICON_COLOR] = c4d.Vector(0, 0.66667, 1) #icon color
    geometry[c4d.ID_BASELIST_ICON_FILE] = str(13364)
    geometry[c4d.NULLOBJECT_DISPLAY] = 14

    #lights setup
    light = c4d.BaseObject(c4d.Onull)
    doc.InsertObject(light)
    light.SetName('Light Setup') #folder name
    light[c4d.ID_BASELIST_ICON_COLORIZE_MODE] = 2
    light[c4d.ID_BASELIST_ICON_COLOR] = c4d.Vector(1, 0.83529, 0) #icon color
    light[c4d.ID_BASELIST_ICON_FILE] = str(200000031)
    light[c4d.NULLOBJECT_DISPLAY] = 14

    #cams setup
    cam = c4d.BaseObject(c4d.Onull)
    doc.InsertObject(cam)
    cam.SetName('Cameras') #folder name
    cam[c4d.ID_BASELIST_ICON_COLORIZE_MODE] = 2
    cam[c4d.ID_BASELIST_ICON_COLOR] = c4d.Vector(1, 0.21961, 0.14902) #icon color
    cam[c4d.ID_BASELIST_ICON_FILE] = str(18170)
    cam[c4d.NULLOBJECT_DISPLAY] = 14
    
    c4d.EventAdd()

    text = """
    SetUp is ready!
    """

    c4d.gui.MessageDialog(text)

if __name__ == '__main__':
    main()
