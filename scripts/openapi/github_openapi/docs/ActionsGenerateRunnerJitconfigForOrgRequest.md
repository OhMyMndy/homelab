# ActionsGenerateRunnerJitconfigForOrgRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the new runner. | 
**runner_group_id** | **int** | The ID of the runner group to register the runner to. | 
**labels** | **List[str]** | The names of the custom labels to add to the runner. **Minimum items**: 1. **Maximum items**: 100. | 
**work_folder** | **str** | The working directory to be used for job execution, relative to the runner install directory. | [optional] [default to '_work']

## Example

```python
from github_openapi.models.actions_generate_runner_jitconfig_for_org_request import ActionsGenerateRunnerJitconfigForOrgRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ActionsGenerateRunnerJitconfigForOrgRequest from a JSON string
actions_generate_runner_jitconfig_for_org_request_instance = ActionsGenerateRunnerJitconfigForOrgRequest.from_json(json)
# print the JSON string representation of the object
print(ActionsGenerateRunnerJitconfigForOrgRequest.to_json())

# convert the object into a dict
actions_generate_runner_jitconfig_for_org_request_dict = actions_generate_runner_jitconfig_for_org_request_instance.to_dict()
# create an instance of ActionsGenerateRunnerJitconfigForOrgRequest from a dict
actions_generate_runner_jitconfig_for_org_request_from_dict = ActionsGenerateRunnerJitconfigForOrgRequest.from_dict(actions_generate_runner_jitconfig_for_org_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


