# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
from inspect import getfullargspec
import json
import pprint
import re  # noqa: F401
from pydantic import BaseModel, ConfigDict, Field, StrictStr, ValidationError, field_validator
from typing import Optional
from github_openapi.models.added_to_project_issue_event import AddedToProjectIssueEvent
from github_openapi.models.converted_note_to_issue_issue_event import ConvertedNoteToIssueIssueEvent
from github_openapi.models.demilestoned_issue_event import DemilestonedIssueEvent
from github_openapi.models.labeled_issue_event import LabeledIssueEvent
from github_openapi.models.locked_issue_event import LockedIssueEvent
from github_openapi.models.milestoned_issue_event import MilestonedIssueEvent
from github_openapi.models.moved_column_in_project_issue_event import MovedColumnInProjectIssueEvent
from github_openapi.models.removed_from_project_issue_event import RemovedFromProjectIssueEvent
from github_openapi.models.renamed_issue_event import RenamedIssueEvent
from github_openapi.models.review_dismissed_issue_event import ReviewDismissedIssueEvent
from github_openapi.models.review_request_removed_issue_event import ReviewRequestRemovedIssueEvent
from github_openapi.models.review_requested_issue_event import ReviewRequestedIssueEvent
from github_openapi.models.state_change_issue_event import StateChangeIssueEvent
from github_openapi.models.timeline_assigned_issue_event import TimelineAssignedIssueEvent
from github_openapi.models.timeline_comment_event import TimelineCommentEvent
from github_openapi.models.timeline_commit_commented_event import TimelineCommitCommentedEvent
from github_openapi.models.timeline_committed_event import TimelineCommittedEvent
from github_openapi.models.timeline_cross_referenced_event import TimelineCrossReferencedEvent
from github_openapi.models.timeline_line_commented_event import TimelineLineCommentedEvent
from github_openapi.models.timeline_reviewed_event import TimelineReviewedEvent
from github_openapi.models.timeline_unassigned_issue_event import TimelineUnassignedIssueEvent
from github_openapi.models.unlabeled_issue_event import UnlabeledIssueEvent
from typing import Union, Any, List, Set, TYPE_CHECKING, Optional, Dict
from typing_extensions import Literal, Self
from pydantic import Field

TIMELINEISSUEEVENTS_ANY_OF_SCHEMAS = ["AddedToProjectIssueEvent", "ConvertedNoteToIssueIssueEvent", "DemilestonedIssueEvent", "LabeledIssueEvent", "LockedIssueEvent", "MilestonedIssueEvent", "MovedColumnInProjectIssueEvent", "RemovedFromProjectIssueEvent", "RenamedIssueEvent", "ReviewDismissedIssueEvent", "ReviewRequestRemovedIssueEvent", "ReviewRequestedIssueEvent", "StateChangeIssueEvent", "TimelineAssignedIssueEvent", "TimelineCommentEvent", "TimelineCommitCommentedEvent", "TimelineCommittedEvent", "TimelineCrossReferencedEvent", "TimelineLineCommentedEvent", "TimelineReviewedEvent", "TimelineUnassignedIssueEvent", "UnlabeledIssueEvent"]

