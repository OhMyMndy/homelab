# IssuesUpdateCommentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | **str** | The contents of the comment. | 

## Example

```python
from github_openapi.models.issues_update_comment_request import IssuesUpdateCommentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IssuesUpdateCommentRequest from a JSON string
issues_update_comment_request_instance = IssuesUpdateCommentRequest.from_json(json)
# print the JSON string representation of the object
print(IssuesUpdateCommentRequest.to_json())

# convert the object into a dict
issues_update_comment_request_dict = issues_update_comment_request_instance.to_dict()
# create an instance of IssuesUpdateCommentRequest from a dict
issues_update_comment_request_from_dict = IssuesUpdateCommentRequest.from_dict(issues_update_comment_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


