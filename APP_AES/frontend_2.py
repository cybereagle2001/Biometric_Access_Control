import tkinter as tk
from tkinter import ttk
from tkinter import filedialog, messagebox, scrolledtext
import os
from datetime import datetime
from backend import *

class BiometricAuthApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Biometric Authentication System")
        self.root.geometry("800x600")

        # Create a notebook (tabbed interface)
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill=tk.BOTH, expand=True)

        # Biometric Authentication Tab
        self.auth_tab = tk.Frame(self.notebook)
        self.notebook.add(self.auth_tab, text="Biometric Authentication")
        self.setup_biometric_auth_tab()

        # File Management Tab
        self.file_tab = tk.Frame(self.notebook)
        self.notebook.add(self.file_tab, text="File Management")
        self.setup_file_management_tab()

        # History Tab
        self.history_tab = tk.Frame(self.notebook)
        self.notebook.add(self.history_tab, text="Operation History")
        self.setup_history_tab()

        # Logs
        self.logs = []

        # Disable File Management and History tabs initially
        self.notebook.tab(1, state="disabled")  # File Management tab
        self.notebook.tab(2, state="disabled")  # History tab

    def setup_biometric_auth_tab(self):
        tk.Label(self.auth_tab, text="Fingerprint Image Path:").grid(row=0, column=0, padx=10, pady=10)
        self.fingerprint_path_entry = tk.Entry(self.auth_tab, width=50)
        self.fingerprint_path_entry.grid(row=0, column=1, padx=10, pady=10)
        tk.Button(self.auth_tab, text="Browse", command=self.browse_fingerprint).grid(row=0, column=2, padx=10, pady=10)

        tk.Button(self.auth_tab, text="Verify Fingerprint", command=self.verify_fingerprint).grid(row=1, column=1, pady=20)

    def setup_file_management_tab(self):
        tk.Label(self.file_tab, text="File Path:").grid(row=0, column=0, padx=10, pady=10)
        self.file_path_entry = tk.Entry(self.file_tab, width=50)
        self.file_path_entry.grid(row=0, column=1, padx=10, pady=10)
        tk.Button(self.file_tab, text="Browse", command=self.browse_file).grid(row=0, column=2, padx=10, pady=10)

        tk.Label(self.file_tab, text="Operation:").grid(row=1, column=0, padx=10, pady=10)
        self.operation_var = tk.StringVar(value="encrypt")
        tk.Radiobutton(self.file_tab, text="Encrypt", variable=self.operation_var, value="encrypt").grid(row=1, column=1, padx=10, pady=10)
        tk.Radiobutton(self.file_tab, text="Decrypt", variable=self.operation_var, value="decrypt").grid(row=1, column=2, padx=10, pady=10)

        tk.Button(self.file_tab, text="Execute Operation", command=self.execute_operation).grid(row=2, column=1, pady=20)

    def setup_history_tab(self):
        self.history_text = scrolledtext.ScrolledText(self.history_tab, width=90, height=20)
        self.history_text.pack(padx=10, pady=10)
        self.history_text.insert(tk.END, "Operation Logs:\n\n")
        self.history_text.config(state=tk.DISABLED)

    def browse_fingerprint(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png *.jpg *.jpeg *.tif")])
        self.fingerprint_path_entry.delete(0, tk.END)
        self.fingerprint_path_entry.insert(0, file_path)

    def browse_file(self):
        file_path = filedialog.askopenfilename()
        self.file_path_entry.delete(0, tk.END)
        self.file_path_entry.insert(0, file_path)

    def verify_fingerprint(self):
        fingerprint_path = self.fingerprint_path_entry.get()
        if not fingerprint_path:
            messagebox.showerror("Error", "Please select a fingerprint image.")
            return

        if verify_fingerprint_only(fingerprint_path):
            messagebox.showinfo("Success", "Fingerprint verified successfully.")
            self.log_operation(f"Fingerprint verified: {fingerprint_path}")
            # Enable File Management and History tabs after successful verification
            self.notebook.tab(1, state="normal")  # File Management tab
            self.notebook.tab(2, state="normal")  # History tab
        else:
            messagebox.showerror("Error", "Fingerprint verification failed.")

    def execute_operation(self):
        fingerprint_path = self.fingerprint_path_entry.get()
        file_path = self.file_path_entry.get()
        operation = self.operation_var.get()

        if not fingerprint_path or not file_path:
            messagebox.showerror("Error", "Please provide both fingerprint and file paths.")
            return

        try:
            biometric_authenticate(fingerprint_path, operation, file_path)
            self.log_operation(f"{operation.capitalize()} operation performed on {file_path}")
            messagebox.showinfo("Success", f"File {operation}ed successfully.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def log_operation(self, message):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"{timestamp} - {message}\n"
        self.logs.append(log_entry)
        self.history_text.config(state=tk.NORMAL)
        self.history_text.insert(tk.END, log_entry)
        self.history_text.config(state=tk.DISABLED)
        self.history_text.yview(tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = BiometricAuthApp(root)
    root.mainloop()
