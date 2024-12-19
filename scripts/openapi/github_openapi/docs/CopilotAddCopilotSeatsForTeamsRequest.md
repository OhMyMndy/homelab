# CopilotAddCopilotSeatsForTeamsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**selected_teams** | **List[str]** | List of team names within the organization to which to grant access to GitHub Copilot. | 

## Example

```python
from github_openapi.models.copilot_add_copilot_seats_for_teams_request import CopilotAddCopilotSeatsForTeamsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CopilotAddCopilotSeatsForTeamsRequest from a JSON string
copilot_add_copilot_seats_for_teams_request_instance = CopilotAddCopilotSeatsForTeamsRequest.from_json(json)
# print the JSON string representation of the object
print(CopilotAddCopilotSeatsForTeamsRequest.to_json())

# convert the object into a dict
copilot_add_copilot_seats_for_teams_request_dict = copilot_add_copilot_seats_for_teams_request_instance.to_dict()
# create an instance of CopilotAddCopilotSeatsForTeamsRequest from a dict
copilot_add_copilot_seats_for_teams_request_from_dict = CopilotAddCopilotSeatsForTeamsRequest.from_dict(copilot_add_copilot_seats_for_teams_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


