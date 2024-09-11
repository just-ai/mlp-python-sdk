from typing import List

import pydantic


def get_parent_classes(cls) -> List[type]:
    parents = []
    bases = cls.__bases__
    if pydantic.main.BaseModel not in bases:
        parents.extend(bases)
        low_level_classes = []
        for cls in bases:
            low_level_classes.extend(get_parent_classes(cls))
        low_level_classes = list(set(low_level_classes))
        parents.extend(low_level_classes)
    else:
        parents.extend([cls for cls in cls.__bases__ if cls != pydantic.main.BaseModel])
    return parents
