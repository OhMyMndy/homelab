# ApiOverview

Api Overview

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**verifiable_password_authentication** | **bool** |  | 
**ssh_key_fingerprints** | [**ApiOverviewSshKeyFingerprints**](ApiOverviewSshKeyFingerprints.md) |  | [optional] 
**ssh_keys** | **List[str]** |  | [optional] 
**hooks** | **List[str]** |  | [optional] 
**github_enterprise_importer** | **List[str]** |  | [optional] 
**web** | **List[str]** |  | [optional] 
**api** | **List[str]** |  | [optional] 
**git** | **List[str]** |  | [optional] 
**packages** | **List[str]** |  | [optional] 
**pages** | **List[str]** |  | [optional] 
**importer** | **List[str]** |  | [optional] 
**actions** | **List[str]** |  | [optional] 
**actions_macos** | **List[str]** |  | [optional] 
**codespaces** | **List[str]** |  | [optional] 
**dependabot** | **List[str]** |  | [optional] 
**copilot** | **List[str]** |  | [optional] 
**domains** | [**ApiOverviewDomains**](ApiOverviewDomains.md) |  | [optional] 

## Example

```python
from github_openapi.models.api_overview import ApiOverview

# TODO update the JSON string below
json = "{}"
# create an instance of ApiOverview from a JSON string
api_overview_instance = ApiOverview.from_json(json)
# print the JSON string representation of the object
print(ApiOverview.to_json())

# convert the object into a dict
api_overview_dict = api_overview_instance.to_dict()
# create an instance of ApiOverview from a dict
api_overview_from_dict = ApiOverview.from_dict(api_overview_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


