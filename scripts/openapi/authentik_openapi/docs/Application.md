# Application

Application Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk** | **str** |  | [readonly] 
**name** | **str** | Application&#39;s display Name. | 
**slug** | **str** | Internal application name, used in URLs. | 
**provider** | **int** |  | [optional] 
**provider_obj** | [**Provider**](Provider.md) |  | [readonly] 
**backchannel_providers** | **List[int]** |  | [optional] 
**backchannel_providers_obj** | [**List[Provider]**](Provider.md) |  | [readonly] 
**launch_url** | **str** | Allow formatting of launch URL | [readonly] 
**open_in_new_tab** | **bool** | Open launch URL in a new browser tab or window. | [optional] 
**meta_launch_url** | **str** |  | [optional] 
**meta_icon** | **str** | Get the URL to the App Icon image. If the name is /static or starts with http it is returned as-is | [readonly] 
**meta_description** | **str** |  | [optional] 
**meta_publisher** | **str** |  | [optional] 
**policy_engine_mode** | [**PolicyEngineMode**](PolicyEngineMode.md) |  | [optional] 
**group** | **str** |  | [optional] 

## Example

```python
from authentik_openapi.models.application import Application

# TODO update the JSON string below
json = "{}"
# create an instance of Application from a JSON string
application_instance = Application.from_json(json)
# print the JSON string representation of the object
print(Application.to_json())

# convert the object into a dict
application_dict = application_instance.to_dict()
# create an instance of Application from a dict
application_from_dict = Application.from_dict(application_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


