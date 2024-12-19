# ConnectionTokenRequest

ConnectionToken Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk** | **str** |  | [optional] 
**provider** | **int** |  | 
**endpoint** | **str** |  | 

## Example

```python
from authentik_openapi.models.connection_token_request import ConnectionTokenRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectionTokenRequest from a JSON string
connection_token_request_instance = ConnectionTokenRequest.from_json(json)
# print the JSON string representation of the object
print(ConnectionTokenRequest.to_json())

# convert the object into a dict
connection_token_request_dict = connection_token_request_instance.to_dict()
# create an instance of ConnectionTokenRequest from a dict
connection_token_request_from_dict = ConnectionTokenRequest.from_dict(connection_token_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


