import RPi.GPIO as GPIO
import sys
from datetime import datetime
from time import sleep

# GPIO SETUP
# output pin definitions
ledMinMod0 = [0, 1, 2, 3]
ledMinMod1 = [0, 1, 2, 3]
ledHourMod0 = [0, 1, 2, 3]
ledHourMod1 = [0, 1, 2, 3]
ledPins = [ledMinMod0, ledMinMod1, ledHourMod0, ledHourMod1]

# suppress warnings
GPIO.setwarnings(False)

# use GPIO pin number
GPIO.setMode(GPIO.BCM)


# set pins as outputs
for mod in ledPins:
    for pin in mod:
        GPIO.setup(pin, GPIO.OUT)

# set truth table for mux
truthTable = [
    "0000",
    "0001",
    "0010",
    "0011",
    "0100",
    "0101",
    "0110",
    "0111",
    "1000",
    "1001",
    "1010",
    "1011",
    "1100",
    "1101",
    "1110",
    "1111",
]

# "MAIN"
# run until stopped by CTRL+C command
while True:
    # use now() from datetime to get current local time
    timeNow = datetime.now()

    # convert previous instance of datetime object to formatted string hh:mm
    currentTime = timeNow.strftime("%H:%M")
    print(currentTime)

    # split the current_time String into hours and minutes
    currentTimeSplit = currentTime.split(':')

    # store the hours and minutes in their respective vars for easier tracking
    currentTimeHour = currentTimeSplit[0]
    currentTimeMinute = currentTimeSplit[1]

    # get the least and most significant values of the minutes and store those in their own vars
    currentTimeMinuteOnes = currentTimeMinute[1]
    currentTimeMinuteTens = currentTimeMinute[0]

    # get the least and most significant values of the hours and store those in their own vars
    currentTimeHourOnes = currentTimeHour[1]
    currentTimeHourTens = currentTimeHour[0]

    currentTimeArray = [currentTimeMinuteOnes, currentTimeMinuteTens, currentTimeHourOnes, currentTimeHourTens]

    # find binary equivalent of each time value in truth_table
    for i in range(len(currentTimeArray)):
        switcher = {
            0: truthTable[0],
            1: truthTable[1],
            2: truthTable[2],
            3: truthTable[3],
            4: truthTable[4],
            5: truthTable[5],
            6: truthTable[6],
            7: truthTable[7],
            8: truthTable[8],
            9: truthTable[9],
            10: truthTable[10],
            11: truthTable[11],
            12: truthTable[12],
            13: truthTable[13],
            14: truthTable[14],
            15: truthTable[15]
        }
        # store truth_table value in muxPinSelection
        muxPinSelection = switcher.get(int(currentTimeArray[i]))

        # handle number formatting errors
        if muxPinSelection is None:
            sys.exit("Error: Number not in Truth Table!")

        # change the bit values of each pin of each module mux to choose the appropriate mux pin address
        for j in range(len(muxPinSelection)):
            ledPins[i][j] = int(muxPinSelection[j])

    # output pin bit values to GPIO
    for mod in ledPins:
        for pin in mod:
            if pin == 0:
                GPIO.output(pin, GPIO.LOW)
            elif pin == 1:
                GPIO.output(pin, GPIO.HIGH)
            else:
                sys.exit("Error: Incorrect bit format!")

    # limit pulling local time to 1 Hz
    sleep(1)
