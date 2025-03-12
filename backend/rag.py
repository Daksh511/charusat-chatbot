from search import retrieve_context
from openai_api import generate_response

def rag_response(query):
    context = retrieve_context(query)
    prompt = f"Context: {context}\nUser Query: {query}\nAnswer based on the above context."
    return generate_response(prompt)
