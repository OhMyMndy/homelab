# PublicUser

Public User

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**login** | **str** |  | 
**id** | **int** |  | 
**user_view_type** | **str** |  | [optional] 
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
**name** | **str** |  | 
**company** | **str** |  | 
**blog** | **str** |  | 
**location** | **str** |  | 
**email** | **str** |  | 
**notification_email** | **str** |  | [optional] 
**hireable** | **bool** |  | 
**bio** | **str** |  | 
**twitter_username** | **str** |  | [optional] 
**public_repos** | **int** |  | 
**public_gists** | **int** |  | 
**followers** | **int** |  | 
**following** | **int** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**plan** | [**PublicUserPlan**](PublicUserPlan.md) |  | [optional] 
**private_gists** | **int** |  | [optional] 
**total_private_repos** | **int** |  | [optional] 
**owned_private_repos** | **int** |  | [optional] 
**disk_usage** | **int** |  | [optional] 
**collaborators** | **int** |  | [optional] 

## Example

```python
from github_openapi.models.public_user import PublicUser

# TODO update the JSON string below
json = "{}"
# create an instance of PublicUser from a JSON string
public_user_instance = PublicUser.from_json(json)
# print the JSON string representation of the object
print(PublicUser.to_json())

# convert the object into a dict
public_user_dict = public_user_instance.to_dict()
# create an instance of PublicUser from a dict
public_user_from_dict = PublicUser.from_dict(public_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


