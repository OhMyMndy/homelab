# CertificateData

Get CertificateKeyPair's data

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **str** |  | [readonly] 

## Example

```python
from authentik_openapi.models.certificate_data import CertificateData

# TODO update the JSON string below
json = "{}"
# create an instance of CertificateData from a JSON string
certificate_data_instance = CertificateData.from_json(json)
# print the JSON string representation of the object
print(CertificateData.to_json())

# convert the object into a dict
certificate_data_dict = certificate_data_instance.to_dict()
# create an instance of CertificateData from a dict
certificate_data_from_dict = CertificateData.from_dict(certificate_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


