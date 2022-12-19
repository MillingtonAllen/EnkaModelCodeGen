from builder.TypedBuilderFactory import is_list, is_map


class Writer:
    def __init__(self, java_class):
        self.java_class = java_class

    def write(self, lombok: bool = False):
        output = ""
        output += f'''package {self.java_class.package_name};\n'''
        output += '''\n'''
        output += f'''import lombok.Data;\n'''
        output += '''\n'''

        contains_map = False
        contains_list = False
        for member in self.java_class.members:
            if member.variable_type.startswith("Map"):
                contains_map = True
            if member.variable_type.startswith("List"):
                contains_list = True

        if contains_list:
            output += f'''import java.util.List;\n'''

        if contains_map:
            output += f'''import java.util.Map;\n'''

        if contains_map or contains_list:
            output += '''\n'''

        output += '''@Data\n'''
        output += f'''public class {self.java_class.class_name} {{\n'''

        for member in self.java_class.members:
            output += f'''    {member.access_specifier} {member.variable_type} {member.variable_name};\n'''
        output += f'''}}\n'''
        return output
