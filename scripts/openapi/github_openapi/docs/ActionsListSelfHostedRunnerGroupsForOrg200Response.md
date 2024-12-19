# ActionsListSelfHostedRunnerGroupsForOrg200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_count** | **float** |  | 
**runner_groups** | [**List[RunnerGroupsOrg]**](RunnerGroupsOrg.md) |  | 

## Example

```python
from github_openapi.models.actions_list_self_hosted_runner_groups_for_org200_response import ActionsListSelfHostedRunnerGroupsForOrg200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ActionsListSelfHostedRunnerGroupsForOrg200Response from a JSON string
actions_list_self_hosted_runner_groups_for_org200_response_instance = ActionsListSelfHostedRunnerGroupsForOrg200Response.from_json(json)
# print the JSON string representation of the object
print(ActionsListSelfHostedRunnerGroupsForOrg200Response.to_json())

# convert the object into a dict
actions_list_self_hosted_runner_groups_for_org200_response_dict = actions_list_self_hosted_runner_groups_for_org200_response_instance.to_dict()
# create an instance of ActionsListSelfHostedRunnerGroupsForOrg200Response from a dict
actions_list_self_hosted_runner_groups_for_org200_response_from_dict = ActionsListSelfHostedRunnerGroupsForOrg200Response.from_dict(actions_list_self_hosted_runner_groups_for_org200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