class TimelineIssueEvents(BaseModel):
    """
    Timeline Event
    """

    # data type: LabeledIssueEvent
    anyof_schema_1_validator: Optional[LabeledIssueEvent] = None
    # data type: UnlabeledIssueEvent
    anyof_schema_2_validator: Optional[UnlabeledIssueEvent] = None
    # data type: MilestonedIssueEvent
    anyof_schema_3_validator: Optional[MilestonedIssueEvent] = None
    # data type: DemilestonedIssueEvent
    anyof_schema_4_validator: Optional[DemilestonedIssueEvent] = None
    # data type: RenamedIssueEvent
    anyof_schema_5_validator: Optional[RenamedIssueEvent] = None
    # data type: ReviewRequestedIssueEvent
    anyof_schema_6_validator: Optional[ReviewRequestedIssueEvent] = None
    # data type: ReviewRequestRemovedIssueEvent
    anyof_schema_7_validator: Optional[ReviewRequestRemovedIssueEvent] = None
    # data type: ReviewDismissedIssueEvent
    anyof_schema_8_validator: Optional[ReviewDismissedIssueEvent] = None
    # data type: LockedIssueEvent
    anyof_schema_9_validator: Optional[LockedIssueEvent] = None
    # data type: AddedToProjectIssueEvent
    anyof_schema_10_validator: Optional[AddedToProjectIssueEvent] = None
    # data type: MovedColumnInProjectIssueEvent
    anyof_schema_11_validator: Optional[MovedColumnInProjectIssueEvent] = None
    # data type: RemovedFromProjectIssueEvent
    anyof_schema_12_validator: Optional[RemovedFromProjectIssueEvent] = None
    # data type: ConvertedNoteToIssueIssueEvent
    anyof_schema_13_validator: Optional[ConvertedNoteToIssueIssueEvent] = None
    # data type: TimelineCommentEvent
    anyof_schema_14_validator: Optional[TimelineCommentEvent] = None
    # data type: TimelineCrossReferencedEvent
    anyof_schema_15_validator: Optional[TimelineCrossReferencedEvent] = None
    # data type: TimelineCommittedEvent
    anyof_schema_16_validator: Optional[TimelineCommittedEvent] = None
    # data type: TimelineReviewedEvent
    anyof_schema_17_validator: Optional[TimelineReviewedEvent] = None
    # data type: TimelineLineCommentedEvent
    anyof_schema_18_validator: Optional[TimelineLineCommentedEvent] = None
    # data type: TimelineCommitCommentedEvent
    anyof_schema_19_validator: Optional[TimelineCommitCommentedEvent] = None
    # data type: TimelineAssignedIssueEvent
    anyof_schema_20_validator: Optional[TimelineAssignedIssueEvent] = None
    # data type: TimelineUnassignedIssueEvent
    anyof_schema_21_validator: Optional[TimelineUnassignedIssueEvent] = None
    # data type: StateChangeIssueEvent
    anyof_schema_22_validator: Optional[StateChangeIssueEvent] = None
    if TYPE_CHECKING:
        actual_instance: Optional[Union[AddedToProjectIssueEvent, ConvertedNoteToIssueIssueEvent, DemilestonedIssueEvent, LabeledIssueEvent, LockedIssueEvent, MilestonedIssueEvent, MovedColumnInProjectIssueEvent, RemovedFromProjectIssueEvent, RenamedIssueEvent, ReviewDismissedIssueEvent, ReviewRequestRemovedIssueEvent, ReviewRequestedIssueEvent, StateChangeIssueEvent, TimelineAssignedIssueEvent, TimelineCommentEvent, TimelineCommitCommentedEvent, TimelineCommittedEvent, TimelineCrossReferencedEvent, TimelineLineCommentedEvent, TimelineReviewedEvent, TimelineUnassignedIssueEvent, UnlabeledIssueEvent]] = None
    else:
        actual_instance: Any = None
    any_of_schemas: Set[str] = { "AddedToProjectIssueEvent", "ConvertedNoteToIssueIssueEvent", "DemilestonedIssueEvent", "LabeledIssueEvent", "LockedIssueEvent", "MilestonedIssueEvent", "MovedColumnInProjectIssueEvent", "RemovedFromProjectIssueEvent", "RenamedIssueEvent", "ReviewDismissedIssueEvent", "ReviewRequestRemovedIssueEvent", "ReviewRequestedIssueEvent", "StateChangeIssueEvent", "TimelineAssignedIssueEvent", "TimelineCommentEvent", "TimelineCommitCommentedEvent", "TimelineCommittedEvent", "TimelineCrossReferencedEvent", "TimelineLineCommentedEvent", "TimelineReviewedEvent", "TimelineUnassignedIssueEvent", "UnlabeledIssueEvent" }

    model_config = {
        "validate_assignment": True,
        "protected_namespaces": (),
    }

    def __init__(self, *args, **kwargs) -> None:
        if args:
            if len(args) > 1:
                raise ValueError("If a position argument is used, only 1 is allowed to set `actual_instance`")
            if kwargs:
                raise ValueError("If a position argument is used, keyword arguments cannot be used.")
            super().__init__(actual_instance=args[0])
        else:
            super().__init__(**kwargs)

    @field_validator('actual_instance')
    def actual_instance_must_validate_anyof(cls, v):
        instance = TimelineIssueEvents.model_construct()
        error_messages = []
        # validate data type: LabeledIssueEvent
        if not isinstance(v, LabeledIssueEvent):
            error_messages.append(f"Error! Input type `{type(v)}` is not `LabeledIssueEvent`")
        else:
            return v

        # validate data type: UnlabeledIssueEvent
        if not isinstance(v, UnlabeledIssueEvent):
            error_messages.append(f"Error! Input type `{type(v)}` is not `UnlabeledIssueEvent`")
        else:
            return v

        # validate data type: MilestonedIssueEvent
        if not isinstance(v, MilestonedIssueEvent):
            error_messages.append(f"Error! Input type `{type(v)}` is not `MilestonedIssueEvent`")
        else:
            return v

        # validate data type: DemilestonedIssueEvent
        if not isinstance(v, DemilestonedIssueEvent):
            error_messages.append(f"Error! Input type `{type(v)}` is not `DemilestonedIssueEvent`")
        else:
            return v

        # validate data type: RenamedIssueEvent
        if not isinstance(v, RenamedIssueEvent):
            error_messages.append(f"Error! Input type `{type(v)}` is not `RenamedIssueEvent`")
        else:
            return v

        # validate data type: ReviewRequestedIssueEvent
        if not isinstance(v, ReviewRequestedIssueEvent):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ReviewRequestedIssueEvent`")
        else:
            return v

        # validate data type: ReviewRequestRemovedIssueEvent
        if not isinstance(v, ReviewRequestRemovedIssueEvent):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ReviewRequestRemovedIssueEvent`")
        else:
            return v

        # validate data type: ReviewDismissedIssueEvent
        if not isinstance(v, ReviewDismissedIssueEvent):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ReviewDismissedIssueEvent`")
        else:
            return v

        # validate data type: LockedIssueEvent
        if not isinstance(v, LockedIssueEvent):
            error_messages.append(f"Error! Input type `{type(v)}` is not `LockedIssueEvent`")
        else:
            return v

        # validate data type: AddedToProjectIssueEvent
        if not isinstance(v, AddedToProjectIssueEvent):
            error_messages.append(f"Error! Input type `{type(v)}` is not `AddedToProjectIssueEvent`")
        else:
            return v

        # validate data type: MovedColumnInProjectIssueEvent
        if not isinstance(v, MovedColumnInProjectIssueEvent):
            error_messages.append(f"Error! Input type `{type(v)}` is not `MovedColumnInProjectIssueEvent`")
        else:
            return v

        # validate data type: RemovedFromProjectIssueEvent
        if not isinstance(v, RemovedFromProjectIssueEvent):
            error_messages.append(f"Error! Input type `{type(v)}` is not `RemovedFromProjectIssueEvent`")
        else:
            return v

        # validate data type: ConvertedNoteToIssueIssueEvent
        if not isinstance(v, ConvertedNoteToIssueIssueEvent):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ConvertedNoteToIssueIssueEvent`")
        else:
            return v

        # validate data type: TimelineCommentEvent
        if not isinstance(v, TimelineCommentEvent):
            error_messages.append(f"Error! Input type `{type(v)}` is not `TimelineCommentEvent`")
        else:
            return v

        # validate data type: TimelineCrossReferencedEvent
        if not isinstance(v, TimelineCrossReferencedEvent):
            error_messages.append(f"Error! Input type `{type(v)}` is not `TimelineCrossReferencedEvent`")
        else:
            return v

        # validate data type: TimelineCommittedEvent
        if not isinstance(v, TimelineCommittedEvent):
            error_messages.append(f"Error! Input type `{type(v)}` is not `TimelineCommittedEvent`")
        else:
            return v

        # validate data type: TimelineReviewedEvent
        if not isinstance(v, TimelineReviewedEvent):
            error_messages.append(f"Error! Input type `{type(v)}` is not `TimelineReviewedEvent`")
        else:
            return v

        # validate data type: TimelineLineCommentedEvent
        if not isinstance(v, TimelineLineCommentedEvent):
            error_messages.append(f"Error! Input type `{type(v)}` is not `TimelineLineCommentedEvent`")
        else:
            return v

        # validate data type: TimelineCommitCommentedEvent
        if not isinstance(v, TimelineCommitCommentedEvent):
            error_messages.append(f"Error! Input type `{type(v)}` is not `TimelineCommitCommentedEvent`")
        else:
            return v

        # validate data type: TimelineAssignedIssueEvent
        if not isinstance(v, TimelineAssignedIssueEvent):
            error_messages.append(f"Error! Input type `{type(v)}` is not `TimelineAssignedIssueEvent`")
        else:
            return v

        # validate data type: TimelineUnassignedIssueEvent
        if not isinstance(v, TimelineUnassignedIssueEvent):
            error_messages.append(f"Error! Input type `{type(v)}` is not `TimelineUnassignedIssueEvent`")
        else:
            return v

        # validate data type: StateChangeIssueEvent
        if not isinstance(v, StateChangeIssueEvent):
            error_messages.append(f"Error! Input type `{type(v)}` is not `StateChangeIssueEvent`")
        else:
            return v

        if error_messages:
            # no match
            raise ValueError("No match found when setting the actual_instance in TimelineIssueEvents with anyOf schemas: AddedToProjectIssueEvent, ConvertedNoteToIssueIssueEvent, DemilestonedIssueEvent, LabeledIssueEvent, LockedIssueEvent, MilestonedIssueEvent, MovedColumnInProjectIssueEvent, RemovedFromProjectIssueEvent, RenamedIssueEvent, ReviewDismissedIssueEvent, ReviewRequestRemovedIssueEvent, ReviewRequestedIssueEvent, StateChangeIssueEvent, TimelineAssignedIssueEvent, TimelineCommentEvent, TimelineCommitCommentedEvent, TimelineCommittedEvent, TimelineCrossReferencedEvent, TimelineLineCommentedEvent, TimelineReviewedEvent, TimelineUnassignedIssueEvent, UnlabeledIssueEvent. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: Dict[str, Any]) -> Self:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Returns the object represented by the json string"""
        instance = cls.model_construct()
        error_messages = []
        # anyof_schema_1_validator: Optional[LabeledIssueEvent] = None
        try:
            instance.actual_instance = LabeledIssueEvent.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_2_validator: Optional[UnlabeledIssueEvent] = None
        try:
            instance.actual_instance = UnlabeledIssueEvent.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_3_validator: Optional[MilestonedIssueEvent] = None
        try:
            instance.actual_instance = MilestonedIssueEvent.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_4_validator: Optional[DemilestonedIssueEvent] = None
        try:
            instance.actual_instance = DemilestonedIssueEvent.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_5_validator: Optional[RenamedIssueEvent] = None
        try:
            instance.actual_instance = RenamedIssueEvent.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_6_validator: Optional[ReviewRequestedIssueEvent] = None
        try:
            instance.actual_instance = ReviewRequestedIssueEvent.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_7_validator: Optional[ReviewRequestRemovedIssueEvent] = None
        try:
            instance.actual_instance = ReviewRequestRemovedIssueEvent.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_8_validator: Optional[ReviewDismissedIssueEvent] = None
        try:
            instance.actual_instance = ReviewDismissedIssueEvent.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_9_validator: Optional[LockedIssueEvent] = None
        try:
            instance.actual_instance = LockedIssueEvent.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_10_validator: Optional[AddedToProjectIssueEvent] = None
        try:
            instance.actual_instance = AddedToProjectIssueEvent.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_11_validator: Optional[MovedColumnInProjectIssueEvent] = None
        try:
            instance.actual_instance = MovedColumnInProjectIssueEvent.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_12_validator: Optional[RemovedFromProjectIssueEvent] = None
        try:
            instance.actual_instance = RemovedFromProjectIssueEvent.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_13_validator: Optional[ConvertedNoteToIssueIssueEvent] = None
        try:
            instance.actual_instance = ConvertedNoteToIssueIssueEvent.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_14_validator: Optional[TimelineCommentEvent] = None
        try:
            instance.actual_instance = TimelineCommentEvent.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_15_validator: Optional[TimelineCrossReferencedEvent] = None
        try:
            instance.actual_instance = TimelineCrossReferencedEvent.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_16_validator: Optional[TimelineCommittedEvent] = None
        try:
            instance.actual_instance = TimelineCommittedEvent.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_17_validator: Optional[TimelineReviewedEvent] = None
        try:
            instance.actual_instance = TimelineReviewedEvent.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_18_validator: Optional[TimelineLineCommentedEvent] = None
        try:
            instance.actual_instance = TimelineLineCommentedEvent.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_19_validator: Optional[TimelineCommitCommentedEvent] = None
        try:
            instance.actual_instance = TimelineCommitCommentedEvent.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_20_validator: Optional[TimelineAssignedIssueEvent] = None
        try:
            instance.actual_instance = TimelineAssignedIssueEvent.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_21_validator: Optional[TimelineUnassignedIssueEvent] = None
        try:
            instance.actual_instance = TimelineUnassignedIssueEvent.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_22_validator: Optional[StateChangeIssueEvent] = None
        try:
            instance.actual_instance = StateChangeIssueEvent.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))

        if error_messages:
            # no match
            raise ValueError("No match found when deserializing the JSON string into TimelineIssueEvents with anyOf schemas: AddedToProjectIssueEvent, ConvertedNoteToIssueIssueEvent, DemilestonedIssueEvent, LabeledIssueEvent, LockedIssueEvent, MilestonedIssueEvent, MovedColumnInProjectIssueEvent, RemovedFromProjectIssueEvent, RenamedIssueEvent, ReviewDismissedIssueEvent, ReviewRequestRemovedIssueEvent, ReviewRequestedIssueEvent, StateChangeIssueEvent, TimelineAssignedIssueEvent, TimelineCommentEvent, TimelineCommitCommentedEvent, TimelineCommittedEvent, TimelineCrossReferencedEvent, TimelineLineCommentedEvent, TimelineReviewedEvent, TimelineUnassignedIssueEvent, UnlabeledIssueEvent. Details: " + ", ".join(error_messages))
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        if hasattr(self.actual_instance, "to_json") and callable(self.actual_instance.to_json):
            return self.actual_instance.to_json()
        else:
            return json.dumps(self.actual_instance)

    def to_dict(self) -> Optional[Union[Dict[str, Any], AddedToProjectIssueEvent, ConvertedNoteToIssueIssueEvent, DemilestonedIssueEvent, LabeledIssueEvent, LockedIssueEvent, MilestonedIssueEvent, MovedColumnInProjectIssueEvent, RemovedFromProjectIssueEvent, RenamedIssueEvent, ReviewDismissedIssueEvent, ReviewRequestRemovedIssueEvent, ReviewRequestedIssueEvent, StateChangeIssueEvent, TimelineAssignedIssueEvent, TimelineCommentEvent, TimelineCommitCommentedEvent, TimelineCommittedEvent, TimelineCrossReferencedEvent, TimelineLineCommentedEvent, TimelineReviewedEvent, TimelineUnassignedIssueEvent, UnlabeledIssueEvent]]:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return None

        if hasattr(self.actual_instance, "to_dict") and callable(self.actual_instance.to_dict):
            return self.actual_instance.to_dict()
        else:
            return self.actual_instance

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.model_dump())


