#!/usr/bin/python3

import sys, getopt
import subprocess

def main(argv):
    direction = ""
    amount = ""

    try:
        opts, args = getopt.getopt(argv, "d:a:", ["direction=", "amount="])
    except getopt.GetoptError:
        print ('test.py -d <up|down> -a <amount>')
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print ('test.py -d <up|down> -a <amount>')
            sys.exit()
        elif opt in ("-d", "--direction"):
            direction = arg
        elif opt in ("-a", "--amount"):
            amount = arg

    change_brightness(direction, amount)

def change_brightness(direction, amount):
    if not amount or amount == "":
        amount = 12

    amount = int(amount)

    current_brightness, error = run_bash_command("cat /sys/class/backlight/amdgpu_bl0/brightness")
    current_brightness = int(current_brightness)

    if direction == "up":
        result = current_brightness + amount
    else:
        result = current_brightness - amount

    if result > 255:
        result = 255
    elif result < 0:
        result = 0

    command = "/bin/echo \"" + str(int(result)) + "\" >> /sys/class/backlight/amdgpu_bl0/brightness\n"
    output, error = run_bash_command(command, True, False)

def run_bash_command(command, shell=False, split=True):
    if split:
        command = command.split()

    print(command)
    process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=shell, text=True, universal_newlines=True)
    output, error = process.communicate()

    return output, error

if __name__ == "__main__":
    main(sys.argv[1:])