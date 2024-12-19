# SigstoreBundle0

Sigstore Bundle v0.1

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**media_type** | **str** |  | [optional] 
**verification_material** | [**SigstoreBundle0VerificationMaterial**](SigstoreBundle0VerificationMaterial.md) |  | [optional] 
**dsse_envelope** | [**SigstoreBundle0DsseEnvelope**](SigstoreBundle0DsseEnvelope.md) |  | [optional] 

## Example

```python
from github_openapi.models.sigstore_bundle0 import SigstoreBundle0

# TODO update the JSON string below
json = "{}"
# create an instance of SigstoreBundle0 from a JSON string
sigstore_bundle0_instance = SigstoreBundle0.from_json(json)
# print the JSON string representation of the object
print(SigstoreBundle0.to_json())

# convert the object into a dict
sigstore_bundle0_dict = sigstore_bundle0_instance.to_dict()
# create an instance of SigstoreBundle0 from a dict
sigstore_bundle0_from_dict = SigstoreBundle0.from_dict(sigstore_bundle0_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


