# ActionsCreateOrgVariableRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the variable. | 
**value** | **str** | The value of the variable. | 
**visibility** | **str** | The type of repositories in the organization that can access the variable. &#x60;selected&#x60; means only the repositories specified by &#x60;selected_repository_ids&#x60; can access the variable. | 
**selected_repository_ids** | **List[int]** | An array of repository ids that can access the organization variable. You can only provide a list of repository ids when the &#x60;visibility&#x60; is set to &#x60;selected&#x60;. | [optional] 

## Example

```python
from github_openapi.models.actions_create_org_variable_request import ActionsCreateOrgVariableRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ActionsCreateOrgVariableRequest from a JSON string
actions_create_org_variable_request_instance = ActionsCreateOrgVariableRequest.from_json(json)
# print the JSON string representation of the object
print(ActionsCreateOrgVariableRequest.to_json())

# convert the object into a dict
actions_create_org_variable_request_dict = actions_create_org_variable_request_instance.to_dict()
# create an instance of ActionsCreateOrgVariableRequest from a dict
actions_create_org_variable_request_from_dict = ActionsCreateOrgVariableRequest.from_dict(actions_create_org_variable_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


