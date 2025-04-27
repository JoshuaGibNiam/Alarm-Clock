# Alarm Clock App (Python, Tkinter + pygame)

This is a simple alarm clock built with Python, using:

- tkinter (with ttkbootstrap for better GUI styling)
- pygame (for playing alarm sounds)

It allows you to:

- Set a custom alarm hour and minute.
- Get notified when the alarm time matches the current time.
- Choose to snooze the alarm (adds 5 minutes).
- Display the current time updating every second.

## Features

- Easy to use interface with a dark theme ("darkly" from ttkbootstrap).
- Current time (hours, minutes, seconds) updated live.
- Custom alarm time — set hours and minutes separately.
- Alarm sound loops when it's time.
- Snooze option — adds 5 minutes to your alarm if you click "Yes".
- Stop option — stops the alarm if you click "No".

## How to Run

1. Install required modules:
    
    - `pip install pygame`
    - `pip install ttkbootstrap`

2. Ensure an audio file named `clock-alarm-8761.mp3` is placed in the same folder as the script.

3. Run the program:
    - `python alarm_clock.py`

## Files and Functions

- AlarmClock class:
  - `__init__()`: Sets up the GUI, initializes pygame, and loads the alarm sound.
  - `sethour()`: Sets the alarm hour.
  - `setmin()`: Sets the alarm minute.
  - `setalarm()`: Updates and displays the alarm time.
  - `checkalarm()`: Checks every second if the current time matches the alarm time.
    - Plays sound when alarm time is reached.
    - Offers a Yes/No pop-up to snooze or stop.
  - `updatetime()`: Updates the displayed current time every second.

## Future Improvements

- Allow setting multiple alarms.
- Add custom snooze duration.
- Add AM/PM format support.
- Allow users to select alarm sound files.

## Credits

- GUI styled with ttkbootstrap.
- Sound playback with pygame.
- Alarm sound from public free resources.