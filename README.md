# Financial RAG Assistant

**A Python-based financial document search project using semantic embeddings and FAISS.**

## Overview

Financial reports contain a large amount of information spread across hundreds of pages. Finding a specific figure or understanding a particular financial detail can take time, especially when the information is not available in one place.

I built this project to make that process easier. It takes a company's annual report, extracts its text, converts the content into smaller searchable sections, and retrieves the most relevant passages based on a user's question.

The project currently uses the **Happiest Minds Technologies FY 2024–25 Annual Report** as its source document.

## What it does

- Extracts text from a PDF while preserving page references.
- Splits the extracted content into smaller, overlapping chunks.
- Generates semantic embeddings using Sentence Transformers.
- Stores and searches those embeddings using FAISS.
- Returns the most relevant passages along with their PDF page numbers.

Unlike a basic keyword search, semantic search can retrieve relevant passages even when the wording of a question differs from the wording in the report.

## Tech stack

| Technology | Purpose |
|---|---|
| Python | Core development |
| PyPDF | PDF text extraction |
| Sentence Transformers | Text embeddings |
| all-MiniLM-L6-v2 | Embedding model |
| FAISS | Vector indexing and similarity search |
| NumPy | Numerical operations |

## How the project works

```text
Annual Report (PDF)
       |
       v
   Text Extraction
       |
       v
   Text Chunking
       |
       v
 Embedding Generation
       |
       v
 FAISS Vector Index
       |
       v
   User Question
       |
       v
 Semantic Similarity Search
       |
       v
 Relevant Passages + Page Numbers
```

## Current implementation

The first working version has been tested locally.

| Component | Current result |
|---|---|
| PDF text extraction | Completed |
| Page-level references | Implemented |
| Text chunking | Completed |
| Text chunks generated | 336 |
| Embedding dimensions | 384 |
| FAISS index creation | Successful |
| Semantic search | Tested locally |

For example, I tested the system with the question:

**"What was the company's revenue in FY 2024–25?"**

The search returned relevant financial passages from different sections of the annual report. This also highlighted an important consideration in financial analysis: standalone and consolidated figures need to be distinguished before presenting an answer.

## Project structure

```text
financial-rag-assistant/
│
├── extract.py
├── chunk.py
├── embed.py
├── search.py
├── requirements.txt
├── .gitignore
│
├── data/
│   └── financial_report.pdf       # Local source file
│
└── vectorstore/
    ├── financial.index            # Generated locally
    └── chunks_metadata.json       # Generated locally
```

The report and generated vector files are kept locally and are not included in this repository.

## Run locally

### 1. Clone the repository

```bash
git clone https://github.com/Rahul-pujari06/financial-rag-assistant.git
cd financial-rag-assistant
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
```

Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Add the source report

Create a `data` folder and place the annual report PDF inside it with this filename:

```text
financial_report.pdf
```

### 5. Run the scripts in order

```bash
python extract.py
python chunk.py
python embed.py
python search.py
```

After indexing is complete, enter a question in the terminal to retrieve relevant passages from the report. Type `exit` to stop the search session.

The embedding model is downloaded the first time it is used, so an internet connection is required for initial setup.

## What I learned

Building this project helped me understand how a document search pipeline works beyond simply writing a SQL query or searching for keywords.

Some of the key concepts I worked with:

- Extracting and preparing unstructured PDF data.
- Splitting text while retaining source information.
- Generating vector embeddings.
- Building a FAISS similarity-search index.
- Understanding semantic similarity scores.
- Checking retrieved financial information against its source.

## What's next

The next stage is to extend the current semantic search pipeline into a complete Retrieval-Augmented Generation (RAG) application.

Planned improvements:

- Integrate an LLM to generate answers from retrieved passages.
- Add source citations and page references to generated answers.
- Build a Streamlit interface for asking questions.
- Test retrieval quality using different financial questions.
- Improve handling of financial tables and standalone versus consolidated figures.

---

**Developer:** Rahul Pujari  
**GitHub:** [Rahul-pujari06](https://github.com/Rahul-pujari06)

