# ReposUpdateBranchProtectionRequestRestrictions

Restrict who can push to the protected branch. User, app, and team `restrictions` are only available for organization-owned repositories. Set to `null` to disable.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**users** | **List[str]** | The list of user &#x60;login&#x60;s with push access | 
**teams** | **List[str]** | The list of team &#x60;slug&#x60;s with push access | 
**apps** | **List[str]** | The list of app &#x60;slug&#x60;s with push access | [optional] 

## Example

```python
from github_openapi.models.repos_update_branch_protection_request_restrictions import ReposUpdateBranchProtectionRequestRestrictions

# TODO update the JSON string below
json = "{}"
# create an instance of ReposUpdateBranchProtectionRequestRestrictions from a JSON string
repos_update_branch_protection_request_restrictions_instance = ReposUpdateBranchProtectionRequestRestrictions.from_json(json)
# print the JSON string representation of the object
print(ReposUpdateBranchProtectionRequestRestrictions.to_json())

# convert the object into a dict
repos_update_branch_protection_request_restrictions_dict = repos_update_branch_protection_request_restrictions_instance.to_dict()
# create an instance of ReposUpdateBranchProtectionRequestRestrictions from a dict
repos_update_branch_protection_request_restrictions_from_dict = ReposUpdateBranchProtectionRequestRestrictions.from_dict(repos_update_branch_protection_request_restrictions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


