# This python program processes the command line arguments using a json file.
# The command parameters are defined in the json file commandLine.json 

try:
  cmdLineDict = readJsonFile('cmdLine.json')
  cmdLineObj  = processCommandLineArgs(cmdLineDict)
except:
  print "Error occured"
