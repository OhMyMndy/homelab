# ProtectedBranchRequiredPullRequestReviewsDismissalRestrictions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | 
**users_url** | **str** |  | 
**teams_url** | **str** |  | 
**users** | [**List[SimpleUser]**](SimpleUser.md) |  | 
**teams** | [**List[Team]**](Team.md) |  | 
**apps** | [**List[Integration]**](Integration.md) |  | [optional] 

## Example

```python
from github_openapi.models.protected_branch_required_pull_request_reviews_dismissal_restrictions import ProtectedBranchRequiredPullRequestReviewsDismissalRestrictions

# TODO update the JSON string below
json = "{}"
# create an instance of ProtectedBranchRequiredPullRequestReviewsDismissalRestrictions from a JSON string
protected_branch_required_pull_request_reviews_dismissal_restrictions_instance = ProtectedBranchRequiredPullRequestReviewsDismissalRestrictions.from_json(json)
# print the JSON string representation of the object
print(ProtectedBranchRequiredPullRequestReviewsDismissalRestrictions.to_json())

# convert the object into a dict
protected_branch_required_pull_request_reviews_dismissal_restrictions_dict = protected_branch_required_pull_request_reviews_dismissal_restrictions_instance.to_dict()
# create an instance of ProtectedBranchRequiredPullRequestReviewsDismissalRestrictions from a dict
protected_branch_required_pull_request_reviews_dismissal_restrictions_from_dict = ProtectedBranchRequiredPullRequestReviewsDismissalRestrictions.from_dict(protected_branch_required_pull_request_reviews_dismissal_restrictions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


