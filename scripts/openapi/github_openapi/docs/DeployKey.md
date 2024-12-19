# DeployKey

An SSH key granting access to a single repository.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**key** | **str** |  | 
**url** | **str** |  | 
**title** | **str** |  | 
**verified** | **bool** |  | 
**created_at** | **str** |  | 
**read_only** | **bool** |  | 
**added_by** | **str** |  | [optional] 
**last_used** | **str** |  | [optional] 
**enabled** | **bool** |  | [optional] 

## Example

```python
from github_openapi.models.deploy_key import DeployKey

# TODO update the JSON string below
json = "{}"
# create an instance of DeployKey from a JSON string
deploy_key_instance = DeployKey.from_json(json)
# print the JSON string representation of the object
print(DeployKey.to_json())

# convert the object into a dict
deploy_key_dict = deploy_key_instance.to_dict()
# create an instance of DeployKey from a dict
deploy_key_from_dict = DeployKey.from_dict(deploy_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


