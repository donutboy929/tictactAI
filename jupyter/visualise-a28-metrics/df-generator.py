import csv
import json
from os import times
import random
import time
import datetime
from numpy import random as rnd

# helper functions
def str_time_prop(start, end, time_format, prop):
    """Get a time at a proportion of a range of two formatted times.

    start and end should be strings specifying times formatted in the
    given format (strftime-style), giving an interval [start, end].
    prop specifies how a proportion of the interval to be taken after
    start.  The returned time will be in the specified format.
    """

    stime = time.mktime(time.strptime(start, time_format))
    etime = time.mktime(time.strptime(end, time_format))

    ptime = stime + prop * (etime - stime)

    return time.strftime(time_format, time.localtime(ptime))


def random_date(start, end, prop):
    return str_time_prop(start, end, '%Y-%m-%d %H:%M:%S', prop)


# start
header = ['id', 'type', 'userId', 'sessionId', 'sceneId', 'timestamp', 'data']
data_csv = list()
id = 0
timestamp = random_date(
    "2020-01-01 01:30:00", "2024-12-01 05:45:44",  random.random())

for i in range(100):
    events_this_sesh = random.randint(2, 3)
    userId = random.randrange(10)
    sessionId = i
    sceneId = random.randrange(20)
    timestamp = datetime.datetime.strptime(
        str(timestamp), '%Y-%m-%d %H:%M:%S') + datetime.timedelta(hours=int(rnd.binomial(n=7, p=0.2, size=1)[0]), minutes=random.randrange(59), seconds=random.randrange(59))
    data = {}
    
    for j in range(events_this_sesh):
        id = id + 1
        type = ''
        data = {}
        if j == 0:
            type = 'CORE_SCENE_JOIN' 
            data['rating'] = None
        elif j == 1:
            type = 'CORE_SCENE_LEAVE'
            data['rating'] = None
        elif j==2:
            type = 'CORE_SCENE_RATE'
            data['rating'] = rnd.binomial(n=5, p=0.6, size=1)[0]

        if j == 1:
            timestamp = datetime.datetime.strptime(
                str(timestamp), '%Y-%m-%d %H:%M:%S') + datetime.timedelta(hours=random.randrange(7), minutes=random.randrange(59), seconds=random.randrange(59))
        elif j == 2:
            timestamp = datetime.datetime.strptime(
                str(timestamp), '%Y-%m-%d %H:%M:%S') + datetime.timedelta(minutes=random.randrange(2), seconds=random.randrange(59))

        data_csv.append([id, type, userId, sessionId, sceneId, datetime.datetime.strptime(
            str(timestamp), '%Y-%m-%d %H:%M:%S'), data])

    

with open('dummy.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)

    # write the header
    writer.writerow(header)

    # write multiple rows
    writer.writerows(data_csv)

# save as json
'''json_data = {}

with open('dummy.csv') as csvFile:
    csvReader = csv.DictReader(csvFile)
    for rows in csvReader:
        id = rows['id']
        json_data[id] = rows

with open('dummy.json', 'w') as jsonFile:
    jsonFile.write(json.dumps(json_data, indent = 4))'''
