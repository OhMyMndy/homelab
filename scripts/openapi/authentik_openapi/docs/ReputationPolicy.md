# ReputationPolicy

Reputation Policy Serializer

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
**check_ip** | **bool** |  | [optional] 
**check_username** | **bool** |  | [optional] 
**threshold** | **int** |  | [optional] 

## Example

```python
from authentik_openapi.models.reputation_policy import ReputationPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of ReputationPolicy from a JSON string
reputation_policy_instance = ReputationPolicy.from_json(json)
# print the JSON string representation of the object
print(ReputationPolicy.to_json())

# convert the object into a dict
reputation_policy_dict = reputation_policy_instance.to_dict()
# create an instance of ReputationPolicy from a dict
reputation_policy_from_dict = ReputationPolicy.from_dict(reputation_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


