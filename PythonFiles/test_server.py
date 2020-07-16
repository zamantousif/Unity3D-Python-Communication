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

    # Do some 'work'
    # time.sleep(1)

    # create Python objects to be serialized and sent
    # dict
    player_dict = {"p1": "player1", "p2": "player2"}
    # list
    p1_list = ["archer", "knight", "villager"]
    # tuple
    p2_tuple = ("tower1", "tower2")
    # string
    actions_str = "move" + " " + "suicide"
    # numbers
    states_num = 1000

    # serialize to JSON prior to sending
    json_dict = json.dumps(player_dict)
    json_list = json.dumps(p1_list)
    json_tuple = json.dumps(p2_tuple)
    json_str = json.dumps(actions_str)
    json_num = json.dumps(states_num)

    # print(json_dict)
    # print(json_list)
    # print(json_tuple)
    # print(json_str)
    # print(json_num)

    # socket.send(b"World")
    socket.send_string("%s" % (json_dict))
    