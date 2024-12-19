# ActionsSetSelectedReposForOrgVariableRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**selected_repository_ids** | **List[int]** | The IDs of the repositories that can access the organization variable. | 

## Example

```python
from github_openapi.models.actions_set_selected_repos_for_org_variable_request import ActionsSetSelectedReposForOrgVariableRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ActionsSetSelectedReposForOrgVariableRequest from a JSON string
actions_set_selected_repos_for_org_variable_request_instance = ActionsSetSelectedReposForOrgVariableRequest.from_json(json)
# print the JSON string representation of the object
print(ActionsSetSelectedReposForOrgVariableRequest.to_json())

# convert the object into a dict
actions_set_selected_repos_for_org_variable_request_dict = actions_set_selected_repos_for_org_variable_request_instance.to_dict()
# create an instance of ActionsSetSelectedReposForOrgVariableRequest from a dict
actions_set_selected_repos_for_org_variable_request_from_dict = ActionsSetSelectedReposForOrgVariableRequest.from_dict(actions_set_selected_repos_for_org_variable_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


