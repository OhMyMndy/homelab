# DependencyGraphCreateRepositorySnapshot201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID of the created snapshot. | 
**created_at** | **str** | The time at which the snapshot was created. | 
**result** | **str** | Either \&quot;SUCCESS\&quot;, \&quot;ACCEPTED\&quot;, or \&quot;INVALID\&quot;. \&quot;SUCCESS\&quot; indicates that the snapshot was successfully created and the repository&#39;s dependencies were updated. \&quot;ACCEPTED\&quot; indicates that the snapshot was successfully created, but the repository&#39;s dependencies were not updated. \&quot;INVALID\&quot; indicates that the snapshot was malformed. | 
**message** | **str** | A message providing further details about the result, such as why the dependencies were not updated. | 

## Example

```python
from github_openapi.models.dependency_graph_create_repository_snapshot201_response import DependencyGraphCreateRepositorySnapshot201Response

# TODO update the JSON string below
json = "{}"
# create an instance of DependencyGraphCreateRepositorySnapshot201Response from a JSON string
dependency_graph_create_repository_snapshot201_response_instance = DependencyGraphCreateRepositorySnapshot201Response.from_json(json)
# print the JSON string representation of the object
print(DependencyGraphCreateRepositorySnapshot201Response.to_json())

# convert the object into a dict
dependency_graph_create_repository_snapshot201_response_dict = dependency_graph_create_repository_snapshot201_response_instance.to_dict()
# create an instance of DependencyGraphCreateRepositorySnapshot201Response from a dict
dependency_graph_create_repository_snapshot201_response_from_dict = DependencyGraphCreateRepositorySnapshot201Response.from_dict(dependency_graph_create_repository_snapshot201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


