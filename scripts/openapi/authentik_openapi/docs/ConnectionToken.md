# ConnectionToken

ConnectionToken Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk** | **str** |  | [optional] 
**provider** | **int** |  | 
**provider_obj** | [**RACProvider**](RACProvider.md) |  | [readonly] 
**endpoint** | **str** |  | 
**endpoint_obj** | [**Endpoint**](Endpoint.md) |  | [readonly] 
**user** | [**GroupMember**](GroupMember.md) |  | [readonly] 

## Example

```python
from authentik_openapi.models.connection_token import ConnectionToken

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectionToken from a JSON string
connection_token_instance = ConnectionToken.from_json(json)
# print the JSON string representation of the object
print(ConnectionToken.to_json())

# convert the object into a dict
connection_token_dict = connection_token_instance.to_dict()
# create an instance of ConnectionToken from a dict
connection_token_from_dict = ConnectionToken.from_dict(connection_token_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


