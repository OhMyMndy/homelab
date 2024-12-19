# SshSigningKey

A public SSH key used to sign Git commits

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | 
**id** | **int** |  | 
**title** | **str** |  | 
**created_at** | **datetime** |  | 

## Example

```python
from github_openapi.models.ssh_signing_key import SshSigningKey

# TODO update the JSON string below
json = "{}"
# create an instance of SshSigningKey from a JSON string
ssh_signing_key_instance = SshSigningKey.from_json(json)
# print the JSON string representation of the object
print(SshSigningKey.to_json())

# convert the object into a dict
ssh_signing_key_dict = ssh_signing_key_instance.to_dict()
# create an instance of SshSigningKey from a dict
ssh_signing_key_from_dict = SshSigningKey.from_dict(ssh_signing_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


