# OrgsListAttestations200ResponseAttestationsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bundle** | [**OrgsListAttestations200ResponseAttestationsInnerBundle**](OrgsListAttestations200ResponseAttestationsInnerBundle.md) |  | [optional] 
**repository_id** | **int** |  | [optional] 
**bundle_url** | **str** |  | [optional] 

## Example

```python
from github_openapi.models.orgs_list_attestations200_response_attestations_inner import OrgsListAttestations200ResponseAttestationsInner

# TODO update the JSON string below
json = "{}"
# create an instance of OrgsListAttestations200ResponseAttestationsInner from a JSON string
orgs_list_attestations200_response_attestations_inner_instance = OrgsListAttestations200ResponseAttestationsInner.from_json(json)
# print the JSON string representation of the object
print(OrgsListAttestations200ResponseAttestationsInner.to_json())

# convert the object into a dict
orgs_list_attestations200_response_attestations_inner_dict = orgs_list_attestations200_response_attestations_inner_instance.to_dict()
# create an instance of OrgsListAttestations200ResponseAttestationsInner from a dict
orgs_list_attestations200_response_attestations_inner_from_dict = OrgsListAttestations200ResponseAttestationsInner.from_dict(orgs_list_attestations200_response_attestations_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


