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
timestamp = datetime.datetime(2020, 1, 2, 9, 0, 0, 0)
# random_date("2020-01-01 01:30:00", "2024-12-01 05:45:44",  random.random())

for i in range(7): # number of sessions
    sceneId = random.randrange(20)
    if True: #i % 10 == 0: 
        timestamp = datetime.datetime.strptime(
            str(timestamp), '%Y-%m-%d %H:%M:%S') + datetime.timedelta(days=1)
    for j in range(10): # userid
        events_this_sesh = random.randint(2, 3) # randomly choose if this user will rate or not
        userId = j
        sessionId = i
        this_timestamp = datetime.datetime.strptime(
            str(timestamp), '%Y-%m-%d %H:%M:%S') + datetime.timedelta(hours=int(rnd.binomial(n=4, p=0.4, size=1)[0]), minutes=random.randrange(59), seconds=random.randrange(59))
        data = {}
        
        for k in range(events_this_sesh):
            id = id + 1
            type = ''
            data = {}
            if k == 0:
                type = 'CORE_SCENE_JOIN' 
                data['rating'] = None
            elif k == 1:
                type = 'CORE_SCENE_LEAVE'
                data['rating'] = None
            elif k==2:
                type = 'CORE_SCENE_RATE'
                data['rating'] = rnd.binomial(n=5, p=0.65, size=1)[0]

            if k == 1:
                this_timestamp = datetime.datetime.strptime(
                    str(this_timestamp), '%Y-%m-%d %H:%M:%S') + datetime.timedelta(hours=int(rnd.binomial(n=7, p=0.3, size=1)[0]), minutes=random.randrange(59), seconds=random.randrange(59))
            elif k == 2:
                this_timestamp = datetime.datetime.strptime(
                    str(this_timestamp), '%Y-%m-%d %H:%M:%S') + datetime.timedelta(minutes=random.randrange(2), seconds=random.randrange(59))

            data_csv.append([id, type, userId, sessionId, sceneId, datetime.datetime.strptime(
                str(this_timestamp), '%Y-%m-%d %H:%M:%S'), data])
    

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