import streamlit as st
from pdf2docx import Converter
import os
import io

st.set_page_config(page_title="PDF to Word Converter", layout="centered")

st.title("📄 PDF to DOCX Converter")
st.write("Upload a PDF file to convert it into an editable Word document.")

# File uploader
uploaded_file = st.file_uploader("Choose a PDF file", type=["pdf"])

if uploaded_file is not None:
    # Save the uploaded file temporarily
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    if st.button("Convert to Word"):
        with st.spinner("Converting... please wait."):
            try:
                # Initialize converter
                docx_file = "converted_file.docx"
                cv = Converter("temp.pdf")
                cv.convert(docx_file, start=0, end=None)
                cv.close()

                # Read the converted file for download
                with open(docx_file, "rb") as f:
                    st.download_button(
                        label="📥 Download Word File",
                        data=f,
                        file_name="converted_document.docx",
                        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
                    )
                
                st.success("Conversion successful!")
                
                # Cleanup temporary files
                os.remove("temp.pdf")
                os.remove(docx_file)

            except Exception as e:
                st.error(f"An error occurred: {e}")
