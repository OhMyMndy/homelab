# OrganizationActionsVariable

Organization variable for GitHub Actions.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the variable. | 
**value** | **str** | The value of the variable. | 
**created_at** | **datetime** | The date and time at which the variable was created, in ISO 8601 format&#39;:&#39; YYYY-MM-DDTHH:MM:SSZ. | 
**updated_at** | **datetime** | The date and time at which the variable was last updated, in ISO 8601 format&#39;:&#39; YYYY-MM-DDTHH:MM:SSZ. | 
**visibility** | **str** | Visibility of a variable | 
**selected_repositories_url** | **str** |  | [optional] 

## Example

```python
from github_openapi.models.organization_actions_variable import OrganizationActionsVariable

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationActionsVariable from a JSON string
organization_actions_variable_instance = OrganizationActionsVariable.from_json(json)
# print the JSON string representation of the object
print(OrganizationActionsVariable.to_json())

# convert the object into a dict
organization_actions_variable_dict = organization_actions_variable_instance.to_dict()
# create an instance of OrganizationActionsVariable from a dict
organization_actions_variable_from_dict = OrganizationActionsVariable.from_dict(organization_actions_variable_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


