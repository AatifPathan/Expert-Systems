!pip install spacy > /dev/null
!python -m spacy download en_core_web_sm > /dev/null
import spacy,re
nlp=spacy.load("en_core_web_sm")
def handle_query(q):
    q=q.lower()
    if "product" in q and ("support" in q or "help" in q):
        return "How can I assist you with product support?"
    elif "return" in q or "replace" in q:
        return "To process a return or replacement, please provide your order number."
    elif "refund" in q or "money back" in q:
        return "Refunds are typically processed within 5–7 business days."
    elif "account" in q or "login" in q or "password" in q:
        return "Can you please specify the issue with your account?"
    elif any(w in q for w in ["delivery","shipping","order","package","track","arrive"]):
        if re.search(r"(where|when).*order|package|delivery|arrive",q):
            return "You can track your order in your account dashboard. Our standard delivery time is 3–5 business days."
        else:
            return "Our standard delivery time is 3–5 business days."
    elif any(w in q for w in ["hi","hello","hey","good morning","good afternoon"]):
        return "Hello! How can I help you today?"
    elif any(w in q for w in ["thank","thanks","appreciate"]):
        return "You're very welcome! 😊 Anything else I can help you with?"
    else:
        return "I'm unable to assist with that. Let me connect you to a human representative."
def start_chat():
    print("🤖 Expert System Chatbot: Hello! How can I help you today?")
    print("(Type 'exit' to end the chat.)")
    while True:
        u=input("🧑 You: ")
        if u.lower() in ["exit","quit","bye"]:
            print("🤖 Chatbot: Thank you! Have a great day. 👋")
            break
        print(f"🤖 Chatbot: {handle_query(u)}\n")
start_chat()
