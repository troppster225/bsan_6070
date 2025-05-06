# BSAN 6070 Final Project
### By: Brandon Acosta, Yardon Sasson, and Tommy Ropp

This project uses data from the 2021 American Community Survey to predict whether an individual is likely to graduate from college, based on a wide range of demographic, socioeconomic, and language-related features. Our goal is to assist scholarship providers, policymakers, and educational organizations in identifying communities that may benefit from targeted support.

Among all models, the Random Forest classifier achieved the most balanced performance across F1 score, accuracy, and AUC, and was selected for deployment. The most influential features across models included English-speaking ability and racial background, particularly for Asian Pacific Islander and biracial individuals. The final application provides insights to help promote more equitable access to higher education.

## General Requirements
* Python 3.11.5
* Jupyter
* pandas
* numpy
* scikit-learn
* matplotlib
* seaborn
* joblib
* access to the 2021 acs census dataset (we are unable to upload the file due to size restrictions)

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone git@github.com:troppster225/bsan_6070.git
2. Go to the final_project folder
3. Run the final_project.ipynb file to see our model development process
4. cd into the directory in your terminal
5. Type the following:
   ```bash
   streamlit run app.py
6. Check out the deployed link: https://gradpredictor.streamlit.app/



## License
This project is for educational purposes only. All code and materials in this repository are provided as-is, with no warranty.
