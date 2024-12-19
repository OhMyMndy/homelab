# PatchedConsentStageRequest

ConsentStage Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**flow_set** | [**List[FlowSetRequest]**](FlowSetRequest.md) |  | [optional] 
**mode** | [**ConsentStageModeEnum**](ConsentStageModeEnum.md) |  | [optional] 
**consent_expire_in** | **str** | Offset after which consent expires. (Format: hours&#x3D;1;minutes&#x3D;2;seconds&#x3D;3). | [optional] 

## Example

```python
from authentik_openapi.models.patched_consent_stage_request import PatchedConsentStageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedConsentStageRequest from a JSON string
patched_consent_stage_request_instance = PatchedConsentStageRequest.from_json(json)
# print the JSON string representation of the object
print(PatchedConsentStageRequest.to_json())

# convert the object into a dict
patched_consent_stage_request_dict = patched_consent_stage_request_instance.to_dict()
# create an instance of PatchedConsentStageRequest from a dict
patched_consent_stage_request_from_dict = PatchedConsentStageRequest.from_dict(patched_consent_stage_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


