# ReposUpdateStatusCheckProtectionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**strict** | **bool** | Require branches to be up to date before merging. | [optional] 
**contexts** | **List[str]** | **Closing down notice**: The list of status checks to require in order to merge into this branch. If any of these checks have recently been set by a particular GitHub App, they will be required to come from that app in future for the branch to merge. Use &#x60;checks&#x60; instead of &#x60;contexts&#x60; for more fine-grained control. | [optional] 
**checks** | [**List[ReposUpdateBranchProtectionRequestRequiredStatusChecksChecksInner]**](ReposUpdateBranchProtectionRequestRequiredStatusChecksChecksInner.md) | The list of status checks to require in order to merge into this branch. | [optional] 

## Example

```python
from github_openapi.models.repos_update_status_check_protection_request import ReposUpdateStatusCheckProtectionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReposUpdateStatusCheckProtectionRequest from a JSON string
repos_update_status_check_protection_request_instance = ReposUpdateStatusCheckProtectionRequest.from_json(json)
# print the JSON string representation of the object
print(ReposUpdateStatusCheckProtectionRequest.to_json())

# convert the object into a dict
repos_update_status_check_protection_request_dict = repos_update_status_check_protection_request_instance.to_dict()
# create an instance of ReposUpdateStatusCheckProtectionRequest from a dict
repos_update_status_check_protection_request_from_dict = ReposUpdateStatusCheckProtectionRequest.from_dict(repos_update_status_check_protection_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


