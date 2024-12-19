# ReposGetAllEnvironments200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_count** | **int** | The number of environments in this repository | [optional] 
**environments** | [**List[Environment]**](Environment.md) |  | [optional] 

## Example

```python
from github_openapi.models.repos_get_all_environments200_response import ReposGetAllEnvironments200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ReposGetAllEnvironments200Response from a JSON string
repos_get_all_environments200_response_instance = ReposGetAllEnvironments200Response.from_json(json)
# print the JSON string representation of the object
print(ReposGetAllEnvironments200Response.to_json())

# convert the object into a dict
repos_get_all_environments200_response_dict = repos_get_all_environments200_response_instance.to_dict()
# create an instance of ReposGetAllEnvironments200Response from a dict
repos_get_all_environments200_response_from_dict = ReposGetAllEnvironments200Response.from_dict(repos_get_all_environments200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


