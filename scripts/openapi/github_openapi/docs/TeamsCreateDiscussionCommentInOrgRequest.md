# TeamsCreateDiscussionCommentInOrgRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | **str** | The discussion comment&#39;s body text. | 

## Example

```python
from github_openapi.models.teams_create_discussion_comment_in_org_request import TeamsCreateDiscussionCommentInOrgRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TeamsCreateDiscussionCommentInOrgRequest from a JSON string
teams_create_discussion_comment_in_org_request_instance = TeamsCreateDiscussionCommentInOrgRequest.from_json(json)
# print the JSON string representation of the object
print(TeamsCreateDiscussionCommentInOrgRequest.to_json())

# convert the object into a dict
teams_create_discussion_comment_in_org_request_dict = teams_create_discussion_comment_in_org_request_instance.to_dict()
# create an instance of TeamsCreateDiscussionCommentInOrgRequest from a dict
teams_create_discussion_comment_in_org_request_from_dict = TeamsCreateDiscussionCommentInOrgRequest.from_dict(teams_create_discussion_comment_in_org_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


