# CopilotSeatDetails

Information about a Copilot Business seat assignment for a user, team, or organization.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assignee** | [**SimpleUser**](SimpleUser.md) |  | 
**organization** | [**NullableOrganizationSimple**](NullableOrganizationSimple.md) |  | [optional] 
**assigning_team** | [**CopilotSeatDetailsAssigningTeam**](CopilotSeatDetailsAssigningTeam.md) |  | [optional] 
**pending_cancellation_date** | **date** | The pending cancellation date for the seat, in &#x60;YYYY-MM-DD&#x60; format. This will be null unless the assignee&#39;s Copilot access has been canceled during the current billing cycle. If the seat has been cancelled, this corresponds to the start of the organization&#39;s next billing cycle. | [optional] 
**last_activity_at** | **datetime** | Timestamp of user&#39;s last GitHub Copilot activity, in ISO 8601 format. | [optional] 
**last_activity_editor** | **str** | Last editor that was used by the user for a GitHub Copilot completion. | [optional] 
**created_at** | **datetime** | Timestamp of when the assignee was last granted access to GitHub Copilot, in ISO 8601 format. | 
**updated_at** | **datetime** | **Closing down notice:** This field is no longer relevant and is closing down. Use the &#x60;created_at&#x60; field to determine when the assignee was last granted access to GitHub Copilot. Timestamp of when the assignee&#39;s GitHub Copilot access was last updated, in ISO 8601 format. | [optional] 
**plan_type** | **str** | The Copilot plan of the organization, or the parent enterprise, when applicable. | [optional] 

## Example

```python
from github_openapi.models.copilot_seat_details import CopilotSeatDetails

# TODO update the JSON string below
json = "{}"
# create an instance of CopilotSeatDetails from a JSON string
copilot_seat_details_instance = CopilotSeatDetails.from_json(json)
# print the JSON string representation of the object
print(CopilotSeatDetails.to_json())

# convert the object into a dict
copilot_seat_details_dict = copilot_seat_details_instance.to_dict()
# create an instance of CopilotSeatDetails from a dict
copilot_seat_details_from_dict = CopilotSeatDetails.from_dict(copilot_seat_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


