from ultralytics import YOLO
model=YOLO('best.pt')
model('1.jpg', save=True)
