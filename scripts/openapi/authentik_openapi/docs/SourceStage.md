# SourceStage

SourceStage Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk** | **str** |  | [readonly] 
**name** | **str** |  | 
**component** | **str** | Get object type so that we know how to edit the object | [readonly] 
**verbose_name** | **str** | Return object&#39;s verbose_name | [readonly] 
**verbose_name_plural** | **str** | Return object&#39;s plural verbose_name | [readonly] 
**meta_model_name** | **str** | Return internal model name | [readonly] 
**flow_set** | [**List[FlowSet]**](FlowSet.md) |  | [optional] 
**source** | **str** |  | 
**resume_timeout** | **str** | Amount of time a user can take to return from the source to continue the flow (Format: hours&#x3D;-1;minutes&#x3D;-2;seconds&#x3D;-3) | [optional] 

## Example

```python
from authentik_openapi.models.source_stage import SourceStage

# TODO update the JSON string below
json = "{}"
# create an instance of SourceStage from a JSON string
source_stage_instance = SourceStage.from_json(json)
# print the JSON string representation of the object
print(SourceStage.to_json())

# convert the object into a dict
source_stage_dict = source_stage_instance.to_dict()
# create an instance of SourceStage from a dict
source_stage_from_dict = SourceStage.from_dict(source_stage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


