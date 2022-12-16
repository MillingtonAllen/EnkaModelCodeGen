from typing import List

from JavaClass import JavaClass
from builder.TypedBuilder import TypedBuilder
from JavaMember import JavaMember
from builder.naming import to_pascal_case, list_of_type, remove_suffix_if_exist
from . import TypedBuilderFactory


class ListBuilder(TypedBuilder):

    def build_as_class(self) -> JavaClass:
        pass

    def build_members(self) -> List[JavaMember]:
        pass

    def build_as_member(self) -> JavaMember:
        cleaned_variable_name = remove_suffix_if_exist("List", self.key)
        pascal_clean_variable_name = to_pascal_case(cleaned_variable_name)
        return JavaMember(
            variable_type=list_of_type(pascal_clean_variable_name),
            variable_name=self.key)