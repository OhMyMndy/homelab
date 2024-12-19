# CodeScanningVariantAnalysisSkippedRepositoriesNotFoundRepos


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**repository_count** | **int** | The total number of repositories that were skipped for this reason. | 
**repository_full_names** | **List[str]** | A list of full repository names that were skipped. This list may not include all repositories that were skipped. | 

## Example

```python
from github_openapi.models.code_scanning_variant_analysis_skipped_repositories_not_found_repos import CodeScanningVariantAnalysisSkippedRepositoriesNotFoundRepos

# TODO update the JSON string below
json = "{}"
# create an instance of CodeScanningVariantAnalysisSkippedRepositoriesNotFoundRepos from a JSON string
code_scanning_variant_analysis_skipped_repositories_not_found_repos_instance = CodeScanningVariantAnalysisSkippedRepositoriesNotFoundRepos.from_json(json)
# print the JSON string representation of the object
print(CodeScanningVariantAnalysisSkippedRepositoriesNotFoundRepos.to_json())

# convert the object into a dict
code_scanning_variant_analysis_skipped_repositories_not_found_repos_dict = code_scanning_variant_analysis_skipped_repositories_not_found_repos_instance.to_dict()
# create an instance of CodeScanningVariantAnalysisSkippedRepositoriesNotFoundRepos from a dict
code_scanning_variant_analysis_skipped_repositories_not_found_repos_from_dict = CodeScanningVariantAnalysisSkippedRepositoriesNotFoundRepos.from_dict(code_scanning_variant_analysis_skipped_repositories_not_found_repos_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


