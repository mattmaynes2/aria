from unittest import TestCase
import socket
import native_comm
import message
import uuid
from threading import Thread

class NativeCommTest (TestCase):

    def setUp (self):
        self.comm = native_comm.NativeComm()

    def test_receive(self):
        self.comm.setup(self)
        #TODO delete next line
        self.comm.active=True
        self.comm.start()
        msg = message.Message(1,{'action':'status'},uuid.uuid4().bytes,uuid.uuid4().bytes)

        sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        sock.sendto(msg.encode(),("127.0.0.1",7600))
        sock.close()


    def message(self,msg):
        print ('This ran')
        self.assertTrue('action' in msg.data)
        self.assertEqual(msg.data['action'], 'status')
        self.comm.teardown()
    """
    def receiveMessage(self):
        UDP_IP = "127.0.0.1"
        UDP_PORT = 5000
        sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        sock.bind((UDP_IP, UDP_PORT))
        data, addr = sock.recvfrom(1024)

        receivedMsg = message.Message.decode(data)

        self.assertTrue( 'action' in receivedMsg.data)
        self.assertEqual(receivedMsg.data['action'],'status')

    def test_send(self):
        msg = message.Message(1,{'action':'status'},uuid.uuid4().bytes,uuid.uuid4().bytes)
        Thread(target=self.receiveMessage).start()
        sleep
        self.comm.send(msg, ("127.0.0.1",5000))
        self.assertTrue(True == False)
    """
