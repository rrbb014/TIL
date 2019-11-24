import threading
import time

import cotyledon
import etcd3

class PrinterService(cotyledon.Service):
    name = "printer"

    def __init__(self, worker_id):
        super(PrinterService, self).__init__(worker_id)
        self._shutdown = threading.Event()
        self.client = etcd3.client()

    def run(self):
        while not self._shutdown.is_set():
            with self.client.lock('print'):
                print("I'm %s and I'm the only one printing" % self.worker_id)
                time.sleep(1)

    def terminate(self):
        self._shutdown.set()

# create manager
manager = cotyledon.ServiceManager()

# Add printerservice 4 
manager.add(PrinterService, 4)

# all run
manager.run()
