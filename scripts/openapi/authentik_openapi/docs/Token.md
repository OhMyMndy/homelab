# Token

Token Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk** | **str** |  | [readonly] 
**managed** | **str** | Objects that are managed by authentik. These objects are created and updated automatically. This flag only indicates that an object can be overwritten by migrations. You can still modify the objects via the API, but expect changes to be overwritten in a later update. | [optional] 
**identifier** | **str** |  | 
**intent** | [**IntentEnum**](IntentEnum.md) |  | [optional] 
**user** | **int** |  | [optional] 
**user_obj** | [**User**](User.md) |  | [readonly] 
**description** | **str** |  | [optional] 
**expires** | **datetime** |  | [optional] 
**expiring** | **bool** |  | [optional] 

## Example

```python
from authentik_openapi.models.token import Token

# TODO update the JSON string below
json = "{}"
# create an instance of Token from a JSON string
token_instance = Token.from_json(json)
# print the JSON string representation of the object
print(Token.to_json())

# convert the object into a dict
token_dict = token_instance.to_dict()
# create an instance of Token from a dict
token_from_dict = Token.from_dict(token_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


