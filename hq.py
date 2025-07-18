import socket
import sys
import random
def handle_client(conn):
    while True:
        msg = conn.recv(64).decode('utf-8')
        if msg:
            print(f"[RECEIVED] {msg}")

            # Simple validation for the received message
            if msg.startswith('POST') and msg.endswith('\n'):
                # Process the message (omitted for simplicity)
                print("[PROCESSING] Storing data...")

                # Send ACKNOWLEDGED message
                if random.random() > PFAIL :
                		conn.sendall(b'ACKNOWLEDGED\n')
            else:
                # Send ERROR_001 message in case of any issues
                conn.sendall(b'ERROR_001\n')

            # Close the connection after sending the reply
            conn.close()
            break

def start_server():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    
    while True:
        conn, addr = server.accept()
        handle_client(conn)

# Server configuration
PORT = 12346#int(sys.argv[1])
PFAIL = 0.0#float(sys.argv[2])
SERVER = '127.0.0.1'
ADDR = (SERVER, PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

print("[STARTING] Server is starting...")
start_server()
