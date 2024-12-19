# DependabotSecret

Set secrets for Dependabot.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the secret. | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from github_openapi.models.dependabot_secret import DependabotSecret

# TODO update the JSON string below
json = "{}"
# create an instance of DependabotSecret from a JSON string
dependabot_secret_instance = DependabotSecret.from_json(json)
# print the JSON string representation of the object
print(DependabotSecret.to_json())

# convert the object into a dict
dependabot_secret_dict = dependabot_secret_instance.to_dict()
# create an instance of DependabotSecret from a dict
dependabot_secret_from_dict = DependabotSecret.from_dict(dependabot_secret_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


