from services.retriever import retrieve_documents
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def generate_answer(query):
    # Step 1: Retrieve context
    docs = retrieve_documents(query)
    context = "\n\n".join(docs)

    # Step 2: Create prompt
    prompt = f"""
    Answer the question using the context below.
    If the answer is not in the context, say "Not found in document".

    Context:
    {context}

    Question:
    {query}
    """

    # Step 3: Gemini model
    model = genai.GenerativeModel("gemini-2.5-flash")

    response = model.generate_content(prompt)

    return response.text