# EventMatcherPolicyRequest

Event Matcher Policy Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**execution_logging** | **bool** | When this option is enabled, all executions of this policy will be logged. By default, only execution errors are logged. | [optional] 
**action** | [**EventActions**](EventActions.md) | Match created events with this action type. When left empty, all action types will be matched. | [optional] 
**client_ip** | **str** | Matches Event&#39;s Client IP (strict matching, for network matching use an Expression Policy) | [optional] 
**app** | [**AppEnum**](AppEnum.md) | Match events created by selected application. When left empty, all applications are matched. | [optional] 
**model** | [**ModelEnum**](ModelEnum.md) | Match events created by selected model. When left empty, all models are matched. When an app is selected, all the application&#39;s models are matched. | [optional] 

## Example

```python
from authentik_openapi.models.event_matcher_policy_request import EventMatcherPolicyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EventMatcherPolicyRequest from a JSON string
event_matcher_policy_request_instance = EventMatcherPolicyRequest.from_json(json)
# print the JSON string representation of the object
print(EventMatcherPolicyRequest.to_json())

# convert the object into a dict
event_matcher_policy_request_dict = event_matcher_policy_request_instance.to_dict()
# create an instance of EventMatcherPolicyRequest from a dict
event_matcher_policy_request_from_dict = EventMatcherPolicyRequest.from_dict(event_matcher_policy_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


