from unittest import TestSuite

from adapter    import adapter_suite
from device     import device_suite
from exchange   import exchange_suite
from hub        import hub_suite

unittest.TestSuite([
    adapter_suite(),
    device_suite(),
    exchange_suite(),
    hub_suite()
]).run({})

