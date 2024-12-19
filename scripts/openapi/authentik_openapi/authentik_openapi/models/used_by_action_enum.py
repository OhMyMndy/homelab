# coding: utf-8

"""
    authentik

    Making authentication simple.

    The version of the OpenAPI document: 2024.6.4
    Contact: hello@goauthentik.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class UsedByActionEnum(str, Enum):
    """
    UsedByActionEnum
    """

    """
    allowed enum values
    """
    CASCADE = 'cascade'
    CASCADE_MANY = 'cascade_many'
    SET_NULL = 'set_null'
    SET_DEFAULT = 'set_default'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of UsedByActionEnum from a JSON string"""
        return cls(json.loads(json_str))


