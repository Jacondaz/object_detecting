from ultralytics import YOLO


# Load a model
model = YOLO('yolov8n.pt')  # pretrained YOLOv8n model

# model = YOLO("yolov8n.yaml")  # build a new model from scratch
# Use the model
# model.train(data="coco128.yaml", epochs=3)  # train the model
# metrics = model.val()  # evaluate model performance on the validation set
# results = model("https://ultralytics.com/images/bus.jpg")  # predict on an image
# Run batched inference on a list of images
# result = model('bus.jpg')  # return a list of Results objects
model.predict('street.jpg', save=True, imgsz=320, conf=0.5)
