# CodeScanningVariantAnalysisScannedRepositoriesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**repository** | [**CodeScanningVariantAnalysisRepository**](CodeScanningVariantAnalysisRepository.md) |  | 
**analysis_status** | [**CodeScanningVariantAnalysisStatus**](CodeScanningVariantAnalysisStatus.md) |  | 
**result_count** | **int** | The number of results in the case of a successful analysis. This is only available for successful analyses. | [optional] 
**artifact_size_in_bytes** | **int** | The size of the artifact. This is only available for successful analyses. | [optional] 
**failure_message** | **str** | The reason of the failure of this repo task. This is only available if the repository task has failed. | [optional] 

## Example

```python
from github_openapi.models.code_scanning_variant_analysis_scanned_repositories_inner import CodeScanningVariantAnalysisScannedRepositoriesInner

# TODO update the JSON string below
json = "{}"
# create an instance of CodeScanningVariantAnalysisScannedRepositoriesInner from a JSON string
code_scanning_variant_analysis_scanned_repositories_inner_instance = CodeScanningVariantAnalysisScannedRepositoriesInner.from_json(json)
# print the JSON string representation of the object
print(CodeScanningVariantAnalysisScannedRepositoriesInner.to_json())

# convert the object into a dict
code_scanning_variant_analysis_scanned_repositories_inner_dict = code_scanning_variant_analysis_scanned_repositories_inner_instance.to_dict()
# create an instance of CodeScanningVariantAnalysisScannedRepositoriesInner from a dict
code_scanning_variant_analysis_scanned_repositories_inner_from_dict = CodeScanningVariantAnalysisScannedRepositoriesInner.from_dict(code_scanning_variant_analysis_scanned_repositories_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


