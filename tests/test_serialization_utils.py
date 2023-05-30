"""Test cases for serialization_utils"""
import pytest
from lib.serialization_utils import JsonSerializer, YamlSerializer, PickleSerializer, DataSerializer


class TestSimpleSerialization:
    """
    Test cases for simple serialization using JSON, YAML, and Pickle serializers.

    This class contains test methods to check serialization and deserialization of dictionary objects with JSON, YAML,
    and Pickle serializers. It includes tests for both non-empty and empty dictionaries.
    """

    def test_json_serializer(self):
        """
        Test the JSON serializer with a non-empty dictionary.
        """
        data_serializer = DataSerializer(JsonSerializer())
        data = {"key": "value"}
        serialized_data = data_serializer.serialize(data)
        assert serialized_data == '{"key": "value"}'
        deserialized_data = data_serializer.deserialize(serialized_data)
        assert deserialized_data == data

    def test_json_serializer_empty_dict(self):
        """
        Test the JSON serializer with an empty dictionary.
        """
        data_serializer = DataSerializer(JsonSerializer())
        data = {}
        serialized_data = data_serializer.serialize(data)
        assert serialized_data == '{}'
        deserialized_data = data_serializer.deserialize(serialized_data)
        assert deserialized_data == data

    def test_yaml_serializer(self):
        """
        Test the YAML serializer with a non-empty dictionary.
        """
        data_serializer = DataSerializer(YamlSerializer())
        data = {"key": "value"}
        serialized_data = data_serializer.serialize(data)
        assert serialized_data.strip() == 'key: value'  # strip to remove leading/trailing whitespace
        deserialized_data = data_serializer.deserialize(serialized_data)
        assert deserialized_data == data

    def test_yaml_serializer_empty_dict(self):
        """
        Test the YAML serializer with an empty dictionary.
        """
        data_serializer = DataSerializer(YamlSerializer())
        data = {}
        serialized_data = data_serializer.serialize(data)
        assert serialized_data.strip() == '{}'
        deserialized_data = data_serializer.deserialize(serialized_data)
        assert deserialized_data == data

    def test_pickle_serializer(self):
        """
        Test the Pickle serializer with a non-empty dictionary.
        """
        data_serializer = DataSerializer(PickleSerializer())
        data = {"key": "value"}
        serialized_data = data_serializer.serialize(data)
        deserialized_data = data_serializer.deserialize(serialized_data)
        assert deserialized_data == data

    def test_pickle_serializer_empty_dict(self):
        """
        Test the Pickle serializer with an empty dictionary.
        """
        data_serializer = DataSerializer(PickleSerializer())
        data = {}
        serialized_data = data_serializer.serialize(data)
        deserialized_data = data_serializer.deserialize(serialized_data)
        assert deserialized_data == data


class TestObjerialization:
    """
    Test cases for serialization of custom objects using JSON, YAML, and Pickle serializers.

    This class contains test methods to check serialization and deserialization of custom objects with JSON, YAML,
    and Pickle serializers.
    """

    class CustomObject:
        """
        A simple custom object to be used in the serialization tests.
        """
        # pylint: disable=too-few-public-methods

        def __init__(self, name, value):
            """
            Initialize the custom object with a name and a value.
            """
            self.name = name
            self.value = value

        def __eq__(self, other):
            """
            Define equality for the custom object.
            """
            return self.__dict__ == other.__dict__

    @pytest.fixture
    def custom_object(self):
        """
        Pytest fixture for creating a custom object.
        """
        return TestObjerialization.CustomObject("test_name", "test_value")

    def test_json_serializer(self, custom_object):
        """
        Test the JSON serializer with a custom object.
        """
        data_serializer = DataSerializer(JsonSerializer())
        serialized_data = data_serializer.serialize(custom_object.__dict__)
        deserialized_data = data_serializer.deserialize(serialized_data)
        assert deserialized_data == custom_object.__dict__

    def test_yaml_serializer(self, custom_object):
        """
        Test the YAML serializer with a custom object.
        """
        data_serializer = DataSerializer(YamlSerializer())
        serialized_data = data_serializer.serialize(custom_object.__dict__)
        deserialized_data = data_serializer.deserialize(serialized_data)
        assert deserialized_data == custom_object.__dict__

    def test_pickle_serializer(self, custom_object):
        """
        Test the Pickle serializer with a custom object.
        """
        data_serializer = DataSerializer(PickleSerializer())
        serialized_data = data_serializer.serialize(custom_object)
        deserialized_data = data_serializer.deserialize(serialized_data)
        assert deserialized_data == custom_object


class TestSerializerStrReprMethods:
    """
    Test cases for the __str__ and __repr__ methods of
        JsonSerializer, YamlSerializer, PickleSerializer, and DataSerializer.

    This class contains test methods to check the outputs of __str__ and __repr__ methods of JsonSerializer,
    YamlSerializer, PickleSerializer, and DataSerializer.
    """

    def test_json_serializer_str(self):
        """
        Test the __str__ method of JsonSerializer.
        """
        json_serializer = JsonSerializer()
        assert str(json_serializer) == 'JsonSerializer()'

    def test_json_serializer_repr(self):
        """
        Test the __repr__ method of JsonSerializer.
        """
        json_serializer = JsonSerializer()
        assert repr(json_serializer) == 'JsonSerializer()'

    def test_yaml_serializer_str(self):
        """
        Test the __str__ method of YamlSerializer.
        """
        yaml_serializer = YamlSerializer()
        assert str(yaml_serializer) == 'YamlSerializer()'

    def test_yaml_serializer_repr(self):
        """
        Test the __repr__ method of YamlSerializer.
        """
        yaml_serializer = YamlSerializer()
        assert repr(yaml_serializer) == 'YamlSerializer()'

    def test_pickle_serializer_str(self):
        """
        Test the __str__ method of PickleSerializer.
        """
        pickle_serializer = PickleSerializer()
        assert str(pickle_serializer) == 'PickleSerializer()'

    def test_pickle_serializer_repr(self):
        """
        Test the __repr__ method of PickleSerializer.
        """
        pickle_serializer = PickleSerializer()
        assert repr(pickle_serializer) == 'PickleSerializer()'

    def test_data_serializer_str(self):
        """
        Test the __str__ method of DataSerializer.
        """
        json_serializer = JsonSerializer()
        data_serializer = DataSerializer(json_serializer)
        assert str(data_serializer) == 'DataSerializer(serializing_strategy=JsonSerializer)'

    def test_data_serializer_repr(self):
        """
        Test the __repr__ method of DataSerializer.
        """
        json_serializer = JsonSerializer()
        data_serializer = DataSerializer(json_serializer)
        assert repr(data_serializer) == 'DataSerializer(serializing_strategy=JsonSerializer)'
