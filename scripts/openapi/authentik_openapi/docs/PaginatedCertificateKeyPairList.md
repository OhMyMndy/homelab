# PaginatedCertificateKeyPairList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | 
**results** | [**List[CertificateKeyPair]**](CertificateKeyPair.md) |  | 

## Example

```python
from authentik_openapi.models.paginated_certificate_key_pair_list import PaginatedCertificateKeyPairList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedCertificateKeyPairList from a JSON string
paginated_certificate_key_pair_list_instance = PaginatedCertificateKeyPairList.from_json(json)
# print the JSON string representation of the object
print(PaginatedCertificateKeyPairList.to_json())

# convert the object into a dict
paginated_certificate_key_pair_list_dict = paginated_certificate_key_pair_list_instance.to_dict()
# create an instance of PaginatedCertificateKeyPairList from a dict
paginated_certificate_key_pair_list_from_dict = PaginatedCertificateKeyPairList.from_dict(paginated_certificate_key_pair_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


