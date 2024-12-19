# CodeScanningCodeqlDatabase

A CodeQL database.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The ID of the CodeQL database. | 
**name** | **str** | The name of the CodeQL database. | 
**language** | **str** | The language of the CodeQL database. | 
**uploader** | [**SimpleUser**](SimpleUser.md) |  | 
**content_type** | **str** | The MIME type of the CodeQL database file. | 
**size** | **int** | The size of the CodeQL database file in bytes. | 
**created_at** | **datetime** | The date and time at which the CodeQL database was created, in ISO 8601 format&#39;:&#39; YYYY-MM-DDTHH:MM:SSZ. | 
**updated_at** | **datetime** | The date and time at which the CodeQL database was last updated, in ISO 8601 format&#39;:&#39; YYYY-MM-DDTHH:MM:SSZ. | 
**url** | **str** | The URL at which to download the CodeQL database. The &#x60;Accept&#x60; header must be set to the value of the &#x60;content_type&#x60; property. | 
**commit_oid** | **str** | The commit SHA of the repository at the time the CodeQL database was created. | [optional] 

## Example

```python
from github_openapi.models.code_scanning_codeql_database import CodeScanningCodeqlDatabase

# TODO update the JSON string below
json = "{}"
# create an instance of CodeScanningCodeqlDatabase from a JSON string
code_scanning_codeql_database_instance = CodeScanningCodeqlDatabase.from_json(json)
# print the JSON string representation of the object
print(CodeScanningCodeqlDatabase.to_json())

# convert the object into a dict
code_scanning_codeql_database_dict = code_scanning_codeql_database_instance.to_dict()
# create an instance of CodeScanningCodeqlDatabase from a dict
code_scanning_codeql_database_from_dict = CodeScanningCodeqlDatabase.from_dict(code_scanning_codeql_database_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


