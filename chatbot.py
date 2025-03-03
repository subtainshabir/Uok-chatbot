import tkinter as tk
from tkinter import messagebox, scrolledtext
from PIL import Image, ImageTk  # For handling images (e.g., jpg)
import google.generativeai as genai  # Import Gemini API

# Set up Google Gemini API key
GEMINI_API_KEY = "AIzaSyBmaFiHkFbyNcb9VSJ_xM793m9qnCFlF_4"  # Replace with actual API key
genai.configure(api_key=GEMINI_API_KEY)

def call_gemini_api(prompt):
    """
    Reads data from a text file, searches for relevant information, and 
    sends the extracted data along with the prompt to the Gemini API.
    """
    file_path = 'data.txt'
    try:
        # Read the text file
        with open(file_path, "r", encoding="utf-8") as file:
            file_data = file.read()

        # Combine the prompt with the file data
        search_prompt = f"Based on the following data:\n{file_data}\n\nAnswer this query: {prompt}"
        
        # Call Gemini API
        model = genai.GenerativeModel("gemini-2.0-flash")
        response = model.generate_content(search_prompt)
        
        return response.text.strip() if response.text else "No relevant information found."
    
    except Exception as e:
        return f"Error: {str(e)}"

def open_text_chatbot():
    """
    Opens a new window for text input and displays the Gemini API generated text.
    """
    def generate_text():
        prompt = prompt_text.get("1.0", tk.END).strip()
        if prompt:
            result = call_gemini_api(prompt)
            if result:
                output_text.config(state=tk.NORMAL)
                output_text.delete("1.0", tk.END)
                output_text.insert(tk.END, result)
                output_text.config(state=tk.DISABLED)
        else:
            messagebox.showwarning("Input Error", "Please enter a prompt.")

    # Create a new window for the text chatbot
    text_window = tk.Toplevel(root)
    text_window.title("Text Chatbot")
    text_window.geometry("500x400")
    
    # Prompt label and text area
    prompt_label = tk.Label(text_window, text="Enter your prompt:")
    prompt_label.pack(pady=5)
    
    prompt_text = scrolledtext.ScrolledText(text_window, wrap=tk.WORD, width=50, height=5)
    prompt_text.pack(pady=5)
    
    # Generate button
    generate_btn = tk.Button(text_window, text="Generate Text", command=generate_text)
    generate_btn.pack(pady=10)
    
    # Output text area (read-only)
    output_label = tk.Label(text_window, text="Generated Text:")
    output_label.pack(pady=5)
    
    output_text = scrolledtext.ScrolledText(text_window, wrap=tk.WORD, width=50, height=10, state=tk.DISABLED)
    output_text.pack(pady=5)

def open_speech_chatbot():
    # Placeholder function for Speech Chatbot integration
    messagebox.showinfo("Speech Chatbot", "Speech Chatbot functionality coming soon!")

def exit_app():
    root.destroy()

# Initialize the main Tkinter window
root = tk.Tk()
root.title("University of Kotli Chatbot")
root.geometry("500x400")
root.resizable(False, False)

# Load University of Kotli Logo using PIL (update path as needed)
try:
    image_path = "D:/chatbot/Uok-chatbot/uok.jpg"  # Ensure correct path
    image = Image.open(image_path)
    image = image.resize((100, 100))  # Resize if needed
    logo = ImageTk.PhotoImage(image)
    logo_label = tk.Label(root, image=logo)
    logo_label.place(x=10, y=10)
except Exception as e:
    print("Error loading logo:", e)

# Title Label
title_label = tk.Label(root, text="University of Kotli Chatbot", font=("Arial", 16, "bold"))
title_label.pack(pady=50)

# Buttons
btn_text = tk.Button(root, text="Text Chatbot", font=("Arial", 12), width=20, command=open_text_chatbot)
btn_text.pack(pady=10)

btn_speech = tk.Button(root, text="Speech Chatbot", font=("Arial", 12), width=20, command=open_speech_chatbot)
btn_speech.pack(pady=10)

btn_exit = tk.Button(root, text="Exit", font=("Arial", 12), width=20, command=exit_app, bg="red", fg="white")
btn_exit.pack(pady=10)

# Run the main loop
root.mainloop()
