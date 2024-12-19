# User8


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
**id** | **int** |  | [optional] 
**login** | **str** |  | [optional] 
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

## Example

```python
from github_openapi.models.user8 import User8

# TODO update the JSON string below
json = "{}"
# create an instance of User8 from a JSON string
user8_instance = User8.from_json(json)
# print the JSON string representation of the object
print(User8.to_json())

# convert the object into a dict
user8_dict = user8_instance.to_dict()
# create an instance of User8 from a dict
user8_from_dict = User8.from_dict(user8_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


