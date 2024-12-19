# SigstoreBundle0VerificationMaterial


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**x509_certificate_chain** | [**SigstoreBundle0VerificationMaterialX509CertificateChain**](SigstoreBundle0VerificationMaterialX509CertificateChain.md) |  | [optional] 
**tlog_entries** | [**List[SigstoreBundle0VerificationMaterialTlogEntriesInner]**](SigstoreBundle0VerificationMaterialTlogEntriesInner.md) |  | [optional] 
**timestamp_verification_data** | **str** |  | [optional] 

## Example

```python
from github_openapi.models.sigstore_bundle0_verification_material import SigstoreBundle0VerificationMaterial

# TODO update the JSON string below
json = "{}"
# create an instance of SigstoreBundle0VerificationMaterial from a JSON string
sigstore_bundle0_verification_material_instance = SigstoreBundle0VerificationMaterial.from_json(json)
# print the JSON string representation of the object
print(SigstoreBundle0VerificationMaterial.to_json())

# convert the object into a dict
sigstore_bundle0_verification_material_dict = sigstore_bundle0_verification_material_instance.to_dict()
# create an instance of SigstoreBundle0VerificationMaterial from a dict
sigstore_bundle0_verification_material_from_dict = SigstoreBundle0VerificationMaterial.from_dict(sigstore_bundle0_verification_material_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


