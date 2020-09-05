# pyalarm

This is a little python project.It is a basic alarm clock created with python.

## Features

- You can set basic alarm here.
- The alarm will rang untill you will manually turn off the alarm.
- This is a terminal bassed application.

## Requirements

- You have to have python3.7.x+ installed in your computer.
  \*You have to install playsound python library to use pyalarm.you can install playaudio using pip-pip insall playsound.

## Documentation

Here I've used python builtin datetime module to get the current time from user computer.Then I took a input from user(alarm time).Then I convert the user input time into international timezone(24 hours).Then I asigned a while loop to constantly getting time from computer and match with the user input.
When the user input and computer's current time will match,it will pass the audio file in playsound library which will start playsing the song.
The song will play into an infinite loop so that user needs to manually kill the software.As we know,an alarm clock's job is to awake or remind the user that it is the time.

## Developer info

#### Developer: Sonet Adhikary

#### Contact: sonet.ad101@gmail.com
