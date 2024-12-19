# CopilotAddCopilotSeatsForUsersRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**selected_usernames** | **List[str]** | The usernames of the organization members to be granted access to GitHub Copilot. | 

## Example

```python
from github_openapi.models.copilot_add_copilot_seats_for_users_request import CopilotAddCopilotSeatsForUsersRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CopilotAddCopilotSeatsForUsersRequest from a JSON string
copilot_add_copilot_seats_for_users_request_instance = CopilotAddCopilotSeatsForUsersRequest.from_json(json)
# print the JSON string representation of the object
print(CopilotAddCopilotSeatsForUsersRequest.to_json())

# convert the object into a dict
copilot_add_copilot_seats_for_users_request_dict = copilot_add_copilot_seats_for_users_request_instance.to_dict()
# create an instance of CopilotAddCopilotSeatsForUsersRequest from a dict
copilot_add_copilot_seats_for_users_request_from_dict = CopilotAddCopilotSeatsForUsersRequest.from_dict(copilot_add_copilot_seats_for_users_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


