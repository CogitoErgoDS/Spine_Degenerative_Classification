import os
import cv2
import time
import pandas as pd
from torchvision import transforms
from tqdm import tqdm

# Define the transform with augmentation
transform = transforms.Compose([
    transforms.ToPILImage(),
    transforms.Resize((224, 224)),
    transforms.RandomHorizontalFlip(),
    transforms.RandomRotation(10),
    transforms.ColorJitter(brightness=0.2, contrast=0.2, saturation=0.2, hue=0.1),
    transforms.ToTensor(),
])

# Load your DataFrame (assuming 'image_path' column contains the file paths)
df = pd.read_csv('path/to/your_dataframe.csv')  # Adjust this to your DataFrame file

# Set the output base folder
output_folder = r'C:\Users\HP1\Desktop\Spiced\capstone-project\data\train_images_transformed'
os.makedirs(output_folder, exist_ok=True)

# Start timing
start_time = time.time()

# Loop through each image path in the DataFrame
for _, row in tqdm(df.iterrows(), total=len(df)):
    image_path = row['image_path']
    relative_path = os.path.relpath(image_path, os.path.commonpath([output_folder, image_path]))
    save_dir = os.path.join(output_folder, os.path.dirname(relative_path))
    
    # Create the corresponding output directory if it doesn't exist
    os.makedirs(save_dir, exist_ok=True)
    
    # Load and process each image
    image = cv2.imread(image_path)
    if image is None:
        print(f"Warning: Could not read image {image_path}")
        continue

    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image_tensor = transform(image)
    image_transformed = image_tensor.permute(1, 2, 0).numpy()
    image_transformed = (image_transformed * 255).astype('uint8')

    # Save the transformed image
    output_path = os.path.join(save_dir, os.path.basename(image_path))
    cv2.imwrite(output_path, cv2.cvtColor(image_transformed, cv2.COLOR_RGB2BGR))

# End timing
end_time = time.time()
total_time = end_time - start_time

print(f"Pre-transformation complete! Total time: {total_time:.2f} seconds.")
print(f"Average time per image: {total_time / len(df):.4f} seconds.")
