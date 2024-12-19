# ReposUpdateBranchProtectionRequestRequiredStatusChecks

Require status checks to pass before merging. Set to `null` to disable.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**strict** | **bool** | Require branches to be up to date before merging. | 
**contexts** | **List[str]** | **Closing down notice**: The list of status checks to require in order to merge into this branch. If any of these checks have recently been set by a particular GitHub App, they will be required to come from that app in future for the branch to merge. Use &#x60;checks&#x60; instead of &#x60;contexts&#x60; for more fine-grained control. | 
**checks** | [**List[ReposUpdateBranchProtectionRequestRequiredStatusChecksChecksInner]**](ReposUpdateBranchProtectionRequestRequiredStatusChecksChecksInner.md) | The list of status checks to require in order to merge into this branch. | [optional] 

## Example

```python
from github_openapi.models.repos_update_branch_protection_request_required_status_checks import ReposUpdateBranchProtectionRequestRequiredStatusChecks

# TODO update the JSON string below
json = "{}"
# create an instance of ReposUpdateBranchProtectionRequestRequiredStatusChecks from a JSON string
repos_update_branch_protection_request_required_status_checks_instance = ReposUpdateBranchProtectionRequestRequiredStatusChecks.from_json(json)
# print the JSON string representation of the object
print(ReposUpdateBranchProtectionRequestRequiredStatusChecks.to_json())

# convert the object into a dict
repos_update_branch_protection_request_required_status_checks_dict = repos_update_branch_protection_request_required_status_checks_instance.to_dict()
# create an instance of ReposUpdateBranchProtectionRequestRequiredStatusChecks from a dict
repos_update_branch_protection_request_required_status_checks_from_dict = ReposUpdateBranchProtectionRequestRequiredStatusChecks.from_dict(repos_update_branch_protection_request_required_status_checks_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


