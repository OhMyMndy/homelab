# ReposUpdateBranchProtectionRequestRequiredPullRequestReviewsDismissalRestrictions

Specify which users, teams, and apps can dismiss pull request reviews. Pass an empty `dismissal_restrictions` object to disable. User and team `dismissal_restrictions` are only available for organization-owned repositories. Omit this parameter for personal repositories.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**users** | **List[str]** | The list of user &#x60;login&#x60;s with dismissal access | [optional] 
**teams** | **List[str]** | The list of team &#x60;slug&#x60;s with dismissal access | [optional] 
**apps** | **List[str]** | The list of app &#x60;slug&#x60;s with dismissal access | [optional] 

## Example

```python
from github_openapi.models.repos_update_branch_protection_request_required_pull_request_reviews_dismissal_restrictions import ReposUpdateBranchProtectionRequestRequiredPullRequestReviewsDismissalRestrictions

# TODO update the JSON string below
json = "{}"
# create an instance of ReposUpdateBranchProtectionRequestRequiredPullRequestReviewsDismissalRestrictions from a JSON string
repos_update_branch_protection_request_required_pull_request_reviews_dismissal_restrictions_instance = ReposUpdateBranchProtectionRequestRequiredPullRequestReviewsDismissalRestrictions.from_json(json)
# print the JSON string representation of the object
print(ReposUpdateBranchProtectionRequestRequiredPullRequestReviewsDismissalRestrictions.to_json())

# convert the object into a dict
repos_update_branch_protection_request_required_pull_request_reviews_dismissal_restrictions_dict = repos_update_branch_protection_request_required_pull_request_reviews_dismissal_restrictions_instance.to_dict()
# create an instance of ReposUpdateBranchProtectionRequestRequiredPullRequestReviewsDismissalRestrictions from a dict
repos_update_branch_protection_request_required_pull_request_reviews_dismissal_restrictions_from_dict = ReposUpdateBranchProtectionRequestRequiredPullRequestReviewsDismissalRestrictions.from_dict(repos_update_branch_protection_request_required_pull_request_reviews_dismissal_restrictions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


