import os
import shutil

# Get current script directory
base_dir = os.path.dirname(os.path.abspath(__file__))

# Define folders
source_folder = os.path.join(base_dir, "source")
destination_folder = os.path.join(base_dir, "moved_images")

# Create destination folder if it doesn't exist
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# Move all .jpg files
for file in os.listdir(source_folder):
    if file.endswith(".jpg"):
        source_path = os.path.join(source_folder, file)
        destination_path = os.path.join(destination_folder, file)

        shutil.move(source_path, destination_path)
        print(f"Moved: {file}")

print("All .jpg files moved successfully!")