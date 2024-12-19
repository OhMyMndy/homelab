# ReposUpdateCommitCommentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | **str** | The contents of the comment | 

## Example

```python
from github_openapi.models.repos_update_commit_comment_request import ReposUpdateCommitCommentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReposUpdateCommitCommentRequest from a JSON string
repos_update_commit_comment_request_instance = ReposUpdateCommitCommentRequest.from_json(json)
# print the JSON string representation of the object
print(ReposUpdateCommitCommentRequest.to_json())

# convert the object into a dict
repos_update_commit_comment_request_dict = repos_update_commit_comment_request_instance.to_dict()
# create an instance of ReposUpdateCommitCommentRequest from a dict
repos_update_commit_comment_request_from_dict = ReposUpdateCommitCommentRequest.from_dict(repos_update_commit_comment_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


