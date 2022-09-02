from pprint import pprint
from typing import Any, Dict, List, Union, Optional

from pydantic import BaseModel, Field

UnknownModel = Dict[str, Any]


def inspect(dictionary: UnknownModel):
    print()
    for field, value in dictionary.items():
        print(f"    {field}: {value.__class__.__name__}")
    

class Character(BaseModel):
    name: str
    active_spec_name: str
    active_spec_role: str
    faction: str