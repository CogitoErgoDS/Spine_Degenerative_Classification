# Classification of Lumbar Spine Damages – BackPropagation for Back

**Author:** Paul Schmelzer  
**Source Dataset:** RSNA Lumbar Spine Challenge (Radiological Society of North America)  
**Goal:** Classify degenerative lumbar spine conditions from MRI images using transfer learning (ResNet-50).

---

## 🧠 Project Overview
This project applies deep learning to MRI images of the lumbar spine to **classify degenerative conditions** that affect the spinal canal and nerve roots.  
The main motivation is to **support radiologists** by automating the detection of key spinal abnormalities.

---

## 🩻 Clinical Background
Degenerative spine conditions can cause pain and mobility loss.  
The challenge focuses on **five conditions** across **five spinal levels** (L1/L2–L5/S1):

- Left Neural Foraminal Narrowing  
- Right Neural Foraminal Narrowing  
- Left Subarticular Stenosis  
- Right Subarticular Stenosis  
- Spinal Canal Stenosis  

Each condition is graded as **Normal/Mild**, **Moderate**, or **Severe**.

---

## 📊 Dataset
- **Origin:** Kaggle RSNA Lumbar Spine Challenge  
- **Subjects:** ~2000 patients  
- **Images per patient:** ~40 sagittal MRI slices → ~80,000 rows  
- **Focus for this project:** Left Neural Foraminal Narrowing at L5/S1  
- **Sampling:** 4,000 images per severity class (balanced by severity, not by person)  
- **Splits:**  
  - Train/Test → 80 % / 20 %  
  - Train/Validation → 80 % / 20 %  
- **Training time:** ≈ 1 hour per epoch, early stopping after 5–9 epochs  

**MRI Types used:**
- Sagittal T1  
- Sagittal T2  
- Axial T2  

*(Sagittal views are better suited for detecting foraminal narrowing.)*

---

## 🧩 Methods
### Model Architecture
- **Transfer Learning:** Pretrained **ResNet-50** (ImageNet-1k weights)  
- **Purpose:** Handle gradient vanishing and extract hierarchical features from medical images  
- **Training variants:**
  1. **With bounding boxes** → higher accuracy on localized regions (e.g., L5/S1)  
  2. **Without bounding boxes** → trained on full images, better generalization  

### Early Stopping
- **Divergence-based:** stop if validation loss exceeds training loss by > 0.5 for ≥ 5 epochs  
- **Plateau-based:** stop if validation loss fails to improve for ≥ 5 epochs  

---

## 📈 Results
- **Baseline accuracy:** ≈ 35 % (majority class)  
- **Final accuracy:** ≈ 85 % on test set  

| Training Type | Performance | Notes |
|----------------|--------------|-------|
| With Bounding Boxes | ⭐ Higher accuracy | Limited generalization |
| Without Bounding Boxes | ⚙️ Slightly lower accuracy | Better generalization across disc levels |

---

## 🚀 Next Steps
- Extend classification to all spinal levels (L1/L2 – L5/S1)  
- Localize damage regions (object detection or segmentation)  
- Compare model variants with/without bounding boxes  
- Explore other pretrained CNNs (EfficientNet, DenseNet)

---

## 🖼️ Visualization Placeholders
*(Add your PowerPoint figures here once exported as `.png`)*

| Figure | Description |
|---------|-------------|
| `fig1_anatomy.png` | Anatomical overview of lumbar spine regions |
| `fig2_foraminal_narrowing.png` | Example of foraminal narrowing (sagittal MRI) |
| `fig3_model_diagram.png` | Network architecture (ResNet-50 fine-tuning) |
| `fig4_results.png` | Accuracy comparison with/without bounding boxes |

---

## 🧾 Citation
Dataset:  
**RSNA Lumbar Spine Degenerative Conditions Dataset**  
Radiological Society of North America (RSNA), 2023.  
[https://www.kaggle.com/competitions/rsna-2023-lumbar-spine-degenerative](https://www.kaggle.com/competitions/rsna-2023-lumbar-spine-degenerative)

---

## 💡 Notes
This repository was created as part of a Kaggle competition project.  
Although not a winning solution, it demonstrates practical ML application in a real-world medical imaging challenge — combining data preprocessing, transfer learning, and early stopping strategies for robust performance.
