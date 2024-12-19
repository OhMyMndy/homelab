# ReposCreateCommitCommentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | **str** | The contents of the comment. | 
**path** | **str** | Relative path of the file to comment on. | [optional] 
**position** | **int** | Line index in the diff to comment on. | [optional] 
**line** | **int** | **Closing down notice**. Use **position** parameter instead. Line number in the file to comment on. | [optional] 

## Example

```python
from github_openapi.models.repos_create_commit_comment_request import ReposCreateCommitCommentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReposCreateCommitCommentRequest from a JSON string
repos_create_commit_comment_request_instance = ReposCreateCommitCommentRequest.from_json(json)
# print the JSON string representation of the object
print(ReposCreateCommitCommentRequest.to_json())

# convert the object into a dict
repos_create_commit_comment_request_dict = repos_create_commit_comment_request_instance.to_dict()
# create an instance of ReposCreateCommitCommentRequest from a dict
repos_create_commit_comment_request_from_dict = ReposCreateCommitCommentRequest.from_dict(repos_create_commit_comment_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


