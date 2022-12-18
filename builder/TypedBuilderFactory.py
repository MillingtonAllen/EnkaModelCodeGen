def is_complex_type(input: any) -> bool:
    if type(input) in [int, float, str, bool]:
        return False
    return True


def to_java_primitive_type(input):
    java_type_map = {str: "String", int: "Integer", bool: "Boolean", float: "Double"}
    return java_type_map[type(input)]


def is_map(variable_name):
    return variable_name[-3:] == "Map"


def is_map_complex(payload):
    for each in payload.values():
        if is_complex_type(each):
            return True
    return False


def is_list(input):
    return type(input) is list


def is_list_complex(payload):
    for each in payload:
        if is_complex_type(each):
            return True
    return False


def is_dict(input):
    return type(input) is dict


def to_pascal_case(input):
    return input[0].upper() + input[1:]


class TypedBuilderFactory:

    @staticmethod
    def create(key: str, value: any):
        from . import ListBuilder, MapBuilder, ObjectBuilder, PrimitiveBuilder

        if not is_complex_type(value):
            return PrimitiveBuilder(key=key, value=value)
        elif is_map(key):  # map must be checked before dict
            return MapBuilder(key=key, value=value)
        elif is_list(value):
            return ListBuilder(key=key, value=value)
        elif is_dict(value):
            return ObjectBuilder(key=key, value=value)
        else:
            raise RuntimeError("Unexpected Member Type")  # TODO custom error type
