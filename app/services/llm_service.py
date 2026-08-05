import ollama


class LLMService:

    def generate_answer(self, context: str, question: str):

        prompt = f"""
You are an AI assistant.

Answer ONLY using the given context.

If the answer is not present in the context,
reply with:

"I couldn't find this information in the uploaded PDF."

Context:
{context}

Question:
{question}

Answer:
"""

        response = ollama.chat(
            model="llama3.2",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response["message"]["content"]