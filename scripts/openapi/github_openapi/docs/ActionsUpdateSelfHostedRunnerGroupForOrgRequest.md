# ActionsUpdateSelfHostedRunnerGroupForOrgRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the runner group. | 
**visibility** | **str** | Visibility of a runner group. You can select all repositories, select individual repositories, or all private repositories. | [optional] 
**allows_public_repositories** | **bool** | Whether the runner group can be used by &#x60;public&#x60; repositories. | [optional] [default to False]
**restricted_to_workflows** | **bool** | If &#x60;true&#x60;, the runner group will be restricted to running only the workflows specified in the &#x60;selected_workflows&#x60; array. | [optional] [default to False]
**selected_workflows** | **List[str]** | List of workflows the runner group should be allowed to run. This setting will be ignored unless &#x60;restricted_to_workflows&#x60; is set to &#x60;true&#x60;. | [optional] 

## Example

```python
from github_openapi.models.actions_update_self_hosted_runner_group_for_org_request import ActionsUpdateSelfHostedRunnerGroupForOrgRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ActionsUpdateSelfHostedRunnerGroupForOrgRequest from a JSON string
actions_update_self_hosted_runner_group_for_org_request_instance = ActionsUpdateSelfHostedRunnerGroupForOrgRequest.from_json(json)
# print the JSON string representation of the object
print(ActionsUpdateSelfHostedRunnerGroupForOrgRequest.to_json())

# convert the object into a dict
actions_update_self_hosted_runner_group_for_org_request_dict = actions_update_self_hosted_runner_group_for_org_request_instance.to_dict()
# create an instance of ActionsUpdateSelfHostedRunnerGroupForOrgRequest from a dict
actions_update_self_hosted_runner_group_for_org_request_from_dict = ActionsUpdateSelfHostedRunnerGroupForOrgRequest.from_dict(actions_update_self_hosted_runner_group_for_org_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

