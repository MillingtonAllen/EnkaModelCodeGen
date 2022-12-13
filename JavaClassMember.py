from pydantic import BaseModel

class JavaClassMember(BaseModel):
    access_specifier: str
    variable_type: str
    variable_name: str
