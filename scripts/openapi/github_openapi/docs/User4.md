# User4


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**avatar_url** | **str** |  | [optional] 
**deleted** | **bool** |  | [optional] 
**email** | **str** |  | [optional] 
**events_url** | **str** |  | [optional] 
**followers_url** | **str** |  | [optional] 
**following_url** | **str** |  | [optional] 
**gists_url** | **str** |  | [optional] 
**gravatar_id** | **str** |  | [optional] 
**html_url** | **str** |  | [optional] 
**id** | **int** |  | 
**login** | **str** |  | 
**name** | **str** |  | [optional] 
**node_id** | **str** |  | [optional] 
**organizations_url** | **str** |  | [optional] 
**received_events_url** | **str** |  | [optional] 
**repos_url** | **str** |  | [optional] 
**site_admin** | **bool** |  | [optional] 
**starred_url** | **str** |  | [optional] 
**subscriptions_url** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**user_view_type** | **str** |  | [optional] 

## Example

```python
from github_openapi.models.user4 import User4

# TODO update the JSON string below
json = "{}"
# create an instance of User4 from a JSON string
user4_instance = User4.from_json(json)
# print the JSON string representation of the object
print(User4.to_json())

# convert the object into a dict
user4_dict = user4_instance.to_dict()
# create an instance of User4 from a dict
user4_from_dict = User4.from_dict(user4_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


