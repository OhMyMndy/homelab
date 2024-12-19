# Artifact

An artifact

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**node_id** | **str** |  | 
**name** | **str** | The name of the artifact. | 
**size_in_bytes** | **int** | The size in bytes of the artifact. | 
**url** | **str** |  | 
**archive_download_url** | **str** |  | 
**expired** | **bool** | Whether or not the artifact has expired. | 
**created_at** | **datetime** |  | 
**expires_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**workflow_run** | [**ArtifactWorkflowRun**](ArtifactWorkflowRun.md) |  | [optional] 

## Example

```python
from github_openapi.models.artifact import Artifact

# TODO update the JSON string below
json = "{}"
# create an instance of Artifact from a JSON string
artifact_instance = Artifact.from_json(json)
# print the JSON string representation of the object
print(Artifact.to_json())

# convert the object into a dict
artifact_dict = artifact_instance.to_dict()
# create an instance of Artifact from a dict
artifact_from_dict = Artifact.from_dict(artifact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


