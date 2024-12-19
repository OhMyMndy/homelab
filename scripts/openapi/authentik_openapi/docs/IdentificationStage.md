# IdentificationStage

IdentificationStage Serializer

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
from authentik_openapi.models.identification_stage import IdentificationStage

# TODO update the JSON string below
json = "{}"
# create an instance of IdentificationStage from a JSON string
identification_stage_instance = IdentificationStage.from_json(json)
# print the JSON string representation of the object
print(IdentificationStage.to_json())

# convert the object into a dict
identification_stage_dict = identification_stage_instance.to_dict()
# create an instance of IdentificationStage from a dict
identification_stage_from_dict = IdentificationStage.from_dict(identification_stage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


