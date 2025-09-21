import tkinter as tk
from tkinter import filedialog, messagebox
import os
import PyPDF2

def merge_pdfs(files, output_path):
    merger = PyPDF2.PdfMerger()
    for pdf in files:
        merger.append(pdf)
    merger.write(output_path)
    merger.close()

def select_files():
    files = filedialog.askopenfilenames(
        title="Pilih File PDF",
        filetypes=[("PDF Files", "*.pdf")]
    )
    if files:
        # Tambahkan file ke listbox tanpa menghapus yang lama
        existing_files = listbox.get(0, tk.END)
        for f in files:
            if f not in existing_files:  # hindari duplikat
                listbox.insert(tk.END, f)

def delete_selected():
    selected = listbox.curselection()  # ambil index yang dipilih
    if not selected:
        messagebox.showwarning("Peringatan", "Pilih file yang mau dihapus!")
        return
    
    for i in reversed(selected):  # hapus dari belakang biar index aman
        listbox.delete(i)

def merge_action():
    files = listbox.get(0, tk.END)
    if not files:
        messagebox.showerror("Error", "Belum ada file yang dipilih!")
        return
    
    # Sorting berdasarkan pilihan user
    sort_option = sort_var.get()
    files = list(files)
    if sort_option == "Nama":
        files.sort(key=lambda x: os.path.basename(x).lower())
    elif sort_option == "Tanggal":
        files.sort(key=lambda x: os.path.getmtime(x))

    # Pilih lokasi output
    output_path = filedialog.asksaveasfilename(
        defaultextension=".pdf",
        filetypes=[("PDF files", "*.pdf")],
        title="Simpan File Gabungan"
    )
    if output_path:
        merge_pdfs(files, output_path)
        messagebox.showinfo("Sukses", f"File berhasil digabung jadi:\n{output_path}")

# GUI
root = tk.Tk()
root.title("PDF Merger")
root.geometry("600x450")

frame = tk.Frame(root)
frame.pack(pady=10)

btn_select = tk.Button(frame, text="Pilih File PDF", command=select_files)
btn_select.pack(side=tk.LEFT, padx=5)

btn_merge = tk.Button(frame, text="Gabungkan", command=merge_action)
btn_merge.pack(side=tk.LEFT, padx=5)

btn_delete = tk.Button(frame, text="Hapus File Terpilih", command=delete_selected)
btn_delete.pack(side=tk.LEFT, padx=5)

# Pilihan sorting
sort_var = tk.StringVar(value="Nama")
sort_label = tk.Label(root, text="Urutkan berdasarkan:")
sort_label.pack()
sort_menu = tk.OptionMenu(root, sort_var, "Nama", "Tanggal")
sort_menu.pack()

# Listbox untuk tampilkan file
listbox = tk.Listbox(root, width=80, height=15, selectmode=tk.MULTIPLE)
listbox.pack(pady=10)

root.mainloop()
