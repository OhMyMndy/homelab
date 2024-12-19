# RunnerLabel

A label for a self hosted runner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier of the label. | [optional] 
**name** | **str** | Name of the label. | 
**type** | **str** | The type of label. Read-only labels are applied automatically when the runner is configured. | [optional] 

## Example

```python
from github_openapi.models.runner_label import RunnerLabel

# TODO update the JSON string below
json = "{}"
# create an instance of RunnerLabel from a JSON string
runner_label_instance = RunnerLabel.from_json(json)
# print the JSON string representation of the object
print(RunnerLabel.to_json())

# convert the object into a dict
runner_label_dict = runner_label_instance.to_dict()
# create an instance of RunnerLabel from a dict
runner_label_from_dict = RunnerLabel.from_dict(runner_label_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


