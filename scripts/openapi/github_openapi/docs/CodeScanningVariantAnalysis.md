# CodeScanningVariantAnalysis

A run of a CodeQL query against one or more repositories.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The ID of the variant analysis. | 
**controller_repo** | [**SimpleRepository**](SimpleRepository.md) |  | 
**actor** | [**SimpleUser**](SimpleUser.md) |  | 
**query_language** | [**CodeScanningVariantAnalysisLanguage**](CodeScanningVariantAnalysisLanguage.md) |  | 
**query_pack_url** | **str** | The download url for the query pack. | 
**created_at** | **datetime** | The date and time at which the variant analysis was created, in ISO 8601 format&#39;:&#39; YYYY-MM-DDTHH:MM:SSZ. | [optional] 
**updated_at** | **datetime** | The date and time at which the variant analysis was last updated, in ISO 8601 format&#39;:&#39; YYYY-MM-DDTHH:MM:SSZ. | [optional] 
**completed_at** | **datetime** | The date and time at which the variant analysis was completed, in ISO 8601 format&#39;:&#39; YYYY-MM-DDTHH:MM:SSZ. Will be null if the variant analysis has not yet completed or this information is not available. | [optional] 
**status** | **str** |  | 
**actions_workflow_run_id** | **int** | The GitHub Actions workflow run used to execute this variant analysis. This is only available if the workflow run has started. | [optional] 
**failure_reason** | **str** | The reason for a failure of the variant analysis. This is only available if the variant analysis has failed. | [optional] 
**scanned_repositories** | [**List[CodeScanningVariantAnalysisScannedRepositoriesInner]**](CodeScanningVariantAnalysisScannedRepositoriesInner.md) |  | [optional] 
**skipped_repositories** | [**CodeScanningVariantAnalysisSkippedRepositories**](CodeScanningVariantAnalysisSkippedRepositories.md) |  | [optional] 

## Example

```python
from github_openapi.models.code_scanning_variant_analysis import CodeScanningVariantAnalysis

# TODO update the JSON string below
json = "{}"
# create an instance of CodeScanningVariantAnalysis from a JSON string
code_scanning_variant_analysis_instance = CodeScanningVariantAnalysis.from_json(json)
# print the JSON string representation of the object
print(CodeScanningVariantAnalysis.to_json())

# convert the object into a dict
code_scanning_variant_analysis_dict = code_scanning_variant_analysis_instance.to_dict()
# create an instance of CodeScanningVariantAnalysis from a dict
code_scanning_variant_analysis_from_dict = CodeScanningVariantAnalysis.from_dict(code_scanning_variant_analysis_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


