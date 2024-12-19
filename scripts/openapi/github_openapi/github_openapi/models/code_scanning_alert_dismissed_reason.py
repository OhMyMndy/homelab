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


class CodeScanningAlertDismissedReason(str, Enum):
    """
    **Required when the state is dismissed.** The reason for dismissing or closing the alert.
    """

    """
    allowed enum values
    """
    FALSE_POSITIVE = 'false positive'
    WON_QUOTE_T_FIX = 'won't fix'
    USED_IN_TESTS = 'used in tests'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of CodeScanningAlertDismissedReason from a JSON string"""
        return cls(json.loads(json_str))


