import streamlit as st
import os
from rag_pipeline import run_rag

st.set_page_config(page_title="Mini RAG Assistant", page_icon="🔍", layout="wide")

# --------------------------
# Load documents
# --------------------------
def load_documents():
    docs = []
    data_dir = "data"

    if not os.path.exists(data_dir):
        st.error("❌ The data/ folder is missing. Upload .txt files inside a data folder.")
        return docs

    files = [f for f in os.listdir(data_dir) if f.endswith(".txt")]

    if not files:
        st.error("❌ No .txt documents found inside data/. Please upload extracted text files.")
        return docs

    for file in files:
        with open(os.path.join(data_dir, file), "r", encoding="utf-8") as f:
            docs.append(f.read())

    return docs

documents = load_documents()

# --------------------------
# Premium UI
# --------------------------
st.markdown(
    """
    <h1 style="text-align:center; font-size:42px;">🔍 Mini RAG – Construction QA Assistant</h1>
    <p style="text-align:center; font-size:18px; color:#5f6368;">
        Ask any question based on the internal construction policy documents.
    </p>
    <br>
    """,
    unsafe_allow_html=True
)

query = st.text_input("💬 Enter your question below:", placeholder="e.g., What factors affect construction delays?")

if st.button("Ask", use_container_width=True):
    if not query.strip():
        st.warning("⚠️ Please enter a question.")
    elif not documents:
        st.error("❌ Documents not loaded. Fix data folder first.")
    else:
        with st.spinner("🔎 Retrieving context..."):
            retrieved, answer = run_rag(query, documents)

        st.subheader("📌 Retrieved Context (Top Matches)")
        for i, chunk in enumerate(retrieved, 1):
            with st.expander(f"📄 Chunk {i}"):
                st.write(chunk)

        st.markdown("<br>", unsafe_allow_html=True)

        st.subheader("💡 Final Answer")
        st.markdown(
            f"""
            <div style="padding: 15px; background-color:#f8f9fa;
                        border-radius:10px; border-left: 5px solid #4CAF50;">
                {answer}
            </div>
            """,
            unsafe_allow_html=True,
        )
