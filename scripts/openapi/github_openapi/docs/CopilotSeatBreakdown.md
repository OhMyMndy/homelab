# CopilotSeatBreakdown

The breakdown of Copilot Business seats for the organization.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** | The total number of seats being billed for the organization as of the current billing cycle. | [optional] 
**added_this_cycle** | **int** | Seats added during the current billing cycle. | [optional] 
**pending_cancellation** | **int** | The number of seats that are pending cancellation at the end of the current billing cycle. | [optional] 
**pending_invitation** | **int** | The number of seats that have been assigned to users that have not yet accepted an invitation to this organization. | [optional] 
**active_this_cycle** | **int** | The number of seats that have used Copilot during the current billing cycle. | [optional] 
**inactive_this_cycle** | **int** | The number of seats that have not used Copilot during the current billing cycle. | [optional] 

## Example

```python
from github_openapi.models.copilot_seat_breakdown import CopilotSeatBreakdown

# TODO update the JSON string below
json = "{}"
# create an instance of CopilotSeatBreakdown from a JSON string
copilot_seat_breakdown_instance = CopilotSeatBreakdown.from_json(json)
# print the JSON string representation of the object
print(CopilotSeatBreakdown.to_json())

# convert the object into a dict
copilot_seat_breakdown_dict = copilot_seat_breakdown_instance.to_dict()
# create an instance of CopilotSeatBreakdown from a dict
copilot_seat_breakdown_from_dict = CopilotSeatBreakdown.from_dict(copilot_seat_breakdown_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


