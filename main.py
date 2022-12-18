import argparse
import os.path
import os

from parser import Parser
from writer import Writer


def parse_args():
    parser = argparse.ArgumentParser(description="Input package_name and json_file")

    parser.add_argument('--package-name',
                        help="specifies package name for generated java files",
                        required=True)
    parser.add_argument('--json-file',
                        help="input Enka api playerInfo json",
                        required=True)

    parser.add_argument('--output-directory',
                            help="directory to write Java files",
                            required=True)

    return parser.parse_args()


def main():
    args = parse_args()
    parser = Parser(package_name=args.package_name)

    if not os.path.exists(args.output_directory):
        os.makedirs(args.output_directory, exist_ok=True)

    with open(args.json_file) as f:
        data = parser.str_to_dict(f.read())

    java_classes = parser.traverse_dict(data)

    for cls in java_classes:
        java_code = Writer(cls).write()
        with open(os.path.join(args.output_directory, f'''{cls.class_name}.java'''), mode='w') as out:
            out.write(java_code)

if __name__ == "__main__":
    main()
