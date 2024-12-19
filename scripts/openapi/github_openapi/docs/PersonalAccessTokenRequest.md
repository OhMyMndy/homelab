# PersonalAccessTokenRequest

Details of a Personal Access Token Request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier of the request for access via fine-grained personal access token. Used as the &#x60;pat_request_id&#x60; parameter in the list and review API calls. | 
**owner** | [**SimpleUser**](SimpleUser.md) |  | 
**permissions_added** | [**PersonalAccessTokenRequestPermissionsAdded**](PersonalAccessTokenRequestPermissionsAdded.md) |  | 
**permissions_upgraded** | [**PersonalAccessTokenRequestPermissionsUpgraded**](PersonalAccessTokenRequestPermissionsUpgraded.md) |  | 
**permissions_result** | [**PersonalAccessTokenRequestPermissionsResult**](PersonalAccessTokenRequestPermissionsResult.md) |  | 
**repository_selection** | **str** | Type of repository selection requested. | 
**repository_count** | **int** | The number of repositories the token is requesting access to. This field is only populated when &#x60;repository_selection&#x60; is &#x60;subset&#x60;. | 
**repositories** | [**List[WebhooksRepositoriesInner]**](WebhooksRepositoriesInner.md) | An array of repository objects the token is requesting access to. This field is only populated when &#x60;repository_selection&#x60; is &#x60;subset&#x60;. | 
**created_at** | **str** | Date and time when the request for access was created. | 
**token_id** | **int** | Unique identifier of the user&#39;s token. This field can also be found in audit log events and the organization&#39;s settings for their PAT grants. | 
**token_name** | **str** | The name given to the user&#39;s token. This field can also be found in an organization&#39;s settings page for Active Tokens. | 
**token_expired** | **bool** | Whether the associated fine-grained personal access token has expired. | 
**token_expires_at** | **str** | Date and time when the associated fine-grained personal access token expires. | 
**token_last_used_at** | **str** | Date and time when the associated fine-grained personal access token was last used for authentication. | 

## Example

```python
from github_openapi.models.personal_access_token_request import PersonalAccessTokenRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PersonalAccessTokenRequest from a JSON string
personal_access_token_request_instance = PersonalAccessTokenRequest.from_json(json)
# print the JSON string representation of the object
print(PersonalAccessTokenRequest.to_json())

# convert the object into a dict
personal_access_token_request_dict = personal_access_token_request_instance.to_dict()
# create an instance of PersonalAccessTokenRequest from a dict
personal_access_token_request_from_dict = PersonalAccessTokenRequest.from_dict(personal_access_token_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


