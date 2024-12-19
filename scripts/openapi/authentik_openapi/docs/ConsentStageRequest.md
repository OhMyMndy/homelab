# ConsentStageRequest

ConsentStage Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**flow_set** | [**List[FlowSetRequest]**](FlowSetRequest.md) |  | [optional] 
**mode** | [**ConsentStageModeEnum**](ConsentStageModeEnum.md) |  | [optional] 
**consent_expire_in** | **str** | Offset after which consent expires. (Format: hours&#x3D;1;minutes&#x3D;2;seconds&#x3D;3). | [optional] 

## Example

```python
from authentik_openapi.models.consent_stage_request import ConsentStageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ConsentStageRequest from a JSON string
consent_stage_request_instance = ConsentStageRequest.from_json(json)
# print the JSON string representation of the object
print(ConsentStageRequest.to_json())

# convert the object into a dict
consent_stage_request_dict = consent_stage_request_instance.to_dict()
# create an instance of ConsentStageRequest from a dict
consent_stage_request_from_dict = ConsentStageRequest.from_dict(consent_stage_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


