# CodeScanningAnalysis


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ref** | **str** | The Git reference, formatted as &#x60;refs/pull/&lt;number&gt;/merge&#x60;, &#x60;refs/pull/&lt;number&gt;/head&#x60;, &#x60;refs/heads/&lt;branch name&gt;&#x60; or simply &#x60;&lt;branch name&gt;&#x60;. | 
**commit_sha** | **str** | The SHA of the commit to which the analysis you are uploading relates. | 
**analysis_key** | **str** | Identifies the configuration under which the analysis was executed. For example, in GitHub Actions this includes the workflow filename and job name. | 
**environment** | **str** | Identifies the variable values associated with the environment in which this analysis was performed. | 
**category** | **str** | Identifies the configuration under which the analysis was executed. Used to distinguish between multiple analyses for the same tool and commit, but performed on different languages or different parts of the code. | [optional] 
**error** | **str** |  | 
**created_at** | **datetime** | The time that the analysis was created in ISO 8601 format: &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;. | [readonly] 
**results_count** | **int** | The total number of results in the analysis. | 
**rules_count** | **int** | The total number of rules used in the analysis. | 
**id** | **int** | Unique identifier for this analysis. | 
**url** | **str** | The REST API URL of the analysis resource. | [readonly] 
**sarif_id** | **str** | An identifier for the upload. | 
**tool** | [**CodeScanningAnalysisTool**](CodeScanningAnalysisTool.md) |  | 
**deletable** | **bool** |  | 
**warning** | **str** | Warning generated when processing the analysis | 

## Example

```python
from github_openapi.models.code_scanning_analysis import CodeScanningAnalysis

# TODO update the JSON string below
json = "{}"
# create an instance of CodeScanningAnalysis from a JSON string
code_scanning_analysis_instance = CodeScanningAnalysis.from_json(json)
# print the JSON string representation of the object
print(CodeScanningAnalysis.to_json())

# convert the object into a dict
code_scanning_analysis_dict = code_scanning_analysis_instance.to_dict()
# create an instance of CodeScanningAnalysis from a dict
code_scanning_analysis_from_dict = CodeScanningAnalysis.from_dict(code_scanning_analysis_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


