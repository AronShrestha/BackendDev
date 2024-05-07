from ariadne import load_schema_from_path
from typing import List

def load_schema()->List[str]:
    type_defs = []
    paths = [
        "api/schema/user_schema"
    ]
    file_name = "schema.graphql"

    for path in paths:
        type_defs.append(
            load_schema_from_path(path+file_name)
        )
    
    return type_defs

