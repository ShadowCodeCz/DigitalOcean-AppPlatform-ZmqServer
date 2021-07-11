import time
import zmq
import logging

logging.basicConfig(level=logging.DEBUG)

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:55555")

logging.debug("[ZMQ SERVER] Start")

i = 0

while True:
    logging.debug(f"[ZMQ SERVER] Waiting for request {i}")
    response = socket.recv_string()
    logging.debug(f"[ZMQ SERVER] Received message '{response}'")
    time.sleep(3)
    logging.debug(f"[ZMQ SERVER] Sending response {i}")
    socket.send_string("DO & App Platform & FLASK & ZMQ")
    i += 1

