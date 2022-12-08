import initialization
import random
import time
import pynput as pyn
import pyautogui as gui
import barnum

f = open('directions.txt', 'r')
directions = f.read()
f.close()

user_input = input(directions).lower()

if user_input == 'q':
    quit()

clicks = ['name text box', 'email address text box',
          'location of show text box', 'other information text box', 'submit button', 'browser url box']

coordinates = []

if user_input:
    print('\nclick on the report button')


def on_click(x, y, button, pressed):
    if pressed:
        coordinates.append((x, y))
        if len(coordinates) < 7:
            print(f'now click {clicks[len(coordinates) - 1]}')
        else:
            print(
                'you now have 20 seconds to press enter to refresh the page before the program begins')
            time.sleep(20)
            global submit
            submit = True
            return False


with pyn.mouse.Listener(
        on_click=on_click) as listener:
    listener.join()

reports = 0


def name():
    name = barnum.create_name()
    return f'{name[0]} {name[1]}'


def location():
    location = barnum.create_city_state_zip()
    return f'{location[1]} {location[2]}'


events = ['drag queen story hour', 'drag queen brunch',
          'pole dancing', 'drag queen karaoke', 'drag queen tea party']

report_button = coordinates[0]

name_box = coordinates[1]

email_box = coordinates[2]

location_box = coordinates[3]

info_box = coordinates[4]

submit_button = coordinates[5]

url_box = coordinates[6]

while submit:
    for target in coordinates:
        gui.moveTo(target[0], target[1], 0.5)
        time.sleep(3)
        gui.click()
        time.sleep(0.5)
# 0.5 seconds between the click and any typing to ensure the steps remain in order in case of a short client lag
        if target == name_box:
            gui.write(name())
            time.sleep(3)
        elif target == email_box:
            gui.write(barnum.create_email())
            time.sleep(3)
        elif target == location_box:
            gui.write(location())
            time.sleep(3)
        elif target == info_box:
            gui.write(
                f'{events[random.randint(0, 4)]} at {barnum.create_street()}')
            time.sleep(3)
        elif target == submit_button:
            reports += 1
            print(f'{reports} reports submitted')
        elif target == url_box:
            gui.press("enter")
            time.sleep(5)
