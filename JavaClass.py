from pydantic import BaseModel
from typing import List

from JavaMember import JavaMember


class JavaClass(BaseModel):
    class_name: str
    package_name: str
    members: List[JavaMember]
