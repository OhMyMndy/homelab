# SigstoreBundle0DsseEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payload** | **str** |  | [optional] 
**payload_type** | **str** |  | [optional] 
**signatures** | [**List[SigstoreBundle0DsseEnvelopeSignaturesInner]**](SigstoreBundle0DsseEnvelopeSignaturesInner.md) |  | [optional] 

## Example

```python
from github_openapi.models.sigstore_bundle0_dsse_envelope import SigstoreBundle0DsseEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of SigstoreBundle0DsseEnvelope from a JSON string
sigstore_bundle0_dsse_envelope_instance = SigstoreBundle0DsseEnvelope.from_json(json)
# print the JSON string representation of the object
print(SigstoreBundle0DsseEnvelope.to_json())

# convert the object into a dict
sigstore_bundle0_dsse_envelope_dict = sigstore_bundle0_dsse_envelope_instance.to_dict()
# create an instance of SigstoreBundle0DsseEnvelope from a dict
sigstore_bundle0_dsse_envelope_from_dict = SigstoreBundle0DsseEnvelope.from_dict(sigstore_bundle0_dsse_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


