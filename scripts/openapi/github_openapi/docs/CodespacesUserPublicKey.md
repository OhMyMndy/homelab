# CodespacesUserPublicKey

The public key used for setting user Codespaces' Secrets.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key_id** | **str** | The identifier for the key. | 
**key** | **str** | The Base64 encoded public key. | 

## Example

```python
from github_openapi.models.codespaces_user_public_key import CodespacesUserPublicKey

# TODO update the JSON string below
json = "{}"
# create an instance of CodespacesUserPublicKey from a JSON string
codespaces_user_public_key_instance = CodespacesUserPublicKey.from_json(json)
# print the JSON string representation of the object
print(CodespacesUserPublicKey.to_json())

# convert the object into a dict
codespaces_user_public_key_dict = codespaces_user_public_key_instance.to_dict()
# create an instance of CodespacesUserPublicKey from a dict
codespaces_user_public_key_from_dict = CodespacesUserPublicKey.from_dict(codespaces_user_public_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


