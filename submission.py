import os
import csv
from glob import glob
from ultralytics import YOLO

# Define the folder containing images and the output CSV file
image_folder = 'images/test/*.jpg'
output_csv = 'submission.csv'

# Class names corresponding to their IDs
class_names = {
    0: "proba_2",
    1: "cheops",
    2: "debris",
    3: "double_star",
    4: "earth_observation_sat_1",
    5: "lisa_pathfinder",
    6: "proba_3_csc",
    7: "proba_3_ocs",
    8: "smart_1",
    9: "soho",
    10: "xmm_newton"
}

# Load your YOLO model
model = YOLO('runs/detect/train73/weights/best.pt')
print("Model loaded successfully.")

# Create or overwrite the CSV file and write the header
with open(output_csv, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['filename', 'class', 'bbox'])

    # Iterate through all images matching the pattern
    for image_path in glob(image_folder):
        filename = os.path.basename(image_path)  # Get the file name from the full path

        # Perform inference on the image
        results = model.predict(image_path)

        # Iterate through the results
        for result in results:
            for det in result.boxes:
                # Extract bounding box (xyxy format) and class label
                bbox = det.xyxy[0].tolist()  # Convert tensor to list
                cls_id = int(det.cls[0])  # Convert class tensor to integer
                cls_name = class_names.get(cls_id, "unknown")  # Get class name or "unknown"

                # Format bbox as a string
                bbox_str = f"[{int(bbox[0])}, {int(bbox[1])}, {int(bbox[2])}, {int(bbox[3])}]"

                # Write the data to the CSV file
                writer.writerow([filename, cls_name, bbox_str])

print(f"Bounding box extraction completed. Results saved to {output_csv}.")
