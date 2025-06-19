from ultralytics import YOLO
import cv2
import os

# Load the YOLO model
model = YOLO('best.pt')

# Specify input and output folders
input_folder = "input"
output_folder = "output"

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Loop through all images in the input folder
for filename in os.listdir(input_folder):
  if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
    image_path = os.path.join(input_folder, filename)  


    # Predict bounding boxes on the image
    results = model(image_path, conf=0.5, iou=0.6)
    r = results[0]

    if len(results) > 0:  # Check if any objects were detected
      im_array = r.plot()  # Generate image with bounding boxes

      # Save the image with bounding boxes in the output folder
      output_filename = os.path.basename(filename)
      cv2.imwrite(f'output/{output_filename}', im_array)

      # Extract and save bounding box information (optional)
      boxes = results[0].boxes
      names = results[0].names
      result = ""
      for i, box in enumerate(boxes):
        class_id = int(box.cls)
        class_name = names[class_id]
        x_min, y_min, x_max, y_max = box.xyxy[0]
        result = (f"{result}\n{class_name} detected at coordinates ({x_min.item():.4f}, {y_min.item():.4f}, {x_max.item():.4f}, {y_max.item():.4f})")

      # Save bounding box information to a text file (optional)
      with open(f'output/{output_filename[:-4]}.txt', 'w') as f:
        f.write(result)

print(f"Processed {len(os.listdir(input_folder))} images. Check the 'output' folder for results.")