# TokenModel

Serializer for BaseGrantModel and RefreshToken

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk** | **int** |  | [readonly] 
**provider** | [**OAuth2Provider**](OAuth2Provider.md) |  | 
**user** | [**User**](User.md) |  | 
**is_expired** | **bool** | Check if token is expired yet. | [readonly] 
**expires** | **datetime** |  | [optional] 
**scope** | **List[str]** |  | 
**id_token** | **str** | Get the token&#39;s id_token as JSON String | [readonly] 
**revoked** | **bool** |  | [optional] 

## Example

```python
from authentik_openapi.models.token_model import TokenModel

# TODO update the JSON string below
json = "{}"
# create an instance of TokenModel from a JSON string
token_model_instance = TokenModel.from_json(json)
# print the JSON string representation of the object
print(TokenModel.to_json())

# convert the object into a dict
token_model_dict = token_model_instance.to_dict()
# create an instance of TokenModel from a dict
token_model_from_dict = TokenModel.from_dict(token_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


