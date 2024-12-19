# ActionsSetRepoAccessToSelfHostedRunnerGroupInOrgRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**selected_repository_ids** | **List[int]** | List of repository IDs that can access the runner group. | 

## Example

```python
from github_openapi.models.actions_set_repo_access_to_self_hosted_runner_group_in_org_request import ActionsSetRepoAccessToSelfHostedRunnerGroupInOrgRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ActionsSetRepoAccessToSelfHostedRunnerGroupInOrgRequest from a JSON string
actions_set_repo_access_to_self_hosted_runner_group_in_org_request_instance = ActionsSetRepoAccessToSelfHostedRunnerGroupInOrgRequest.from_json(json)
# print the JSON string representation of the object
print(ActionsSetRepoAccessToSelfHostedRunnerGroupInOrgRequest.to_json())

# convert the object into a dict
actions_set_repo_access_to_self_hosted_runner_group_in_org_request_dict = actions_set_repo_access_to_self_hosted_runner_group_in_org_request_instance.to_dict()
# create an instance of ActionsSetRepoAccessToSelfHostedRunnerGroupInOrgRequest from a dict
actions_set_repo_access_to_self_hosted_runner_group_in_org_request_from_dict = ActionsSetRepoAccessToSelfHostedRunnerGroupInOrgRequest.from_dict(actions_set_repo_access_to_self_hosted_runner_group_in_org_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


