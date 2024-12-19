# AuthenticatorDuoStageManualDeviceImportRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**duo_user_id** | **str** |  | 
**username** | **str** |  | 

## Example

```python
from authentik_openapi.models.authenticator_duo_stage_manual_device_import_request import AuthenticatorDuoStageManualDeviceImportRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticatorDuoStageManualDeviceImportRequest from a JSON string
authenticator_duo_stage_manual_device_import_request_instance = AuthenticatorDuoStageManualDeviceImportRequest.from_json(json)
# print the JSON string representation of the object
print(AuthenticatorDuoStageManualDeviceImportRequest.to_json())

# convert the object into a dict
authenticator_duo_stage_manual_device_import_request_dict = authenticator_duo_stage_manual_device_import_request_instance.to_dict()
# create an instance of AuthenticatorDuoStageManualDeviceImportRequest from a dict
authenticator_duo_stage_manual_device_import_request_from_dict = AuthenticatorDuoStageManualDeviceImportRequest.from_dict(authenticator_duo_stage_manual_device_import_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


