import tkinter as tk
import requests
import zipfile
import io
import os

def download():
    url = entry.get()
    if 'github.com' not in url:
        status.config(text="Invalid GitHub URL")
        return
    repo = url.rstrip('/').replace('github.com/', 'api.github.com/repos/')
    r = requests.get(f'{repo}/zipball/main')
    if r.status_code != 200:
        r = requests.get(f'{repo}/zipball/master')
    if r.status_code == 200:
        z = zipfile.ZipFile(io.BytesIO(r.content))
        z.extractall('.')
        status.config(text=f"Extracted: {z.namelist()[0]}")
    else:
        status.config(text="Failed")

root = tk.Tk()
root.title("Git Clone")
tk.Label(root, text="GitHub URL:").pack()
entry = tk.Entry(root, width=50)
entry.pack()
tk.Button(root, text="Download", command=download).pack()
status = tk.Label(root, text="")
status.pack()
root.mainloop()