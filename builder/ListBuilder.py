from typing import List

from JavaClass import JavaClass
from JavaMember import JavaMember
from builder.naming import list_of_type
from .CollectionTypedBuilder import CollectionTypedBuilder


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
        return super().get_class_name_without_suffix(suffix="List")
