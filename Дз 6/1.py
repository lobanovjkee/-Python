import time
import os


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


class TrafficLight:
    __color = "red"

    def running(self):
        print("\033[31m {}".format(TrafficLight.__color))
        TrafficLight.__color = "yellow"
        time.sleep(7)
        cls()
        print("\033[6m\033[33m {}".format(TrafficLight.__color))
        TrafficLight.__color = 'green'
        time.sleep(2)
        cls()
        print("\033[32m {}".format(TrafficLight.__color))
        TrafficLight.__color = 'yellow'
        time.sleep(7)
        cls()
        print("\033[6m\033[33m {}".format(TrafficLight.__color))
        TrafficLight.__color = 'red'
        time.sleep(2)
        cls()


while True:
    TrafficLight().running()
