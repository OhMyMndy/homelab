# ReposUpdateBranchProtectionRequestRequiredPullRequestReviewsBypassPullRequestAllowances

Allow specific users, teams, or apps to bypass pull request requirements.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**users** | **List[str]** | The list of user &#x60;login&#x60;s allowed to bypass pull request requirements. | [optional] 
**teams** | **List[str]** | The list of team &#x60;slug&#x60;s allowed to bypass pull request requirements. | [optional] 
**apps** | **List[str]** | The list of app &#x60;slug&#x60;s allowed to bypass pull request requirements. | [optional] 

## Example

```python
from github_openapi.models.repos_update_branch_protection_request_required_pull_request_reviews_bypass_pull_request_allowances import ReposUpdateBranchProtectionRequestRequiredPullRequestReviewsBypassPullRequestAllowances

# TODO update the JSON string below
json = "{}"
# create an instance of ReposUpdateBranchProtectionRequestRequiredPullRequestReviewsBypassPullRequestAllowances from a JSON string
repos_update_branch_protection_request_required_pull_request_reviews_bypass_pull_request_allowances_instance = ReposUpdateBranchProtectionRequestRequiredPullRequestReviewsBypassPullRequestAllowances.from_json(json)
# print the JSON string representation of the object
print(ReposUpdateBranchProtectionRequestRequiredPullRequestReviewsBypassPullRequestAllowances.to_json())

# convert the object into a dict
repos_update_branch_protection_request_required_pull_request_reviews_bypass_pull_request_allowances_dict = repos_update_branch_protection_request_required_pull_request_reviews_bypass_pull_request_allowances_instance.to_dict()
# create an instance of ReposUpdateBranchProtectionRequestRequiredPullRequestReviewsBypassPullRequestAllowances from a dict
repos_update_branch_protection_request_required_pull_request_reviews_bypass_pull_request_allowances_from_dict = ReposUpdateBranchProtectionRequestRequiredPullRequestReviewsBypassPullRequestAllowances.from_dict(repos_update_branch_protection_request_required_pull_request_reviews_bypass_pull_request_allowances_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


