"""
Provides serializers with choice of JSON, YAML or pickle via strategy pattern
As more processes become long-running daemons instead of short-lived batch calls then we need strong capabilities
    to pass objects around CIDW servers.
Also intended somewhat to provide example of using interfaces, inheritance, typing etal.
"""
import abc
import io
import json
import pickle
import typing

import yaml


class SerializingStrategy(abc.ABC):
    """ specify the simple interface (1 method :/ ) for serializging strategies"""

    @abc.abstractmethod
    def __call__(self, data: typing.Any, deserialize: bool = False) -> typing.Any:
        pass


class JsonSerializer(SerializingStrategy):
    """
    This class implements JSON serialization and deserialization.
    """

    def __call__(self, data: typing.Any, deserialize: bool = False) -> typing.Any:
        """
        Callable method for JsonSerializer class that serializes or deserializes data depending on the deserialize flag.

        Args:
            data (type Any for serializing, str for deserializing): Data to be serialized or deserialized.
            deserialize (bool, optional): Flag to indicate if data should be deserialized. Defaults to False.

        Returns:
            str or dict: Serialized or deserialized data.
        """
        if deserialize:
            if not isinstance(data, str):
                raise ValueError(f'Type: {type(data)} cannot be deserialized')
            return json.loads(data)
        return json.dumps(data)

    def __str__(self):
        """
        String representation of JsonSerializer object.

        Returns:
            str: JsonSerializer class in string format.
        """
        return "JsonSerializer()"

    def __repr__(self):
        """
        Formal string representation of JsonSerializer object.

        Returns:
            str: JsonSerializer class in formal string format.
        """
        return "JsonSerializer()"


class YamlSerializer(SerializingStrategy):
    """
    This class implements YAML serialization and deserialization.
    """

    def __call__(self, data: typing.Any, deserialize: bool = False) -> typing.Any:
        """
        Callable method for YamlSerializer class that serializes or deserializes data depending on the deserialize flag.

        Args:
            data (str or dict): Data to be serialized or deserialized.
            deserialize (bool, optional): Flag to indicate if data should be deserialized. Defaults to False.

        Returns:
            str or dict: Serialized or deserialized data.
        """
        if deserialize:
            if not isinstance(data, str):
                raise ValueError(f'Type: {type(data)} cannot be deserialized')
            return yaml.full_load(data)
        return yaml.dump(data)

    def __str__(self):
        """
        String representation of YamlSerializer object.

        Returns:
            str: YamlSerializer class in string format.
        """
        return f"YamlSerializer()"

    def __repr__(self):
        """
        Formal string representation of YamlSerializer object.

        Returns:
            str: YamlSerializer class in formal string format.
        """
        return f"YamlSerializer()"


class PickleSerializer(SerializingStrategy):
    """
    This class implements Pickle serialization and deserialization.
    """

    def __call__(self, data: typing.Any, deserialize: bool = False) -> typing.Any:
        """
        Callable method for PickleSerializer class that serializes
            or deserializes data depending on the deserialize flag.

        Args:
            data (str or dict): Data to be serialized or deserialized.
            deserialize (bool, optional): Flag to indicate if data should be deserialized. Defaults to False.

        Returns:
            str or dict: Serialized or deserialized data.
        """
        if deserialize:
            if not isinstance(data, bytes):
                raise ValueError(f'Type: {type(data)} cannot be deserialized')
            return pickle.load(io.BytesIO(data))
        return pickle.dumps(data)

    def __str__(self):
        """
        String representation of PickleSerializer object.

        Returns:
            str: PickleSerializer class in string format.
        """
        return f"PickleSerializer()"

    def __repr__(self):
        """
        Formal string representation of PickleSerializer object.

        Returns:
            str: PickleSerializer class in formal string format.
        """
        return f"PickleSerializer()"


class DataSerializer:
    """
    This class implements a strategy pattern for serialization and deserialization using different formats.
    Our primary usage will be in passing objects between servers, to cache or to Redis
    """

    def __init__(self, serializing_strategy: SerializingStrategy):
        """
        Constructor for DataSerializer class.

        Args:
            serializing_strategy (object): An instance of JsonSerializer, YamlSerializer, or PickleSerializer.
        """
        self.serializing_strategy = serializing_strategy

    def serialize(self, data: typing.Any) -> typing.Union[str, bytes]:
        """
        Serializes data using the provided serialization strategy.

        Args:
            data (str or dict): Data to be serialized.

        Returns:
            str: Serialized data.
        """
        return self.serializing_strategy(data)

    def deserialize(self, data: typing.Union[str, bytes]) -> typing.Any:
        """
        Deserializes data using the provided deserialization strategy.

        Args:
            data (str): Serialized data.

        Returns:
            dict: Deserialized data.
        """
        return self.serializing_strategy(data, deserialize=True)

    def __str__(self):
        """
        String representation of DataSerializer object.

        Returns:
            str: DataSerializer class in string format, showing the serializing strategy.
        """
        return f"DataSerializer(serializing_strategy={self.serializing_strategy.__class__.__name__})"

    def __repr__(self):
        """
        Formal string representation of DataSerializer object.

        Returns:
            str: DataSerializer class in formal string format, showing the serializing strategy.
        """
        return f"DataSerializer(serializing_strategy={self.serializing_strategy.__class__.__name__})"


if __name__ == '__main__':
    """
    A simple example of using each of the serializers to marshal and unmarshal data
    """
    # construct DataSerializers of each type
    dcjs = DataSerializer(JsonSerializer())
    dcyl = DataSerializer(YamlSerializer())
    dcpk = DataSerializer(PickleSerializer())
    # setup data structure to be serilized, dict with single, list and dict values
    datain = {'key1': 'value1', 'key2': ['k2Val1', 'k2Val', 'k2Val3'],
              'key3': {'k3K1': 'k3K1Val1', 'k3K2': ['k3K2Val2', 'k3K2Val2']}}
    # call each serializer, storing the string returned
    sjs = dcjs.serialize(datain)
    yls = dcyl.serialize(datain)
    pks = dcpk.serialize(datain)
    # print the strings to show what the serialized values look like
    print(f'JSON:\n{sjs}\n')
    print(f'YAML:\n{yls}\n')
    print(f'Pickle:\n{pks}\n')
    # now deserialize the strings back to the original data structure and print
    sjd = dcjs.deserialize(sjs)
    print(f'JSON Load is type {type(sjd)}\n{sjd}')
    yld = dcyl.deserialize(yls)
    print(f'YAML Load is type {type(yld)}\n{yld}\n')
    pkd = dcpk.deserialize(pks)
    print(f'Pickle Load is type {type(pkd)}\n{pkd}\n')
