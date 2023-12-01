import requests
import argparse
from pathlib import Path
import tkinter as tk
from tkinter import scrolledtext


def manga_history():
    manga_history_url = "http://localhost:3000/history"
    history = get_history(manga_history_url)

    if history:
        result.config(state=tk.NORMAL)
        result.delete(1.0, tk.END)
        result.insert(tk.END, "Manga Recommendation History\n")
        for num, rec in enumerate(history, start=1):
            manga_title = rec.get('title')
            result.insert(tk.END, f'{num},' f'{manga_title}\n')
        result.config(state=tk.DISABLED)


def get_history(manga_history_url):
    answer = requests.get(manga_history_url)
    if answer.status_code == 200:
        return answer.json()
    else:
        print(f"We are unable to get the manga history. Error {answer.status_code}")
        return None
    

if __name__ == "__main__":
    window = tk.Tk()
    window.title("Manga History")

    title = tk.Label(window, text="Click the button to get the history of all the recommended mangas!\n",
                     cursor="hand2", 
                    font=("TkHeadingFont", 20) )
    title.pack(pady=20)


    rec_button = tk.Button(window, text="Show Manga History",
            cursor="hand2", 
            font=("TkHeadingFont", 20),
            bg="#4B527E", 
            fg="white",
            command=manga_history)
    rec_button.pack(pady=20)

    result = scrolledtext.ScrolledText(window, width=200, height=100, state=tk.DISABLED)
    result.pack(pady=20)
    window.mainloop()
    