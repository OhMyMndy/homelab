# ApiOverviewDomains


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**website** | **List[str]** |  | [optional] 
**codespaces** | **List[str]** |  | [optional] 
**copilot** | **List[str]** |  | [optional] 
**packages** | **List[str]** |  | [optional] 
**actions** | **List[str]** |  | [optional] 
**actions_inbound** | [**ApiOverviewDomainsActionsInbound**](ApiOverviewDomainsActionsInbound.md) |  | [optional] 
**artifact_attestations** | [**ApiOverviewDomainsArtifactAttestations**](ApiOverviewDomainsArtifactAttestations.md) |  | [optional] 

## Example

```python
from github_openapi.models.api_overview_domains import ApiOverviewDomains

# TODO update the JSON string below
json = "{}"
# create an instance of ApiOverviewDomains from a JSON string
api_overview_domains_instance = ApiOverviewDomains.from_json(json)
# print the JSON string representation of the object
print(ApiOverviewDomains.to_json())

# convert the object into a dict
api_overview_domains_dict = api_overview_domains_instance.to_dict()
# create an instance of ApiOverviewDomains from a dict
api_overview_domains_from_dict = ApiOverviewDomains.from_dict(api_overview_domains_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


