# EventMatcherPolicy

Event Matcher Policy Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk** | **str** |  | [readonly] 
**name** | **str** |  | 
**execution_logging** | **bool** | When this option is enabled, all executions of this policy will be logged. By default, only execution errors are logged. | [optional] 
**component** | **str** | Get object component so that we know how to edit the object | [readonly] 
**verbose_name** | **str** | Return object&#39;s verbose_name | [readonly] 
**verbose_name_plural** | **str** | Return object&#39;s plural verbose_name | [readonly] 
**meta_model_name** | **str** | Return internal model name | [readonly] 
**bound_to** | **int** | Return objects policy is bound to | [readonly] 
**action** | [**EventActions**](EventActions.md) | Match created events with this action type. When left empty, all action types will be matched. | [optional] 
**client_ip** | **str** | Matches Event&#39;s Client IP (strict matching, for network matching use an Expression Policy) | [optional] 
**app** | [**AppEnum**](AppEnum.md) | Match events created by selected application. When left empty, all applications are matched. | [optional] 
**model** | [**ModelEnum**](ModelEnum.md) | Match events created by selected model. When left empty, all models are matched. When an app is selected, all the application&#39;s models are matched. | [optional] 

## Example

```python
from authentik_openapi.models.event_matcher_policy import EventMatcherPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of EventMatcherPolicy from a JSON string
event_matcher_policy_instance = EventMatcherPolicy.from_json(json)
# print the JSON string representation of the object
print(EventMatcherPolicy.to_json())

# convert the object into a dict
event_matcher_policy_dict = event_matcher_policy_instance.to_dict()
# create an instance of EventMatcherPolicy from a dict
event_matcher_policy_from_dict = EventMatcherPolicy.from_dict(event_matcher_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


