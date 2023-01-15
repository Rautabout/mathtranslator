import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import messagebox

def reset():
    input_textarea.configure(state='normal')
    input_textarea.delete(1.0, 'end')
    input_textarea.configure(state='disabled')

    output_textarea.configure(state='normal')
    output_textarea.delete(1.0, 'end')
    output_textarea.configure(state='disabled')

    mathml_button.configure(state='normal')
    latex_button.configure(state='normal')
    docx_button.configure(state='normal')
    input_var.set(None)
    output_var.set(None)

def convert():
    # get the input and output formats
    input_format = input_var.get()
    output_format = output_var.get()
    input_text = input_textarea.get(1.0, 'end')
    if input_format == output_format:
        messagebox.showerror("Error", "Choose different input and output formats")
        return
    # perform the conversion here
    output_text = "Converted Text"

    output_textarea.configure(state='normal')
    output_textarea.delete(1.0, 'end')
    output_textarea.insert(tk.INSERT, output_text)
    output_textarea.configure(state='disabled')

root = tk.Tk()
root.title("Math Translator")

error_label = ttk.Label(root, text="")
error_label.grid(column=0, row=2, columnspan=2)

#reset button
reset_button = ttk.Button(root, text="Reset", command=reset)
reset_button.grid(column=0, row=3, columnspan=2, pady=10)

# create the input frame
input_frame = ttk.Frame(root)
input_frame.grid(column=0, row=0, padx=10, pady=10)

# create the input format radio buttons
input_var = tk.StringVar()
mathml_button = ttk.Radiobutton(input_frame, text='MathML', variable=input_var, value='mathml')
mathml_button.grid(column=0, row=0)
latex_button = ttk.Radiobutton(input_frame, text='LaTeX', variable=input_var, value='latex')
latex_button.grid(column=1, row=0)
docx_button = ttk.Radiobutton(input_frame, text='Docx', variable=input_var, value='docx')
docx_button.grid(column=2, row=0)

# create the input text area
input_textarea = scrolledtext.ScrolledText(input_frame, width=40, height=10)
input_textarea.grid(column=0, row=1, columnspan=3, padx=10, pady=10)

# create the output frame
output_frame = ttk.Frame(root)
output_frame.grid(column=1, row=0, padx=10, pady=10)

# create the output format radio buttons
output_var = tk.StringVar()
mathml_button = ttk.Radiobutton(output_frame, text='MathML', variable=output_var, value='mathml')
mathml_button.grid(column=0, row=0)
latex_button = ttk.Radiobutton(output_frame, text='LaTeX', variable=output_var, value='latex')
latex_button.grid(column=1, row=0)
docx_button = ttk.Radiobutton(output_frame, text='Docx', variable=output_var, value='docx')
docx_button.grid(column=2, row=0)

output_textarea = scrolledtext.ScrolledText(output_frame, width=40, height=10)
output_textarea.grid(column=0, row=1, columnspan=3, padx=10, pady=10)

# create the convert button
convert_button = ttk.Button(root, text="Convert", command=convert)
convert_button.grid(column=0, row=1, columnspan=2, pady=10)
