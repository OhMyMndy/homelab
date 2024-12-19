# ReposUpdateBranchProtectionRequestRequiredStatusChecksChecksInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | **str** | The name of the required check | 
**app_id** | **int** | The ID of the GitHub App that must provide this check. Omit this field to automatically select the GitHub App that has recently provided this check, or any app if it was not set by a GitHub App. Pass -1 to explicitly allow any app to set the status. | [optional] 

## Example

```python
from github_openapi.models.repos_update_branch_protection_request_required_status_checks_checks_inner import ReposUpdateBranchProtectionRequestRequiredStatusChecksChecksInner

# TODO update the JSON string below
json = "{}"
# create an instance of ReposUpdateBranchProtectionRequestRequiredStatusChecksChecksInner from a JSON string
repos_update_branch_protection_request_required_status_checks_checks_inner_instance = ReposUpdateBranchProtectionRequestRequiredStatusChecksChecksInner.from_json(json)
# print the JSON string representation of the object
print(ReposUpdateBranchProtectionRequestRequiredStatusChecksChecksInner.to_json())

# convert the object into a dict
repos_update_branch_protection_request_required_status_checks_checks_inner_dict = repos_update_branch_protection_request_required_status_checks_checks_inner_instance.to_dict()
# create an instance of ReposUpdateBranchProtectionRequestRequiredStatusChecksChecksInner from a dict
repos_update_branch_protection_request_required_status_checks_checks_inner_from_dict = ReposUpdateBranchProtectionRequestRequiredStatusChecksChecksInner.from_dict(repos_update_branch_protection_request_required_status_checks_checks_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


