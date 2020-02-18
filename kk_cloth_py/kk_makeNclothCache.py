# Kitt Khosla
#Batch runs in shot, and requires the "path/file.ma" and the "path/doCacheNcloth.mel" script.
import maya.cmds as mc

outputdir = "/path/nCache/"
clothCages = ["name_geo", "name2_geo", "name3_geo"]
clothArgs = ["2", "1", "10", "OneFilePerFrame", "1", "", "0", "", "0", "add", "0", "1", "1", "0", "1"]
clothVer = 4

def makeNclothCache(ver, args, cages):
	mc.select(clothCages)
	mc.doCreateNclothCache(version=ver, filepath=outputdir, args=clothArgs)

makeNclothCache(clothVer, clothArgs, clothCages)
