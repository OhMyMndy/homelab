# Collaborator

Collaborator

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**login** | **str** |  | 
**id** | **int** |  | 
**email** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
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
**permissions** | [**CollaboratorPermissions**](CollaboratorPermissions.md) |  | [optional] 
**role_name** | **str** |  | 
**user_view_type** | **str** |  | [optional] 

## Example

```python
from github_openapi.models.collaborator import Collaborator

# TODO update the JSON string below
json = "{}"
# create an instance of Collaborator from a JSON string
collaborator_instance = Collaborator.from_json(json)
# print the JSON string representation of the object
print(Collaborator.to_json())

# convert the object into a dict
collaborator_dict = collaborator_instance.to_dict()
# create an instance of Collaborator from a dict
collaborator_from_dict = Collaborator.from_dict(collaborator_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


