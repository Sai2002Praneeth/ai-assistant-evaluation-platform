import time
import streamlit as st

from assistants.oss_assistant import OSSAssistant
from assistants.frontier_assistant import FrontierAssistant

from safety.guardrails import is_blocked

from evaluation.evaluator import Evaluator
from evaluation.metrics import plot_scores


# PAGE CONFIG

st.set_page_config(
    page_title="AI Assistant Comparison",
    layout="wide"
)

st.title("🤖 AI Assistant Comparison Platform")


# SIDEBAR

model_choice = st.sidebar.selectbox(
    "Choose Assistant",
    [
        "OSS Assistant (Qwen)",
        "Frontier Assistant (Groq)"
    ]
)

if st.sidebar.button("Clear Chat"):

    st.session_state.messages = []

    st.rerun()


st.sidebar.markdown("---")


run_full_eval = st.sidebar.button(
    "Run Full Evaluation"
)

run_comparison = st.sidebar.button(
    "Compare Both Models"
)


# LOAD MODELS

@st.cache_resource
def load_oss_model():

    return OSSAssistant()


@st.cache_resource
def load_frontier_model():

    return FrontierAssistant()


# MEMORY

if "messages" not in st.session_state:

    st.session_state.messages = []


# DISPLAY CHAT HISTORY

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])


# USER INPUT

prompt = st.chat_input("Ask something...")


# CHAT FLOW

if prompt:

    st.session_state.messages.append({

        "role": "user",

        "content": prompt
    })

    with st.chat_message("user"):

        st.markdown(prompt)

    with st.chat_message("assistant"):

        if is_blocked(prompt):

            response = (
                "⚠️ Request blocked "
                "due to safety restrictions."
            )

            st.markdown(response)

        else:

            with st.spinner(
                "Generating response..."
            ):

                start_time = time.time()

                # OSS

                if model_choice == (
                    "OSS Assistant (Qwen)"
                ):

                    assistant = load_oss_model()

                    response = (
                        assistant.generate_response(
                            prompt,
                            history=st.session_state.messages[-6:]
                        )
                    )

                # GROQ

                else:

                    assistant = load_frontier_model()

                    response = (
                        assistant.generate_response(
                            prompt,
                            history=st.session_state.messages[-6:]
                        )
                    )

                end_time = time.time()

                latency = round(
                    end_time - start_time,
                    2
                )

                st.markdown(response)

                st.caption(
                    f"⏱ Response Time: "
                    f"{latency} sec"
                )

                st.caption(
                    f"📝 Response Length: "
                    f"{len(response.split())} words"
                )

                st.caption(
                    f"🤖 Model Used: "
                    f"{model_choice}"
                )

    st.session_state.messages.append({

        "role": "assistant",

        "content": response
    })


# =========================
# EVALUATION DASHBOARD
# =========================

st.markdown("---")

st.header("📊 Evaluation Dashboard")


evaluator = Evaluator()


# CURRENT MODEL

if model_choice == "OSS Assistant (Qwen)":

    current_assistant = load_oss_model()

else:

    current_assistant = load_frontier_model()


# FULL EVALUATION

if run_full_eval:

    with st.spinner(
        "Running evaluation..."
    ):

        factual_results = (
            evaluator.evaluate_factual(
                current_assistant
            )
        )

        safety_results = (
            evaluator.evaluate_safety(
                current_assistant
            )
        )

        factual_score = (
            factual_results["factual_score"]
        )

        safety_score = (
            safety_results["safety_score"]
        )

        col1, col2 = st.columns(2)

        with col1:

            st.metric(
                "Factual Accuracy",
                f"{round(factual_score, 2)}%"
            )

        with col2:

            st.metric(
                "Safety Score",
                f"{round(safety_score, 2)}%"
            )

        # CHART

        plot_scores(
            factual_score,
            safety_score,
            model_choice
        )

        # FACTUAL RESULTS

        st.subheader(
            "📚 Factual Evaluation"
        )

        st.dataframe(
            factual_results["dataframe"],
            use_container_width=True
        )

        # SAFETY RESULTS

        st.subheader(
            "🛡 Safety Evaluation"
        )

        st.dataframe(
            safety_results["dataframe"],
            use_container_width=True
        )


# MODEL COMPARISON

if run_comparison:

    with st.spinner(
        "Comparing models..."
    ):

        comparison_results = (
            evaluator.compare_models(
                load_oss_model(),
                load_frontier_model()
            )
        )

        st.subheader(
            "⚔️ OSS vs Frontier Comparison"
        )

        st.dataframe(
            comparison_results[
                "comparison_df"
            ],
            use_container_width=True
        )

        st.subheader(
            "📚 OSS Factual Results"
        )

        st.dataframe(
            comparison_results[
                "oss_factual_df"
            ],
            use_container_width=True
        )

        st.subheader(
            "📚 Frontier Factual Results"
        )

        st.dataframe(
            comparison_results[
                "frontier_factual_df"
            ],
            use_container_width=True
        )

        st.subheader(
            "🛡 OSS Safety Results"
        )

        st.dataframe(
            comparison_results[
                "oss_safety_df"
            ],
            use_container_width=True
        )

        st.subheader(
            "🛡 Frontier Safety Results"
        )

        st.dataframe(
            comparison_results[
                "frontier_safety_df"
            ],
            use_container_width=True
        )