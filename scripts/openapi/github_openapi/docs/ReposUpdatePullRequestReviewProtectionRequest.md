# ReposUpdatePullRequestReviewProtectionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dismissal_restrictions** | [**ReposUpdateBranchProtectionRequestRequiredPullRequestReviewsDismissalRestrictions**](ReposUpdateBranchProtectionRequestRequiredPullRequestReviewsDismissalRestrictions.md) |  | [optional] 
**dismiss_stale_reviews** | **bool** | Set to &#x60;true&#x60; if you want to automatically dismiss approving reviews when someone pushes a new commit. | [optional] 
**require_code_owner_reviews** | **bool** | Blocks merging pull requests until [code owners](https://docs.github.com/articles/about-code-owners/) have reviewed. | [optional] 
**required_approving_review_count** | **int** | Specifies the number of reviewers required to approve pull requests. Use a number between 1 and 6 or 0 to not require reviewers. | [optional] 
**require_last_push_approval** | **bool** | Whether the most recent push must be approved by someone other than the person who pushed it. Default: &#x60;false&#x60; | [optional] [default to False]
**bypass_pull_request_allowances** | [**ReposUpdateBranchProtectionRequestRequiredPullRequestReviewsBypassPullRequestAllowances**](ReposUpdateBranchProtectionRequestRequiredPullRequestReviewsBypassPullRequestAllowances.md) |  | [optional] 

## Example

```python
from github_openapi.models.repos_update_pull_request_review_protection_request import ReposUpdatePullRequestReviewProtectionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReposUpdatePullRequestReviewProtectionRequest from a JSON string
repos_update_pull_request_review_protection_request_instance = ReposUpdatePullRequestReviewProtectionRequest.from_json(json)
# print the JSON string representation of the object
print(ReposUpdatePullRequestReviewProtectionRequest.to_json())

# convert the object into a dict
repos_update_pull_request_review_protection_request_dict = repos_update_pull_request_review_protection_request_instance.to_dict()
# create an instance of ReposUpdatePullRequestReviewProtectionRequest from a dict
repos_update_pull_request_review_protection_request_from_dict = ReposUpdatePullRequestReviewProtectionRequest.from_dict(repos_update_pull_request_review_protection_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


