import zmq

context = zmq.Context()

print("Connecting to the server..")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:9999")

for request in range(10):
    print("Sending request %s ..." % request)
    socket.send(b"Hello")

    # Receive the reply
    message = socket.recv()
    print("Received from server %s [ %s ]" % (request, message))

