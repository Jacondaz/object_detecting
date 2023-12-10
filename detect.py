from ultralytics import YOLO
import os

# model = YOLO("yolov8n.yaml")  # build a new model from scratch
# model.train(data="coco128.yaml", epochs=3)  # train the model
# metrics = model.val()  # evaluate model performance on the validation set
# Run batched inference on a list of images
# result = model('bus.jpg')  # return a list of Results objects

fds = os.listdir("C:/Users/karet/PycharmProjects/object_detecting_yolo/src/example2")
model = YOLO('yolov8n.pt')  # pretrained YOLOv8n model
count = 0
for img in fds:
    model.predict('src/example2/' + img, save=True, imgsz=320, conf=0.5)
    count += 1
    print(f'Изображение {count} обработано')
