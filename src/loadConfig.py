import json
import os

def load_config(configFile):
    with open(configFile) as json_file:
        data = json.load(json_file)
    return data

def load_source_files(sc, source_files):
    #Spark
    #sc.addPyFile(os.path.join(source_files,"commonCassandraDB.py"))
    return sc
