# ActionsListRepoAccessToSelfHostedRunnerGroupInOrg200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_count** | **float** |  | 
**repositories** | [**List[MinimalRepository]**](MinimalRepository.md) |  | 

## Example

```python
from github_openapi.models.actions_list_repo_access_to_self_hosted_runner_group_in_org200_response import ActionsListRepoAccessToSelfHostedRunnerGroupInOrg200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ActionsListRepoAccessToSelfHostedRunnerGroupInOrg200Response from a JSON string
actions_list_repo_access_to_self_hosted_runner_group_in_org200_response_instance = ActionsListRepoAccessToSelfHostedRunnerGroupInOrg200Response.from_json(json)
# print the JSON string representation of the object
print(ActionsListRepoAccessToSelfHostedRunnerGroupInOrg200Response.to_json())

# convert the object into a dict
actions_list_repo_access_to_self_hosted_runner_group_in_org200_response_dict = actions_list_repo_access_to_self_hosted_runner_group_in_org200_response_instance.to_dict()
# create an instance of ActionsListRepoAccessToSelfHostedRunnerGroupInOrg200Response from a dict
actions_list_repo_access_to_self_hosted_runner_group_in_org200_response_from_dict = ActionsListRepoAccessToSelfHostedRunnerGroupInOrg200Response.from_dict(actions_list_repo_access_to_self_hosted_runner_group_in_org200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


