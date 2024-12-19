# UsersGetAuthenticated200Response


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
**private_gists** | **int** |  | 
**total_private_repos** | **int** |  | 
**owned_private_repos** | **int** |  | 
**disk_usage** | **int** |  | 
**collaborators** | **int** |  | 
**two_factor_authentication** | **bool** |  | 
**plan** | [**PublicUserPlan**](PublicUserPlan.md) |  | [optional] 
**business_plus** | **bool** |  | [optional] 
**ldap_dn** | **str** |  | [optional] 

## Example

```python
from github_openapi.models.users_get_authenticated200_response import UsersGetAuthenticated200Response

# TODO update the JSON string below
json = "{}"
# create an instance of UsersGetAuthenticated200Response from a JSON string
users_get_authenticated200_response_instance = UsersGetAuthenticated200Response.from_json(json)
# print the JSON string representation of the object
print(UsersGetAuthenticated200Response.to_json())

# convert the object into a dict
users_get_authenticated200_response_dict = users_get_authenticated200_response_instance.to_dict()
# create an instance of UsersGetAuthenticated200Response from a dict
users_get_authenticated200_response_from_dict = UsersGetAuthenticated200Response.from_dict(users_get_authenticated200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


