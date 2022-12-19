from typing import List

from JavaClass import JavaClass
from JavaMember import JavaMember
from .CollectionTypedBuilder import CollectionTypedBuilder
from .TypedBuilderFactory import is_complex_type, to_java_primitive_type
from .naming import map_of_type


class MapBuilder(CollectionTypedBuilder):
    def build_as_class(self, package_name) -> JavaClass:
        self.raise_if_contains_primitives(self.value.values())
        return super().build_as_class_without_suffix(package_name, suffix="Map")

    def build_members(self) -> List[JavaMember]:
        return super().build_members_from_iterable(self.value.values())

    def build_as_member(self):
        return JavaMember(
            variable_type=map_of_type("String", self.get_class_name()),
            variable_name=self.key)

    def get_class_name(self):
        java_type = self.determine_primitive_type()
        if java_type is not None:
            return java_type
        return super().get_class_name_without_suffix(suffix="Map")

    def determine_primitive_type(self):
        out_type = None
        for each in self.value.values():
            if not is_complex_type(each):
                java_type = to_java_primitive_type(each)
                if out_type is None:
                    out_type = java_type
                if out_type == "Integer" and java_type == "Double":
                    out_type = java_type
        return out_type