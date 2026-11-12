
import streamlit as st
import requests

st.set_page_config(
    page_title="Financial RAG Assistant",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Financial RAG Assistant")
st.write(
    "Ask questions about the Happiest Minds Technologies "
    "FY 2024-25 annual report."
)

API_URL = "http://127.0.0.1:8000"

question = st.text_input(
    "Enter your financial question",
    placeholder="What was the consolidated revenue in FY 2024-25?"
)

if st.button("Ask Question", type="primary"):

    if not question.strip():
        st.warning("Please enter a question.")

    else:
        try:
            with st.spinner("Analyzing the annual report..."):

                response = requests.post(
                    f"{API_URL}/ask",
                    json={"question": question},
                    timeout=120
                )

                response.raise_for_status()
                result = response.json()

            st.subheader("Answer")
            st.write(result["answer"])

            st.subheader("Source References")

            for source in result.get("sources", []):

                with st.expander(
                    f"PDF Page {source['pdf_page']} "
                    f"| Score: {source['similarity_score']}"
                ):
                    st.write(source["excerpt"])

        except requests.exceptions.ConnectionError:
            st.error(
                "Cannot connect to the API. "
                "Please start your FastAPI server first."
            )

        except requests.exceptions.RequestException as error:
            st.error(f"API error: {error}")

        except Exception as error:
            st.error(f"Something went wrong: {error}")
