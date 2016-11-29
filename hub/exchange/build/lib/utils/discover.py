import socket
from ipc import Message
import uuid
sock= socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
uuid=uuid.uuid4().bytes
msg=Message(1,data={'action':'status'},sender=uuid,receiver=Message.DEFAULT_ADDRESS)

sock.sendto(msg.encode(),('localhost',7600))

msg=Message(2,data={'action':'discover'},sender=uuid,receiver=Message.DEFAULT_ADDRESS)

sock.sendto(msg.encode(),('localhost',7600))
print(Message.decode(sock.recv(4096)))



