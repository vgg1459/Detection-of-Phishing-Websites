## Project Overview
A machine-learning based web application that identifies whether a given URL is Legitimate or Phishing.
The project uses a trained ML model and a simple user interface built using Streamlit/HTML templates.

## Features
  - URL-based phishing detection  
  - ML model trained using scikit-learn  
  - Lightweight and fast  
  - Simple web interface  
  - Beginner-friendly code
    
## Technologies Used
**Languages:** Python, HTML, CSS  
**Libraries & Frameworks:** Scikit-learn (ML model), Joblib (model loading), Pandas & NumPy (data handling), Streamlit (web UI), Flask (backend framework)  
**Machine Learning:** Random Forest Classifier, TF-IDF Vectorizer (for converting URLs to features)

## Instructions to run the code

1. Install following dependencies:
```bash
pip install streamlit scikit-learn joblib pandas numpy
```
2. Run the application:
```bash
streamlit run app.py
```

## Disclaimer
Due to environment differences or incomplete deployment files, some parts of the application **may not run fully**.  
The core ML model (`phishing_model.pkl`) and related logic are intact and can be demonstrated separately if needed.

## Screenshots of Working Model

![Phishing Homepage](https://github.com/user-attachments/assets/cb9b1318-b82d-4a6f-be65-9c1a6e75a1d3)
![phishing-illegitimate wbsite](https://github.com/user-attachments/assets/6a24d35f-86bb-444a-9448-0eea471a1b30)
![phishing-secure website](https://github.com/user-attachments/assets/03a758e5-10ef-4901-b00d-90b912055d41)


