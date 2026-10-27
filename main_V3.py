import time
import random
import platform
import sys


def wait_for_y(prompt="Press 'y' to continue: "):
    os_name = platform.system()

    
    if os_name == "Windows":
        try:
            import msvcrt
            print(prompt)
            while True:
                key = msvcrt.getch()
                if key.decode("utf-8", errors="ignore").lower() == "y":
                    return
        except Exception:
            pass

    
    if hasattr(sys.stdin, "isatty") and sys.stdin.isatty():
        if os_name in ("Linux", "Darwin"):
            try:
                import tty
                import termios
                print(prompt)
                fd = sys.stdin.fileno()
                old_settings = termios.tcgetattr(fd)

                try:
                    tty.setcbreak(fd)
                    while True:
                        ch = sys.stdin.read(1)
                        if ch.lower() == "y":
                            return
                finally:
                    termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
            except Exception:
                pass

    
    while True:
        response = input(prompt).strip().lower()
        if response == "y":
            return
        print("Please press 'y' to continue.")


wait_for_y()


print("Your pc ran into an error we will repair your computer for you. Your computer may restart. [error code 1.3621.34]")
print("========================================================================")
wait_for_y()
time.sleep(2)

print("loading 5% [-]")
time.sleep(random.uniform(1, 3))
print("loading 10% [/]")
time.sleep(random.uniform(1, 3))
print("loading 15% [|]")
time.sleep(random.uniform(1, 3))
print("loading 20% [-]")
time.sleep(random.uniform(1, 3))
print("loading 25% [/]")
time.sleep(random.uniform(1, 3))
print("loading 30% [|]")
time.sleep(random.uniform(1, 3))
print("loading 35% [-]")
time.sleep(random.uniform(1, 3))
print("loading 40% [/]")
time.sleep(random.uniform(1, 3))
print("loading 45% [|]")
time.sleep(random.uniform(1, 3))
print("loading 50% [-]")
time.sleep(random.uniform(1, 3))
print("loading 55% [/]")
time.sleep(random.uniform(1, 3))
print("loading 60% [|]")
time.sleep(random.uniform(1, 3))
print("loading 65% [-]")
time.sleep(random.uniform(1, 3))
print("loading 70% [/]")
time.sleep(random.uniform(1, 3))
print("loading 75% [|]")
time.sleep(random.uniform(1, 3))
print("loading 80% [-]")
time.sleep(random.uniform(1, 3))
print("loading 85% [/]")
time.sleep(random.uniform(1, 3))
print("loading 90% [|]")
time.sleep(random.uniform(1, 3))
print("loading 95% [-]")
time.sleep(1)
print("loading 100% [/]")
time.sleep(1)
print("loaded :D")
print("-------------------------------------------------------------------------------------")

wait_for_y()
print("testing WIFI")
time.sleep(0.1)
print("connecting to WIFI")
time.sleep(1.3)
print("~~")
time.sleep(0.2)
print("~~~~")
time.sleep(2.1)
print("~~~~~~")
time.sleep(0.1)
print("~~~~~~~~~~")
time.sleep(1.1)
print("~~~~~~~~~~~")
time.sleep(2.1)
print("connected to WIFI")
time.sleep(random.uniform(0.1, 1))
print("testing WIFI speed and pinging server")
print("-------------------------------------------------------------------------------------")
time.sleep(random.uniform(1, 3))
print("testing speed")
time.sleep(random.uniform(0.1, 1))
print("Wifi speed ")
print(random.uniform(10, 100))
time.sleep(random.uniform(0.1, 2))
print("Wifi")
print("OK")
print("------------------------------------------------------------------------------------")

wait_for_y()
time.sleep(1)
print("testing RAM in 3 sec")
time.sleep(0.1)
print(".")
print("3")
time.sleep(1)
print(".")
print("2")
time.sleep(1)
print(".")
print("1")
time.sleep(1)
print("Testing Ram %")
for i in range(5):
    print(random.uniform(10, 100))
    time.sleep(random.uniform(0.1, 1))
print("RAM usage ok")
print("--------------------------------------------------------------------------------------")

time.sleep(1)
wait_for_y()
print("Testing CPU in 3 sec")
time.sleep(0.1)
print(".")
print("3")
time.sleep(1)
print(".")
print("2")
time.sleep(1)
print(".")
print("1")
time.sleep(1)
for i in range(5):
    print(random.uniform(20, 100))
    time.sleep(random.uniform(0.1, 1))
print("CPU usage ok")
print("---------------------------------------------------------------------------------------")

time.sleep(0.9)
wait_for_y()
print("testing storage")
print("storage type detected")
time.sleep(0.1)
print("SSD")
print("Testing for speed and virus on SSD in 3 sec")
time.sleep(0.1)
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)
print("Testing speed")
for i in range(5):
    print(random.uniform(500, 1000))
    time.sleep(random.uniform(0.1, 1))
print("speed ok")
time.sleep(0.2)

wait_for_y()
print("Testing for Virus")
time.sleep(0.1)
print("This may take a while")
for i in range(30):
    print("[/]")
    time.sleep(0.3)
    print("[-]")
    time.sleep(0.3)
    print("[|]")
print("Getting results")
time.sleep(1)
print("C drive ok")
print("Downloads ok, Desktop ok, Piches ok, Documents ok")
time.sleep(0.3)
print("SSD ok")
for i in range(30):
    print("[/]")
    time.sleep(0.3)
    print("[-]")
    time.sleep(0.3)
    print("[|]")
time.sleep(1)
print("--------------------------------------------------------------------------------------")

wait_for_y()
print("Testing GPU in 3 sec")
time.sleep(0.1)
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)
for i in range(5):
    print(random.uniform(20, 100))
    time.sleep(random.uniform(0.1, 1))
time.sleep(0.8)
print("Tested GPU stress test")
time.sleep(1)
print("---------------------------------------------------------------------------------------")

wait_for_y("Press 'y' to restart into os: ")
print("Your computer will now restart and has passed all the tests")
for i in range(30):
    print("[/]")
    time.sleep(0.3)
    print("[-]")
    time.sleep(0.3)
    print("[|]")
print(".................................................................................................................................")
print(".................................................................................................................................")
print(".................................................................................................................................")
print(".................................................................................................................................")
