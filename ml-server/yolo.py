from ultralytics import YOLO
import cv2


def predict(filename):
    model = YOLO('best.pt')
    results = model(filename, conf=0.5, iou=0.6)
    r = results[0]
    im_array = r.plot()  
    cv2.imwrite(f'output/{filename}', im_array)
    boxes = results[0].boxes
    names = results[0].names
    result = ""
    for i, box in enumerate(boxes):
        class_id = int(box.cls) 
        class_name = names[class_id] 
        x_min, y_min, x_max, y_max = box.xyxy[0]
        result = (f"{result}\n{class_name} detected at coordinates ({x_min.item():.4f}, {y_min.item():.4f}, {x_max.item():.4f}, {y_max.item():.4f})\n")

    return result