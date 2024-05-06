import pyautogui


# source venv/bin/activate
# Не работает без дополнительных программ
# sudo apt-get install python3-tk python3-dev
# sudo apt install gnome-screenshot

pyautogui.screenshot(
    'path_to_file.jpg',
    region=(0,0,300,400)

)