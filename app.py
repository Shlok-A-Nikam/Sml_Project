import streamlit as st
from src.pipeline.trainer_pipeline import TrainerPipeline
from src.pipeline.predict_pipeline import PredictPipeline


def main():
    st.title("Student Performance Prediction")
    
    page = st.sidebar.selectbox("Choose Page", ["Train Model", "Make Prediction"])
    
    if page == "Train Model":
        train_page()
    else:
        predict_page()

def train_page():
    st.subheader("Train Machine Learning Model")
    st.write("This will run data ingestion and train the model on student performance data.")
    
    if st.button("Run Data Ingestion and Model Training"):
        with st.spinner("Running data ingestion and model training..."):
            trainer_pipeline = TrainerPipeline()
            trainer_pipeline.initiate_trainer_pipeline()
        st.success("Data ingestion and model training completed successfully!")

def predict_page():
    st.subheader("Predict Student Performance")
    st.write("Enter the student information to predict total performance.")

    col1, col2 = st.columns(2)
    
    with col1:
        gender = st.selectbox("Gender", ["male", "female"])
        ethnicity = st.selectbox("Race/Ethnicity", ["group A", "group B", "group C", "group D", "group E"])
        parent_education = st.selectbox("Parental Level of Education", 
                                       ["high school", "some college", "associate's degree", 
                                        "bachelor's degree", "master's degree", "some high school"])
        lunch = st.selectbox("Lunch Type", ["standard", "free/reduced"])
    
    with col2:
        test_prep = st.selectbox("Test Preparation Course", ["none", "completed"])
        math_score = st.number_input("Math Score", min_value=0, max_value=100, value=50)
        reading_score = st.number_input("Reading Score", min_value=0, max_value=100, value=50)
        writing_score = st.number_input("Writing Score", min_value=0, max_value=100, value=50)

    if st.button("Predict Total Score"):
        try:
            features = {
                'gender': gender,
                'race/ethnicity': ethnicity,
                'parental level of education': parent_education,
                'lunch': lunch,
                'test preparation course': test_prep,
                'math score': math_score,
                'reading score': reading_score,
                'writing score': writing_score
            }
            predict_pipeline = PredictPipeline()
            prediction = predict_pipeline.predict(features)
            st.success(f"Predicted Total Score: {prediction[0]:.2f}")
        except Exception as e:
            st.error(f"Error in prediction: {str(e)}")

if __name__ == "__main__":
    main()