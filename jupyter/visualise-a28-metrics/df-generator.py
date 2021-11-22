import csv
import json
from os import times
import random
import time
import datetime
from numpy import random as rnd
import uuid

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
rating_categories = ['Network', 'Collab Tools', 'Chat', 'Cat4', 'Cat5', 'Cat6']
header = ['id', 'type', 'userId', 'sceneId', 'timestamp', 'data']
data_csv = list()
data_json = list()
id = 0
timestamp = datetime.datetime(2021, 6, 2, 9, 0, 0, 0)
# random_date("2020-01-01 01:30:00", "2024-12-01 05:45:44",  random.random())

userId_arr = []
# generate 10 users:
for i in range(10):
    userId_arr.append(str(uuid.uuid4()))


for i in range(500): # number of sessions
    sceneId = str(uuid.uuid4())
    timestamp = datetime.datetime.strptime(
        str(timestamp), '%Y-%m-%d %H:%M:%S') + datetime.timedelta(days=1)

    #skip this day if weekend
    if timestamp.weekday() >= 5 or timestamp > datetime.datetime.now():
        continue
    
    for j in range(10): # userid
        events_this_sesh = random.randint(2, 3) # randomly choose if this user will rate or not
        userId = userId_arr[j - 1]
        this_timestamp = datetime.datetime.strptime(
            str(timestamp), '%Y-%m-%d %H:%M:%S') + datetime.timedelta(hours=int(rnd.binomial(n=4, p=0.4, size=1)[0]), minutes=random.randrange(59), seconds=random.randrange(59))
        data = {}
        
        for k in range(events_this_sesh):
            id = str(uuid.uuid4())
            type = ''
            data = {}
            if k == 0:
                type = 'CORE_SCENE_JOIN' 
                data['ratingValue'] = None
                data['ratingCategory'] = None
            elif k == 1:
                type = 'CORE_SCENE_LEAVE'
                data['ratingValue'] = None
                data['ratingCategory'] = None
            elif k==2:
                type = 'CORE_SCENE_RATE'
                random_index = random.randint(0, len(rating_categories) - 1)
                data['ratingValue'] = int(rnd.binomial(
                    n=5, p=random_index/len(rating_categories), size=1)[0])
                data['ratingCategory'] = rating_categories[random_index]

            if k == 1:
                this_timestamp = datetime.datetime.strptime(
                    str(this_timestamp), '%Y-%m-%d %H:%M:%S') + datetime.timedelta(hours=int(rnd.binomial(n=7, p=0.3, size=1)[0]), minutes=random.randrange(59), seconds=random.randrange(59))
            elif k == 2:
                this_timestamp = datetime.datetime.strptime(
                    str(this_timestamp), '%Y-%m-%d %H:%M:%S') + datetime.timedelta(minutes=random.randrange(2), seconds=random.randrange(59))

            data_csv.append([id, type, userId, sceneId, datetime.datetime.strptime(
                str(this_timestamp), '%Y-%m-%d %H:%M:%S'), data])
            
            temp_json_vals = [id, type, userId, sceneId, time.mktime(datetime.datetime.strptime(
                str(this_timestamp), '%Y-%m-%d %H:%M:%S').timetuple()), data]
            json_dict = dict(zip(header, temp_json_vals))
            data_json.append(json_dict)
            
    

with open('dummy.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)

    # write the header
    writer.writerow(header)

    # write multiple rows
    writer.writerows(data_csv)

# save as json
json_data = {}

with open('dummy.json', 'w') as jsonFile:
    jsonFile.write(json.dumps(data_json, default= str, indent= 4))
