# CodeScanningCreateVariantAnalysisRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**language** | [**CodeScanningVariantAnalysisLanguage**](CodeScanningVariantAnalysisLanguage.md) |  | 
**query_pack** | **str** | A Base64-encoded tarball containing a CodeQL query and all its dependencies | 
**repositories** | **List[str]** | List of repository names (in the form &#x60;owner/repo-name&#x60;) to run the query against. Precisely one property from &#x60;repositories&#x60;, &#x60;repository_lists&#x60; and &#x60;repository_owners&#x60; is required. | [optional] 
**repository_lists** | **List[str]** | List of repository lists to run the query against. Precisely one property from &#x60;repositories&#x60;, &#x60;repository_lists&#x60; and &#x60;repository_owners&#x60; is required. | [optional] 
**repository_owners** | **List[str]** | List of organization or user names whose repositories the query should be run against. Precisely one property from &#x60;repositories&#x60;, &#x60;repository_lists&#x60; and &#x60;repository_owners&#x60; is required. | [optional] 

## Example

```python
from github_openapi.models.code_scanning_create_variant_analysis_request import CodeScanningCreateVariantAnalysisRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CodeScanningCreateVariantAnalysisRequest from a JSON string
code_scanning_create_variant_analysis_request_instance = CodeScanningCreateVariantAnalysisRequest.from_json(json)
# print the JSON string representation of the object
print(CodeScanningCreateVariantAnalysisRequest.to_json())

# convert the object into a dict
code_scanning_create_variant_analysis_request_dict = code_scanning_create_variant_analysis_request_instance.to_dict()
# create an instance of CodeScanningCreateVariantAnalysisRequest from a dict
code_scanning_create_variant_analysis_request_from_dict = CodeScanningCreateVariantAnalysisRequest.from_dict(code_scanning_create_variant_analysis_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


