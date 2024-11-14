import streamlit as st
import torch
from torchvision import transforms
from PIL import Image
import pydicom
import cv2
from my_model import model_for_prediction  # This imports the model from just_a_model.py

# Define transformation to process the images before input into the model
transform = transforms.Compose([
    transforms.ToPILImage(),
    transforms.Resize((224, 224)),
    transforms.ColorJitter(brightness=0.2, contrast=0.2, saturation=0.2, hue=0.1),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])

# Function to load and preprocess the DICOM image
def load_image(image_file):
    dicom_image = pydicom.dcmread(image_file)
    image = dicom_image.pixel_array.astype(float)
    image = (image / image.max() * 255).astype('uint8')
    if len(image.shape) == 2:  # Grayscale to RGB
        image = cv2.cvtColor(image, cv2.COLOR_GRAY2RGB)
    return image

# Streamlit app interface
st.title("Spine Damage Prediction")

st.write("Upload a DICOM file to predict spine damage severity.")

# Upload file from the user
uploaded_file = st.file_uploader("Choose a DICOM file", type="dcm")

if uploaded_file is not None:
    # Load the image
    image = load_image(uploaded_file)
    st.image(image, caption="Uploaded MRI Image", use_column_width=True)

    # Preprocess the image for the model (add batch dimension and transform)
    image_tensor = transform(image).unsqueeze(0)  # Add batch dimension
    image_tensor = image_tensor.to(torch.device('cuda' if torch.cuda.is_available() else 'cpu'))
    
    # Make the prediction
    with torch.no_grad():
        output = model_for_prediction(image_tensor)
        _, predicted_class = torch.max(output, 1)
    
    # Display the result
    st.write(f"Predicted Spine Damage Severity: {predicted_class.item()}")
