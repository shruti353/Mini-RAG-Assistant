# 🏗️ Mini RAG – Retrieval Augmented Generation Pipeline  
### _with Hybrid Search • Citations • Highlighting • PDF Support • Streamlit UI_

A production-grade **Retrieval-Augmented Generation (RAG)** system designed for a **construction marketplace AI assistant**.  
The assistant answers questions **strictly from internal documents** using:

-  Hybrid Retrieval (BM25 + Embeddings)  
-  Document Chunking  
-  LLM Grounded Answer Generation  
-  Sentence Highlighting  
-  Citations  
-  JSON Report Export  
-  PDF/TXT Upload Support  
-  Dark Theme UI  
-  Chat History  

---

#  Features

##  1. Document Chunking  
- Upload **PDF** or **TXT** files  
- Automatic PDF → text conversion  
- Splits documents into overlapping chunks  
- Stored for retrieval + display  

---

##  2. Hybrid Retrieval  
Choose retrieval mode:

| Mode | Description |
|------|-------------|
| **Hybrid (BM25 + Embeddings)** | Best relevance, combines keyword + semantic search |
| **Embeddings Only** | Pure semantic similarity using MiniLM |
| **BM25 Only** | Fast keyword-based retrieval |

---

##  3. LLM Answer Generation  
Uses **OpenRouter** to query high-quality open-source models:

- Mistral-7B-Instruct  
- LLaMA-3-8B  
- Qwen-2.5-7B  
- DeepSeek-R1-Distill  

All answers are:

- grounded to retrieved text  
- citation-enforced  
- formatting-clean  

---

##  4. Premium UI Features  
- Sentence highlighting  
- Collapsible chunk boxes  
- Dark mode  
- Chat history persistence  
- JSON report export  

---

# 🏛️ Architecture

```
User Query
      ↓
Chunked Documents  ← PDF/TXT Upload
      ↓
Hybrid Retrieval (BM25 + Embeddings)
      ↓
Top Relevant Chunks (Highlighted)
      ↓
LLM (via OpenRouter) — Grounded Answer Generation
      ↓
Answer + Citations + JSON Export
```

---

#  Project Structure

```
Mini-RAG-Pipeline/
│
├── app.py                     # Streamlit UI (premium version)
├── rag_pipeline.py            # Core RAG logic: BM25, embeddings, hybrid search
├── requirements.txt           # Dependencies
├── README.md                  # Documentation
│
├── /data                      # PDF/TXT documents
│
├── /outputs                   # JSON exported responses
│
└── /notebooks
     └── evaluation.ipynb      # Optional evaluation notebook
```

---

#  Installation

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/Mini-RAG-Pipeline.git
cd Mini-RAG-Pipeline
```

### 2. Create & activate virtual environment  
**Windows**
```bash
python -m venv venv
venv\Scripts\activate
```

**Mac/Linux**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install requirements
```bash
pip install -r requirements.txt
```

### 4. Set OpenRouter API key  
**PowerShell**
```bash
setx OPENROUTER_API_KEY "your_key_here"
```

**Mac/Linux**
```bash
export OPENROUTER_API_KEY="your_key_here"
```

---

#  Running the RAG Application

```bash
streamlit run app.py
```

Then open:

👉 http://localhost:8501/

---

#  How the System Works

### 1. Upload Documents  
- PDF → automatic extraction  
- TXT → loaded directly  
- Chunked into ~250 token windows  

### 2. Retrieve Top Chunks  
Depending on retrieval mode:
- BM25  
- Embeddings  
- Hybrid (BM25 + Embeddings)

### 3. LLM Generates Grounded Answer  
LLM is instructed to:
- Use **only** retrieved chunks  
- Add citations  
- Avoid hallucinations  

### 4. Answer Display  
- Highlighted matching sentences  
- Collapsible chunk boxes  
- JSON export available  

---

#  Example Query

**“What factors affect construction project delays?”**

**System Output Includes:**
- Retrieved chunk text  
- Highlighted matching parts  
- Final answer (clean + with citations)  

---

#  Evaluation (Optional)

`notebooks/evaluation.ipynb` includes:

- Recall@k  
- Relevance scoring  
- Hallucination detection  
- Model comparison  
- Chunk-level error analysis  

---

#  Tech Stack

| Component | Tool |
|-----------|------|
| Embeddings | Sentence-Transformers (MiniLM-L6-v2) |
| Vector Search | FAISS |
| Keyword Search | BM25 (rank_bm25) |
| LLM Inference | OpenRouter API |
| Frontend | Streamlit |
| Backend | Python |

---

# 📦 Exporting Reports

You can download:

- Retrieved chunks  
- Final answer  
- Model used  
- Retrieval mode  
- Timestamp  

as a `.json` file.

---

# 🧑‍💻 Developer: **Shruti Thakkar**  
AI/ML Engineer — RAG • NLP • LLMs  

---

#  Conclusion

This Mini-RAG demonstrates:

- Complete retrieval pipeline  
- Hybrid search  
- Transparent grounding  
- Production-level UI  
- Modern features (highlighting, citations, JSON export)  
- Clean engineering design

Perfect for interviews, portfolio, and real-world use.

