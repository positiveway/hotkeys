#!/usr/bin/sudo /home/user/PycharmProjects/hotkeys/venv/bin/python
import os

os.environ["PYNPUT_BACKEND_KEYBOARD"] = "uinput"
os.environ["PYNPUT_BACKEND_MOUSE"] = "dummy"
backend_name = os.environ.get('PYNPUT_BACKEND_KEYBOARD', None)
print(backend_name)

from pynput import keyboard


def on_press(key):
    try:
        print('alphanumeric key {0} pressed'.format(
            key.char))
    except AttributeError:
        print('special key {0} pressed'.format(
            key))


def on_release(key):
    print('{0} released'.format(
        key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False


if __name__ == '__main__':
    # Collect events until released
    with keyboard.Listener(
            on_press=on_press,
            on_release=on_release,
            suppress=True,
    ) as listener:
        try:
            listener.join()
        except Exception as e:
            raise e
