import os
from PyPDF2 import PdfReader, PdfWriter, Transformation
import tkinter as tk
from tkinter import filedialog, messagebox


def mirror_pdf_pypdf2(input_path, output_path):
    reader = PdfReader(input_path)
    writer = PdfWriter()

    for page in reader.pages:
        width = float(page.mediabox.width)
        transformation = Transformation().scale(sx=-1, sy=1).translate(tx=width, ty=0)
        page.add_transformation(transformation)
        writer.add_page(page)

    with open(output_path, "wb") as f:
        writer.write(f)



def select_input_file():
    file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    if file_path:
        input_entry.delete(0, tk.END)
        input_entry.insert(0, file_path)


def select_output_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF Files", "*.pdf")])
    if file_path:
        output_entry.delete(0, tk.END)
        output_entry.insert(0, file_path)


def run_mirror():
    input_path = input_entry.get()
    output_path = output_entry.get()
    if not os.path.isfile(input_path):
        messagebox.showerror("Error", "Invalid input file.")
        return
    try:
        mirror_pdf_pypdf2(input_path, output_path)
        messagebox.showinfo("Success", f"Mirrored PDF saved to:\n{output_path}")
    except Exception as e:
        messagebox.showerror("Error", str(e))


# GUI setup
root = tk.Tk()
root.title("PDF Mirror Tool")
root.geometry("400x200")

frame = tk.Frame(root, padx=10, pady=10)
frame.pack(fill="both", expand=True)

tk.Label(frame, text="Input PDF:").grid(row=0, column=0, sticky="w")
input_entry = tk.Entry(frame, width=40)
input_entry.grid(row=0, column=1, padx=5)
tk.Button(frame, text="Browse", command=select_input_file).grid(row=0, column=2)

tk.Label(frame, text="Output PDF:").grid(row=1, column=0, sticky="w")
output_entry = tk.Entry(frame, width=40)
output_entry.grid(row=1, column=1, padx=5)
tk.Button(frame, text="Browse", command=select_output_file).grid(row=1, column=2)

tk.Button(frame, text="Mirror PDF", command=run_mirror).grid(row=2, column=1, pady=20)

root.mainloop()
