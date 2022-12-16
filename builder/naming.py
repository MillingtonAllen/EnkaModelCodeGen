def to_pascal_case(input):
    return input[0].upper() + input[1:]


def list_of_type(type_name: str):
    return f'''List<{type_name}>'''


def map_of_type(key_type_name: str, value_type_name: str):
    return f'''Map<{key_type_name}, {value_type_name}>'''

def remove_suffix_if_exist(suffix:str, input:str):
    if len(suffix) == 0:
        return input

    if not input.endswith(suffix):
        return input

    return input[:-1*len(suffix)]