# To start Jarvis
import multiprocessing


def startJarvis():
    print("process 1 is running")
    from main import start
    start()

# To run Hot Word
def listenHotWords():
    print("process 2 is running")
    from engine.features import hotword
    hotword()

# Start both processes
if __name__ == "__main__":
    p1 = multiprocessing.Process(target=startJarvis)
    p2 = multiprocessing.Process(target=listenHotWords)
    p1.start()
    p2.start()
    p1.join()

    if p2.is_alive():
        p2.terminate()
        p2.join()

    print("system stop")