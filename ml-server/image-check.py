import os
import cv2
from ultralytics import YOLO

# Initialize the model
model = YOLO('best.pt')

# Define input and output directories
input_dir = 'input'
output_dir = 'output'
os.makedirs(output_dir, exist_ok=True)

# Function to process and save image with bounding boxes
def process_image(img_path, output_path):
    results = model(img_path, conf=0.5, iou=0.6)
    r = results[0]
    im_array = r.plot()  # Plot bounding boxes on the image
    
    # Save the image with bounding boxes
    cv2.imwrite(output_path, im_array)

# Traverse the directory
for root, dirs, files in os.walk(input_dir):
    for file in files:
        # Process only image files (modify extensions as needed)
        if file.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff')):
            img_path = os.path.join(root, file)
            relative_path = os.path.relpath(img_path, input_dir)
            output_path = os.path.join(output_dir, relative_path)
            
            # Ensure the output directory exists
            os.makedirs(os.path.dirname(output_path), exist_ok=True)
            
            # Process the image and save it
            process_image(img_path, output_path)

print("Processing complete.")
