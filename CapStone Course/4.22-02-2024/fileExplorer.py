import os
import tkinter as tk
from tkinter import filedialog, ttk

class FileExplorerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple File Explorer")

        self.current_folder_path = os.getcwd()
        self.create_widgets()

    def create_widgets(self):
        self.tree = ttk.Treeview(self.root)
        self.tree.pack(side='left', fill='both', expand=True)

        scrollbar = ttk.Scrollbar(self.root, orient='vertical', command=self.tree.yview)
        scrollbar.pack(side='right', fill='y')
        self.tree.configure(yscrollcommand=scrollbar.set)

        self.tree["columns"] = ("Type")
        self.tree.column("#0", width=250)
        self.tree.column("Type", width=100)
        self.tree.heading("#0", text="Name")
        self.tree.heading("Type", text="Type")

        self.tree.bind("<Double-1>", self.on_item_selected)

        self.browse_button = tk.Button(self.root, text="Browse Folder", command=self.browse_folder)
        self.browse_button.pack(pady=10)

    def browse_folder(self):
        folder_path = filedialog.askdirectory()
        if folder_path:
            self.current_folder_path = folder_path
            self.list_contents(folder_path)

    def list_contents(self, folder_path):
        self.tree.delete(*self.tree.get_children())
        files = os.listdir(folder_path)
        for item in files:
            item_path = os.path.join(folder_path, item)
            item_type = "Folder" if os.path.isdir(item_path) else "File"
            self.tree.insert('', 'end', text=item, values=(item_type,))

    def on_item_selected(self, event):
        item = self.tree.selection()[0]
        item_text = self.tree.item(item, "text")
        item_type = self.tree.item(item, "values")[0]

        if item_type == "Folder":
            folder_path = os.path.join(self.current_folder_path, item_text)
            self.current_folder_path = folder_path
            self.list_contents(folder_path)
        else:
            file_path = os.path.join(self.current_folder_path, item_text)
            self.open_file(file_path)

    def open_file(self, file_path):
        try:
            os.startfile(file_path)
        except OSError as e:
            print(f"Error opening file: {e}")

def main():
    root = tk.Tk()
    app = FileExplorerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()