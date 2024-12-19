# ExpiringBaseGrantModel

Serializer for BaseGrantModel and ExpiringBaseGrant

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk** | **int** |  | [readonly] 
**provider** | [**OAuth2Provider**](OAuth2Provider.md) |  | 
**user** | [**User**](User.md) |  | 
**is_expired** | **bool** | Check if token is expired yet. | [readonly] 
**expires** | **datetime** |  | [optional] 
**scope** | **List[str]** |  | 

## Example

```python
from authentik_openapi.models.expiring_base_grant_model import ExpiringBaseGrantModel

# TODO update the JSON string below
json = "{}"
# create an instance of ExpiringBaseGrantModel from a JSON string
expiring_base_grant_model_instance = ExpiringBaseGrantModel.from_json(json)
# print the JSON string representation of the object
print(ExpiringBaseGrantModel.to_json())

# convert the object into a dict
expiring_base_grant_model_dict = expiring_base_grant_model_instance.to_dict()
# create an instance of ExpiringBaseGrantModel from a dict
expiring_base_grant_model_from_dict = ExpiringBaseGrantModel.from_dict(expiring_base_grant_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


