# OrgsListAttestations200ResponseAttestationsInnerBundle

The attestation's Sigstore Bundle. Refer to the [Sigstore Bundle Specification](https://github.com/sigstore/protobuf-specs/blob/main/protos/sigstore_bundle.proto) for more information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**media_type** | **str** |  | [optional] 
**verification_material** | **Dict[str, object]** |  | [optional] 
**dsse_envelope** | **Dict[str, object]** |  | [optional] 

## Example

```python
from github_openapi.models.orgs_list_attestations200_response_attestations_inner_bundle import OrgsListAttestations200ResponseAttestationsInnerBundle

# TODO update the JSON string below
json = "{}"
# create an instance of OrgsListAttestations200ResponseAttestationsInnerBundle from a JSON string
orgs_list_attestations200_response_attestations_inner_bundle_instance = OrgsListAttestations200ResponseAttestationsInnerBundle.from_json(json)
# print the JSON string representation of the object
print(OrgsListAttestations200ResponseAttestationsInnerBundle.to_json())

# convert the object into a dict
orgs_list_attestations200_response_attestations_inner_bundle_dict = orgs_list_attestations200_response_attestations_inner_bundle_instance.to_dict()
# create an instance of OrgsListAttestations200ResponseAttestationsInnerBundle from a dict
orgs_list_attestations200_response_attestations_inner_bundle_from_dict = OrgsListAttestations200ResponseAttestationsInnerBundle.from_dict(orgs_list_attestations200_response_attestations_inner_bundle_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


