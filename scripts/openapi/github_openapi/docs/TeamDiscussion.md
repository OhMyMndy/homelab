# TeamDiscussion

A team discussion is a persistent record of a free-form conversation within a team.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**author** | [**NullableSimpleUser**](NullableSimpleUser.md) |  | 
**body** | **str** | The main text of the discussion. | 
**body_html** | **str** |  | 
**body_version** | **str** | The current version of the body content. If provided, this update operation will be rejected if the given version does not match the latest version on the server. | 
**comments_count** | **int** |  | 
**comments_url** | **str** |  | 
**created_at** | **datetime** |  | 
**last_edited_at** | **datetime** |  | 
**html_url** | **str** |  | 
**node_id** | **str** |  | 
**number** | **int** | The unique sequence number of a team discussion. | 
**pinned** | **bool** | Whether or not this discussion should be pinned for easy retrieval. | 
**private** | **bool** | Whether or not this discussion should be restricted to team members and organization owners. | 
**team_url** | **str** |  | 
**title** | **str** | The title of the discussion. | 
**updated_at** | **datetime** |  | 
**url** | **str** |  | 
**reactions** | [**ReactionRollup**](ReactionRollup.md) |  | [optional] 

## Example

```python
from github_openapi.models.team_discussion import TeamDiscussion

# TODO update the JSON string below
json = "{}"
# create an instance of TeamDiscussion from a JSON string
team_discussion_instance = TeamDiscussion.from_json(json)
# print the JSON string representation of the object
print(TeamDiscussion.to_json())

# convert the object into a dict
team_discussion_dict = team_discussion_instance.to_dict()
# create an instance of TeamDiscussion from a dict
team_discussion_from_dict = TeamDiscussion.from_dict(team_discussion_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


