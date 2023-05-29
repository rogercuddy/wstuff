"""Test cases for serialization_utils"""
import pytest
from lib.serialization_utils import JsonSerializer, YamlSerializer, PickleSerializer, DataSerializer


class TestSimpleSerialization:

    def test_json_serializer(self):
        data_serializer = DataSerializer(JsonSerializer())
        data = {"key": "value"}
        serialized_data = data_serializer.serialize(data)
        assert serialized_data == '{"key": "value"}'
        deserialized_data = data_serializer.deserialize(serialized_data)
        assert deserialized_data == data

    def test_json_serializer_empty_dict(self):
        # Test with empty dictionary
        data_serializer = DataSerializer(JsonSerializer())
        data = {}
        serialized_data = data_serializer.serialize(data)
        assert serialized_data == '{}'
        deserialized_data = data_serializer.deserialize(serialized_data)
        assert deserialized_data == data

    def test_yaml_serializer(self):
        data_serializer = DataSerializer(YamlSerializer())
        data = {"key": "value"}
        serialized_data = data_serializer.serialize(data)
        assert serialized_data.strip() == 'key: value'  # strip to remove leading/trailing whitespace
        deserialized_data = data_serializer.deserialize(serialized_data)
        assert deserialized_data == data

    def test_yaml_serializer_empty_dict(self):
        data_serializer = DataSerializer(YamlSerializer())
        # Test with empty dictionary
        data = {}
        serialized_data = data_serializer.serialize(data)
        assert serialized_data.strip() == '{}'
        deserialized_data = data_serializer.deserialize(serialized_data)
        assert deserialized_data == data

    def test_pickle_serializer(self):
        data_serializer = DataSerializer(PickleSerializer())
        data = {"key": "value"}
        serialized_data = data_serializer.serialize(data)
        deserialized_data = data_serializer.deserialize(serialized_data)
        assert deserialized_data == data

    def test_pickle_serializer_empty_dict(self):
        data_serializer = DataSerializer(PickleSerializer())
        # Test with empty dictionary
        data = {}
        serialized_data = data_serializer.serialize(data)
        deserialized_data = data_serializer.deserialize(serialized_data)
        assert deserialized_data == data


class TestObjerialization:
    class CustomObject:
        def __init__(self, name, value):
            self.name = name
            self.value = value

        def __eq__(self, other):
            return self.__dict__ == other.__dict__

    @pytest.fixture
    def custom_object(self):
        return TestObjerialization.CustomObject("test_name", "test_value")

    def test_json_serializer(self, custom_object):
        data_serializer = DataSerializer(JsonSerializer())
        serialized_data = data_serializer.serialize(custom_object.__dict__)
        deserialized_data = data_serializer.deserialize(serialized_data)
        assert deserialized_data == custom_object.__dict__

    def test_yaml_serializer(self, custom_object):
        data_serializer = DataSerializer(YamlSerializer())
        serialized_data = data_serializer.serialize(custom_object.__dict__)
        deserialized_data = data_serializer.deserialize(serialized_data)
        assert deserialized_data == custom_object.__dict__

    def test_pickle_serializer(self, custom_object):
        data_serializer = DataSerializer(PickleSerializer())
        serialized_data = data_serializer.serialize(custom_object)
        deserialized_data = data_serializer.deserialize(serialized_data)
        assert deserialized_data == custom_object


class TestSerializerStrReprMethods:
    def test_json_serializer_str(self):
        json_serializer = JsonSerializer()
        assert str(json_serializer) == 'JsonSerializer()'

    def test_json_serializer_repr(self):
        json_serializer = JsonSerializer()
        assert repr(json_serializer) == 'JsonSerializer()'

    def test_yaml_serializer_str(self):
        yaml_serializer = YamlSerializer()
        assert str(yaml_serializer) == 'YamlSerializer()'

    def test_yaml_serializer_repr(self):
        yaml_serializer = YamlSerializer()
        assert repr(yaml_serializer) == 'YamlSerializer()'

    def test_pickle_serializer_str(self):
        pickle_serializer = PickleSerializer()
        assert str(pickle_serializer) == 'PickleSerializer()'

    def test_pickle_serializer_repr(self):
        pickle_serializer = PickleSerializer()
        assert repr(pickle_serializer) == 'PickleSerializer()'

    def test_data_serializer_str(self):
        json_serializer = JsonSerializer()
        data_serializer = DataSerializer(json_serializer)
        assert str(data_serializer) == 'DataSerializer(serializing_strategy=JsonSerializer)'

    def test_data_serializer_repr(self):
        json_serializer = JsonSerializer()
        data_serializer = DataSerializer(json_serializer)
        assert repr(data_serializer) == 'DataSerializer(serializing_strategy=JsonSerializer)'
