# Healthcare Fraud Detection Analysis

This project aims to develop an accurate and precise healthcare provider fraud detection system using machine learning algorithms. The system analyzes healthcare data to identify fraudulent activities and promote integrity within the healthcare industry.

![Medicare Fraud](medicare_fraud-1.jpg)

## Business Understanding

Healthcare fraud is a significant challenge globally, resulting in financial losses, compromised patient care, and reduced trust in the healthcare system. Detecting fraudulent activities manually is time-consuming and prone to errors. Therefore, an automated fraud detection system is needed to enhance transparency, accountability, and financial sustainability in healthcare.

## Data Understanding

The project utilizes a comprehensive dataset obtained from Kaggle. The dataset contains information such as provider details, patient demographics, medical procedures, and billing information. Exploratory data analysis (EDA) is performed to gain insights into the dataset and identify patterns related to fraudulent activities. Visualizations are used to present the distribution of fraud cases, correlations between variables, and other relevant insights.

## Modeling and Evaluation

The project employs several machine learning algorithms to detect healthcare provider fraud, including KNN (K-Nearest Neighbors), Decision Tree, SVM (Support Vector Machine), Gradient Boost, Logistic Regression, and XGBoost classifiers. Each classifier is trained on the dataset and evaluated using various metrics such as AUC score, recall rate, precision, and F1 score. The final model, Grid Search Random Forest, combines the predictions of multiple classifiers to enhance overall fraud detection performance.

The performance of the final model is compared to a baseline model, which represents the accuracy achieved by traditional manual detection methods. The final model significantly outperforms the baseline, demonstrating its effectiveness in identifying fraudulent activities in healthcare providers.

## Conclusion

The healthcare provider fraud detection system developed in this project offers an effective and reliable solution to combat fraud within the healthcare industry. By harnessing the power of machine learning algorithms and advanced techniques, the system enhances transparency, improves patient care, and safeguards the financial integrity of healthcare organizations. Its implementation can assist insurance companies, government agencies, and healthcare providers in detecting and preventing fraudulent activities, leading to substantial cost savings and upholding the trust and credibility of the healthcare system.

## Project Installation Instructions

To install the project, you will need to have Anaconda installed. Then you can proceed to create a virtual environment.

### 1. Install Anaconda

Please refer to the following documentation:
- [Windows Installation Guide](https://github.com/learn-co-curriculum/dsc-data-science-env-windows-installation.git)
- [macOS Installation Guide](https://github.com/learn-co-curriculum/dsc-data-science-env-mac-installation.git)

### 2. Create a Virtual Environment

Once Anaconda is installed, you can create a virtual environment by following the instructions in the repository:
- [Creating a Virtual Environment](https://github.com/learn-co-curriculum/dsc-data-science-env-config.git)

## Repository Navigation

To use the project, follow these steps:
- Fork and Clone the repository: `git clone https://github.com/Eddie-254/Capstone-Project.git`
- Navigate to the project directory: `cd 'directory name'`
- Launch Jupyter Notebook (from Anaconda): `jupyter notebook`
- Open the project notebooks: `HealthCare_cleaning& EDA.ipynb`, `HealthCare_modelling.ipynb`
- Follow the instructions in the notebook to run the project and analyze the results.

### Acknowledgments

We would like to acknowledge the contributions of the following Data Scientists:
1. [Sharon Chelangat](https://github.com/Chelangat-sharon)
2. [Kinoti Martin](https://github.com/kinoti-m-martin)
3. [Peter Onsomu](https://github.com/pkonsomu2020)
4. [Swaleh Mwadime](https://github.com/swalehmwadime)
5. [Victoria Nabea](https://github.com/VikkieN)
6. [Edwin Nderitu](https://github.com/Eddie-254)

Feel free to contribute to the [project](https://github.com/Eddie-254/Capstone-Project.git) by opening issues or submitting pull requests.
