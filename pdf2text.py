import fitz  # PyMuPDF
import tkinter as tk
from tkinter import filedialog, messagebox

def pdf_to_text(pdf_path, txt_path):
    try:
        pdf_document = fitz.open(pdf_path)
        text = ""

        for page_num in range(pdf_document.page_count):
            page = pdf_document.load_page(page_num)
            text += page.get_text()

        with open(txt_path, 'w', encoding='utf-8') as txt_file:
            txt_file.write(text)

        messagebox.showinfo("Success", f"Text extracted and saved to {txt_path}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to extract text: {e}")

def open_file():
    file_path = filedialog.askopenfilename(
        filetypes=[("PDF Files", "*.pdf")], title="Select a PDF File"
    )
    if file_path:
        save_path = filedialog.asksaveasfilename(
            defaultextension=".txt", filetypes=[("Text Files", "*.txt")], title="Save As"
        )
        if save_path:
            pdf_to_text(file_path, save_path)

def main():
    root = tk.Tk()
    root.title("PDF to Text Converter")
    root.geometry("300x150")
    
    label = tk.Label(root, text="Drag and drop a PDF file or click 'Open' to select a file", wraplength=250)
    label.pack(pady=10)
    
    open_button = tk.Button(root, text="Open PDF File", command=open_file)
    open_button.pack(pady=10)
    
    root.mainloop()

if __name__ == "__main__":
    main()
