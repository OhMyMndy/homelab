# CopilotSeatDetailsAssigningTeam

The team through which the assignee is granted access to GitHub Copilot, if applicable.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**node_id** | **str** |  | 
**name** | **str** |  | 
**slug** | **str** |  | 
**description** | **str** |  | 
**privacy** | **str** |  | [optional] 
**notification_setting** | **str** |  | [optional] 
**permission** | **str** |  | 
**permissions** | [**TeamPermissions**](TeamPermissions.md) |  | [optional] 
**url** | **str** |  | 
**html_url** | **str** |  | 
**members_url** | **str** |  | 
**repositories_url** | **str** |  | 
**parent** | [**NullableTeamSimple**](NullableTeamSimple.md) |  | 
**sync_to_organizations** | **str** |  | 
**group_id** | **str** |  | [optional] 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from github_openapi.models.copilot_seat_details_assigning_team import CopilotSeatDetailsAssigningTeam

# TODO update the JSON string below
json = "{}"
# create an instance of CopilotSeatDetailsAssigningTeam from a JSON string
copilot_seat_details_assigning_team_instance = CopilotSeatDetailsAssigningTeam.from_json(json)
# print the JSON string representation of the object
print(CopilotSeatDetailsAssigningTeam.to_json())

# convert the object into a dict
copilot_seat_details_assigning_team_dict = copilot_seat_details_assigning_team_instance.to_dict()
# create an instance of CopilotSeatDetailsAssigningTeam from a dict
copilot_seat_details_assigning_team_from_dict = CopilotSeatDetailsAssigningTeam.from_dict(copilot_seat_details_assigning_team_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


