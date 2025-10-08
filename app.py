import streamlit as st
import pandas as pd
from lead_scoring import process_leads

st.title("LeadGen+ | Smart Lead Enrichment Tool")
st.write("Upload your CSV of leads (columns: company_name, email, website, company_size, industry)")

# Upload CSV
uploaded_file = st.file_uploader("Choose CSV", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("Original Leads Data:")
    st.dataframe(df)
    
    # Process leads
    st.write("Processing leads...")
    processed_df = process_leads(df)
    
    st.write("Processed Leads (Sorted by Score):")
    st.dataframe(processed_df)
    
    # Download CSV
    csv = processed_df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="Download Processed Leads CSV",
        data=csv,
        file_name='processed_leads.csv',
        mime='text/csv'
    )
