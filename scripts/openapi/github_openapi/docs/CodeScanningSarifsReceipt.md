# CodeScanningSarifsReceipt


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | An identifier for the upload. | [optional] 
**url** | **str** | The REST API URL for checking the status of the upload. | [optional] [readonly] 

## Example

```python
from github_openapi.models.code_scanning_sarifs_receipt import CodeScanningSarifsReceipt

# TODO update the JSON string below
json = "{}"
# create an instance of CodeScanningSarifsReceipt from a JSON string
code_scanning_sarifs_receipt_instance = CodeScanningSarifsReceipt.from_json(json)
# print the JSON string representation of the object
print(CodeScanningSarifsReceipt.to_json())

# convert the object into a dict
code_scanning_sarifs_receipt_dict = code_scanning_sarifs_receipt_instance.to_dict()
# create an instance of CodeScanningSarifsReceipt from a dict
code_scanning_sarifs_receipt_from_dict = CodeScanningSarifsReceipt.from_dict(code_scanning_sarifs_receipt_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


