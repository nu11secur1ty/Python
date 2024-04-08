#!/usr/bin/python

import tkinter as tk
import pyshorteners
import os
import sys


def get_resource_path(relative_path):
    if getattr(sys, 'frozen', False):
        bundle_dir = sys._MEIPASS
        return os.path.join(bundle_dir, relative_path)
    base_path = os.path.abspath('.')
    return os.path.join(base_path, relative_path)


def shorten():
    shortener = pyshorteners.Shortener()
    short_url = shortener.tinyurl.short(longurl_entry.get())
    shorturl_entry.delete(0, tk.END)
    shorturl_entry.insert(0, short_url)


root = tk.Tk()
root.title("Shorter Link Generator App")
root.geometry("400x200")


FONT = ("Arial", 12)
LABEL_BG = "#ECECEC"
ENTRY_BG = "white"
BUTTON_BG = "#24A0ED"
BUTTON_FG = "white"

container_frame = tk.Frame(root)
container_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

longurl_label = tk.Label(container_frame, text="Enter original URL", font=FONT, bg=LABEL_BG)
longurl_entry = tk.Entry(container_frame, font=FONT, width=40, bg=ENTRY_BG)
shorturl_label = tk.Label(container_frame, text="Output shortened URL", font=FONT, bg=LABEL_BG)
shorturl_entry = tk.Entry(container_frame, font=FONT, width=40, bg=ENTRY_BG)
shorten_button = tk.Button(container_frame, text="Shorten URL", font=FONT, bg=BUTTON_BG, fg=BUTTON_FG, command=shorten)

longurl_label.pack(pady=(0, 5))
longurl_entry.pack(pady=(0, 10))
shorturl_label.pack(pady=(0, 5))
shorturl_entry.pack(pady=(0, 10))
shorten_button.pack()

root.mainloop()
