# CodespacesPublicKey

The public key used for setting Codespaces secrets.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key_id** | **str** | The identifier for the key. | 
**key** | **str** | The Base64 encoded public key. | 
**id** | **int** |  | [optional] 
**url** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 

## Example

```python
from github_openapi.models.codespaces_public_key import CodespacesPublicKey

# TODO update the JSON string below
json = "{}"
# create an instance of CodespacesPublicKey from a JSON string
codespaces_public_key_instance = CodespacesPublicKey.from_json(json)
# print the JSON string representation of the object
print(CodespacesPublicKey.to_json())

# convert the object into a dict
codespaces_public_key_dict = codespaces_public_key_instance.to_dict()
# create an instance of CodespacesPublicKey from a dict
codespaces_public_key_from_dict = CodespacesPublicKey.from_dict(codespaces_public_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


