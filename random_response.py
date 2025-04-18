import random

def generate_ai_response():
    responses = [
        "I'm here to help you with your accounting needs!",
        "Can you provide more details about your expense?",
        "That sounds interesting! Let me process that for you.",
        "Got it! Let me update your records.",
        "I'm not sure I understand. Could you clarify?"
    ]
    return random.choice(responses)