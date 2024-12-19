# CaptchaStage

CaptchaStage Serializer

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
**public_key** | **str** | Public key, acquired your captcha Provider. | 
**js_url** | **str** |  | [optional] 
**api_url** | **str** |  | [optional] 
**score_min_threshold** | **float** |  | [optional] 
**score_max_threshold** | **float** |  | [optional] 
**error_on_invalid_score** | **bool** | When enabled and the received captcha score is outside of the given threshold, the stage will show an error message. When not enabled, the flow will continue, but the data from the captcha will be available in the context for policy decisions | [optional] 

## Example

```python
from authentik_openapi.models.captcha_stage import CaptchaStage

# TODO update the JSON string below
json = "{}"
# create an instance of CaptchaStage from a JSON string
captcha_stage_instance = CaptchaStage.from_json(json)
# print the JSON string representation of the object
print(CaptchaStage.to_json())

# convert the object into a dict
captcha_stage_dict = captcha_stage_instance.to_dict()
# create an instance of CaptchaStage from a dict
captcha_stage_from_dict = CaptchaStage.from_dict(captcha_stage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


