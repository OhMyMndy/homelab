# ActionsSecret

Set secrets for GitHub Actions.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the secret. | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from github_openapi.models.actions_secret import ActionsSecret

# TODO update the JSON string below
json = "{}"
# create an instance of ActionsSecret from a JSON string
actions_secret_instance = ActionsSecret.from_json(json)
# print the JSON string representation of the object
print(ActionsSecret.to_json())

# convert the object into a dict
actions_secret_dict = actions_secret_instance.to_dict()
# create an instance of ActionsSecret from a dict
actions_secret_from_dict = ActionsSecret.from_dict(actions_secret_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


