# NullableIntegration

GitHub apps are a new way to extend GitHub. They can be installed directly on organizations and user accounts and granted access to specific repositories. They come with granular permissions and built-in webhooks. GitHub apps are first class actors within GitHub.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier of the GitHub app | 
**slug** | **str** | The slug name of the GitHub app | [optional] 
**node_id** | **str** |  | 
**client_id** | **str** |  | [optional] 
**owner** | [**NullableSimpleUser**](NullableSimpleUser.md) |  | 
**name** | **str** | The name of the GitHub app | 
**description** | **str** |  | 
**external_url** | **str** |  | 
**html_url** | **str** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**permissions** | [**IntegrationPermissions**](IntegrationPermissions.md) |  | 
**events** | **List[str]** | The list of events for the GitHub app | 
**installations_count** | **int** | The number of installations associated with the GitHub app | [optional] 
**client_secret** | **str** |  | [optional] 
**webhook_secret** | **str** |  | [optional] 
**pem** | **str** |  | [optional] 

## Example

```python
from github_openapi.models.nullable_integration import NullableIntegration

# TODO update the JSON string below
json = "{}"
# create an instance of NullableIntegration from a JSON string
nullable_integration_instance = NullableIntegration.from_json(json)
# print the JSON string representation of the object
print(NullableIntegration.to_json())

# convert the object into a dict
nullable_integration_dict = nullable_integration_instance.to_dict()
# create an instance of NullableIntegration from a dict
nullable_integration_from_dict = NullableIntegration.from_dict(nullable_integration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


