from JavaClass import JavaClass
from JavaMember import JavaMember
from builder.TypedBuilder import TypedBuilder


class PrimitiveBuilder(TypedBuilder):
    def build_as_class(self) -> JavaClass:
        return super().build_as_class()

    def build_as_member(self) -> JavaMember:
        java_type_map = {str: "String", int: "Integer", bool: "Boolean", float: "Double"}
        return JavaMember(
            variable_type=java_type_map[type(self.value)],
            variable_name=self.key)
