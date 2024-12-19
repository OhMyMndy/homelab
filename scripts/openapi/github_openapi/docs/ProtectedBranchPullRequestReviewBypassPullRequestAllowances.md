# ProtectedBranchPullRequestReviewBypassPullRequestAllowances

Allow specific users, teams, or apps to bypass pull request requirements.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**users** | [**List[SimpleUser]**](SimpleUser.md) | The list of users allowed to bypass pull request requirements. | [optional] 
**teams** | [**List[Team]**](Team.md) | The list of teams allowed to bypass pull request requirements. | [optional] 
**apps** | [**List[Integration]**](Integration.md) | The list of apps allowed to bypass pull request requirements. | [optional] 

## Example

```python
from github_openapi.models.protected_branch_pull_request_review_bypass_pull_request_allowances import ProtectedBranchPullRequestReviewBypassPullRequestAllowances

# TODO update the JSON string below
json = "{}"
# create an instance of ProtectedBranchPullRequestReviewBypassPullRequestAllowances from a JSON string
protected_branch_pull_request_review_bypass_pull_request_allowances_instance = ProtectedBranchPullRequestReviewBypassPullRequestAllowances.from_json(json)
# print the JSON string representation of the object
print(ProtectedBranchPullRequestReviewBypassPullRequestAllowances.to_json())

# convert the object into a dict
protected_branch_pull_request_review_bypass_pull_request_allowances_dict = protected_branch_pull_request_review_bypass_pull_request_allowances_instance.to_dict()
# create an instance of ProtectedBranchPullRequestReviewBypassPullRequestAllowances from a dict
protected_branch_pull_request_review_bypass_pull_request_allowances_from_dict = ProtectedBranchPullRequestReviewBypassPullRequestAllowances.from_dict(protected_branch_pull_request_review_bypass_pull_request_allowances_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


