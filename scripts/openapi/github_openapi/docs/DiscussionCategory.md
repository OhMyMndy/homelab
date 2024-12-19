# DiscussionCategory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | 
**description** | **str** |  | 
**emoji** | **str** |  | 
**id** | **int** |  | 
**is_answerable** | **bool** |  | 
**name** | **str** |  | 
**node_id** | **str** |  | [optional] 
**repository_id** | **int** |  | 
**slug** | **str** |  | 
**updated_at** | **str** |  | 

## Example

```python
from github_openapi.models.discussion_category import DiscussionCategory

# TODO update the JSON string below
json = "{}"
# create an instance of DiscussionCategory from a JSON string
discussion_category_instance = DiscussionCategory.from_json(json)
# print the JSON string representation of the object
print(DiscussionCategory.to_json())

# convert the object into a dict
discussion_category_dict = discussion_category_instance.to_dict()
# create an instance of DiscussionCategory from a dict
discussion_category_from_dict = DiscussionCategory.from_dict(discussion_category_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


