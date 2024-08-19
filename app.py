import tkinter as tk
from transformers import pipeline

def generate_text():
    prompt = prompt_entry.get()

    if not prompt:
        result_label.config(text="Please enter a prompt.")
        return

    try:
        result = pipe(prompt, max_length=100, num_beams=4)
        result_text = result[0]['generated_text']
        result_label.config(text=result_text)
    except Exception as e:
        result_label.config(text=f"Error: {e}")

# Create the main window
root = tk.Tk()
root.title("AI Text Generator")

# Create labels and entry fields
prompt_label = tk.Label(root, text="Enter Prompt:")
prompt_entry = tk.Entry(root, width=50)
result_label = tk.Label(root, text="")

# Create the generate button
generate_button = tk.Button(root, text="Generate", command=generate_text)

# Grid layout
prompt_label.grid(row=0, column=0, padx=5, pady=5)
prompt_entry.grid(row=0, column=1, padx=5, pady=5)
generate_button.grid(row=1, column=0, columnspan=2, padx=5, pady=5)
result_label.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

# Use a pipeline as a high-level helper
from transformers import pipeline

pipe = pipeline("text-generation", model="distilbert/distilgpt2")

root.mainloop()
