# PreviewRuleMatches200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**matches** | [**List[PreviewRuleMatches200ResponseMatchesInner]**](PreviewRuleMatches200ResponseMatchesInner.md) |  | 
**type** | **str** | Echoes the &#x60;type&#x60; provided in the request.  | 
**preview_for** | **str** | Echoes the &#x60;previewFor&#x60; provided in the request.  | 

## Example

```python
from tailscale_openapi.models.preview_rule_matches200_response import PreviewRuleMatches200Response

# TODO update the JSON string below
json = "{}"
# create an instance of PreviewRuleMatches200Response from a JSON string
preview_rule_matches200_response_instance = PreviewRuleMatches200Response.from_json(json)
# print the JSON string representation of the object
print(PreviewRuleMatches200Response.to_json())

# convert the object into a dict
preview_rule_matches200_response_dict = preview_rule_matches200_response_instance.to_dict()
# create an instance of PreviewRuleMatches200Response from a dict
preview_rule_matches200_response_from_dict = PreviewRuleMatches200Response.from_dict(preview_rule_matches200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


