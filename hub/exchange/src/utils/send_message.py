import socket
from adapter import Message
import uuid
sock= socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
uuid=uuid.uuid4().bytes
msg=Message(1,data={'action':'status'},sender=uuid,receiver=Message.DEFAULT_ADDRESS)

sock.sendto(msg.encode(),('localhost',7600))

msg=Message(2,data={'action':'status'},sender=uuid,receiver=b'`\x99Di\n\x84O\x91\x9dl\xe6\xd8\xad\xe4>\xc9')

sock.sendto(msg.encode(),('localhost',7600))
print(Message.decode(sock.recv(4096)))



