RSNA 2024 Lumbar Spine Degenerative Classification

Introduction: 

Low back pain is the leading cause of disability worldwide, as reported by the World Health Organization, affecting approximately 619 million people in 2020. The prevalence of low back pain increases with age, with most individuals experiencing it at some point in their lives. Pain and limited mobility are common symptoms of spondylosis, a collection of degenerative spine conditions characterized by the degeneration of intervertebral discs and subsequent narrowing of the spinal canal (spinal stenosis). This can lead to compression or irritation of the nerves in the lower back, significantly impacting the quality of life.

Magnetic Resonance Imaging (MRI) offers a detailed visualization of the lumbar spine, including vertebrae, discs, and nerves, enabling radiologists to assess the presence and severity of degenerative conditions accurately. Proper diagnosis and grading of these conditions are crucial for guiding treatment and potential surgical interventions aimed at alleviating back pain and enhancing overall health.

The Radiological Society of North America (RSNA) has partnered with the American Society of Neuroradiology (ASNR) to conduct a competition exploring the potential of artificial intelligence (AI) in aiding the detection and classification of degenerative spine conditions using lumbar spine MRI images.


Classification of five lumbar spine degenerative conditions:

    Left Neural Foraminal Narrowing
    Right Neural Foraminal Narrowing
    Left Subarticular Stenosis
    Right Subarticular Stenosis
    Spinal Canal Stenosis

For each imaging study in the dataset, severity scores (Normal/Mild, Moderate, or Severe) have been provided for these five conditions across the intervertebral disc levels L1/L2, L2/L3, L3/L4, L4/L5, and L5/S1.

The ground truth dataset was created through collaboration between the RSNA challenge planning task force and eight imaging sites across five continents. This expertly curated, multi-institutional dataset aims to enhance standardized classification of degenerative lumbar spine conditions and facilitate the development of tools for accurate and rapid disease classification.
Evaluation Metrics

Submissions for the competition will be evaluated based on the average of sample weighted log losses and an any_severe_spinal prediction. The specific sample weights are as follows:

    1 for Normal/Mild
    2 for Moderate
    4 for Severe

 
![Alt text]("C:\Users\HP1\Desktop\Spiced\capstone-project\Presenation\images\Picture1.png")
