from JavaClass import JavaClass
from JavaMember import JavaMember
from .TypedBuilder import TypedBuilder
from .exceptions.exceptions import NotSupportedOnPrimitiveException


class PrimitiveBuilder(TypedBuilder):
    def build_as_class(self, package_name) -> JavaClass:
        raise NotSupportedOnPrimitiveException("Can not build class of primitive")

    def build_as_member(self) -> JavaMember:
        return JavaMember(
            variable_type=self.get_class_name(self.value),
            variable_name=self.key)

    def get_class_name(self, input):
        java_type_map = {str: "String", int: "Integer", bool: "Boolean", float: "Double"}
        return java_type_map[type(input)]