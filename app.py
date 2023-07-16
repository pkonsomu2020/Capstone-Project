import streamlit as st
import pandas as pd
import pickle
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
import warnings
import base64
warnings.filterwarnings("ignore")
st.set_option('deprecation.showPyplotGlobalUse', False)


def main():
    # st.title('Healthcare Provider Fraud Detector')
    html_temp="""
    <div style="background-color:teal;padding:10px">
    <h2 style="color:white;text-align:center;">FraudGuard </h2>
   """ 
    # Render the HTML content
    st.markdown(html_temp, unsafe_allow_html=True)
    st.markdown("""
    Welcome to our Healthcare Insurance Fraud Detection App! This interactive web application utilizes the power of machine learning to detect fraudulent claims in your insurance data.
    """)

    st.header("How to Use the App")

    st.markdown("""
    1. **Upload CSV File:** To get started, upload your claims batch file in CSV format by clicking the "Browse Files" button. The app will automatically process the data and perform fraud detection analysis.

    2. **Flagged Claims Table:** Once the data is processed, the "Flagged Claims" table will display the detected fraudulent claims along with relevant information. You can explore the details of each flagged claim, such as policy numbers, claim amounts, and timestamps.

    3. **Download for Investigation:** If you need further investigation, you can download the "Flagged Claims" table in CSV format by clicking the "Download" button. This will allow you to conduct a more in-depth analysis offline.
    """)

    
    # Upload CSV file
    uploaded_file = st.file_uploader("Upload CSV file", type="csv")
    
    if uploaded_file is not None:
        # Read the uploaded file as a DataFrame
        df = pd.read_csv(uploaded_file)
        
        # Perform preprocessing on the data
        processed_data = preprocess_data(df)
        
        # Load the trained model
        with open('xgboost_model_reduced_features.pkl', 'rb') as file:
            model = pickle.load(file)
        
        # Make predictions
        predictions = model.predict(processed_data)
        
        # Count fraudulent activities
        fraud_count = sum(predictions)
        
        # Calculate percentages
        total_samples = len(predictions)
        fraud_percentage = (fraud_count / total_samples) * 100
        
        # Display the predicted output
        #st.write("Predicted Output:")
        #st.write(predictions)
        
        # Display the fraudulent activity count and percentage
        st.header("File Results:")
        st.markdown("<span style='font-size: 24px;'><b>Count:</b></span> <span style='font-size: 24px;'>{}</span>".format(fraud_count), unsafe_allow_html=True)
        st.markdown("<span style='font-size: 24px;'><b>Percentage:</b></span> <span style='font-size: 24px;'>{:.2f}%</span>".format(fraud_percentage), unsafe_allow_html=True)

        
        # Get the rows with fraudulent activities
        fraud_rows = df.loc[predictions == 1, :]
        fraud_rows["PotentialFraud"] = 1

        # Display the fraudulent rows
        if not fraud_rows.empty:
            st.header("Flagged Claims:")
            st.dataframe(fraud_rows)

            # Add a button to download the flagged claims DataFrame as a CSV file
            if st.button("Download Flagged Claims"):
                # Create a link to download the DataFrame as a CSV file
                tmp_download_link = download_link(fraud_rows, "flagged_claims.csv", "Click here to download the flagged claims!")
                st.markdown(tmp_download_link, unsafe_allow_html=True)
        else:
            st.write("No fraudulent activities detected.")

        # Plot a bar chart of fraudulent activities
        plot_fraud_chart(predictions)

        # Check if any fraudulent activities are detected
        if fraud_count > 0:
            # Display the "Predict" button
            if st.button("Predict"):
                # Perform any additional actions you want to take on button click
                pass

def preprocess_data(df):
    # Perform preprocessing steps on the DataFrame
    # Ensure that the preprocessing steps match those used during training
    
    # Identify categorical columns
    categorical_cols = df.select_dtypes(include="object").columns
    
    # Encode categorical columns
    for col in categorical_cols:
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col])
    
    # Apply feature scaling if required
    
    return df


def plot_fraud_chart(predictions):
    st.subheader("Fraudulent Claims Percentage (Pie Chart)")

    st.markdown("""
    The pie chart visually represents the percentage of fraudulent claims detected in the uploaded data. It provides an overview of the overall extent of potential fraudulent activities within the claims batch.
    """)

    # Create a DataFrame for plotting
    df = pd.DataFrame(predictions, columns=["Fraudulent"])
    
    # Count the occurrences of 'Not Fraudulent' and 'Fraudulent'
    counts = df["Fraudulent"].value_counts()
    
    # Convert the counts into a percentage
    percentages = counts / counts.sum() * 100
    
    # Labels for the pie chart
    labels = ["Not Fraudulent", "Fraudulent"]
    
    # Plot a pie chart
    plt.figure(figsize=(8, 6))
    plt.pie(percentages, labels=labels, autopct='%1.1f%%')
    plt.title("Fraudulent Activities")
    st.pyplot()

    st.markdown("""
        ### Disclaimer

        Please note that the accuracy of fraud detection may vary depending on the quality and quantity of data provided. Our machine learning model aims to identify potential fraudulent claims, but it is essential to conduct thorough investigations to confirm fraud cases.

        For any questions or assistance, please feel free to contact our support team. We hope this app helps you in safeguarding against healthcare insurance fraud.
        """)
def download_link(df, file_name, link_text):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="{file_name}">{link_text}</a>'
    return href
    
if __name__ == "__main__":
    main()
