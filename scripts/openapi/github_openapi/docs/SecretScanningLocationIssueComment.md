# SecretScanningLocationIssueComment

Represents an 'issue_comment' secret scanning location type. This location type shows that a secret was detected in a comment on an issue.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**issue_comment_url** | **str** | The API URL to get the issue comment where the secret was detected. | 

## Example

```python
from github_openapi.models.secret_scanning_location_issue_comment import SecretScanningLocationIssueComment

# TODO update the JSON string below
json = "{}"
# create an instance of SecretScanningLocationIssueComment from a JSON string
secret_scanning_location_issue_comment_instance = SecretScanningLocationIssueComment.from_json(json)
# print the JSON string representation of the object
print(SecretScanningLocationIssueComment.to_json())

# convert the object into a dict
secret_scanning_location_issue_comment_dict = secret_scanning_location_issue_comment_instance.to_dict()
# create an instance of SecretScanningLocationIssueComment from a dict
secret_scanning_location_issue_comment_from_dict = SecretScanningLocationIssueComment.from_dict(secret_scanning_location_issue_comment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


