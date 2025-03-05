from transformers import GPT2LMHeadModel, GPT2Tokenizer
from termcolor import colored

# Загружаем модель и токенайзер
model = GPT2LMHeadModel.from_pretrained("gpt2")
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
tokenizer.pad_token = tokenizer.eos_token

# Храним контекст чата
chat_history = []

# Функция генерации с контекстом
def generate_response(prompt, max_new_tokens=150, temperature=0.7, top_p=0.95, top_k=40, do_sample=True):
    # Добавляем историю чата в промпт
    system_instruction = "You are fucking crazy AI, your name is Jake."
    history = "\n".join(chat_history[-5:])  
    full_prompt = f"{system_instruction}\n{history}\nHuman: {prompt}\nAI:"
    
    # Токенизация и генерация
    inputs = tokenizer(full_prompt, return_tensors="pt", padding=True, truncation=True)
    outputs = model.generate(
        **inputs,
        max_new_tokens=max_new_tokens,
        temperature=temperature,
        top_p=top_p,
        top_k=top_k,
        repetition_penalty = 1.2,
        pad_token_id=tokenizer.eos_token_id,
        do_sample=do_sample
    )
    
    # Очистка и вывод ответа
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    print(f"Raw response: {response}")
    ai_response = response.split("AI:")[-1].strip().split("\n")[0]
    chat_history.append(f"Human: {prompt}")
    chat_history.append(f"AI: {ai_response}")
    return ai_response

# Функция запуска чата
def start_ai_chat():
    global chat_history
    chat_history = []
    print("Welcome to AI_Mix chat! Type 'exit' to quit")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        ai_response = generate_response(user_input)
        print(f"AI: {colored(ai_response, 'yellow')}")