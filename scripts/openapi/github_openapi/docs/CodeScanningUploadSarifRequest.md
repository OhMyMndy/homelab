# CodeScanningUploadSarifRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**commit_sha** | **str** | The SHA of the commit to which the analysis you are uploading relates. | 
**ref** | **str** | The full Git reference, formatted as &#x60;refs/heads/&lt;branch name&gt;&#x60;, &#x60;refs/tags/&lt;tag&gt;&#x60;, &#x60;refs/pull/&lt;number&gt;/merge&#x60;, or &#x60;refs/pull/&lt;number&gt;/head&#x60;. | 
**sarif** | **str** | A Base64 string representing the SARIF file to upload. You must first compress your SARIF file using [&#x60;gzip&#x60;](http://www.gnu.org/software/gzip/manual/gzip.html) and then translate the contents of the file into a Base64 encoding string. For more information, see \&quot;[SARIF support for code scanning](https://docs.github.com/code-security/secure-coding/sarif-support-for-code-scanning).\&quot; | 
**checkout_uri** | **str** | The base directory used in the analysis, as it appears in the SARIF file. This property is used to convert file paths from absolute to relative, so that alerts can be mapped to their correct location in the repository. | [optional] 
**started_at** | **datetime** | The time that the analysis run began. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;. | [optional] 
**tool_name** | **str** | The name of the tool used to generate the code scanning analysis. If this parameter is not used, the tool name defaults to \&quot;API\&quot;. If the uploaded SARIF contains a tool GUID, this will be available for filtering using the &#x60;tool_guid&#x60; parameter of operations such as &#x60;GET /repos/{owner}/{repo}/code-scanning/alerts&#x60;. | [optional] 
**validate** | **bool** | Whether the SARIF file will be validated according to the code scanning specifications. This parameter is intended to help integrators ensure that the uploaded SARIF files are correctly rendered by code scanning. | [optional] 

## Example

```python
from github_openapi.models.code_scanning_upload_sarif_request import CodeScanningUploadSarifRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CodeScanningUploadSarifRequest from a JSON string
code_scanning_upload_sarif_request_instance = CodeScanningUploadSarifRequest.from_json(json)
# print the JSON string representation of the object
print(CodeScanningUploadSarifRequest.to_json())

# convert the object into a dict
code_scanning_upload_sarif_request_dict = code_scanning_upload_sarif_request_instance.to_dict()
# create an instance of CodeScanningUploadSarifRequest from a dict
code_scanning_upload_sarif_request_from_dict = CodeScanningUploadSarifRequest.from_dict(code_scanning_upload_sarif_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


