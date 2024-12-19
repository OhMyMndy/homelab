# CodeScanningVariantAnalysisRepository

Repository Identifier

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | A unique identifier of the repository. | 
**name** | **str** | The name of the repository. | 
**full_name** | **str** | The full, globally unique, name of the repository. | 
**private** | **bool** | Whether the repository is private. | 
**stargazers_count** | **int** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from github_openapi.models.code_scanning_variant_analysis_repository import CodeScanningVariantAnalysisRepository

# TODO update the JSON string below
json = "{}"
# create an instance of CodeScanningVariantAnalysisRepository from a JSON string
code_scanning_variant_analysis_repository_instance = CodeScanningVariantAnalysisRepository.from_json(json)
# print the JSON string representation of the object
print(CodeScanningVariantAnalysisRepository.to_json())

# convert the object into a dict
code_scanning_variant_analysis_repository_dict = code_scanning_variant_analysis_repository_instance.to_dict()
# create an instance of CodeScanningVariantAnalysisRepository from a dict
code_scanning_variant_analysis_repository_from_dict = CodeScanningVariantAnalysisRepository.from_dict(code_scanning_variant_analysis_repository_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


