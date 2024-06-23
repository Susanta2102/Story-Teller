# Generate Stories from Images with Streamlit and Gemini-Pro

This Streamlit web app lets you unleash your creativity by generating stories based on uploaded images using Google's GenerativeAI service (Gemini-Pro).

### Run on Streamlit
[Image to Story generator]((https://story-teller-ix.streamlit.app/))

## 1. Features:

- **Image Upload:** Upload an image to spark your story.
- **AI-powered Story Generation:** Gemini-Pro analyzes the image and generates a unique short story inspired by the visual content.
- **Creative Exploration:** Explore different story possibilities from a single image.

## 2. Requirements:

- Python 3.x
- Streamlit (`pip install streamlit`)
- `dotenv` library (`pip install python-dotenv`)
- Pillow library (`pip install Pillow`)
- Google Cloud Project with GenerativeAI API enabled ([https://cloud.google.com/ai/generative-ai](https://cloud.google.com/ai/generative-ai))

## 3. Setup:  

1. Create a virtual environment (recommended): `python -m venv venv`
2. Activate the environment: `source venv/bin/activate` (Windows: `venv\Scripts\activate`)
3. Install dependencies: Refer to the requirements section and install the necessary libraries.
4. Create a `.env` file in the project directory:
   - Add `GOOGLE_API_KEY=<YOUR_API_KEY>` (replace with your GenerativeAI API key)

## 4. Running the App:

1. Open a terminal in the project directory.
2. Run the app: `streamlit run app.py`
3. Access the app in your web browser at http://localhost:8501.
   
## 5. Usage:  

1. Click "Choose an image..." and upload a picture that ignites your imagination.
2. Click the "Generate a Story" button.
3. The app will analyze the image and generate a creative short story based on its interpretation.

## 6. Disclaimer:

- This is a basic example using a free-tier API. The stories may vary in detail and coherence. 
- Consider the limitations of image analysis and the quality of uploaded images for best results.
