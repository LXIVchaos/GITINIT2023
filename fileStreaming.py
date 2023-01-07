import json
def readJsonFile(fileName):
    jfile = open(fileName, "r")
    jdata = json.loads(jfile.read())
    jfile.close()
    return jdata

def writeJsonFile(fileName, data):
    jfile = open(fileName, "w")
    jfile.write(json.dump(data))
    jfile.close()