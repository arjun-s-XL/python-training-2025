import threading
def print_numbers():
    for i in range(5):
        print("NUmbers:",i)
thread=threading.Thread(target=print_numbers)
thread.start()
thread.join()