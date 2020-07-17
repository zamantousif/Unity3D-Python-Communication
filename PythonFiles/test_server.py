import time
import json
import zmq

# create zmq context and bind socket to port
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:9999")

while True:
    # Wait for the next request from client
    message = socket.recv()
    print("Received request: %s" % message)

    # create a Python dictionary to be serialized and sent
    data = {"name":"state", "timestep":1, "p1_villager_health":100, "p1_knight_health":50, "p1_archer_health":20.25, \
            "p2_tower1_health":10.5, "p2_tower2_health":27.75, "p1_stone":400, "p1_castle_build":"False"}

    json_data = json.dumps(data, indent = 4)
    socket.send_string("%s" % (json_data))
    