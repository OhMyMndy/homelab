# ApiOverviewDomainsArtifactAttestations


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**trust_domain** | **str** |  | [optional] 
**services** | **List[str]** |  | [optional] 

## Example

```python
from github_openapi.models.api_overview_domains_artifact_attestations import ApiOverviewDomainsArtifactAttestations

# TODO update the JSON string below
json = "{}"
# create an instance of ApiOverviewDomainsArtifactAttestations from a JSON string
api_overview_domains_artifact_attestations_instance = ApiOverviewDomainsArtifactAttestations.from_json(json)
# print the JSON string representation of the object
print(ApiOverviewDomainsArtifactAttestations.to_json())

# convert the object into a dict
api_overview_domains_artifact_attestations_dict = api_overview_domains_artifact_attestations_instance.to_dict()
# create an instance of ApiOverviewDomainsArtifactAttestations from a dict
api_overview_domains_artifact_attestations_from_dict = ApiOverviewDomainsArtifactAttestations.from_dict(api_overview_domains_artifact_attestations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


