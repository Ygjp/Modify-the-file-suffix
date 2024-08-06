import os
import tkinter as tk
from tkinter import filedialog, messagebox
def modify_file_extension(path, old_ext, new_ext):
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(old_ext):
                old_file = os.path.join(root, file)
                new_file = os.path.splitext(old_file)[0] + new_ext
                os.rename(old_file, new_file)
    messagebox.showinfo("成功", "文件扩展名修改成功！")
def select_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        folder_entry.delete(0, tk.END)
        folder_entry.insert(0, folder_path)
def start_modification():
    folder_path = folder_entry.get()
    old_ext = old_ext_entry.get()
    new_ext = new_ext_entry.get()

    if not folder_path or not old_ext or not new_ext:
        messagebox.showwarning("警告", "所有字段必须填写")
        return
    if not old_ext.startswith("."):
        old_ext = "." + old_ext
    if not new_ext.startswith("."):
        new_ext = "." + new_ext
    modify_file_extension(folder_path, old_ext, new_ext)
root = tk.Tk()
root.title("批量修改文件扩展名")
folder_label = tk.Label(root, text="选择文件夹：")
folder_label.grid(row=0, column=0, padx=10, pady=10)
folder_entry = tk.Entry(root, width=50)
folder_entry.grid(row=0, column=1, padx=10, pady=10)
folder_button = tk.Button(root, text="浏览", command=select_folder)
folder_button.grid(row=0, column=2, padx=10, pady=10)
old_ext_label = tk.Label(root, text="当前扩展名（例如：.txt）：")
old_ext_label.grid(row=1, column=0, padx=10, pady=10)
old_ext_entry = tk.Entry(root, width=20)
old_ext_entry.grid(row=1, column=1, padx=10, pady=10)
new_ext_label = tk.Label(root, text="新扩展名（例如：.md）：")
new_ext_label.grid(row=2, column=0, padx=10, pady=10)
new_ext_entry = tk.Entry(root, width=20)
new_ext_entry.grid(row=2, column=1, padx=10, pady=10)
start_button = tk.Button(root, text="开始修改", command=start_modification)
start_button.grid(row=3, column=1, padx=10, pady=10)
root.mainloop()
