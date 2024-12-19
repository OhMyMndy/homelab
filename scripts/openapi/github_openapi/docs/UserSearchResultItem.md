# UserSearchResultItem

User Search Result Item

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**login** | **str** |  | 
**id** | **int** |  | 
**node_id** | **str** |  | 
**avatar_url** | **str** |  | 
**gravatar_id** | **str** |  | 
**url** | **str** |  | 
**html_url** | **str** |  | 
**followers_url** | **str** |  | 
**subscriptions_url** | **str** |  | 
**organizations_url** | **str** |  | 
**repos_url** | **str** |  | 
**received_events_url** | **str** |  | 
**type** | **str** |  | 
**score** | **float** |  | 
**following_url** | **str** |  | 
**gists_url** | **str** |  | 
**starred_url** | **str** |  | 
**events_url** | **str** |  | 
**public_repos** | **int** |  | [optional] 
**public_gists** | **int** |  | [optional] 
**followers** | **int** |  | [optional] 
**following** | **int** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**name** | **str** |  | [optional] 
**bio** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**location** | **str** |  | [optional] 
**site_admin** | **bool** |  | 
**hireable** | **bool** |  | [optional] 
**text_matches** | [**List[SearchResultTextMatchesInner]**](SearchResultTextMatchesInner.md) |  | [optional] 
**blog** | **str** |  | [optional] 
**company** | **str** |  | [optional] 
**suspended_at** | **datetime** |  | [optional] 
**user_view_type** | **str** |  | [optional] 

## Example

```python
from github_openapi.models.user_search_result_item import UserSearchResultItem

# TODO update the JSON string below
json = "{}"
# create an instance of UserSearchResultItem from a JSON string
user_search_result_item_instance = UserSearchResultItem.from_json(json)
# print the JSON string representation of the object
print(UserSearchResultItem.to_json())

# convert the object into a dict
user_search_result_item_dict = user_search_result_item_instance.to_dict()
# create an instance of UserSearchResultItem from a dict
user_search_result_item_from_dict = UserSearchResultItem.from_dict(user_search_result_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


