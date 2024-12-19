# ChecksCreateRequestOutputAnnotationsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** | The path of the file to add an annotation to. For example, &#x60;assets/css/main.css&#x60;. | 
**start_line** | **int** | The start line of the annotation. Line numbers start at 1. | 
**end_line** | **int** | The end line of the annotation. | 
**start_column** | **int** | The start column of the annotation. Annotations only support &#x60;start_column&#x60; and &#x60;end_column&#x60; on the same line. Omit this parameter if &#x60;start_line&#x60; and &#x60;end_line&#x60; have different values. Column numbers start at 1. | [optional] 
**end_column** | **int** | The end column of the annotation. Annotations only support &#x60;start_column&#x60; and &#x60;end_column&#x60; on the same line. Omit this parameter if &#x60;start_line&#x60; and &#x60;end_line&#x60; have different values. | [optional] 
**annotation_level** | **str** | The level of the annotation. | 
**message** | **str** | A short description of the feedback for these lines of code. The maximum size is 64 KB. | 
**title** | **str** | The title that represents the annotation. The maximum size is 255 characters. | [optional] 
**raw_details** | **str** | Details about this annotation. The maximum size is 64 KB. | [optional] 

## Example

```python
from github_openapi.models.checks_create_request_output_annotations_inner import ChecksCreateRequestOutputAnnotationsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ChecksCreateRequestOutputAnnotationsInner from a JSON string
checks_create_request_output_annotations_inner_instance = ChecksCreateRequestOutputAnnotationsInner.from_json(json)
# print the JSON string representation of the object
print(ChecksCreateRequestOutputAnnotationsInner.to_json())

# convert the object into a dict
checks_create_request_output_annotations_inner_dict = checks_create_request_output_annotations_inner_instance.to_dict()
# create an instance of ChecksCreateRequestOutputAnnotationsInner from a dict
checks_create_request_output_annotations_inner_from_dict = ChecksCreateRequestOutputAnnotationsInner.from_dict(checks_create_request_output_annotations_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


