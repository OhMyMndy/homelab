# CodeScanningVariantAnalysisRepoTask


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**repository** | [**SimpleRepository**](SimpleRepository.md) |  | 
**analysis_status** | [**CodeScanningVariantAnalysisStatus**](CodeScanningVariantAnalysisStatus.md) |  | 
**artifact_size_in_bytes** | **int** | The size of the artifact. This is only available for successful analyses. | [optional] 
**result_count** | **int** | The number of results in the case of a successful analysis. This is only available for successful analyses. | [optional] 
**failure_message** | **str** | The reason of the failure of this repo task. This is only available if the repository task has failed. | [optional] 
**database_commit_sha** | **str** | The SHA of the commit the CodeQL database was built against. This is only available for successful analyses. | [optional] 
**source_location_prefix** | **str** | The source location prefix to use. This is only available for successful analyses. | [optional] 
**artifact_url** | **str** | The URL of the artifact. This is only available for successful analyses. | [optional] 

## Example

```python
from github_openapi.models.code_scanning_variant_analysis_repo_task import CodeScanningVariantAnalysisRepoTask

# TODO update the JSON string below
json = "{}"
# create an instance of CodeScanningVariantAnalysisRepoTask from a JSON string
code_scanning_variant_analysis_repo_task_instance = CodeScanningVariantAnalysisRepoTask.from_json(json)
# print the JSON string representation of the object
print(CodeScanningVariantAnalysisRepoTask.to_json())

# convert the object into a dict
code_scanning_variant_analysis_repo_task_dict = code_scanning_variant_analysis_repo_task_instance.to_dict()
# create an instance of CodeScanningVariantAnalysisRepoTask from a dict
code_scanning_variant_analysis_repo_task_from_dict = CodeScanningVariantAnalysisRepoTask.from_dict(code_scanning_variant_analysis_repo_task_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


