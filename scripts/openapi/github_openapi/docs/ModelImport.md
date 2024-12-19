# ModelImport

A repository import from an external source.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vcs** | **str** |  | 
**use_lfs** | **bool** |  | [optional] 
**vcs_url** | **str** | The URL of the originating repository. | 
**svc_root** | **str** |  | [optional] 
**tfvc_project** | **str** |  | [optional] 
**status** | **str** |  | 
**status_text** | **str** |  | [optional] 
**failed_step** | **str** |  | [optional] 
**error_message** | **str** |  | [optional] 
**import_percent** | **int** |  | [optional] 
**commit_count** | **int** |  | [optional] 
**push_percent** | **int** |  | [optional] 
**has_large_files** | **bool** |  | [optional] 
**large_files_size** | **int** |  | [optional] 
**large_files_count** | **int** |  | [optional] 
**project_choices** | [**List[ImportProjectChoicesInner]**](ImportProjectChoicesInner.md) |  | [optional] 
**message** | **str** |  | [optional] 
**authors_count** | **int** |  | [optional] 
**url** | **str** |  | 
**html_url** | **str** |  | 
**authors_url** | **str** |  | 
**repository_url** | **str** |  | 
**svn_root** | **str** |  | [optional] 

## Example

```python
from github_openapi.models.model_import import ModelImport

# TODO update the JSON string below
json = "{}"
# create an instance of ModelImport from a JSON string
model_import_instance = ModelImport.from_json(json)
# print the JSON string representation of the object
print(ModelImport.to_json())

# convert the object into a dict
model_import_dict = model_import_instance.to_dict()
# create an instance of ModelImport from a dict
model_import_from_dict = ModelImport.from_dict(model_import_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


