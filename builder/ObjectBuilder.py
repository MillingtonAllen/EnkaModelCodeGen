from typing import List

from JavaClass import JavaClass
from JavaMember import JavaMember
from .TypedBuilder import TypedBuilder
from .naming import to_pascal_case
from .TypedBuilderFactory import TypedBuilderFactory


class ObjectBuilder(TypedBuilder):

    def build_as_class(self, package_name) -> JavaClass:
        return JavaClass(
            class_name=self.get_class_name(self.key),
            package_name=package_name,
            members=self.build_members())

    def build_members(self) -> List[JavaMember]:
        members = []
        for key, value in self.value.items():
            members.append(TypedBuilderFactory.create(key, value).build_as_member())
        return members

    def build_as_member(self) -> JavaMember:
        return JavaMember(
            variable_type=self.get_class_name(self.key),
            variable_name=self.key)

    def get_class_name(self, input):
        return to_pascal_case(input)