class Writer:
    def __init__(self, java_class):
        self.java_class = java_class

    def write(self):
        output = ""
        output += f'''package {self.java_class.package_name};\n'''
        output += '''\n'''
        output += f'''public class {self.java_class.class_name} {{\n'''

        for member in self.java_class.members:
            output += f'''    {member.access_specifier} {member.variable_type} {member.variable_name};\n'''
        output += f'''}}\n'''
        return output
