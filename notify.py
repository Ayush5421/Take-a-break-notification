from plyer import notification
import time

if __name__ == '__main__':
    while True:
        notification.notify(
            title="Alarm Clock",
            message="wake up at 7'o clock",
            timeout=5)
        time.sleep(20)
