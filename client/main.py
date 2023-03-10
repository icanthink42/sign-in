import tkinter as tk

import facial_rec
import requests

server = "http://127.0.0.1:5000/"


def no_pressed():
    window.destroy()


def yes_pressed():
    print("a")
    requests.post(f"{server}/sign_in", timeout=3, json={"user": user})
    print("b")
    window.destroy()


while True:
    user_id = facial_rec.detect_face()[0].split(".")[0]
    user = requests.post(f"{server}/get_name", timeout=3, json={"id": user_id}).text

    window = tk.Tk()
    window.attributes("-fullscreen", True)
    greeting = tk.Label(text=f"Sign in {user}?", font=("Arial", 15))
    yes_button = tk.Button(
        text="👍",
        width=25,
        height=5,
        bg="green",
        fg="yellow",
        font=("Arial", 15),
        command=lambda: yes_pressed(),
    )
    no_button = tk.Button(
        text="👎",
        width=25,
        height=5,
        bg="red",
        fg="yellow",
        font=("Arial", 15),
        command=lambda: no_pressed(),
    )
    greeting.pack()
    yes_button.pack()
    no_button.pack()
    window.mainloop()
