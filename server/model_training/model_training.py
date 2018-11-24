import json
import numpy as np

emotions = ["anger", "contempt", "disgust", "fear", "happiness", "neutral", "sadness", "surprise"]

def normalize(v):
    normalized_v = v / np.sqrt((np.sum(v ** 2)))
    return normalized_v

def convertTargetInformationToJSON(txt_path):
    raw_data = open(txt_path, "r").read()
    j = {}
    trucks = raw_data.split("\n")
    for t in trucks:
        truck_info = t.split(" -> ")
        id = truck_info[0]
        emotions_list = truck_info[1].split(" ")
        emotions_values = normalize(list(map(int, emotions_list)))
        for i in range(len(emotions)):
            j[id][emotions[i]] = emotions_values[i]
    return j


# Both JSON have the same tracks and the first one
# has the information of the explicative variables
# and the second onw the target variables.
def mergeTrackJSONFields(j1 , j2):
    j = {}
    for key in j1:
        fields1 = j1[key]
        if key in j2:
            fields2 = j2[key]
            for field in fields1:
                j[key][field] = fields1[field]
            for field in fields2:
                j[key][field] = fields2[field]
    return j

def saveJSONToPath(json_path, fileName, data):
        filePathName = json_path + '/' + fileName + '.json'
        with open(filePathName, 'w') as fp:
            json.dump(data, fp)


def getTrackJSONFromPath(json_path, fileName):
    filePathName = json_path + '/' + fileName + '.json'
    with open(filePathName) as data_file:
        data = json.load(data_file)
    return data




if __name__ == '__main__':
    convertTargetInformationToJSON("")