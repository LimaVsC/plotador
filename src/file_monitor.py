import time
import threading
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os


class MyHandler(FileSystemEventHandler):
    def __init__(self, path, on_change):
        super().__init__()
        self.path = path
        self.on_change = on_change
        self.last_mtime = os.path.getmtime(path)

    def on_modified(self, event):
        new_mtime = os.path.getmtime(self.path)
        if new_mtime != self.last_mtime:
            self.last_mtime = new_mtime
            print("Arquivo modificado!")
            self.on_change()


class Monitor:
    def __init__(self, path, name, on_change):
        self.path = path
        self.name = name
        self.on_change = on_change
        self.observer = Observer()
        self.thread = threading.Thread(target=self._run, daemon=True)

    def _run(self):
        handler = MyHandler(self.path, self.on_change)
        self.observer.schedule(handler,
                               path=os.path.dirname(self.path)
                               if self.path != "." else ".",
                               recursive=False)
        self.observer.start()
        while self.observer.is_alive():
            time.sleep(1)

    def start(self):
        if not self.thread.is_alive():
            print("Começando monitoramento")
            self.thread = threading.Thread(target=self._run, daemon=True)
            self.thread.start()

    def stop(self):
        print("Parando monitoramento...")
        if self.observer.is_alive():
            self.observer.stop()
            self.observer.join()
