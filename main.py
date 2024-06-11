import random
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk
import numpy as np
from collections import Counter
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def run_simulation():
    trialResults = {key: 0 for key in range(11)}
    simulationTrials = int(entry.get())

    for i in range(simulationTrials):
        envelopes = list(range(1, 11))
        random.shuffle(envelopes)
        correctChoices = 0

        for j in range(len(envelopes)):
            guess = random.randint(1, len(envelopes))
            if guess == envelopes[j]:
                correctChoices += 1

        trialResults[correctChoices] += 1

    x = list(range(11))
    y = [trialResults[i] for i in range(11)]

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(x, y)
    ax.set_xlabel('Number of Correct Choices')
    ax.set_ylabel('Frequency')
    ax.set_title('Simulation of Correct Choices in Trials')

    # Reset display
    for widget in display_frame.winfo_children():
        widget.destroy()

    canvas = FigureCanvasTkAgg(fig, master=display_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    
    choices = []
    for key, value in trialResults.items():
        choices.extend([key] * value)
    mean = np.mean(choices)
    median = np.median(choices)
    mode = Counter(choices).most_common(1)[0][0]
    data_range = np.ptp(choices)

    stats_text = f"Mean: {mean:.2f}\nMedian: {median:.2f}\nMode: {mode}\nRange: {data_range}"
    stats_label.config(text=stats_text)
    

window = tk.Tk()
window.title("Envelope Simulation")
window.geometry("800x600")

style = ttk.Style()
style.configure("TButton", borderwidth=5, relief="solid", foreground="green", font=("Arial", 14))

input_frame = tk.Frame(window)
input_frame.pack(pady=20)

label = tk.Label(input_frame, text="Number of trials:", font=("Arial", 14))
label.pack(side=tk.LEFT, padx=5, pady=5)

entry = tk.Entry(input_frame)
entry.pack(side=tk.LEFT, padx=5, pady=5)

button = ttk.Button(input_frame, text="Run Simulation", command=run_simulation, style="TButton")
button.pack(side=tk.LEFT, padx=5, pady=5)

stats_label = tk.Label(input_frame, text="", font=("Arial", 14), justify=tk.LEFT)
stats_label.pack(side=tk.LEFT, padx=20, pady=5)

display_frame = tk.Frame(window)
display_frame.pack(pady=20, fill=tk.BOTH, expand=True)

display_frame.columnconfigure(0, weight=1)
display_frame.rowconfigure(0, weight=1)

window.mainloop()
