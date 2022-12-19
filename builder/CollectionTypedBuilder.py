from abc import ABC

from JavaClass import JavaClass
from .MemberMerger import merge
from .TypedBuilderFactory import TypedBuilderFactory, is_complex_type
from .TypedBuilder import TypedBuilder
from .exceptions.exceptions import NotSupportedOnPrimitiveException
from .naming import map_of_type, to_pascal_case, remove_suffix_if_exist


class CollectionTypedBuilder(TypedBuilder, ABC):
    def build_and_merge_entry_members(self, merged_members, entry):
        members = []
        for key, value in entry.items():
            members.append(TypedBuilderFactory.create(key, value).build_as_member())
        return merge(merged_members, members)

    def raise_if_contains_primitives(self, payload):
        for each in payload:
            if not is_complex_type(each):
                raise NotSupportedOnPrimitiveException("Can not build class of primitive")

    def build_as_class_without_suffix(self, package_name, suffix="") -> JavaClass:
        return JavaClass(
            class_name=self.get_class_name_without_suffix(suffix=suffix),
            package_name=package_name,
            members=self.build_members()
        )

    def build_members_from_iterable(self, iterable):
        merged_members = []
        for entry in iterable:
            merged_members = self.build_and_merge_entry_members(merged_members, entry)
        return merged_members

    def get_class_name_without_suffix(self, suffix=""):
        cleaned_variable_name = remove_suffix_if_exist(suffix, self.key)
        pascal_clean_variable_name = to_pascal_case(cleaned_variable_name)
        return pascal_clean_variable_name

    def build_members(self):
        raise NotImplementedError()
