from abc import ABC


class ModelSerializer(ABC):
    """
    Abstract class for all Model Serializers
    """
    def __init__(self, obj):
        self.__obj = obj

    # def __init__(self, **kwargs):
    #     self.__field_type = kwargs.get('field_type_map', {})
    #     self.__data = {}
    #
    # def validate(self, **kwargs):
    #     raise NotImplementedError()
    #
    # def validated_data(self):
    #     """
    #     Can be overridden to return validated data in desired format
    #     """
    #     return self.__data
    #
    # def get_field_type(self, field_name):
    #     if not self.__field_type.get(field_name, None):
    #         raise SerializerException("Improperly Configured serializer")
    #     return self.__field_type.get(field_name)

    @property
    def data(self):
        return vars(self.__obj)


class LocationSerializer(ModelSerializer):
    """
    Could be extended to be used as deserializer, with validations
    """
    pass


class UserSerializer(ModelSerializer):
    """
    Could be extended to be used as deserializer, with validations
    """

    @property
    def data(self):
        attr_dict = vars(self.__obj)
        attr_dict['location'] = LocationSerializer(self.__obj.location)
        attr_dict['city'] = self.__obj.location.city
        attr_dict['latitude'] = self.__obj.location.latitude
        attr_dict['longitude'] = self.__obj.location.longitude
        return attr_dict

