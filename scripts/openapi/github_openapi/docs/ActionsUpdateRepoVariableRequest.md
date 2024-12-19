# ActionsUpdateRepoVariableRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the variable. | [optional] 
**value** | **str** | The value of the variable. | [optional] 

## Example

```python
from github_openapi.models.actions_update_repo_variable_request import ActionsUpdateRepoVariableRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ActionsUpdateRepoVariableRequest from a JSON string
actions_update_repo_variable_request_instance = ActionsUpdateRepoVariableRequest.from_json(json)
# print the JSON string representation of the object
print(ActionsUpdateRepoVariableRequest.to_json())

# convert the object into a dict
actions_update_repo_variable_request_dict = actions_update_repo_variable_request_instance.to_dict()
# create an instance of ActionsUpdateRepoVariableRequest from a dict
actions_update_repo_variable_request_from_dict = ActionsUpdateRepoVariableRequest.from_dict(actions_update_repo_variable_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


