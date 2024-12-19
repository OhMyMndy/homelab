# ProtectedBranchPullRequestReviewDismissalRestrictions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**users** | [**List[SimpleUser]**](SimpleUser.md) | The list of users with review dismissal access. | [optional] 
**teams** | [**List[Team]**](Team.md) | The list of teams with review dismissal access. | [optional] 
**apps** | [**List[Integration]**](Integration.md) | The list of apps with review dismissal access. | [optional] 
**url** | **str** |  | [optional] 
**users_url** | **str** |  | [optional] 
**teams_url** | **str** |  | [optional] 

## Example

```python
from github_openapi.models.protected_branch_pull_request_review_dismissal_restrictions import ProtectedBranchPullRequestReviewDismissalRestrictions

# TODO update the JSON string below
json = "{}"
# create an instance of ProtectedBranchPullRequestReviewDismissalRestrictions from a JSON string
protected_branch_pull_request_review_dismissal_restrictions_instance = ProtectedBranchPullRequestReviewDismissalRestrictions.from_json(json)
# print the JSON string representation of the object
print(ProtectedBranchPullRequestReviewDismissalRestrictions.to_json())

# convert the object into a dict
protected_branch_pull_request_review_dismissal_restrictions_dict = protected_branch_pull_request_review_dismissal_restrictions_instance.to_dict()
# create an instance of ProtectedBranchPullRequestReviewDismissalRestrictions from a dict
protected_branch_pull_request_review_dismissal_restrictions_from_dict = ProtectedBranchPullRequestReviewDismissalRestrictions.from_dict(protected_branch_pull_request_review_dismissal_restrictions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


