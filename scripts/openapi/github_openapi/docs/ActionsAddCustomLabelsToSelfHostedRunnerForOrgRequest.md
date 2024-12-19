# ActionsAddCustomLabelsToSelfHostedRunnerForOrgRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**labels** | **List[str]** | The names of the custom labels to add to the runner. | 

## Example

```python
from github_openapi.models.actions_add_custom_labels_to_self_hosted_runner_for_org_request import ActionsAddCustomLabelsToSelfHostedRunnerForOrgRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ActionsAddCustomLabelsToSelfHostedRunnerForOrgRequest from a JSON string
actions_add_custom_labels_to_self_hosted_runner_for_org_request_instance = ActionsAddCustomLabelsToSelfHostedRunnerForOrgRequest.from_json(json)
# print the JSON string representation of the object
print(ActionsAddCustomLabelsToSelfHostedRunnerForOrgRequest.to_json())

# convert the object into a dict
actions_add_custom_labels_to_self_hosted_runner_for_org_request_dict = actions_add_custom_labels_to_self_hosted_runner_for_org_request_instance.to_dict()
# create an instance of ActionsAddCustomLabelsToSelfHostedRunnerForOrgRequest from a dict
actions_add_custom_labels_to_self_hosted_runner_for_org_request_from_dict = ActionsAddCustomLabelsToSelfHostedRunnerForOrgRequest.from_dict(actions_add_custom_labels_to_self_hosted_runner_for_org_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


