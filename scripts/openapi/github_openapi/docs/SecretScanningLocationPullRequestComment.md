# SecretScanningLocationPullRequestComment

Represents a 'pull_request_comment' secret scanning location type. This location type shows that a secret was detected in a comment on a pull request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pull_request_comment_url** | **str** | The API URL to get the pull request comment where the secret was detected. | 

## Example

```python
from github_openapi.models.secret_scanning_location_pull_request_comment import SecretScanningLocationPullRequestComment

# TODO update the JSON string below
json = "{}"
# create an instance of SecretScanningLocationPullRequestComment from a JSON string
secret_scanning_location_pull_request_comment_instance = SecretScanningLocationPullRequestComment.from_json(json)
# print the JSON string representation of the object
print(SecretScanningLocationPullRequestComment.to_json())

# convert the object into a dict
secret_scanning_location_pull_request_comment_dict = secret_scanning_location_pull_request_comment_instance.to_dict()
# create an instance of SecretScanningLocationPullRequestComment from a dict
secret_scanning_location_pull_request_comment_from_dict = SecretScanningLocationPullRequestComment.from_dict(secret_scanning_location_pull_request_comment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


