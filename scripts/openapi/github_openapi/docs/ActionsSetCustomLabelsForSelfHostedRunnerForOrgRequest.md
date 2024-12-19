# ActionsSetCustomLabelsForSelfHostedRunnerForOrgRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**labels** | **List[str]** | The names of the custom labels to set for the runner. You can pass an empty array to remove all custom labels. | 

## Example

```python
from github_openapi.models.actions_set_custom_labels_for_self_hosted_runner_for_org_request import ActionsSetCustomLabelsForSelfHostedRunnerForOrgRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ActionsSetCustomLabelsForSelfHostedRunnerForOrgRequest from a JSON string
actions_set_custom_labels_for_self_hosted_runner_for_org_request_instance = ActionsSetCustomLabelsForSelfHostedRunnerForOrgRequest.from_json(json)
# print the JSON string representation of the object
print(ActionsSetCustomLabelsForSelfHostedRunnerForOrgRequest.to_json())

# convert the object into a dict
actions_set_custom_labels_for_self_hosted_runner_for_org_request_dict = actions_set_custom_labels_for_self_hosted_runner_for_org_request_instance.to_dict()
# create an instance of ActionsSetCustomLabelsForSelfHostedRunnerForOrgRequest from a dict
actions_set_custom_labels_for_self_hosted_runner_for_org_request_from_dict = ActionsSetCustomLabelsForSelfHostedRunnerForOrgRequest.from_dict(actions_set_custom_labels_for_self_hosted_runner_for_org_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


