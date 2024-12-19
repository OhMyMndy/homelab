# TokenSetKeyRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | 

## Example

```python
from authentik_openapi.models.token_set_key_request import TokenSetKeyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TokenSetKeyRequest from a JSON string
token_set_key_request_instance = TokenSetKeyRequest.from_json(json)
# print the JSON string representation of the object
print(TokenSetKeyRequest.to_json())

# convert the object into a dict
token_set_key_request_dict = token_set_key_request_instance.to_dict()
# create an instance of TokenSetKeyRequest from a dict
token_set_key_request_from_dict = TokenSetKeyRequest.from_dict(token_set_key_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


