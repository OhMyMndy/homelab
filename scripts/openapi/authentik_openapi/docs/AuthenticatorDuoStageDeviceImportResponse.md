# AuthenticatorDuoStageDeviceImportResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [readonly] 
**error** | **str** |  | [readonly] 

## Example

```python
from authentik_openapi.models.authenticator_duo_stage_device_import_response import AuthenticatorDuoStageDeviceImportResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticatorDuoStageDeviceImportResponse from a JSON string
authenticator_duo_stage_device_import_response_instance = AuthenticatorDuoStageDeviceImportResponse.from_json(json)
# print the JSON string representation of the object
print(AuthenticatorDuoStageDeviceImportResponse.to_json())

# convert the object into a dict
authenticator_duo_stage_device_import_response_dict = authenticator_duo_stage_device_import_response_instance.to_dict()
# create an instance of AuthenticatorDuoStageDeviceImportResponse from a dict
authenticator_duo_stage_device_import_response_from_dict = AuthenticatorDuoStageDeviceImportResponse.from_dict(authenticator_duo_stage_device_import_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


