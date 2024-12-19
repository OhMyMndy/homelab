# ReposCreateAttestationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bundle** | [**OrgsListAttestations200ResponseAttestationsInnerBundle**](OrgsListAttestations200ResponseAttestationsInnerBundle.md) |  | 

## Example

```python
from github_openapi.models.repos_create_attestation_request import ReposCreateAttestationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReposCreateAttestationRequest from a JSON string
repos_create_attestation_request_instance = ReposCreateAttestationRequest.from_json(json)
# print the JSON string representation of the object
print(ReposCreateAttestationRequest.to_json())

# convert the object into a dict
repos_create_attestation_request_dict = repos_create_attestation_request_instance.to_dict()
# create an instance of ReposCreateAttestationRequest from a dict
repos_create_attestation_request_from_dict = ReposCreateAttestationRequest.from_dict(repos_create_attestation_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


