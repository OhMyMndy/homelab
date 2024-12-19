# CodeScanningVariantAnalysisSkippedRepoGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**repository_count** | **int** | The total number of repositories that were skipped for this reason. | 
**repositories** | [**List[CodeScanningVariantAnalysisRepository]**](CodeScanningVariantAnalysisRepository.md) | A list of repositories that were skipped. This list may not include all repositories that were skipped. This is only available when the repository was found and the user has access to it. | 

## Example

```python
from github_openapi.models.code_scanning_variant_analysis_skipped_repo_group import CodeScanningVariantAnalysisSkippedRepoGroup

# TODO update the JSON string below
json = "{}"
# create an instance of CodeScanningVariantAnalysisSkippedRepoGroup from a JSON string
code_scanning_variant_analysis_skipped_repo_group_instance = CodeScanningVariantAnalysisSkippedRepoGroup.from_json(json)
# print the JSON string representation of the object
print(CodeScanningVariantAnalysisSkippedRepoGroup.to_json())

# convert the object into a dict
code_scanning_variant_analysis_skipped_repo_group_dict = code_scanning_variant_analysis_skipped_repo_group_instance.to_dict()
# create an instance of CodeScanningVariantAnalysisSkippedRepoGroup from a dict
code_scanning_variant_analysis_skipped_repo_group_from_dict = CodeScanningVariantAnalysisSkippedRepoGroup.from_dict(code_scanning_variant_analysis_skipped_repo_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


