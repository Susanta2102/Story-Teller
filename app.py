import streamlit as st
import os
from dotenv import load_dotenv
from PIL import Image
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def input_image_setup(uploaded_file):
    """Processes the uploaded image file."""
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        image_part = {
            "mime_type": uploaded_file.type,
            "data": bytes_data
        }
        return [image_part]
    else:
        st.error("Please upload an image.")

def generate_story(input_prompt, image):
    """Generates a story using the Gemini Pro model."""
    model = genai.GenerativeModel("gemini-1.5-pro-latest")  # Latest Gemini Pro model
    response = model.generate_content([input_prompt, image[0]])
    return response.text

# Streamlit App
st.set_page_config(page_title="Story Generator")
st.title("Image to Story Generator")
st.write("Upload an image to create a story.")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)

input_prompt = """
You are a master storyteller. Carefully examine the image and weave a captivating and imaginative short story inspired by it. 
Delve into the details, emotions, and possible narratives hidden within the image. 
Be creative and explore unique perspectives to craft a truly engaging story.
"""

if st.button("Generate a Story"):
    if uploaded_file:
        image_data = input_image_setup(uploaded_file)
        with st.spinner("Crafting your story..."):  # Show a progress spinner
            story = generate_story(input_prompt, image_data)
        st.subheader("Your Short Story:")
        st.write(story)
    else:
        st.error("Please upload an image to generate a story.")
