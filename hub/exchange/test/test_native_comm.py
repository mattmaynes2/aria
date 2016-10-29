from unittest import TestCase
import socket
import native_comm
import message
import uuid


class NativeCommTest (TestCase):

    def setUp (self):
        self.comm = native_comm.NativeComm

    def test_send(self):
        self.comm._addresses[uuid.uuid4().bytes]=('127.0.0.1','5000')
        msg = message.Message(1,{'action':'status'},uuid.uuid4().bytes,uuid.uuid4().bytes)
        self.comm.send(msg)

        UDP_IP = "127.0.0.1"
        UDP_PORT = 5000
        sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        sock.bind((UDP_IP, UDP_PORT))
        data, addr = sock.recvfrom(1024)

        receivedMsg = message.Message.decode(data)

        self.assertTrue( 'action' in receivedMsg.data)
        self.assertEquals(receivedMsg.data['action'],'status')
