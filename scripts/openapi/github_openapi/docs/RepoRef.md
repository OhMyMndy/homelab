# RepoRef


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**url** | **str** |  | 

## Example

```python
from github_openapi.models.repo_ref import RepoRef

# TODO update the JSON string below
json = "{}"
# create an instance of RepoRef from a JSON string
repo_ref_instance = RepoRef.from_json(json)
# print the JSON string representation of the object
print(RepoRef.to_json())

# convert the object into a dict
repo_ref_dict = repo_ref_instance.to_dict()
# create an instance of RepoRef from a dict
repo_ref_from_dict = RepoRef.from_dict(repo_ref_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


