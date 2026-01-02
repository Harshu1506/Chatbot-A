import tkinter as tk

def thriya_response(user_input):
    user_input = user_input.lower()

    if user_input in ["hi", "hello"]:
        return "Hello! I am Thriya. How can I help you?"
    elif "name" in user_input:
        return "My name is Thriya, a virtual assistant."
    elif "purpose" in user_input:
        return "My purpose is to assist users with basic information."
    elif "help" in user_input:
        return "You can ask me about my name, purpose, or say hello."
    elif "bye" in user_input:
        return "Goodbye! Have a nice day 😊"
    else:
        return "Sorry, I didn’t understand that."

def send_message():
    user_text = entry.get()
    chat_area.insert(tk.END, "You: " + user_text + "\n")
    reply = thriya_response(user_text)
    chat_area.insert(tk.END, "Thriya: " + reply + "\n\n")
    entry.delete(0, tk.END)

# GUI Window
window = tk.Tk()
window.title("Thriya - Beginner Virtual Assistant")

chat_area = tk.Text(window, height=15, width=50)
chat_area.pack(pady=10)

entry = tk.Entry(window, width=40)
entry.pack(side=tk.LEFT, padx=10)

send_button = tk.Button(window, text="Send", command=send_message)
send_button.pack(side=tk.LEFT)

window.mainloop()
 