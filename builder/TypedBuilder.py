from typing import List

from JavaClass import JavaClass
from JavaMember import JavaMember


class TypedBuilder:
    def __init__(self, key: str, value: any):
        self.key = key
        self.value = value

    def build_as_class(self) -> JavaClass:
        raise NotImplementedError()

    def build_as_member(self) -> JavaMember:
        raise NotImplementedError()