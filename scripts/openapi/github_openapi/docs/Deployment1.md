# Deployment1

The [deployment](https://docs.github.com/rest/deployments/deployments#list-deployments).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **str** |  | 
**creator** | [**User2**](User2.md) |  | 
**description** | **str** |  | 
**environment** | **str** |  | 
**id** | **int** |  | 
**node_id** | **str** |  | 
**original_environment** | **str** |  | 
**payload** | [**Deployment1Payload**](Deployment1Payload.md) |  | 
**performed_via_github_app** | [**App6**](App6.md) |  | [optional] 
**production_environment** | **bool** |  | [optional] 
**ref** | **str** |  | 
**repository_url** | **str** |  | 
**sha** | **str** |  | 
**statuses_url** | **str** |  | 
**task** | **str** |  | 
**transient_environment** | **bool** |  | [optional] 
**updated_at** | **str** |  | 
**url** | **str** |  | 

## Example

```python
from github_openapi.models.deployment1 import Deployment1

# TODO update the JSON string below
json = "{}"
# create an instance of Deployment1 from a JSON string
deployment1_instance = Deployment1.from_json(json)
# print the JSON string representation of the object
print(Deployment1.to_json())

# convert the object into a dict
deployment1_dict = deployment1_instance.to_dict()
# create an instance of Deployment1 from a dict
deployment1_from_dict = Deployment1.from_dict(deployment1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


