# AppsCreateFromManifest201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier of the GitHub app | 
**slug** | **str** | The slug name of the GitHub app | [optional] 
**node_id** | **str** |  | 
**client_id** | **str** |  | 
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
**client_secret** | **str** |  | 
**webhook_secret** | **str** |  | 
**pem** | **str** |  | 

## Example

```python
from github_openapi.models.apps_create_from_manifest201_response import AppsCreateFromManifest201Response

# TODO update the JSON string below
json = "{}"
# create an instance of AppsCreateFromManifest201Response from a JSON string
apps_create_from_manifest201_response_instance = AppsCreateFromManifest201Response.from_json(json)
# print the JSON string representation of the object
print(AppsCreateFromManifest201Response.to_json())

# convert the object into a dict
apps_create_from_manifest201_response_dict = apps_create_from_manifest201_response_instance.to_dict()
# create an instance of AppsCreateFromManifest201Response from a dict
apps_create_from_manifest201_response_from_dict = AppsCreateFromManifest201Response.from_dict(apps_create_from_manifest201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


