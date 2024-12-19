# SimpleUser

A GitHub user.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**login** | **str** |  | 
**id** | **int** |  | 
**node_id** | **str** |  | 
**avatar_url** | **str** |  | 
**gravatar_id** | **str** |  | 
**url** | **str** |  | 
**html_url** | **str** |  | 
**followers_url** | **str** |  | 
**following_url** | **str** |  | 
**gists_url** | **str** |  | 
**starred_url** | **str** |  | 
**subscriptions_url** | **str** |  | 
**organizations_url** | **str** |  | 
**repos_url** | **str** |  | 
**events_url** | **str** |  | 
**received_events_url** | **str** |  | 
**type** | **str** |  | 
**site_admin** | **bool** |  | 
**starred_at** | **str** |  | [optional] 
**user_view_type** | **str** |  | [optional] 

## Example

```python
from github_openapi.models.simple_user import SimpleUser

# TODO update the JSON string below
json = "{}"
# create an instance of SimpleUser from a JSON string
simple_user_instance = SimpleUser.from_json(json)
# print the JSON string representation of the object
print(SimpleUser.to_json())

# convert the object into a dict
simple_user_dict = simple_user_instance.to_dict()
# create an instance of SimpleUser from a dict
simple_user_from_dict = SimpleUser.from_dict(simple_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


