import streamlit as st
import joblib


# Load the pre-trained model
model = joblib.load('phishing_model.pkl')

def predict_phishing(url_features):
    prediction = model.predict([url_features])
    return prediction[0]

# Set up the Streamlit interface
st.title('Phishing Website Detection')
st.write('This tool predicts whether a website might be phishing or not.')

# Input features
# For simplicity, we assume numerical input corresponding to features. Adjust according to your actual feature set.
feature_input = st.text_input("Enter URL features separated by commas:", "0,1,0,-1,1,...")

if st.button('Predict'):
    url_features = list(map(int, feature_input.split(',')))
    result = predict_phishing(url_features)
    if result == 1:
        st.warning('This website is likely a phishing site.')
    else:
        st.success('This website is likely secure.')

# Run the Streamlit app by entering `streamlit run app.py` in your terminal.
