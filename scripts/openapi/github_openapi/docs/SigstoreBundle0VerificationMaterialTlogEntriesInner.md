# SigstoreBundle0VerificationMaterialTlogEntriesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**log_index** | **str** |  | [optional] 
**log_id** | [**SigstoreBundle0VerificationMaterialTlogEntriesInnerLogId**](SigstoreBundle0VerificationMaterialTlogEntriesInnerLogId.md) |  | [optional] 
**kind_version** | [**SigstoreBundle0VerificationMaterialTlogEntriesInnerKindVersion**](SigstoreBundle0VerificationMaterialTlogEntriesInnerKindVersion.md) |  | [optional] 
**integrated_time** | **str** |  | [optional] 
**inclusion_promise** | [**SigstoreBundle0VerificationMaterialTlogEntriesInnerInclusionPromise**](SigstoreBundle0VerificationMaterialTlogEntriesInnerInclusionPromise.md) |  | [optional] 
**inclusion_proof** | **str** |  | [optional] 
**canonicalized_body** | **str** |  | [optional] 

## Example

```python
from github_openapi.models.sigstore_bundle0_verification_material_tlog_entries_inner import SigstoreBundle0VerificationMaterialTlogEntriesInner

# TODO update the JSON string below
json = "{}"
# create an instance of SigstoreBundle0VerificationMaterialTlogEntriesInner from a JSON string
sigstore_bundle0_verification_material_tlog_entries_inner_instance = SigstoreBundle0VerificationMaterialTlogEntriesInner.from_json(json)
# print the JSON string representation of the object
print(SigstoreBundle0VerificationMaterialTlogEntriesInner.to_json())

# convert the object into a dict
sigstore_bundle0_verification_material_tlog_entries_inner_dict = sigstore_bundle0_verification_material_tlog_entries_inner_instance.to_dict()
# create an instance of SigstoreBundle0VerificationMaterialTlogEntriesInner from a dict
sigstore_bundle0_verification_material_tlog_entries_inner_from_dict = SigstoreBundle0VerificationMaterialTlogEntriesInner.from_dict(sigstore_bundle0_verification_material_tlog_entries_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


