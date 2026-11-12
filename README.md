# Financial RAG Assistant

An AI-powered financial document question-answering application built using Retrieval-Augmented Generation (RAG). It allows users to ask questions about the Happiest Minds Technologies FY 2024–25 annual report and receive context-grounded answers with PDF page references.

## Key Features

- PDF text extraction and preprocessing using PyPDF
- Text chunking with overlapping sections and page metadata
- Semantic embeddings using Sentence Transformers
- Vector similarity search using FAISS
- LLM-powered answer generation using Groq GPT-OSS 20B
- RAG pipeline orchestration using LangChain
- Source references with PDF page numbers
- REST API development using FastAPI
- Interactive web interface using Streamlit

## System Architecture

User Question  
↓  
Streamlit Frontend  
↓  
FastAPI Backend  
↓  
Sentence Transformer Embeddings  
↓  
FAISS Vector Search  
↓  
Relevant Document Chunks  
↓  
LangChain + Groq LLM  
↓  
Answer with Source References

## Technology Stack

- **Programming:** Python
- **Document Processing:** PyPDF
- **Embeddings:** Sentence Transformers
- **Vector Search:** FAISS
- **LLM:** Groq GPT-OSS 20B
- **Framework:** LangChain
- **Backend:** FastAPI
- **Frontend:** Streamlit

## Project Structure

```text
financial-rag-assistant/
├── data/
├── vectorstore/
├── extract.py
├── chunk.py
├── embed.py
├── search.py
├── main.py
├── api.py
├── app.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Setup and Installation

### 1. Clone the repository

```bash
git clone https://github.com/Rahul-pujari06/financial-rag-assistant.git
cd financial-rag-assistant
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate on Windows:

```powershell
.\venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the Groq API key

Create a `.env` file in the project root:

```text
GROQ_API_KEY=your_groq_api_key
```

### 5. Add the annual report

Place the PDF file at:

```text
data/financial_report.pdf
```

### 6. Process the document

Run these scripts in order:

```bash
python extract.py
python chunk.py
python embed.py
```

### 7. Start the FastAPI backend

```bash
uvicorn api:app --reload
```

API documentation:

http://127.0.0.1:8000/docs

### 8. Start the Streamlit frontend

Open a second terminal:

```bash
streamlit run app.py
```

Application URL:

http://localhost:8501

## Security

- API keys must be stored in `.env`.
- Never upload `.env`, private credentials, or sensitive documents.
- Generated vector-store files and local environment files are excluded using `.gitignore`.

## Future Improvements

- Retrieval accuracy evaluation
- Cross-encoder reranking
- Improved financial answer validation
- Support for multiple financial reports

## Author

**Rahul Pujari**

[GitHub Profile](https://github.com/Rahul-pujari06)
