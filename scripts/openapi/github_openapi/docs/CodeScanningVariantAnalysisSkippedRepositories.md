# CodeScanningVariantAnalysisSkippedRepositories

Information about repositories that were skipped from processing. This information is only available to the user that initiated the variant analysis.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_mismatch_repos** | [**CodeScanningVariantAnalysisSkippedRepoGroup**](CodeScanningVariantAnalysisSkippedRepoGroup.md) |  | 
**not_found_repos** | [**CodeScanningVariantAnalysisSkippedRepositoriesNotFoundRepos**](CodeScanningVariantAnalysisSkippedRepositoriesNotFoundRepos.md) |  | 
**no_codeql_db_repos** | [**CodeScanningVariantAnalysisSkippedRepoGroup**](CodeScanningVariantAnalysisSkippedRepoGroup.md) |  | 
**over_limit_repos** | [**CodeScanningVariantAnalysisSkippedRepoGroup**](CodeScanningVariantAnalysisSkippedRepoGroup.md) |  | 

## Example

```python
from github_openapi.models.code_scanning_variant_analysis_skipped_repositories import CodeScanningVariantAnalysisSkippedRepositories

# TODO update the JSON string below
json = "{}"
# create an instance of CodeScanningVariantAnalysisSkippedRepositories from a JSON string
code_scanning_variant_analysis_skipped_repositories_instance = CodeScanningVariantAnalysisSkippedRepositories.from_json(json)
# print the JSON string representation of the object
print(CodeScanningVariantAnalysisSkippedRepositories.to_json())

# convert the object into a dict
code_scanning_variant_analysis_skipped_repositories_dict = code_scanning_variant_analysis_skipped_repositories_instance.to_dict()
# create an instance of CodeScanningVariantAnalysisSkippedRepositories from a dict
code_scanning_variant_analysis_skipped_repositories_from_dict = CodeScanningVariantAnalysisSkippedRepositories.from_dict(code_scanning_variant_analysis_skipped_repositories_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


