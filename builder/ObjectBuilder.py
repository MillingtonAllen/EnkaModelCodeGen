from typing import List

from JavaClass import JavaClass
from JavaMember import JavaMember
from builder.TypedBuilder import TypedBuilder
from builder.naming import to_pascal_case
from . import TypedBuilderFactory


class ObjectBuilder(TypedBuilder):

    def build_as_class(self) -> JavaClass:
        pass

    def build_members(self) -> List[JavaMember]:
        members = []
        for key, value in self.value:
            members.append(TypedBuilderFactory.create(key, value).build_as_member())
        return members

    def build_as_member(self) -> JavaMember:
        return JavaMember(
            variable_type=to_pascal_case(self.key),
            variable_name=self.key)
