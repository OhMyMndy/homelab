# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class CodeScanningAlertClassification(str, Enum):
    """
    A classification of the file. For example to identify it as generated.
    """

    """
    allowed enum values
    """
    SOURCE = 'source'
    GENERATED = 'generated'
    TEST = 'test'
    LIBRARY = 'library'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of CodeScanningAlertClassification from a JSON string"""
        return cls(json.loads(json_str))


