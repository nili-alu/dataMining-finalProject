import streamlit as st


def about_page():
    st.title("About Heart Disease Prediction Application")
    st.write("""
    This web application predicts the likelihood of heart disease based on various input features such as age, gender, chest pain type, etc.
    
    The prediction model used in this application is trained on a dataset and saved using pickle. The model predicts the probability of having heart disease, and the application displays the result accordingly.
    
    This application is for education purposes only and should not be used as a substitute for professional medical advice. If you have concerns about your heart health, please consult a healthcare professional.
    """)

    st.title(
        "Data Dictionary")

    st.markdown("""
### Input Features:
- **age**: age in years
- **sex**: sex
    - 1 = male
    - 0 = female
- **cp**: chest pain type
    - Value 0: typical angina
    - Value 1: atypical angina
    - Value 2: non-anginal pain
    - Value 3: asymptomatic
- **trestbps**: resting blood pressure (in mm Hg on admission to the hospital)
- **chol**: serum cholestoral in mg/dl
- **fbs**: (fasting blood sugar > 120 mg/dl)
    - 1 = true;
    - 0 = false
- **restecg**: resting electrocardiographic results
    - Value 0: normal
    - Value 1: having ST-T wave abnormality (T wave inversions and/or ST elevation or depression of > 0.05 mV)
    - Value 2: showing probable or definite left ventricular hypertrophy by Estes' criteria
- **thalach**: maximum heart rate achieved
- **exang**: exercise induced angina
    - 1 = yes
    - 0 = no
- **oldpeak**: ST depression induced by exercise relative to rest
- **slope**: the slope of the peak exercise ST segment
    - Value 0: upsloping
    - Value 1: flat
    - Value 2: downsloping
- **ca**: number of major vessels (0-3) colored by flourosopy
- **thal**:
    - 0 = error (in the original dataset 0 maps to NaN's)
    - 1 = fixed defect
    - 2 = normal
    - 3 = reversable defect

### Target (the label):
- 0 = person may not have heart disease
- 1 = person may have heart disease
""")
