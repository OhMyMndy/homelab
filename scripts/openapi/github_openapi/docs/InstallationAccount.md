# InstallationAccount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the enterprise. | 
**email** | **str** |  | [optional] 
**login** | **str** |  | 
**id** | **int** | Unique identifier of the enterprise | 
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
**description** | **str** | A short description of the enterprise. | [optional] 
**website_url** | **str** | The enterprise&#39;s website URL. | [optional] 
**slug** | **str** | The slug url identifier for the enterprise. | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from github_openapi.models.installation_account import InstallationAccount

# TODO update the JSON string below
json = "{}"
# create an instance of InstallationAccount from a JSON string
installation_account_instance = InstallationAccount.from_json(json)
# print the JSON string representation of the object
print(InstallationAccount.to_json())

# convert the object into a dict
installation_account_dict = installation_account_instance.to_dict()
# create an instance of InstallationAccount from a dict
installation_account_from_dict = InstallationAccount.from_dict(installation_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


