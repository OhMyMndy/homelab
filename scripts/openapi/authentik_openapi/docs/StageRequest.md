# StageRequest

Stage Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**flow_set** | [**List[FlowSetRequest]**](FlowSetRequest.md) |  | [optional] 

## Example

```python
from authentik_openapi.models.stage_request import StageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of StageRequest from a JSON string
stage_request_instance = StageRequest.from_json(json)
# print the JSON string representation of the object
print(StageRequest.to_json())

# convert the object into a dict
stage_request_dict = stage_request_instance.to_dict()
# create an instance of StageRequest from a dict
stage_request_from_dict = StageRequest.from_dict(stage_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


