import mlflow
import mlflow.pytorch
import torch
import pydicom
import cv2
from torch.utils.data import Dataset
from torchvision import transforms

# Load the model
model_path = r"C:\Users\HP1\Desktop\Spiced\capstone-project\mlruns\711328181724227740\deaa903e488043d19aad572a6c429479\artifacts\final_model"
model_for_prediction = mlflow.pytorch.load_model(model_path)

# Set model to evaluation mode
model_for_prediction.eval()

# Prepare data transform (to resize, jitter, and normalize the image)
transform = transforms.Compose([
    transforms.ToPILImage(),
    transforms.Resize((224, 224)),
    transforms.ColorJitter(brightness=0.2, contrast=0.2, saturation=0.2, hue=0.1),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])

# Dataset class for loading MRI images
class MRIDataset(Dataset):
    def __init__(self, data, transform=None):
        self.data = data
        self.transform = transform
        self.data['severity'] = self.data['severity'].astype(int)

    def __getitem__(self, index):
        row = self.data.iloc[index]
        image_path = row['image_path']
        label = row['severity']
        dicom_image = pydicom.dcmread(image_path)
        image = dicom_image.pixel_array.astype(float)
        image = (image / image.max() * 255).astype('uint8')
        if len(image.shape) == 2:  # Grayscale to RGB
            image = cv2.cvtColor(image, cv2.COLOR_GRAY2RGB)
        image_tensor = self.transform(image) if self.transform else torch.from_numpy(image).permute(2, 0, 1)
        return image_tensor, torch.tensor(label).long()

    def __len__(self):
        return len(self.data)
