from ultralytics import YOLO
import os


def detect(diction):
    i = 0
    fds = os.listdir(f'src/{diction}')
    for img in fds:
        model.predict(f'src/{diction}/' + img, save=True, save_txt=True, imgsz=640, conf=0.6)
        i += 1
        print(f'{i} изображение обработано')


if __name__ == '__main__':
    model = YOLO('yolov8x.pt')
    dictionary = os.listdir("src/")
    count = 0
    for d in dictionary:
        detect(d)
        count += 1
        print(f'{count} видео обработано')
