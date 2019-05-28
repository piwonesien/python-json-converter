import unittest

from BackendTask import PropertySet
from BackendTask import Property
from BackendTask import Converter


class Test_test_BackendTask(unittest.TestCase):

    def test_propertyset_create(self):

        a_property_set = PropertySet('Test')

        self.assertEquals(a_property_set.type, 'PropertySet')
        self.assertEquals(a_property_set.name, 'Test')
        self.assertTrue(len(a_property_set.properties) == 0)

    def test_property_create(self):

        a_property = Property('Test', 100)

        self.assertEquals(a_property.type, 'Property')
        self.assertEquals(a_property.name, 'Test')
        self.assertEquals(a_property.value, 100)

    def test_propertyset_repr(self):
        a_property_set = PropertySet('Test')
        self.assertEqual(a_property_set.__repr__(), '{"name": "Test", "type": "PropertySet", "properties": []}')

        a_property_set.properties.append(Property('Test', 100))
        self.assertEqual(a_property_set.__repr__(), '{"name": "Test", "type": "PropertySet", "properties": ['
                                                    '{"name": "Test", "value": 100, "type": "Property"}]}')

    def test_property_repr(self):
        a_property0 = Property('Test', 100)
        self.assertEqual(a_property0.__repr__(), '{"name": "Test", "value": 100, "type": "Property"}')

        a_property1 = Property('Test', 1.23)
        self.assertEqual(a_property1.__repr__(), '{"name": "Test", "value": 1.23, "type": "Property"}')

        a_property2 = Property('Test', "test")
        self.assertEqual(a_property2.__repr__(), '{"name": "Test", "value": "test", "type": "Property"}')

    def test_converter_serialize(self):
        a_property_set = PropertySet('Test')
        a_property_set.properties.append(Property('Test', 100))
        self.assertEqual(Converter.serialize(a_property_set), '{"name": "Test", "type": "PropertySet", "properties": ['
                                                    '{"name": "Test", "value": 100, "type": "Property"}]}')

    def test_converter_deserialize(self):
        a_property_set = Converter.deserialize('{"name": "Test", "type": "PropertySet", "properties": ['
                                               '{"name": "Test", "value": 100, "type": "Property"}]}')
        self.assertEquals(a_property_set.type, 'PropertySet')
        self.assertEquals(a_property_set.name, 'Test')
        self.assertTrue(len(a_property_set.properties) == 1)
        self.assertEquals(a_property_set.properties[0].type, 'Property')
        self.assertEquals(a_property_set.properties[0].name, 'Test')
        self.assertEquals(a_property_set.properties[0].value, 100)

    def test_converter_float(self):
        self.assertEquals(Converter.is_float("asdf"), False)
        self.assertEquals(Converter.is_float("1"), True)
        self.assertEquals(Converter.is_float("123"), True)
        self.assertEquals(Converter.is_float("-1"), True)
        self.assertEquals(Converter.is_float("12ew"), False)
        self.assertEquals(Converter.is_float("1.0"), True)
        self.assertEquals(Converter.is_float("0.9"), True)
        self.assertEquals(Converter.is_float("-0.5"), True)

    def test_converter_int(self):
        self.assertEquals(Converter.is_int("asdf"), False)
        self.assertEquals(Converter.is_int("1"), True)
        self.assertEquals(Converter.is_int("123"), True)
        self.assertEquals(Converter.is_int("-1"), True)
        self.assertEquals(Converter.is_int("12ew"), False)
        self.assertEquals(Converter.is_int("1.0"), False)
        self.assertEquals(Converter.is_int("0.9"), False)
        self.assertEquals(Converter.is_int("-0.5"), False)


if __name__ == '__main__':
    unittest.main()
