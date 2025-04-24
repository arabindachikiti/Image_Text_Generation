import streamlit as st
import google.generativeai as genai
from PIL import Image

# Configure your API key
genai.configure(api_key="AIzaSyAwXQIVa_3KlCjC8w41Ic3LhEm94_pHKrs")

# Load Gemini Vision model
model = genai.GenerativeModel("gemini-2.5-flash-preview-04-17")

st.title("🖼️ Image Describer App")
st.write("Upload an image and I'll describe it!")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_container_width=True)

    if st.button("Generate Description"):
        with st.spinner("Analyzing image..."):
            response = model.generate_content(["Describe this image.", image])
            st.success("Done!")
            st.subheader("📝 Description:")
            st.write(response.text)