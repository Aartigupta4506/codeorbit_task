import streamlit as st
import numpy as np
from PIL import Image

from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.applications.mobilenet_v2 import (
    preprocess_input,
    decode_predictions
)


# Page configuration
st.set_page_config(
    page_title="AI Image Classifier",
    page_icon="🖼️",
    layout="centered"
)


# Title
st.title("🖼️ AI Image Classification")

st.write(
    "Upload an image and let the pretrained AI model "
    "predict the object in the image."
)


# Load pretrained model
@st.cache_resource
def load_model():
    return MobileNetV2(weights="imagenet")


model = load_model()


# Upload image
uploaded_file = st.file_uploader(
    "📤 Upload an image",
    type=["jpg", "jpeg", "png"]
)


# Classification
if uploaded_file is not None:

    image = Image.open(uploaded_file).convert("RGB")

    st.subheader("📷 Uploaded Image")

    st.image(
        image,
        caption="Uploaded Image",
        use_container_width=True
    )

    # Resize image
    image_resized = image.resize((224, 224))

    # Convert image to NumPy array
    image_array = np.array(image_resized)

    # Add batch dimension
    image_array = np.expand_dims(
        image_array,
        axis=0
    )

    # Preprocess image
    image_array = preprocess_input(image_array)

    # Make prediction
    predictions = model.predict(
        image_array,
        verbose=0
    )

    # Get top 3 predictions
    results = decode_predictions(
        predictions,
        top=3
    )[0]


    # Display predictions
    st.subheader("🤖 Prediction Results")

    for rank, (_, label, confidence) in enumerate(
        results,
        start=1
    ):

        display_label = label.replace(
            "_",
            " "
        ).title()

        st.write(
            f"**{rank}. {display_label}**"
        )

        st.progress(
            float(confidence)
        )

        st.caption(
            f"Confidence: {confidence * 100:.2f}%"
        )


    # Main prediction
    main_label = results[0][1].replace(
        "_",
        " "
    ).title()

    st.success(
        f"🎯 Predicted Label: **{main_label}**"
    )


# Explanation
st.divider()

st.subheader("🧠 How the Pretrained Model Works")

st.write(
    """
    MobileNetV2 is a pretrained image classification model.

    It has already learned to recognize many different
    objects from the ImageNet dataset.

    When we upload an image, the image is resized and
    converted into numbers that the model can understand.

    The model analyzes visual features such as edges,
    shapes and textures.

    It then gives probabilities for different object
    categories. The category with the highest probability
    becomes the main predicted label.
    """
)


# Footer
st.divider()

st.caption(
    "CodeOrbit Tech AI Internship • Task 3 • "
    "Pretrained Image Classification"
)