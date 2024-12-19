# ApplicationRequest

Application Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Application&#39;s display Name. | 
**slug** | **str** | Internal application name, used in URLs. | 
**provider** | **int** |  | [optional] 
**backchannel_providers** | **List[int]** |  | [optional] 
**open_in_new_tab** | **bool** | Open launch URL in a new browser tab or window. | [optional] 
**meta_launch_url** | **str** |  | [optional] 
**meta_description** | **str** |  | [optional] 
**meta_publisher** | **str** |  | [optional] 
**policy_engine_mode** | [**PolicyEngineMode**](PolicyEngineMode.md) |  | [optional] 
**group** | **str** |  | [optional] 

## Example

```python
from authentik_openapi.models.application_request import ApplicationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationRequest from a JSON string
application_request_instance = ApplicationRequest.from_json(json)
# print the JSON string representation of the object
print(ApplicationRequest.to_json())

# convert the object into a dict
application_request_dict = application_request_instance.to_dict()
# create an instance of ApplicationRequest from a dict
application_request_from_dict = ApplicationRequest.from_dict(application_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


