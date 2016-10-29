from threading import Thread

class Adapter (Thread):
    """Adapters convert from internal message structure to external device protocols

    Adapters are responsible for implementing this all functions in the parent adapter class and
    communicating to different specific protocols. It is the responsibility of the adapter to
    translate from internal universal unique identifier to physical addresses and communicate to
    network devices. Each adapter is responsible for the reliable transmission for messages across
    the network in any given format.

    Each adapter sends and receives on an independent thread. The thread will be setup and run
    by an external exchange controller. The adapter class should not execute itself.

    Adapters require a delegate to notify whenever a message is received from the network. This
    patter allows the Adapter to provide asynchronous service for any listeners. Adapter delegates
    are required to provide the following interface methods

        discovered (device: Device)
            A new device has been discovered and should be added to the system.

        received (message: Message)
            A message has been received on the system and should be processed.

    Attributes:
        active (boolean): If this adapter is currently online and transmitting data
        delegate (obj): Delegate that implements adapter delegate methods
    """

    def __init__ (self):
        super().__init__()
        self.active = False
        self._delegates = []

    def add_delegate (self, delegate):
        """Adds a delegate to listen to this adapter's notifications

        Arguments:
            delegate (Delegate): The delegate to notify

        Returns:
            True if the delegate was not already added, False otherwise
        """
        if delegate in self._delegates:
            return False
        self._delegates.append(delegate)
        return True

    def notify (self, event, data):
        """Notifies all delegates of the given event with the supplied data

        Arguments:
            event (str): Name of event to trigger
            data (obj): Data to pass to delegate
        """
        for delegate in self._delegates:
            getattr(delegate, event)(data)

    def setup (self):
        """Setup the adapter for communication across the network

        This method should allocate any physical devices that are required to send messages
        through the network. After setup the adapter should be in an active state.

        Returns:
            True if successful, False otherwise.
        """
        self.active     = True
        return True

    def discover (self):
        """Send a discovery message request across the network to find any new devices

        Returns:
            True if successful, False otherwise.
        """
        pass

    def send (self, message):
        """Sends a message to a receiver using this adapter's protocol

        Arguments:
            message (exchange.Message): Internal exchange message to send

        Returns:
            True if successful, False otherwise
        """
        pass

    def teardown (self):
        """Release any allocated resources for this adapter

        Returns:
            True if successful, False otherwise.
        """
        self.active = False
        return True

    def receive (self):
        """Receives a message from the network, translates it and passes it to the adapter delegate

        Returns
            True if successful, False otherwise.
        """
        pass

    def run (self):
        """Runs the adapter in a loop while it is active

        Returns
            True on normal termination, False otherwise.
        """
        self.setup()
        while (self.active):
            self.receive()
        return True
