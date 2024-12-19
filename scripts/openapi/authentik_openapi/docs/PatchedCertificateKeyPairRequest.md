# PatchedCertificateKeyPairRequest

CertificateKeyPair Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**certificate_data** | **str** | PEM-encoded Certificate data | [optional] 
**key_data** | **str** | Optional Private Key. If this is set, you can use this keypair for encryption. | [optional] 

## Example

```python
from authentik_openapi.models.patched_certificate_key_pair_request import PatchedCertificateKeyPairRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedCertificateKeyPairRequest from a JSON string
patched_certificate_key_pair_request_instance = PatchedCertificateKeyPairRequest.from_json(json)
# print the JSON string representation of the object
print(PatchedCertificateKeyPairRequest.to_json())

# convert the object into a dict
patched_certificate_key_pair_request_dict = patched_certificate_key_pair_request_instance.to_dict()
# create an instance of PatchedCertificateKeyPairRequest from a dict
patched_certificate_key_pair_request_from_dict = PatchedCertificateKeyPairRequest.from_dict(patched_certificate_key_pair_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


