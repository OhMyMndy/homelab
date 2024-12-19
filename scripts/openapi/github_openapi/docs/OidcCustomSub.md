# OidcCustomSub

Actions OIDC Subject customization

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include_claim_keys** | **List[str]** | Array of unique strings. Each claim key can only contain alphanumeric characters and underscores. | 

## Example

```python
from github_openapi.models.oidc_custom_sub import OidcCustomSub

# TODO update the JSON string below
json = "{}"
# create an instance of OidcCustomSub from a JSON string
oidc_custom_sub_instance = OidcCustomSub.from_json(json)
# print the JSON string representation of the object
print(OidcCustomSub.to_json())

# convert the object into a dict
oidc_custom_sub_dict = oidc_custom_sub_instance.to_dict()
# create an instance of OidcCustomSub from a dict
oidc_custom_sub_from_dict = OidcCustomSub.from_dict(oidc_custom_sub_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


