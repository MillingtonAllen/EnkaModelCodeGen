from pydantic import BaseModel
from typing import List

from JavaClassMember import JavaClassMember


class JavaClass(BaseModel):
    class_name: str
    package_name: str
    members: List[JavaClassMember]
