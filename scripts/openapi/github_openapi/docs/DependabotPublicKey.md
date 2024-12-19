# DependabotPublicKey

The public key used for setting Dependabot Secrets.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key_id** | **str** | The identifier for the key. | 
**key** | **str** | The Base64 encoded public key. | 

## Example

```python
from github_openapi.models.dependabot_public_key import DependabotPublicKey

# TODO update the JSON string below
json = "{}"
# create an instance of DependabotPublicKey from a JSON string
dependabot_public_key_instance = DependabotPublicKey.from_json(json)
# print the JSON string representation of the object
print(DependabotPublicKey.to_json())

# convert the object into a dict
dependabot_public_key_dict = dependabot_public_key_instance.to_dict()
# create an instance of DependabotPublicKey from a dict
dependabot_public_key_from_dict = DependabotPublicKey.from_dict(dependabot_public_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


