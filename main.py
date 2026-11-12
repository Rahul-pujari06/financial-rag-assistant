
from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

from search import search_report


# 1. Load environment variables
load_dotenv()


# 2. Initialize Groq
llm = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0,
    max_tokens=1024
)


# 3. Improved financial analysis prompt
prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
        You are a financial document analysis assistant.

        Answer questions using ONLY the provided financial report context.

        IMPORTANT NUMERICAL ACCURACY RULES:

        1. Preserve financial figures exactly as stated in the source.
        2. Always mention the original unit, such as lakhs or crores.
        3. Do not invent, estimate, or modify financial figures.
        4. Do not convert lakhs into crores unless explicitly requested.
        5. If conversion is requested, calculate carefully.
        6. Distinguish consolidated and standalone financial figures.
        7. Never combine figures from different financial statements.
        8. If information is unavailable, clearly say so.
        9. Do not invent PDF page numbers or citations.
        10. If multiple figures are relevant, explain what each represents.

        Give a clear, concise and accurate answer.
        """
    ),
    (
        "human",
        """
        FINANCIAL REPORT CONTEXT:

        {context}

        USER QUESTION:

        {question}

        Answer using the financial report context.
        """
    )
])


# 4. Create LangChain pipeline
rag_chain = prompt | llm | StrOutputParser()


# 5. Main RAG function
def ask_question(question):

    # Retrieve relevant document chunks
    results = search_report(question, top_k=3)

    if not results:
        return {
            "answer": "No relevant information found in the report.",
            "sources": []
        }

    # Prepare context for LLM
    context_parts = []

    for result in results:

        context_parts.append(
            f"""
            PDF Page: {result['page']}
            Similarity Score: {result['score']:.4f}

            Financial Information:
            {result['text']}
            """
        )

    context = "\n".join(context_parts)

    # Generate answer
    answer = rag_chain.invoke({
        "context": context,
        "question": question
    })

    # Create structured sources directly from FAISS metadata
    sources = []

    for result in results:

        sources.append({
            "pdf_page": int(result["page"]),
            "similarity_score": round(
                float(result["score"]), 4
            ),
            "excerpt": result["text"][:300]
        })

    # Return answer and source information separately
    return {
        "answer": answer,
        "sources": sources
    }


# 6. Terminal testing
if __name__ == "__main__":

    print("\nFinancial RAG Assistant Ready!")

    while True:

        question = input(
            "\nAsk a financial question (or type exit): "
        )

        if question.lower().strip() == "exit":
            print("Application closed.")
            break

        if not question.strip():
            print("Please enter a question.")
            continue

        try:
            result = ask_question(question)

            print("\nANSWER:\n")
            print(result["answer"])

            print("\nSOURCE REFERENCES:")

            for source in result["sources"]:
                print(source)

        except Exception as e:
            print("Error:", str(e))
