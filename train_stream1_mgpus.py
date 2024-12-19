from ultralytics import YOLO
# Initialize model and specify the checkpoint
model = YOLO('yolo11x.pt')  # Use a pretrained YOLO model
#model = YOLO('yolov8x.pt')
#model = YOLO('runs/detect/train56/weights/best.pt')  # Use a pretrained YOLOv8 model
# Train the model with custom dataset
model.train(
    data='stream1.yaml',  # Path to YAML config
    epochs=25,                            # Number of epochs
    imgsz=1024,                            # Image size
    batch=24,                             # Batch size
    device=[0,1,2,3],                     # GPU device ID
    workers=1

)
metrics = model.val(data='stream1.yaml', imgsz=1024, batch=24, conf=0.50, iou=0.6, device=[0,1,2,3], plots=True)
print(metrics)



