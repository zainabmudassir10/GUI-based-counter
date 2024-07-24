import tkinter as tk
import re

def words_counter(data):
    words = data.split()
    return len(words)

def sentence_counter(data):
    sentences = re.split(r'[.?,]', data)
    sentences = [s for s in sentences if s.strip()]
    return len(sentences)

def update_counts():
    text = text_entry.get("1.0", tk.END)  # Get text from the text area
    word_count = words_counter(text)
    sentence_count = sentence_counter(text)
    
    word_count_label.config(text=f"Words: {word_count}")
    sentence_count_label.config(text=f"Sentences: {sentence_count}")

# Create the main window
root = tk.Tk()
root.title("Word and Sentence Counter")

# Create and place widgets
text_entry = tk.Text(root, height=10, width=40)
text_entry.pack(padx=10, pady=10)

count_button = tk.Button(root, text="Count", command=update_counts)
count_button.pack(pady=5)

word_count_label = tk.Label(root, text="Words: 0")
word_count_label.pack(pady=5)

sentence_count_label = tk.Label(root, text="Sentences: 0")
sentence_count_label.pack(pady=5)

# Run the application
root.mainloop()
