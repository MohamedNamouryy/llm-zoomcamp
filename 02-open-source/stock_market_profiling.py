import streamlit as st
import requests
from transformers import pipeline

# Set up Finnhub API key (unchanged)
finnhub_api_key = "add your key"

# Step 1: Load the Hugging Face text-generation model (e.g., GPT-2)
def load_model():
    generator = pipeline('text-generation', model='gpt2')  # You can change the model to something else like GPT-Neo
    return generator

# Step 2: Fetch live data from Finnhub API (unchanged)
def fetch_financial_data(symbol):
    url = f"https://finnhub.io/api/v1/stock/profile2?symbol={symbol}&token={finnhub_api_key}"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Step 3: Generate a financial summary using Hugging Face model
def generate_financial_summary(query, model):
    # Generate the text based on the query
    response = model(query, max_length=300, num_return_sequences=1)
    
    # Extract the generated text
    return response[0]['generated_text']

# Step 4: Use Streamlit for the Web App Interface
def main():
    st.title("Financial Advisor RAG System with Hugging Face")
    st.write("Ask any financial question and receive a summary based on live data.")

    # Load the model
    model = load_model()

    # User inputs
    user_query = st.text_input("Enter your financial query:")
    stock_symbol = st.text_input("Enter the stock symbol (e.g., AAPL for Apple):")

    if st.button("Get Financial Summary"):
        if user_query:
            # Generate summary based on user query and display it
            summary = generate_financial_summary(user_query, model)
            st.write("### Summary based on your query:")
            st.write(summary)
        else:
            st.write("Please enter a query.")

if __name__ == "__main__":
    main()
