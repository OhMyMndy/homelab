# Runner

A self hosted runner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The id of the runner. | 
**runner_group_id** | **int** | The id of the runner group. | [optional] 
**name** | **str** | The name of the runner. | 
**os** | **str** | The Operating System of the runner. | 
**status** | **str** | The status of the runner. | 
**busy** | **bool** |  | 
**labels** | [**List[RunnerLabel]**](RunnerLabel.md) |  | 

## Example

```python
from github_openapi.models.runner import Runner

# TODO update the JSON string below
json = "{}"
# create an instance of Runner from a JSON string
runner_instance = Runner.from_json(json)
# print the JSON string representation of the object
print(Runner.to_json())

# convert the object into a dict
runner_dict = runner_instance.to_dict()
# create an instance of Runner from a dict
runner_from_dict = Runner.from_dict(runner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


