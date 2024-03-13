import os
import re
from datetime import timedelta
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["video_base"]
objects = ['person', 'bicycle', 'car', 'motorcycle', 'airplane', 'bus', 'train', 'truck', 'boat', 'traffic light', 'fire hydrant', 'stop sign', 'parking meter', 'bench', 'bird', 'cat', 'dog', 'horse', 'sheep', 'cow', 'elephant', 'bear', 'zebra', 'giraffe', 'backpack', 'umbrella', 'handbag', 'tie', 'suitcase', 'frisbee', 'skis', 'snowboard', 'sports ball', 'kite', 'baseball bat', 'baseball glove', 'skateboard', 'surfboard', 'tennis racket', 'bottle', 'wine glass', 'cup', 'fork', 'knife', 'spoon', 'bowl', 'banana', 'apple', 'sandwich', 'orange', 'broccoli', 'carrot', 'hot dog', 'pizza', 'donut', 'cake', 'chair', 'couch', 'potted plant', 'bed', 'dining table', 'toilet', 'tv', 'laptop', 'mouse', 'remote', 'keyboard', 'cell phone', 'microwave', 'oven', 'toaster', 'sink', 'refrigerator', 'book', 'clock', 'vase', 'scissors', 'teddy bear', 'hair drier', 'toothbrush']


def object_sort(name_file):
    list_with_num = list()
    dd = os.listdir('./runs/detect/predict2/labels')
    frames = {i: [] for i in range(79)}
    frames_new = {i: [] for i in range(79)}
    j = 0

    for file in dd:
        a = list(re.split('[-.]', file)[:-1])
        if a[0] == name_file:
            with open(f'./runs/detect/predict2/labels/{file}', 'r') as text:
                for line in text:
                    temp = list(map(int, re.split('[-.]', file)[1:-2]))
                    a = timedelta(hours=temp[0], minutes=temp[1], seconds=temp[2])
                    a = int(a.total_seconds())
                    frames[int(line[0])].append(a)
        else:
            continue
    for lis in frames.values():
        len_arr = len(lis)
        total_list = list()

        if len_arr == 0:
            j += 1
            continue
        else:
            start = lis[0]
            for i in range(1, len_arr):
                if lis[i] - lis[i - 1] > 5:
                    if start == lis[i - 1]:
                        total_list.append(f'{start}')
                        start = lis[i]
                    else:
                        total_list.append(f'{start}-{lis[i - 1]}')
                        start = lis[i]
            total_list.append(f'{start}-{lis[-1]}')
            frames_new[j] = total_list
            j += 1

    with open(f'./results/{name_file}.txt', 'a+') as temp:
        for key, value in frames_new.items():
            if len(value) != 0:
                db[objects[key]].insert_one({f'{name_file}': value})

