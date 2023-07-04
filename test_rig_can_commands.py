import time
import threading
import can

class TestRig:
    def __init__(self):
        self.bus = can.interface.Bus()
        self.data = None
        self.data_lock = threading.Lock()

    def Start_Operation(self):
        # Start any necessary background processes or threads
        threading.Thread(target=self._simulate_data_reception).start()

    def Stop_Operation(self):
        # Stop any background processes or threads
        self.bus.shutdown()
        
    def Init_Payload(self):
            # Stop any background processes or threads
            
        self.bus.shutdown()
        
    def start_logging(self):
            # Stop any background processes or threads
        self.bus.shutdown()
        
    def send_data(self, data):
        with self.data_lock:
            self.data = data
            # Send the data via CAN bus
            message = can.Message(data=data)
            self.bus.send(message)

    def get_data(self):
        with self.data_lock:
            return self.data

    def _simulate_data_reception(self):
        while True:
            # Receive data from the CAN bus
            message = self.bus.recv(timeout=1.0)
            if message is not None:
                with self.data_lock:
                    self.data = message.data

            # Sleep for a certain duration before the next iteration
            time.sleep(0.1)

# Usage example
test_rig = TestRig()
test_rig.start()

# Send data
data_to_send = [1, 2, 3, 4]
test_rig.send_data(data_to_send)

# Receive data
received_data = test_rig.get_data()
if received_data is not None:
    # Process the received data
    # Stop the test rig
    test_rig.stop()
