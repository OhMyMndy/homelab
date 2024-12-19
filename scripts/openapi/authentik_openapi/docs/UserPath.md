# UserPath


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**paths** | **List[str]** |  | [readonly] 

## Example

```python
from authentik_openapi.models.user_path import UserPath

# TODO update the JSON string below
json = "{}"
# create an instance of UserPath from a JSON string
user_path_instance = UserPath.from_json(json)
# print the JSON string representation of the object
print(UserPath.to_json())

# convert the object into a dict
user_path_dict = user_path_instance.to_dict()
# create an instance of UserPath from a dict
user_path_from_dict = UserPath.from_dict(user_path_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


