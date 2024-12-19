# SourceStageRequest

SourceStage Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**flow_set** | [**List[FlowSetRequest]**](FlowSetRequest.md) |  | [optional] 
**source** | **str** |  | 
**resume_timeout** | **str** | Amount of time a user can take to return from the source to continue the flow (Format: hours&#x3D;-1;minutes&#x3D;-2;seconds&#x3D;-3) | [optional] 

## Example

```python
from authentik_openapi.models.source_stage_request import SourceStageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SourceStageRequest from a JSON string
source_stage_request_instance = SourceStageRequest.from_json(json)
# print the JSON string representation of the object
print(SourceStageRequest.to_json())

# convert the object into a dict
source_stage_request_dict = source_stage_request_instance.to_dict()
# create an instance of SourceStageRequest from a dict
source_stage_request_from_dict = SourceStageRequest.from_dict(source_stage_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


