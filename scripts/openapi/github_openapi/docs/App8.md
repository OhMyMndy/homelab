# App8

GitHub apps are a new way to extend GitHub. They can be installed directly on organizations and user accounts and granted access to specific repositories. They come with granular permissions and built-in webhooks. GitHub apps are first class actors within GitHub.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | 
**description** | **str** |  | 
**events** | **List[str]** | The list of events for the GitHub app | [optional] 
**external_url** | **str** |  | 
**html_url** | **str** |  | 
**id** | **int** | Unique identifier of the GitHub app | 
**name** | **str** | The name of the GitHub app | 
**node_id** | **str** |  | 
**owner** | [**User2**](User2.md) |  | 
**permissions** | [**App2Permissions**](App2Permissions.md) |  | [optional] 
**slug** | **str** | The slug name of the GitHub app | [optional] 
**updated_at** | **datetime** |  | 

## Example

```python
from github_openapi.models.app8 import App8

# TODO update the JSON string below
json = "{}"
# create an instance of App8 from a JSON string
app8_instance = App8.from_json(json)
# print the JSON string representation of the object
print(App8.to_json())

# convert the object into a dict
app8_dict = app8_instance.to_dict()
# create an instance of App8 from a dict
app8_from_dict = App8.from_dict(app8_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


