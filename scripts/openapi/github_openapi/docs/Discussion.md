# Discussion

A Discussion in a repository.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active_lock_reason** | **str** |  | 
**answer_chosen_at** | **str** |  | 
**answer_chosen_by** | [**User2**](User2.md) |  | 
**answer_html_url** | **str** |  | 
**author_association** | **str** | How the author is associated with the repository. | 
**body** | **str** |  | 
**category** | [**DiscussionCategory**](DiscussionCategory.md) |  | 
**comments** | **int** |  | 
**created_at** | **datetime** |  | 
**html_url** | **str** |  | 
**id** | **int** |  | 
**locked** | **bool** |  | 
**node_id** | **str** |  | 
**number** | **int** |  | 
**reactions** | [**Reactions**](Reactions.md) |  | [optional] 
**repository_url** | **str** |  | 
**state** | **str** | The current state of the discussion. &#x60;converting&#x60; means that the discussion is being converted from an issue. &#x60;transferring&#x60; means that the discussion is being transferred from another repository. | 
**state_reason** | **str** | The reason for the current state | 
**timeline_url** | **str** |  | [optional] 
**title** | **str** |  | 
**updated_at** | **datetime** |  | 
**user** | [**User1**](User1.md) |  | 
**labels** | [**List[Label]**](Label.md) |  | [optional] 

## Example

```python
from github_openapi.models.discussion import Discussion

# TODO update the JSON string below
json = "{}"
# create an instance of Discussion from a JSON string
discussion_instance = Discussion.from_json(json)
# print the JSON string representation of the object
print(Discussion.to_json())

# convert the object into a dict
discussion_dict = discussion_instance.to_dict()
# create an instance of Discussion from a dict
discussion_from_dict = Discussion.from_dict(discussion_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


