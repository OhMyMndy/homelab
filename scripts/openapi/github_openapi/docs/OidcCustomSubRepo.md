# OidcCustomSubRepo

Actions OIDC subject customization for a repository

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**use_default** | **bool** | Whether to use the default template or not. If &#x60;true&#x60;, the &#x60;include_claim_keys&#x60; field is ignored. | 
**include_claim_keys** | **List[str]** | Array of unique strings. Each claim key can only contain alphanumeric characters and underscores. | [optional] 

## Example

```python
from github_openapi.models.oidc_custom_sub_repo import OidcCustomSubRepo

# TODO update the JSON string below
json = "{}"
# create an instance of OidcCustomSubRepo from a JSON string
oidc_custom_sub_repo_instance = OidcCustomSubRepo.from_json(json)
# print the JSON string representation of the object
print(OidcCustomSubRepo.to_json())

# convert the object into a dict
oidc_custom_sub_repo_dict = oidc_custom_sub_repo_instance.to_dict()
# create an instance of OidcCustomSubRepo from a dict
oidc_custom_sub_repo_from_dict = OidcCustomSubRepo.from_dict(oidc_custom_sub_repo_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


