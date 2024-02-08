from ultralytics import YOLO
import os

# model = YOLO("yolov8n.yaml")  # build a new model from scratch
# model.train(data="coco128.yaml", epochs=3)  # train the model
# metrics = model.val()  # evaluate model performance on the validation set
# Run batched inference on a list of images
# result = model('bus.jpg')  # return a list of Results objects

model = YOLO('yolov8n.pt')  # pretrained YOLOv8n model
dictionary = os.listdir("C:/Users/Никита/PycharmProjects/object_detecting/src/")
i = 0
for d in dictionary:
    count = 0
    i += 1
    fds = os.listdir(f'C:/Users/Никита/PycharmProjects/object_detecting/src/{d}')
    # if os.path.isdir(f'C:/Users/Никита/PycharmProjects/object_detecting/src/{filename}'):
    for img in fds:
        model.predict(f'src/{d}/' + img, save=True, imgsz=320, conf=0.6)
        count += 1
        print(f'{i} видео')
        print(f'Изображение {count} обработано')
