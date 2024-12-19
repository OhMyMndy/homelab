# PatchedConnectionTokenRequest

ConnectionToken Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk** | **str** |  | [optional] 
**provider** | **int** |  | [optional] 
**endpoint** | **str** |  | [optional] 

## Example

```python
from authentik_openapi.models.patched_connection_token_request import PatchedConnectionTokenRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedConnectionTokenRequest from a JSON string
patched_connection_token_request_instance = PatchedConnectionTokenRequest.from_json(json)
# print the JSON string representation of the object
print(PatchedConnectionTokenRequest.to_json())

# convert the object into a dict
patched_connection_token_request_dict = patched_connection_token_request_instance.to_dict()
# create an instance of PatchedConnectionTokenRequest from a dict
patched_connection_token_request_from_dict = PatchedConnectionTokenRequest.from_dict(patched_connection_token_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


