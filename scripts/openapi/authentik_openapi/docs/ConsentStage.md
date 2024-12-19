# ConsentStage

ConsentStage Serializer

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
**mode** | [**ConsentStageModeEnum**](ConsentStageModeEnum.md) |  | [optional] 
**consent_expire_in** | **str** | Offset after which consent expires. (Format: hours&#x3D;1;minutes&#x3D;2;seconds&#x3D;3). | [optional] 

## Example

```python
from authentik_openapi.models.consent_stage import ConsentStage

# TODO update the JSON string below
json = "{}"
# create an instance of ConsentStage from a JSON string
consent_stage_instance = ConsentStage.from_json(json)
# print the JSON string representation of the object
print(ConsentStage.to_json())

# convert the object into a dict
consent_stage_dict = consent_stage_instance.to_dict()
# create an instance of ConsentStage from a dict
consent_stage_from_dict = ConsentStage.from_dict(consent_stage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


