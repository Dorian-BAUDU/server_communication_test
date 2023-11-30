import socket
import numpy as np

def run_server():
    print("starting server")

    test = "string of test"
    test_2 = np.array(([2, 7, 'test char',np.pi]))

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_ip = "127.0.0.17"
    server_port = 7777
    server.bind((server_ip, server_port))

    # listen for incoming connections
    server.listen(0)
    print(f"Listening on {server_ip}:{server_port}")
    client_socket, client_address = server.accept()
    print(f"Accepted connection from {client_address[0]}:{client_address[1]}")

    while True:
        request = client_socket.recv(2048)
        request = request.decode("utf-8") #convert bytes to string

        if request.lower() == 'close':
            client_socket.send("closed".encode("utf-8"))
            break
        
        if request.lower() == 'test':
            print("test receive")

        print(f"Receive : {request}")

        response = "accepted".encode("utf-8")
        variable = test_2
        client_socket.send(response)
        client_socket.send(variable)

    client_socket.close()
    print("Connection to client shut down.")
    server.close()

if __name__ == '__main__':
    run_server()
        