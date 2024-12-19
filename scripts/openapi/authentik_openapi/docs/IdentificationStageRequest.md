# IdentificationStageRequest

IdentificationStage Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**flow_set** | [**List[FlowSetRequest]**](FlowSetRequest.md) |  | [optional] 
**user_fields** | [**List[UserFieldsEnum]**](UserFieldsEnum.md) | Fields of the user object to match against. (Hold shift to select multiple options) | [optional] 
**password_stage** | **str** | When set, shows a password field, instead of showing the password field as seaprate step. | [optional] 
**case_insensitive_matching** | **bool** | When enabled, user fields are matched regardless of their casing. | [optional] 
**show_matched_user** | **bool** | When a valid username/email has been entered, and this option is enabled, the user&#39;s username and avatar will be shown. Otherwise, the text that the user entered will be shown | [optional] 
**enrollment_flow** | **str** | Optional enrollment flow, which is linked at the bottom of the page. | [optional] 
**recovery_flow** | **str** | Optional recovery flow, which is linked at the bottom of the page. | [optional] 
**passwordless_flow** | **str** | Optional passwordless flow, which is linked at the bottom of the page. | [optional] 
**sources** | **List[str]** | Specify which sources should be shown. | [optional] 
**show_source_labels** | **bool** |  | [optional] 
**pretend_user_exists** | **bool** | When enabled, the stage will succeed and continue even when incorrect user info is entered. | [optional] 

## Example

```python
from authentik_openapi.models.identification_stage_request import IdentificationStageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IdentificationStageRequest from a JSON string
identification_stage_request_instance = IdentificationStageRequest.from_json(json)
# print the JSON string representation of the object
print(IdentificationStageRequest.to_json())

# convert the object into a dict
identification_stage_request_dict = identification_stage_request_instance.to_dict()
# create an instance of IdentificationStageRequest from a dict
identification_stage_request_from_dict = IdentificationStageRequest.from_dict(identification_stage_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


