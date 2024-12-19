# ReposUpdateBranchProtectionRequestRequiredPullRequestReviews

Require at least one approving review on a pull request, before merging. Set to `null` to disable.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dismissal_restrictions** | [**ReposUpdateBranchProtectionRequestRequiredPullRequestReviewsDismissalRestrictions**](ReposUpdateBranchProtectionRequestRequiredPullRequestReviewsDismissalRestrictions.md) |  | [optional] 
**dismiss_stale_reviews** | **bool** | Set to &#x60;true&#x60; if you want to automatically dismiss approving reviews when someone pushes a new commit. | [optional] 
**require_code_owner_reviews** | **bool** | Blocks merging pull requests until [code owners](https://docs.github.com/articles/about-code-owners/) review them. | [optional] 
**required_approving_review_count** | **int** | Specify the number of reviewers required to approve pull requests. Use a number between 1 and 6 or 0 to not require reviewers. | [optional] 
**require_last_push_approval** | **bool** | Whether the most recent push must be approved by someone other than the person who pushed it. Default: &#x60;false&#x60;. | [optional] [default to False]
**bypass_pull_request_allowances** | [**ReposUpdateBranchProtectionRequestRequiredPullRequestReviewsBypassPullRequestAllowances**](ReposUpdateBranchProtectionRequestRequiredPullRequestReviewsBypassPullRequestAllowances.md) |  | [optional] 

## Example

```python
from github_openapi.models.repos_update_branch_protection_request_required_pull_request_reviews import ReposUpdateBranchProtectionRequestRequiredPullRequestReviews

# TODO update the JSON string below
json = "{}"
# create an instance of ReposUpdateBranchProtectionRequestRequiredPullRequestReviews from a JSON string
repos_update_branch_protection_request_required_pull_request_reviews_instance = ReposUpdateBranchProtectionRequestRequiredPullRequestReviews.from_json(json)
# print the JSON string representation of the object
print(ReposUpdateBranchProtectionRequestRequiredPullRequestReviews.to_json())

# convert the object into a dict
repos_update_branch_protection_request_required_pull_request_reviews_dict = repos_update_branch_protection_request_required_pull_request_reviews_instance.to_dict()
# create an instance of ReposUpdateBranchProtectionRequestRequiredPullRequestReviews from a dict
repos_update_branch_protection_request_required_pull_request_reviews_from_dict = ReposUpdateBranchProtectionRequestRequiredPullRequestReviews.from_dict(repos_update_branch_protection_request_required_pull_request_reviews_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


