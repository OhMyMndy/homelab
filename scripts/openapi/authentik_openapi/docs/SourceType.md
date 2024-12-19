# SourceType

Serializer for SourceType

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**verbose_name** | **str** |  | 
**urls_customizable** | **bool** |  | 
**request_token_url** | **str** |  | [readonly] 
**authorization_url** | **str** |  | [readonly] 
**access_token_url** | **str** |  | [readonly] 
**profile_url** | **str** |  | [readonly] 
**oidc_well_known_url** | **str** |  | [readonly] 
**oidc_jwks_url** | **str** |  | [readonly] 

## Example

```python
from authentik_openapi.models.source_type import SourceType

# TODO update the JSON string below
json = "{}"
# create an instance of SourceType from a JSON string
source_type_instance = SourceType.from_json(json)
# print the JSON string representation of the object
print(SourceType.to_json())

# convert the object into a dict
source_type_dict = source_type_instance.to_dict()
# create an instance of SourceType from a dict
source_type_from_dict = SourceType.from_dict(source_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


