from typing import Optional
import c4d

def main():

    #trash setup
    trash = c4d.BaseObject(c4d.Onull)
    doc.InsertObject(trash)
    trash.SetName('Trash / Archive')
    trash[c4d.ID_BASELIST_ICON_COLORIZE_MODE] = 2
    trash[c4d.ID_BASELIST_ICON_COLOR] = c4d.Vector(0.18824, 0.70196, 0.74902)
    trash[c4d.ID_BASELIST_ICON_FILE] = str(440000193)
    trash[c4d.NULLOBJECT_DISPLAY] = 4
    trash[c4d.NULLOBJECT_ORIENTATION] = 3

    #geometry setup
    geometry = c4d.BaseObject(c4d.Onull)
    doc.InsertObject(geometry)
    geometry.SetName('Geometry')
    geometry[c4d.ID_BASELIST_ICON_COLORIZE_MODE] = 2
    geometry[c4d.ID_BASELIST_ICON_COLOR] = c4d.Vector(0, 0.66667, 1)
    geometry[c4d.ID_BASELIST_ICON_FILE] = str(13364)
    geometry[c4d.NULLOBJECT_DISPLAY] = 14

    #lights setup
    light = c4d.BaseObject(c4d.Onull)
    doc.InsertObject(light)
    light.SetName('Light Setup')
    light[c4d.ID_BASELIST_ICON_COLORIZE_MODE] = 2
    light[c4d.ID_BASELIST_ICON_COLOR] = c4d.Vector(1, 0.83529, 0)
    light[c4d.ID_BASELIST_ICON_FILE] = str(200000031)
    light[c4d.NULLOBJECT_DISPLAY] = 14

    #cams setup
    cam = c4d.BaseObject(c4d.Onull)
    doc.InsertObject(cam)
    cam.SetName('Cameras')
    cam[c4d.ID_BASELIST_ICON_COLORIZE_MODE] = 2
    cam[c4d.ID_BASELIST_ICON_COLOR] = c4d.Vector(1, 0.21961, 0.14902)
    cam[c4d.ID_BASELIST_ICON_FILE] = str(18170)
    cam[c4d.NULLOBJECT_DISPLAY] = 14
    
    c4d.EventAdd()
    c4d.gui.MessageDialog("SetUp is ready!")


if __name__ == '__main__':
    main()