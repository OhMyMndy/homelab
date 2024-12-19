# SourceRequest

Source Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Source&#39;s display Name. | 
**slug** | **str** | Internal source name, used in URLs. | 
**enabled** | **bool** |  | [optional] 
**authentication_flow** | **str** | Flow to use when authenticating existing users. | [optional] 
**enrollment_flow** | **str** | Flow to use when enrolling new users. | [optional] 
**policy_engine_mode** | [**PolicyEngineMode**](PolicyEngineMode.md) |  | [optional] 
**user_matching_mode** | [**UserMatchingModeEnum**](UserMatchingModeEnum.md) | How the source determines if an existing user should be authenticated or a new user enrolled. | [optional] 
**user_path_template** | **str** |  | [optional] 

## Example

```python
from authentik_openapi.models.source_request import SourceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SourceRequest from a JSON string
source_request_instance = SourceRequest.from_json(json)
# print the JSON string representation of the object
print(SourceRequest.to_json())

# convert the object into a dict
source_request_dict = source_request_instance.to_dict()
# create an instance of SourceRequest from a dict
source_request_from_dict = SourceRequest.from_dict(source_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


