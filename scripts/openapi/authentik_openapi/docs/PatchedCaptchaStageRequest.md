# PatchedCaptchaStageRequest

CaptchaStage Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**flow_set** | [**List[FlowSetRequest]**](FlowSetRequest.md) |  | [optional] 
**public_key** | **str** | Public key, acquired your captcha Provider. | [optional] 
**private_key** | **str** | Private key, acquired your captcha Provider. | [optional] 
**js_url** | **str** |  | [optional] 
**api_url** | **str** |  | [optional] 
**score_min_threshold** | **float** |  | [optional] 
**score_max_threshold** | **float** |  | [optional] 
**error_on_invalid_score** | **bool** | When enabled and the received captcha score is outside of the given threshold, the stage will show an error message. When not enabled, the flow will continue, but the data from the captcha will be available in the context for policy decisions | [optional] 

## Example

```python
from authentik_openapi.models.patched_captcha_stage_request import PatchedCaptchaStageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedCaptchaStageRequest from a JSON string
patched_captcha_stage_request_instance = PatchedCaptchaStageRequest.from_json(json)
# print the JSON string representation of the object
print(PatchedCaptchaStageRequest.to_json())

# convert the object into a dict
patched_captcha_stage_request_dict = patched_captcha_stage_request_instance.to_dict()
# create an instance of PatchedCaptchaStageRequest from a dict
patched_captcha_stage_request_from_dict = PatchedCaptchaStageRequest.from_dict(patched_captcha_stage_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


