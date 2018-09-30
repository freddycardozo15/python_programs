# This python program processes the command line arguments using a json file.
# The command parameters are defined in the json file commandLine.json 

__author__ = 'Freddy Cardozo'

try:
  # Read the command line argument fields from the json file 'commandLineArguments.json'
  cmdLineDict = readJsonFile('commandLineArguments.json')
  cmdLineObj  = processCommandLineArgs(cmdLineDict)
except:
  print "Error occured"
