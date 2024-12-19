# CopilotCancelCopilotSeatAssignmentForUsersRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**selected_usernames** | **List[str]** | The usernames of the organization members for which to revoke access to GitHub Copilot. | 

## Example

```python
from github_openapi.models.copilot_cancel_copilot_seat_assignment_for_users_request import CopilotCancelCopilotSeatAssignmentForUsersRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CopilotCancelCopilotSeatAssignmentForUsersRequest from a JSON string
copilot_cancel_copilot_seat_assignment_for_users_request_instance = CopilotCancelCopilotSeatAssignmentForUsersRequest.from_json(json)
# print the JSON string representation of the object
print(CopilotCancelCopilotSeatAssignmentForUsersRequest.to_json())

# convert the object into a dict
copilot_cancel_copilot_seat_assignment_for_users_request_dict = copilot_cancel_copilot_seat_assignment_for_users_request_instance.to_dict()
# create an instance of CopilotCancelCopilotSeatAssignmentForUsersRequest from a dict
copilot_cancel_copilot_seat_assignment_for_users_request_from_dict = CopilotCancelCopilotSeatAssignmentForUsersRequest.from_dict(copilot_cancel_copilot_seat_assignment_for_users_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


