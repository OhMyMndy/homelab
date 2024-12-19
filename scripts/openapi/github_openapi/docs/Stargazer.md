# Stargazer

Stargazer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**starred_at** | **datetime** |  | 
**user** | [**NullableSimpleUser**](NullableSimpleUser.md) |  | 

## Example

```python
from github_openapi.models.stargazer import Stargazer

# TODO update the JSON string below
json = "{}"
# create an instance of Stargazer from a JSON string
stargazer_instance = Stargazer.from_json(json)
# print the JSON string representation of the object
print(Stargazer.to_json())

# convert the object into a dict
stargazer_dict = stargazer_instance.to_dict()
# create an instance of Stargazer from a dict
stargazer_from_dict = Stargazer.from_dict(stargazer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


