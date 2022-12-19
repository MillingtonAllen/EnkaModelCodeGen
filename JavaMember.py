from pydantic import BaseModel

class JavaMember(BaseModel):
    access_specifier: str = "private"
    variable_type: str
    variable_name: str
