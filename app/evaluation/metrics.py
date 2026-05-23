import matplotlib.pyplot as plt
import streamlit as st


def plot_scores(
    factual_score,
    safety_score,
    model_name
):

    categories = [
        "Factual Accuracy",
        "Safety"
    ]

    scores = [
        factual_score,
        safety_score
    ]

    fig, ax = plt.subplots(figsize=(6, 4))

    ax.bar(categories, scores)

    ax.set_ylim(0, 100)

    ax.set_ylabel("Score (%)")

    ax.set_title(
        f"{model_name} Evaluation Scores"
    )

    st.pyplot(fig)