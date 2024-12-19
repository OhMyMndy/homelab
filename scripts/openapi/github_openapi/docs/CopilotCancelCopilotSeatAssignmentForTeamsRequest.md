# CopilotCancelCopilotSeatAssignmentForTeamsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**selected_teams** | **List[str]** | The names of teams from which to revoke access to GitHub Copilot. | 

## Example

```python
from github_openapi.models.copilot_cancel_copilot_seat_assignment_for_teams_request import CopilotCancelCopilotSeatAssignmentForTeamsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CopilotCancelCopilotSeatAssignmentForTeamsRequest from a JSON string
copilot_cancel_copilot_seat_assignment_for_teams_request_instance = CopilotCancelCopilotSeatAssignmentForTeamsRequest.from_json(json)
# print the JSON string representation of the object
print(CopilotCancelCopilotSeatAssignmentForTeamsRequest.to_json())

# convert the object into a dict
copilot_cancel_copilot_seat_assignment_for_teams_request_dict = copilot_cancel_copilot_seat_assignment_for_teams_request_instance.to_dict()
# create an instance of CopilotCancelCopilotSeatAssignmentForTeamsRequest from a dict
copilot_cancel_copilot_seat_assignment_for_teams_request_from_dict = CopilotCancelCopilotSeatAssignmentForTeamsRequest.from_dict(copilot_cancel_copilot_seat_assignment_for_teams_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


