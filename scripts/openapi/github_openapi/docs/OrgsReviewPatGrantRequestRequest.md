# OrgsReviewPatGrantRequestRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | Action to apply to the request. | 
**reason** | **str** | Reason for approving or denying the request. Max 1024 characters. | [optional] 

## Example

```python
from github_openapi.models.orgs_review_pat_grant_request_request import OrgsReviewPatGrantRequestRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OrgsReviewPatGrantRequestRequest from a JSON string
orgs_review_pat_grant_request_request_instance = OrgsReviewPatGrantRequestRequest.from_json(json)
# print the JSON string representation of the object
print(OrgsReviewPatGrantRequestRequest.to_json())

# convert the object into a dict
orgs_review_pat_grant_request_request_dict = orgs_review_pat_grant_request_request_instance.to_dict()
# create an instance of OrgsReviewPatGrantRequestRequest from a dict
orgs_review_pat_grant_request_request_from_dict = OrgsReviewPatGrantRequestRequest.from_dict(orgs_review_pat_grant_request_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


