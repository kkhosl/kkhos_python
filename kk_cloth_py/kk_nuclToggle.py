# Kitt Khosla
#nucleus on/off shelf button
import maya.cmds as mc

nucleus = mc.ls(type="nucleus")[-1]
state = mc.getAttr(nucleus+".enable")
if state:
    mc.setAttr(nucleus+".enable", 0)
else:
    mc.setAttr(nucleus+".enable", 1)
    
#mc.warning("xxx" + " " + str getAttr(nucleus+".enable")