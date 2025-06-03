import random
import tkinter as tk
from tkinter import messagebox

class GuessingGameGUI:
    def __init__(self, root):  # ✅ Corrected __init__
        self.root = root
        self.root.title("🎯 Number Guessing Game")
        self.root.geometry("400x300")
        self.root.configure(bg="#f0f8ff")

        self.secret_number = random.randint(1, 100)
        self.attempts = 0

        # Title label
        self.title_label = tk.Label(
            root, text="Guess the Number!",
            font=("Helvetica", 18, "bold"),
            bg="#f0f8ff", fg="#2e8b57"
        )
        self.title_label.pack(pady=15)

        # Instruction label
        self.instruction_label = tk.Label(
            root, text="Enter a number between 1 and 100:",
            font=("Helvetica", 12),
            bg="#f0f8ff", fg="#333"
        )
        self.instruction_label.pack()

        # Entry box
        self.entry = tk.Entry(
            root, font=("Helvetica", 14),
            width=10, justify="center", bd=2, relief="groove"
        )
        self.entry.pack(pady=10)
        self.entry.focus()

        # Guess button
        self.guess_button = tk.Button(
            root, text="Guess 🎲",
            command=self.check_guess,
            font=("Helvetica", 12, "bold"),
            bg="#4caf50", fg="white",
            padx=10, pady=5,
            activebackground="#45a049",
            relief="raised", bd=3
        )
        self.guess_button.pack()

        # Feedback label
        self.feedback_label = tk.Label(
            root, text="", font=("Helvetica", 12),
            bg="#f0f8ff", fg="#d2691e"
        )
        self.feedback_label.pack(pady=15)

    def check_guess(self):
        try:
            guess = int(self.entry.get())
        except ValueError:
            messagebox.showerror("Invalid input", "❌ Please enter a valid number.")
            return

        self.attempts += 1

        if guess < self.secret_number:
            self.feedback_label.config(text="⬇ Too low! Try again.")
        elif guess > self.secret_number:
            self.feedback_label.config(text="⬆ Too high! Try again.")
        else:
            messagebox.showinfo("🎉 You did it!",
                                f"✅ Correct! You guessed it in {self.attempts} tries.")
            self.root.destroy()  # Close window on success

        self.entry.delete(0, tk.END)

# ✅ Corrected this line too
if __name__ == "__main__":
    root = tk.Tk()
    game = GuessingGameGUI(root)
    root.mainloop()
