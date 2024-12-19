# ReactionsCreateForTeamDiscussionCommentInOrgRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | **str** | The [reaction type](https://docs.github.com/rest/reactions/reactions#about-reactions) to add to the team discussion comment. | 

## Example

```python
from github_openapi.models.reactions_create_for_team_discussion_comment_in_org_request import ReactionsCreateForTeamDiscussionCommentInOrgRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReactionsCreateForTeamDiscussionCommentInOrgRequest from a JSON string
reactions_create_for_team_discussion_comment_in_org_request_instance = ReactionsCreateForTeamDiscussionCommentInOrgRequest.from_json(json)
# print the JSON string representation of the object
print(ReactionsCreateForTeamDiscussionCommentInOrgRequest.to_json())

# convert the object into a dict
reactions_create_for_team_discussion_comment_in_org_request_dict = reactions_create_for_team_discussion_comment_in_org_request_instance.to_dict()
# create an instance of ReactionsCreateForTeamDiscussionCommentInOrgRequest from a dict
reactions_create_for_team_discussion_comment_in_org_request_from_dict = ReactionsCreateForTeamDiscussionCommentInOrgRequest.from_dict(reactions_create_for_team_discussion_comment_in_org_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


