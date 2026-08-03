import streamlit as st
import joblib
from pathlib import Path


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="EmotionAI | NLP Emotion Classifier",
    page_icon="🧠",
    layout="centered"
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown("""
<style>

.main {
    padding-top: 2rem;
}

.title {
    text-align: center;
    font-size: 42px;
    font-weight: 700;
    margin-bottom: 5px;
}

.subtitle {
    text-align: center;
    font-size: 17px;
    color: #888;
    margin-bottom: 30px;
}

.info-card {
    padding: 18px;
    border-radius: 12px;
    border: 1px solid rgba(128,128,128,0.2);
    margin-top: 25px;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# LOAD MODEL ARTIFACTS
# ============================================================

BASE_DIR = Path(__file__).resolve().parent

MODEL_PATH = BASE_DIR / "models" / "emotion_classifier.pkl"
ENCODER_PATH = BASE_DIR / "models" / "label_encoder.pkl"


@st.cache_resource
def load_artifacts():

    model = joblib.load(MODEL_PATH)
    label_encoder = joblib.load(ENCODER_PATH)

    return model, label_encoder


model, label_encoder = load_artifacts()


# ============================================================
# HEADER
# ============================================================

st.markdown(
    '<div class="title">🧠 EmotionAI</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Classical NLP • TF-IDF • Linear SVM'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# INTRODUCTION
# ============================================================

st.write(
    "Enter a sentence below and the trained NLP model will "
    "predict the emotion expressed in the text."
)


# ============================================================
# TEXT INPUT
# ============================================================

user_text = st.text_area(
    "Enter your text",
    placeholder="Example: I am extremely happy today!",
    height=150
)


# ============================================================
# ANALYZE BUTTON
# ============================================================

if st.button(
    "🔍 Analyze Emotion",
    use_container_width=True
):

    if not user_text.strip():

        st.warning(
            "Please enter some text before analyzing."
        )

    else:

        # ----------------------------------------------------
        # MODEL PREDICTION
        # ----------------------------------------------------

        prediction = model.predict([user_text])[0]


        # ----------------------------------------------------
        # CONVERT NUMERIC CLASS → ACTUAL EMOTION
        # ----------------------------------------------------

        emotion = label_encoder.inverse_transform(
            [prediction]
        )[0]


        # ----------------------------------------------------
        # DISPLAY RESULT
        # ----------------------------------------------------

        st.markdown("---")

        st.subheader("🎯 Predicted Emotion")

        st.markdown(
            f"# {emotion.title()}"
        )

        st.caption(
            f"Model predicted class: {prediction}"
        )


        # ----------------------------------------------------
        # TECHNICAL DETAILS
        # ----------------------------------------------------

        with st.expander("🔬 View prediction details"):

            st.write(
                f"**Predicted class:** `{prediction}`"
            )

            st.write(
                f"**Emotion:** `{emotion}`"
            )


# ============================================================
# MODEL INFORMATION
# ============================================================

st.markdown("---")

st.subheader("🧠 Model Architecture")

st.write(
    "Raw Text → TF-IDF Vectorization → Linear SVM → Emotion"
)


# ============================================================
# PROJECT INFORMATION
# ============================================================

st.markdown(
    """
    <div class="info-card">

    <b>About this project</b>

    <br><br>

    This application uses a classical Natural Language Processing
    pipeline to classify the emotion expressed in user-provided text.

    <br><br>

    <b>Technologies:</b><br>
    Python • Scikit-learn • TF-IDF • Linear SVM • Streamlit

    </div>
    """,
    unsafe_allow_html=True
)