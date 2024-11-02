import os
import cv2
import time
import pydicom
import numpy as np
import pandas as pd
from torchvision import transforms
from tqdm import tqdm

# Define the transform with augmentation
transform = transforms.Compose([
    transforms.ToPILImage(),
    transforms.Resize((224, 224)),
    transforms.RandomHorizontalFlip(),  # Randomly flip the image horizontally
    transforms.RandomRotation(10),       # Randomly rotate the image by ±10 degrees
    transforms.ColorJitter(brightness=0.2, contrast=0.2, saturation=0.2, hue=0.1),  # Adjust color properties
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])

# Set the output base folder
output_folder = r'C:\Users\HP1\Desktop\Spiced\capstone-project\data\train_images'
os.makedirs(output_folder, exist_ok=True)

# Start timing
start_time = time.time()

# Loop through each image path in the DataFrame
for _, row in tqdm(df_end.iterrows(), total=len(df_end)):
    image_path = row['image_path']
    output_folder = os.path.abspath(output_folder)
    image_path = os.path.abspath(image_path)
    
    # Create the relative path and output directory
    relative_path = os.path.relpath(image_path, os.path.commonpath([output_folder, image_path]))
    save_dir = os.path.join(output_folder, os.path.dirname(relative_path))
    
    # Create the corresponding output directory if it doesn't exist
    os.makedirs(save_dir, exist_ok=True)

    # Load the DICOM image
    try:
        dicom_image = pydicom.dcmread(image_path)
        image_array = dicom_image.pixel_array

        # Normalize and convert to 8-bit for transformation
        image_array = cv2.normalize(image_array, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)
        image_rgb = cv2.cvtColor(image_array, cv2.COLOR_GRAY2RGB)  # Convert to RGB

        # Apply transformations
        image_tensor = transform(image_rgb)
        image_transformed = image_tensor.permute(1, 2, 0).numpy()
        image_transformed = (image_transformed * 255).astype('uint8')

        # Save the transformed image with .png extension
        output_path = os.path.join(save_dir, os.path.basename(image_path).replace('.dcm', '.png'))
        cv2.imwrite(output_path, cv2.cvtColor(image_transformed, cv2.COLOR_RGB2BGR))
    except Exception as e:
        print(f"Error processing {image_path}: {e}")

# End timing
end_time = time.time()
total_time = end_time - start_time

print(f"Pre-transformation complete! Total time: {total_time:.2f} seconds.")
print(f"Average time per image: {total_time / len(df_end):.4f} seconds.")


import os
import cv2
import time
import pydicom
import numpy as np
import pandas as pd
from torchvision import transforms
from tqdm import tqdm

# Define the transform with augmentation
transform = transforms.Compose([
    transforms.ToPILImage(),
    transforms.Resize((224, 224)),
    transforms.RandomHorizontalFlip(),  # Randomly flip the image horizontally
    transforms.RandomRotation(10),       # Randomly rotate the image by ±10 degrees
    transforms.ColorJitter(brightness=0.2, contrast=0.2, saturation=0.2, hue=0.1),  # Adjust color properties
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])

# Set the output base folder
output_folder = r'C:\Users\HP1\Desktop\Spiced\capstone-project\data\train_images'
os.makedirs(output_folder, exist_ok=True)

# Start timing
start_time = time.time()

# Loop through each image path in the DataFrame
for _, row in tqdm(df_end.iterrows(), total=len(df_end)):
    image_path = row['image_path']
    output_folder = os.path.abspath(output_folder)
    image_path = os.path.abspath(image_path)
    
    # Create the relative path and output directory
    relative_path = os.path.relpath(image_path, os.path.commonpath([output_folder, image_path]))
    save_dir = os.path.join(output_folder, os.path.dirname(relative_path))
    
    # Create the corresponding output directory if it doesn't exist
    os.makedirs(save_dir, exist_ok=True)

    # Load the DICOM image
    try:
        dicom_image = pydicom.dcmread(image_path)
        image_array = dicom_image.pixel_array

        # Normalize and convert to 8-bit for transformation
        image_array = cv2.normalize(image_array, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)
        image_rgb = cv2.cvtColor(image_array, cv2.COLOR_GRAY2RGB)  # Convert to RGB

        # Apply transformations
        image_tensor = transform(image_rgb)
        image_transformed = image_tensor.permute(1, 2, 0).numpy()
        image_transformed = (image_transformed * 255).astype('uint8')

        # Replace the pixel array in the DICOM object with the transformed image
        transformed_image = cv2.cvtColor(image_transformed, cv2.COLOR_RGB2BGR)  # Convert back to BGR for DICOM

        # If the original DICOM image is grayscale, convert back to single channel
        if len(transformed_image.shape) == 3 and transformed_image.shape[2] == 3:
            transformed_image = cv2.cvtColor(transformed_image, cv2.COLOR_BGR2GRAY)

        # Update the pixel_array in the DICOM object
        dicom_image.PixelData = transformed_image.tobytes()
        dicom_image.Rows, dicom_image.Columns = transformed_image.shape  # Update dimensions

        # Save the transformed DICOM image in the output directory
        output_path = os.path.join(save_dir, os.path.basename(image_path))
        dicom_image.save_as(output_path)
    except Exception as e:
        print(f"Error processing {image_path}: {e}")

# End timing
end_time = time.time()
total_time = end_time - start_time

print(f"Pre-transformation complete! Total time: {total_time:.2f} seconds.")
print(f"Average time per image: {total_time / len(df_end):.4f} seconds.")
