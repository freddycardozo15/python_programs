from argparse    import ArgumentParser
from json        import load as jsonLoad
from collections import OrderedDict as od

# Description :   Process command line arguments using argparse python module
# Input Arguments:
#    1. cmdLineDict : Dictionary having all the options being passed
# Return Value:
#    cmdLineObj  : Argument Parser object having all the parsed objects
def processCommandLineArgs(cmdLineDict=od()):
    argParseObj = ArgumentParser(description="Parse the command line arguments")
    try:
        for option in cmdLineDict.keys():
            subOptionArr = list()
            for optionArg, optionArgValue in cmdLineDict[option].items():
                if type(optionArgValue) is str:
                    subOptionArr.append("{}='{}'".format(optionArg, str(optionArgValue)))
                else:
                    subOptionArr.append("{}={}".format(optionArg, str(optionArgValue)))
            subOptionStr = ','.join(subOptionArr)
            cmdLineStr   = "'" +  option + "'" + ',' + subOptionStr
            cmdLineStr   = "argParseObj.add_argument({})".format(cmdLineStr)
            returnVal    = eval(cmdLineStr)
            if returnVal == 0:
                print("add_arguement worked fine \n")
    except StopIteration:
        pass
    cmdLineObj = argParseObj.parse_args()
    return cmdLineObj


# Description :   Reads a json file and forms a dictionary
# Input Arguments:
#           cmdLineDict : Dictionary having all the options being passed
# Return Value:
#            Argument Parser object having all the parsed objects
def readJsonFile(jsonFile):
    jsonData = od(jsonLoad(open(jsonFile, mode='r')))
    return jsonData
