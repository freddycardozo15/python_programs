import argparse
from collections import OrderedDict as od

# Description :   Process command line arguments using argparse python module
# Input Arguments:
#    1. cmdLineDict : Dictionary having all the options being passed
# Return Value:
#    cmdLineObj  : Argument Parser object having all the parsed objects
def processCommandLineArgs(cmdLineDict=od()):
    argParseObj = argparse.ArgumentParser(description="Parse the command line arguments")
    for option in cmdLineDict:
        subOptionArr = list()
        for optionArgs, optionArgValue in cmdLineDict[option].items():
            if type(optionArgValue) is str or type(optionArgValue) is unicode:
                subOptionArr.append("{}='{}'".format(subOption, str(optionArgValue)))
            else:
                subOptionArr.append("{}={}".format(subOption, str(optionArgValue)))
        subOptionStr = ','.join(subOptionArr)
        cmdLineStr = "'" +  option + "'" + ',' + subOptionStr
        cmdLineStr = "argParseObj.add_argument({})".format(cmdLineStr)
        ret = eval(cmdLineStr)
    cmdLineObj = argParseObj.parse_args()
    return cmdLineObj
