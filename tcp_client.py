import socket

def start_tcp_client():
    try:
        client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        
        client_socket.connect(('localhost',8080))
        
        message = 'Good night'
        client_socket.sendall(message.encode())
        
        data = client_socket.recv(1024)
        print("Recieved from server:",data.decode())       
    except Exception as e:
        print(f'error {e}')
        
    finally:
        client_socket.close()
        
        
if __name__ == "__main__":
    start_tcp_client()