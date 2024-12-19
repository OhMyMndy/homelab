# PatchedTokenRequest

Token Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**managed** | **str** | Objects that are managed by authentik. These objects are created and updated automatically. This flag only indicates that an object can be overwritten by migrations. You can still modify the objects via the API, but expect changes to be overwritten in a later update. | [optional] 
**identifier** | **str** |  | [optional] 
**intent** | [**IntentEnum**](IntentEnum.md) |  | [optional] 
**user** | **int** |  | [optional] 
**description** | **str** |  | [optional] 
**expires** | **datetime** |  | [optional] 
**expiring** | **bool** |  | [optional] 

## Example

```python
from authentik_openapi.models.patched_token_request import PatchedTokenRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedTokenRequest from a JSON string
patched_token_request_instance = PatchedTokenRequest.from_json(json)
# print the JSON string representation of the object
print(PatchedTokenRequest.to_json())

# convert the object into a dict
patched_token_request_dict = patched_token_request_instance.to_dict()
# create an instance of PatchedTokenRequest from a dict
patched_token_request_from_dict = PatchedTokenRequest.from_dict(patched_token_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


