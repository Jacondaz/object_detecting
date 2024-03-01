from ultralytics import YOLO
import os
from object_sort import object_sort


def detect(diction):
    i = 0
    fds = os.listdir(f'src/{diction}')
    for img in fds:
        model.predict(f'src/{diction}/' + img, save=True, save_txt=True, imgsz=640, conf=0.6)
        i += 1
        print(f'{i} изображение обработано')


if __name__ == '__main__':
    scanned_files = list()
    model = YOLO('yolov8m.pt')
    dictionary = os.listdir("src/")
    count = 0
    for d in dictionary:
        if d not in scanned_files:
            #detect(d)
            object_sort(d)
            scanned_files.append(d)
            count += 1
            print(f'{count} видео обработано')
        else:
            print("Видео уже обработано")
