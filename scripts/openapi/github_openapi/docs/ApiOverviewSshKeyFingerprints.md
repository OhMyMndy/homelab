# ApiOverviewSshKeyFingerprints


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sha256_rsa** | **str** |  | [optional] 
**sha256_dsa** | **str** |  | [optional] 
**sha256_ecdsa** | **str** |  | [optional] 
**sha256_ed25519** | **str** |  | [optional] 

## Example

```python
from github_openapi.models.api_overview_ssh_key_fingerprints import ApiOverviewSshKeyFingerprints

# TODO update the JSON string below
json = "{}"
# create an instance of ApiOverviewSshKeyFingerprints from a JSON string
api_overview_ssh_key_fingerprints_instance = ApiOverviewSshKeyFingerprints.from_json(json)
# print the JSON string representation of the object
print(ApiOverviewSshKeyFingerprints.to_json())

# convert the object into a dict
api_overview_ssh_key_fingerprints_dict = api_overview_ssh_key_fingerprints_instance.to_dict()
# create an instance of ApiOverviewSshKeyFingerprints from a dict
api_overview_ssh_key_fingerprints_from_dict = ApiOverviewSshKeyFingerprints.from_dict(api_overview_ssh_key_fingerprints_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


