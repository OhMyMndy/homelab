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


class InvalidResponseActionEnum(str, Enum):
    """
    InvalidResponseActionEnum
    """

    """
    allowed enum values
    """
    RETRY = 'retry'
    RESTART = 'restart'
    RESTART_WITH_CONTEXT = 'restart_with_context'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of InvalidResponseActionEnum from a JSON string"""
        return cls(json.loads(json_str))


