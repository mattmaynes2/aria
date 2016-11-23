import socket
from adapter import Message
import uuid
sock= socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
uid=uuid.uuid4().bytes
msg=Message(1,data={'action':'status'},sender=uid,receiver=Message.DEFAULT_ADDRESS)

sock.sendto(msg.encode(),('localhost',7600))

msg=Message(2,data={'action':'status'},sender=uid,receiver=uuid.UUID('d0fb74f0-994f-49bc-94f3-c24b11a6edd3').bytes)

sock.sendto(msg.encode(),('localhost',7600))
print(Message.decode(sock.recv(4096)))



