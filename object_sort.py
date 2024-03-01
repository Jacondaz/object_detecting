import os
import re
from datetime import timedelta


def object_sort(name_file):
    list_with_num = list()
    dd = os.listdir('./runs/detect/predict2/labels')
    frames = {i: [] for i in range(70)}
    frames_new = {i: [] for i in range(70)}
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
            temp.write(f'{key}, {value}\n')
