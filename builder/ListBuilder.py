from typing import List

from JavaClass import JavaClass
from JavaMember import JavaMember
from .naming import list_of_type
from .CollectionTypedBuilder import CollectionTypedBuilder
from .TypedBuilderFactory import is_complex_type, to_java_primitive_type


class ListBuilder(CollectionTypedBuilder):
    def build_as_class(self, package_name) -> JavaClass:
        self.raise_if_contains_primitives(self.value)
        return super().build_as_class_without_suffix(package_name, suffix="List")

    def build_members(self) -> List[JavaMember]:
        return super().build_members_from_iterable(self.value)

    def build_as_member(self) -> JavaMember:
        return JavaMember(
            variable_type=list_of_type(self.get_class_name()),
            variable_name=self.key)

    def get_class_name(self):
        java_type = self.determine_primitive_type()
        if java_type is not None:
            return java_type
        return super().get_class_name_without_suffix(suffix="List")

    def determine_primitive_type(self):
        out_type = None
        for each in self.value:
            if not is_complex_type(each):
                java_type = to_java_primitive_type(each)
                if out_type is None:
                    out_type = java_type
                if out_type == "Integer" and java_type == "Double":
                    out_type = java_type
        return out_type