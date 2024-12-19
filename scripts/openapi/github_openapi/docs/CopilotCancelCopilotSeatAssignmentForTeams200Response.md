# CopilotCancelCopilotSeatAssignmentForTeams200Response

The total number of seats set to \"pending cancellation\" for members of the specified team(s).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**seats_cancelled** | **int** |  | 

## Example

```python
from github_openapi.models.copilot_cancel_copilot_seat_assignment_for_teams200_response import CopilotCancelCopilotSeatAssignmentForTeams200Response

# TODO update the JSON string below
json = "{}"
# create an instance of CopilotCancelCopilotSeatAssignmentForTeams200Response from a JSON string
copilot_cancel_copilot_seat_assignment_for_teams200_response_instance = CopilotCancelCopilotSeatAssignmentForTeams200Response.from_json(json)
# print the JSON string representation of the object
print(CopilotCancelCopilotSeatAssignmentForTeams200Response.to_json())

# convert the object into a dict
copilot_cancel_copilot_seat_assignment_for_teams200_response_dict = copilot_cancel_copilot_seat_assignment_for_teams200_response_instance.to_dict()
# create an instance of CopilotCancelCopilotSeatAssignmentForTeams200Response from a dict
copilot_cancel_copilot_seat_assignment_for_teams200_response_from_dict = CopilotCancelCopilotSeatAssignmentForTeams200Response.from_dict(copilot_cancel_copilot_seat_assignment_for_teams200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


