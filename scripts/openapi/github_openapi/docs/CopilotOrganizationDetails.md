# CopilotOrganizationDetails

Information about the seat breakdown and policies set for an organization with a Copilot Business or Copilot Enterprise subscription.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**seat_breakdown** | [**CopilotSeatBreakdown**](CopilotSeatBreakdown.md) |  | 
**public_code_suggestions** | **str** | The organization policy for allowing or disallowing Copilot to make suggestions that match public code. | 
**ide_chat** | **str** | The organization policy for allowing or disallowing organization members to use Copilot Chat within their editor. | [optional] 
**platform_chat** | **str** | The organization policy for allowing or disallowing organization members to use Copilot features within github.com. | [optional] 
**cli** | **str** | The organization policy for allowing or disallowing organization members to use Copilot within their CLI. | [optional] 
**seat_management_setting** | **str** | The mode of assigning new seats. | 
**plan_type** | **str** | The Copilot plan of the organization, or the parent enterprise, when applicable. | [optional] 

## Example

```python
from github_openapi.models.copilot_organization_details import CopilotOrganizationDetails

# TODO update the JSON string below
json = "{}"
# create an instance of CopilotOrganizationDetails from a JSON string
copilot_organization_details_instance = CopilotOrganizationDetails.from_json(json)
# print the JSON string representation of the object
print(CopilotOrganizationDetails.to_json())

# convert the object into a dict
copilot_organization_details_dict = copilot_organization_details_instance.to_dict()
# create an instance of CopilotOrganizationDetails from a dict
copilot_organization_details_from_dict = CopilotOrganizationDetails.from_dict(copilot_organization_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


