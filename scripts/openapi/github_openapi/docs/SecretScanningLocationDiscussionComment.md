# SecretScanningLocationDiscussionComment

Represents a 'discussion_comment' secret scanning location type. This location type shows that a secret was detected in a comment on a discussion.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**discussion_comment_url** | **str** | The API URL to get the discussion comment where the secret was detected. | 

## Example

```python
from github_openapi.models.secret_scanning_location_discussion_comment import SecretScanningLocationDiscussionComment

# TODO update the JSON string below
json = "{}"
# create an instance of SecretScanningLocationDiscussionComment from a JSON string
secret_scanning_location_discussion_comment_instance = SecretScanningLocationDiscussionComment.from_json(json)
# print the JSON string representation of the object
print(SecretScanningLocationDiscussionComment.to_json())

# convert the object into a dict
secret_scanning_location_discussion_comment_dict = secret_scanning_location_discussion_comment_instance.to_dict()
# create an instance of SecretScanningLocationDiscussionComment from a dict
secret_scanning_location_discussion_comment_from_dict = SecretScanningLocationDiscussionComment.from_dict(secret_scanning_location_discussion_comment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


