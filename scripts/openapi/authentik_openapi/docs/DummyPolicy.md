# DummyPolicy

Dummy Policy Serializer

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
**result** | **bool** |  | [optional] 
**wait_min** | **int** |  | [optional] 
**wait_max** | **int** |  | [optional] 

## Example

```python
from authentik_openapi.models.dummy_policy import DummyPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of DummyPolicy from a JSON string
dummy_policy_instance = DummyPolicy.from_json(json)
# print the JSON string representation of the object
print(DummyPolicy.to_json())

# convert the object into a dict
dummy_policy_dict = dummy_policy_instance.to_dict()
# create an instance of DummyPolicy from a dict
dummy_policy_from_dict = DummyPolicy.from_dict(dummy_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


