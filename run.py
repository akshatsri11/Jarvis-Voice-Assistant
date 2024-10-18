# To start Jarvis
import multiprocessing
import subprocess


def startJarvis():
    print("Jarvis is activated")
    from main import start
    start()

# To run Hot Word
def listenHotWords():
    print("Hot Word is activated")
    from engine.features import hotword
    hotword()

# Start both processes
if __name__ == "__main__":
    p1 = multiprocessing.Process(target=startJarvis)
    p2 = multiprocessing.Process(target=listenHotWords)
    p1.start()
    subprocess.call([r'device.bat'])
    p2.start()    
    p1.join()

    if p2.is_alive():
        p2.terminate()
        p2.join()

    print("system stop")