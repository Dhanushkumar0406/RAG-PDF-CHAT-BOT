from app.services.llm_service import LLMService

llm = LLMService()

answer = llm.generate_answer(
    context="Artificial Intelligence is the simulation of human intelligence.",
    question="What is Artificial Intelligence?"
)

print(answer)