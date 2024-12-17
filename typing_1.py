import pyautogui
import time

def type_string_at_60_wpm(string):
   
    delay_between_chars = 0.2

    time.sleep(5)
    for char in string:
        pyautogui.typewrite(char)
        time.sleep(delay_between_chars)

if __name__ == "__main__":
    text = "Hello, this is a test string! Make sure your Google Docs window is active."
    type_string_at_60_wpm(text)