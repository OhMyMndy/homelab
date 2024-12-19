# SecretScanningLocationPullRequestReview

Represents a 'pull_request_review' secret scanning location type. This location type shows that a secret was detected in a review on a pull request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pull_request_review_url** | **str** | The API URL to get the pull request review where the secret was detected. | 

## Example

```python
from github_openapi.models.secret_scanning_location_pull_request_review import SecretScanningLocationPullRequestReview

# TODO update the JSON string below
json = "{}"
# create an instance of SecretScanningLocationPullRequestReview from a JSON string
secret_scanning_location_pull_request_review_instance = SecretScanningLocationPullRequestReview.from_json(json)
# print the JSON string representation of the object
print(SecretScanningLocationPullRequestReview.to_json())

# convert the object into a dict
secret_scanning_location_pull_request_review_dict = secret_scanning_location_pull_request_review_instance.to_dict()
# create an instance of SecretScanningLocationPullRequestReview from a dict
secret_scanning_location_pull_request_review_from_dict = SecretScanningLocationPullRequestReview.from_dict(secret_scanning_location_pull_request_review_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


