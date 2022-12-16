from typing import List

from JavaClass import JavaClass
from JavaMember import JavaMember
from builder.TypedBuilder import TypedBuilder
from builder.naming import map_of_type, to_pascal_case
from . import TypedBuilderFactory


class MapBuilder(TypedBuilder):
    def build_as_class(self) -> JavaClass:
        pass

    def build_members(self, payload: dict) -> List[JavaMember]:
        pass

    def build_as_member(self):
        return JavaMember(
            variable_type=map_of_type("String", to_pascal_case(self.key)),
            variable_name=self.key)
