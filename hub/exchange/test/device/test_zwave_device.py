from device.zwave_device import ZWaveDevice
from device.data_types import DataType
from unittest import TestCase
from unittest.mock import Mock
from unittest import mock
import uuid
import unittest

class ZWaveDeviceTest(TestCase):

    def setUp(self):
        self.mockNode = Mock()
        self.mockNode.get_values.return_value = {}
        self.mockNode.name = "testdevice"
        self.mockNode.product_name = "testproduct"
        self.mockNode.manufacturer_name = "unittest"
        self.mockNode.version = 1
        self.mockNode.location = ""

        self.mockValues = {}
        mockValueBrightness = Mock()
        mockValueBrightness.label = "Brightness"
        mockValueBrightness.type = "Byte"
        mockValueBrightness.command_class = 38
        mockValueBrightness.max = 255
        mockValueBrightness.min = 0
        mockValueBrightness.data = 10
        mockValueBrightness.is_read_only = False

        mockValueColour = Mock()
        mockValueColour.label = "Colour"
        mockValueColour.command_class = 51
        mockValueColour.is_read_only = False
        mockValueColour.type = "String"
        
        self.mockValues["Colour"] = mockValueColour
        self.mockValues["Brightness"] = mockValueBrightness
        self.mockNode.get_values.return_value = self.mockValues

    def test_device_has_correct_name(self):
        self.mockNode.name = "testdevice"
        device = ZWaveDevice(self.mockNode)
        self.assertEqual("testdevice", device.name)

    def test_device_uses_product_name_if_name_is_empty(self):
        self.mockNode.name = ""
        self.mockNode.product_name = "productname"
        device = ZWaveDevice(self.mockNode)
        self.assertEqual("productname", device.name)

    def test_device_version_is_correct(self):
        device = ZWaveDevice(self.mockNode)
        self.assertEqual("1", device.version)
    
    def test_device_builds_correct_device_type(self):
        device = ZWaveDevice(self.mockNode)
        deviceType = device.deviceType
        self.assertEqual("testproduct", deviceType.name)
        self.assertEqual("zwave", deviceType.protocol)
        self.assertEqual("unittest", deviceType.maker)
        brightnessAttribute = deviceType.getAttribute("Brightness")
        self.assertEqual(True, brightnessAttribute.isControllable)
        self.assertEqual("Brightness", brightnessAttribute.name)
        brightnessParameters = brightnessAttribute.parameters
        self.assertEqual("Brightness", brightnessParameters[0].name)
        self.assertEqual(0, brightnessParameters[0].min)
        self.assertEqual(99, brightnessParameters[0].max)
        self.assertEqual(None, brightnessParameters[0].step)
        self.assertEqual(10, brightnessParameters[0].value)
        self.assertEqual(DataType.Byte, brightnessParameters[0]._dataType)

    def test_device_parameter_max_is_99_for_byte_value_command_class_38(self):
        '''
        Explanation
        ZWave values with command class 38 (COMMAND_CLASS_SWITCH_MULTILEVEL) have unusual behaviour
        The max valaue is 255, however, values in the range 100-254 are invalid, which makes it 
        difficult to create a slider for the value. Solution is to make the max 99, as values in the
        range 0-99 are interpreted as a percentage by the device.

        See the Z-Wave Command Class Specification: 
        http://z-wave.sigmadesigns.com/wp-content/uploads/2016/08/SDS12657-12-Z-Wave-Command-Class-Specification-A-M.pdf
        '''
        device = ZWaveDevice(self.mockNode)
        deviceType = device.deviceType 
        brightnessAttribute = deviceType.getAttribute("Brightness")
        brightnessParameters = brightnessAttribute.parameters
        self.assertEqual(99, brightnessParameters[0].max)
        self.assertEqual(0, brightnessParameters[0].min)

    def test_attribute_type_is_color_for_command_class_color(self):
        '''
        Explanation
        After tests with a Z-wave RGB bulb, we discovered that the lightbulb reports the type of 
        its Colour value as a String. This needs to be translated to a type Color for our system, in
        order for the UI to display a colour picker, etc.
        '''
        
        device = ZWaveDevice(self.mockNode)
        deviceType = device.deviceType
        colourAttribute = deviceType.getAttribute("Colour")
        self.assertEqual(DataType.Color, colourAttribute.parameters[0].dataType)

        
    def test_translation_from_string_colour_to_bytes(self):
        '''
        Explanation
        Colour values send within our system need to be translated into the proper format for 
        Z-wave
        Our Colours are hex strings in the format "rrggbb"
        Z-wave colours need to be the bytes of a string in the format "#rrggbb0000"
        '''
        
        device = ZWaveDevice(self.mockNode)
        deviceType = device.deviceType
        colourAttribute = deviceType.getAttribute("Colour")
        incomingColour = "ff00ff"
        expectedColour = b'#ff00ff0000'
        device.setValue("Colour", "ff00ff")
        self.assertEqual(expectedColour, self.mockValues["Colour"].data)

    def test_device_get_value_should_return_dictionary(self):
        '''
        HTTP GATEWAY RELIES ON THIS FORMAT
        The dictionary is Json-Serialized
        ''' 
        device = ZWaveDevice(self.mockNode)
        value = device.getValue("Brightness")
        self.assertEqual(10, value["value"])
        self.assertEqual("Brightness", value["name"])

    @mock.patch("device.zwave_device.time")
    def test_process_event_should_create_dictionary_representation_of_event(self, mockTime):
        '''
        HTTP GATEWAY RELIES ON THIS FORMAT
        The dictionary is Json-Serialized
        '''
        mockVal = self.mockValues["Brightness"]
        device = ZWaveDevice(self.mockNode)
        mockTime.time.return_value = 30
        ret = device.processEvent("Brightness")
        self.assertEqual("device.event", ret["event"])
        self.assertEqual(30000, ret["timestamp"])
        self.assertEqual("testdevice", ret["device"])
        self.assertEqual("testproduct", ret["deviceType"])
        self.assertEqual("Brightness", ret["attribute"]["name"])
        self.assertEqual("Brightness", ret["attribute"]["parameters"][0]["name"])
        self.assertEqual(10, ret["attribute"]["parameters"][0]["value"])
        self.assertEqual(DataType.Byte, ret["attribute"]["parameters"][0]["dataType"])

        
    @mock.patch("device.zwave_device.time")
    def test_process_event_should_ignore_events_for_untracked_system_values(self, mockTime):
        mockVal = self.mockValues["Brightness"]
        device = ZWaveDevice(self.mockNode)
        mockTime.time.return_value = 30
        self.assertEqual(None, device.processEvent("NodeIDChanged"))
