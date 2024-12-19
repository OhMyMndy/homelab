# UserSourceConnection

OAuth Source Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk** | **int** |  | [readonly] 
**user** | **int** |  | [readonly] 
**source** | [**Source**](Source.md) |  | [readonly] 
**created** | **datetime** |  | [readonly] 

## Example

```python
from authentik_openapi.models.user_source_connection import UserSourceConnection

# TODO update the JSON string below
json = "{}"
# create an instance of UserSourceConnection from a JSON string
user_source_connection_instance = UserSourceConnection.from_json(json)
# print the JSON string representation of the object
print(UserSourceConnection.to_json())

# convert the object into a dict
user_source_connection_dict = user_source_connection_instance.to_dict()
# create an instance of UserSourceConnection from a dict
user_source_connection_from_dict = UserSourceConnection.from_dict(user_source_connection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


