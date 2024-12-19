# RunnerApplication

Runner Application

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**os** | **str** |  | 
**architecture** | **str** |  | 
**download_url** | **str** |  | 
**filename** | **str** |  | 
**temp_download_token** | **str** | A short lived bearer token used to download the runner, if needed. | [optional] 
**sha256_checksum** | **str** |  | [optional] 

## Example

```python
from github_openapi.models.runner_application import RunnerApplication

# TODO update the JSON string below
json = "{}"
# create an instance of RunnerApplication from a JSON string
runner_application_instance = RunnerApplication.from_json(json)
# print the JSON string representation of the object
print(RunnerApplication.to_json())

# convert the object into a dict
runner_application_dict = runner_application_instance.to_dict()
# create an instance of RunnerApplication from a dict
runner_application_from_dict = RunnerApplication.from_dict(runner_application_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


