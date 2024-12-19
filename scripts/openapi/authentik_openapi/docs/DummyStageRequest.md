# DummyStageRequest

DummyStage Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**flow_set** | [**List[FlowSetRequest]**](FlowSetRequest.md) |  | [optional] 
**throw_error** | **bool** |  | [optional] 

## Example

```python
from authentik_openapi.models.dummy_stage_request import DummyStageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DummyStageRequest from a JSON string
dummy_stage_request_instance = DummyStageRequest.from_json(json)
# print the JSON string representation of the object
print(DummyStageRequest.to_json())

# convert the object into a dict
dummy_stage_request_dict = dummy_stage_request_instance.to_dict()
# create an instance of DummyStageRequest from a dict
dummy_stage_request_from_dict = DummyStageRequest.from_dict(dummy_stage_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


