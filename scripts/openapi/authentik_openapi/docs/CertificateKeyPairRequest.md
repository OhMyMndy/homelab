# CertificateKeyPairRequest

CertificateKeyPair Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**certificate_data** | **str** | PEM-encoded Certificate data | 
**key_data** | **str** | Optional Private Key. If this is set, you can use this keypair for encryption. | [optional] 

## Example

```python
from authentik_openapi.models.certificate_key_pair_request import CertificateKeyPairRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CertificateKeyPairRequest from a JSON string
certificate_key_pair_request_instance = CertificateKeyPairRequest.from_json(json)
# print the JSON string representation of the object
print(CertificateKeyPairRequest.to_json())

# convert the object into a dict
certificate_key_pair_request_dict = certificate_key_pair_request_instance.to_dict()
# create an instance of CertificateKeyPairRequest from a dict
certificate_key_pair_request_from_dict = CertificateKeyPairRequest.from_dict(certificate_key_pair_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


