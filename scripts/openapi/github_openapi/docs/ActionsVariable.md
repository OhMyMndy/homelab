# ActionsVariable


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the variable. | 
**value** | **str** | The value of the variable. | 
**created_at** | **datetime** | The date and time at which the variable was created, in ISO 8601 format&#39;:&#39; YYYY-MM-DDTHH:MM:SSZ. | 
**updated_at** | **datetime** | The date and time at which the variable was last updated, in ISO 8601 format&#39;:&#39; YYYY-MM-DDTHH:MM:SSZ. | 

## Example

```python
from github_openapi.models.actions_variable import ActionsVariable

# TODO update the JSON string below
json = "{}"
# create an instance of ActionsVariable from a JSON string
actions_variable_instance = ActionsVariable.from_json(json)
# print the JSON string representation of the object
print(ActionsVariable.to_json())

# convert the object into a dict
actions_variable_dict = actions_variable_instance.to_dict()
# create an instance of ActionsVariable from a dict
actions_variable_from_dict = ActionsVariable.from_dict(actions_variable_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


