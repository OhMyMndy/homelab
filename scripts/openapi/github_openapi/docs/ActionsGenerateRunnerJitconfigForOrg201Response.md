# ActionsGenerateRunnerJitconfigForOrg201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**runner** | [**Runner**](Runner.md) |  | 
**encoded_jit_config** | **str** | The base64 encoded runner configuration. | 

## Example

```python
from github_openapi.models.actions_generate_runner_jitconfig_for_org201_response import ActionsGenerateRunnerJitconfigForOrg201Response

# TODO update the JSON string below
json = "{}"
# create an instance of ActionsGenerateRunnerJitconfigForOrg201Response from a JSON string
actions_generate_runner_jitconfig_for_org201_response_instance = ActionsGenerateRunnerJitconfigForOrg201Response.from_json(json)
# print the JSON string representation of the object
print(ActionsGenerateRunnerJitconfigForOrg201Response.to_json())

# convert the object into a dict
actions_generate_runner_jitconfig_for_org201_response_dict = actions_generate_runner_jitconfig_for_org201_response_instance.to_dict()
# create an instance of ActionsGenerateRunnerJitconfigForOrg201Response from a dict
actions_generate_runner_jitconfig_for_org201_response_from_dict = ActionsGenerateRunnerJitconfigForOrg201Response.from_dict(actions_generate_runner_jitconfig_for_org201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


