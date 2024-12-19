# TeamDiscussionComment

A reply to a discussion within a team.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**author** | [**NullableSimpleUser**](NullableSimpleUser.md) |  | 
**body** | **str** | The main text of the comment. | 
**body_html** | **str** |  | 
**body_version** | **str** | The current version of the body content. If provided, this update operation will be rejected if the given version does not match the latest version on the server. | 
**created_at** | **datetime** |  | 
**last_edited_at** | **datetime** |  | 
**discussion_url** | **str** |  | 
**html_url** | **str** |  | 
**node_id** | **str** |  | 
**number** | **int** | The unique sequence number of a team discussion comment. | 
**updated_at** | **datetime** |  | 
**url** | **str** |  | 
**reactions** | [**ReactionRollup**](ReactionRollup.md) |  | [optional] 

## Example

```python
from github_openapi.models.team_discussion_comment import TeamDiscussionComment

# TODO update the JSON string below
json = "{}"
# create an instance of TeamDiscussionComment from a JSON string
team_discussion_comment_instance = TeamDiscussionComment.from_json(json)
# print the JSON string representation of the object
print(TeamDiscussionComment.to_json())

# convert the object into a dict
team_discussion_comment_dict = team_discussion_comment_instance.to_dict()
# create an instance of TeamDiscussionComment from a dict
team_discussion_comment_from_dict = TeamDiscussionComment.from_dict(team_discussion_comment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


