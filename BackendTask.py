import re

class PropertySet(object):

    def __init__(self, name, *args, **kwargs):
        super(PropertySet, self).__init__(*args, **kwargs)

        self.type = 'PropertySet'
        self.name = name
        self.properties = []

    def __repr__(self):
        return f'{{"name": "{self.name}", "type": "{self.type}", "properties": {self.properties}}}'


class Property(object):

    def __init__(self, name, value, *args, **kwargs):
        super(Property, self).__init__(*args, **kwargs)

        self.type = 'Property'
        self.name = name
        self.value = value

    def __repr__(self):
        val = "\"" + self.value + "\"" if type(self.value) is str else self.value
        return f'{{"name": "{self.name}", "value": {val}, "type": "{self.type}"}}'


class Converter:
    @staticmethod
    def serialize(json_object: PropertySet) -> str:
        return json_object.__repr__()

    @staticmethod
    def deserialize(json_string: str) -> PropertySet:
        json_dict = Converter.create_dictionary(json_string)

        # Specific JSON stuff:
        propertyset = PropertySet(json_dict["name"])
        for item in json_dict["properties"]:
            propertyset.properties.append(
                Property(item["name"] if "name" in item else None, item["value"] if "value" in item else None)
            )

        return propertyset

    @staticmethod
    def create_dictionary(json_string: str):
        # Split string into a list with each entry as a first level KV pair:
        # -> ['"key": value', ...]
        # A nested value is also one value at this point
        json_list = re.findall(r"[ ]*\"[A-Za-z0-9]+\":[ ]*(?:\[[^\]]+])|(?:[^{\[,\]}]+)", json_string)
        # Understanding regex:
        # \"[A-Za-z0-9]+\": -> search for key
        # [ ]* -> allow whitespaces
        # (?:\[[^\]]+])|(?:(?:[^{\[,\]}]+)) -> OR check:
        # First part: search for lists
        # Second part: search for commas in non list entries

        json_dict = {}
        for element in json_list:
            element = element.strip()
            kv = re.findall("\"([A-Za-z0-9]+)\":(.+)", element)
            json_dict[kv[0][0]] = Converter.parse_data(kv[0][1])
        return json_dict

    @staticmethod
    def parse_data(string: str):
        string = string.strip()

        # Datatype is string
        if string.startswith("\""):
            return string.replace("\"", "")
        # Datatype is list
        if string.startswith("["):
            # Here we assume that in a list is always a list of objects,
            # for other list types use a more complex regex (e.g. regex above)
            items = re.findall("{[^}]+}", string)
            item_list = []
            for item in items:
                # Each list item contain a new json object -> recursive dictionary creator
                item_list.append(Converter.create_dictionary(item))
            return item_list
        if Converter.is_int(string):
            return int(string)
        if Converter.is_float(string):
            return float(string)

    @staticmethod
    def is_float(input_string: str):
        try:
            float(input_string)
        except ValueError:
            return False
        return True

    @staticmethod
    def is_int(input_string: str):
        try:
            int(input_string)
        except ValueError:
            return False
        return True


