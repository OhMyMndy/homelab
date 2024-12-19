# SecretScanningLocationPullRequestReviewComment

Represents a 'pull_request_review_comment' secret scanning location type. This location type shows that a secret was detected in a review comment on a pull request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pull_request_review_comment_url** | **str** | The API URL to get the pull request review comment where the secret was detected. | 

## Example

```python
from github_openapi.models.secret_scanning_location_pull_request_review_comment import SecretScanningLocationPullRequestReviewComment

# TODO update the JSON string below
json = "{}"
# create an instance of SecretScanningLocationPullRequestReviewComment from a JSON string
secret_scanning_location_pull_request_review_comment_instance = SecretScanningLocationPullRequestReviewComment.from_json(json)
# print the JSON string representation of the object
print(SecretScanningLocationPullRequestReviewComment.to_json())

# convert the object into a dict
secret_scanning_location_pull_request_review_comment_dict = secret_scanning_location_pull_request_review_comment_instance.to_dict()
# create an instance of SecretScanningLocationPullRequestReviewComment from a dict
secret_scanning_location_pull_request_review_comment_from_dict = SecretScanningLocationPullRequestReviewComment.from_dict(secret_scanning_location_pull_request_review_comment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


