from .composite_structure import _composite_structure
from .element_restrictions import _element_restrictions
from .message_structure import _message_structure
from .segment_structure import _segment_structure
from .unit_names import _unit_names
from copy import deepcopy
from typing import Union


_spec_dct = {
    "composite_structure": _composite_structure,
    "element_restrictions": _element_restrictions,
    "message_structure": _message_structure,
    "segment_structure": _segment_structure,
    "unit_names": _unit_names,
}


def get_specs(spec: str, version: Union[str, None] = None) -> dict:
    """
    Use this function only to get specifications - to prevent any changes to them as they might be used anywhere

    :param spec: name of specifications
    :param version: EDIFACT version
    :return:
    """
    dct = _spec_dct[spec]
    if version is None:
        return deepcopy(dct)
    if version not in dct:
        raise ValueError(f"EDIFACT version {version} is not implemented, getting {spec} failed")
    return dct[spec][version]
