# University of Kotli Chatbot  

A simple chatbot application built using **Tkinter** for the graphical user interface and **Google Gemini API** for text-based responses. The chatbot provides two main functionalities:  

- **Text Chatbot**: Allows users to enter a query, and the chatbot fetches relevant information from a text file (`data.txt`) and responds using the Gemini API.  
- **Speech Chatbot**: Similar to the text chatbot but includes a "Speak" button to convert the response into speech using **pyttsx3**.  

---

## Features  

✅ **Text Chatbot** – Enter a text query and receive an AI-generated response.  
✅ **Speech Chatbot** – The chatbot reads out responses using text-to-speech.  
✅ **File-based Knowledge** – Responses are generated based on data stored in `data.txt`.  
✅ **Google Gemini AI Integration** – Uses **Gemini-2.0-flash** for generating responses.  
✅ **Tkinter GUI** – Simple and user-friendly interface.  

---

## How It Works  

1. The chatbot reads data from `data.txt` to enhance response accuracy.  
2. The user enters a prompt, and the chatbot queries Google Gemini AI.  
3. The **text chatbot** displays the response, while the **speech chatbot** speaks it out.  

---

## Installation  

### Requirements  
- Python 3.x  
- Tkinter (comes with Python)  
- PIL (for handling images)  
- `pyttsx3` (for text-to-speech)  
- Google Gemini API Key
