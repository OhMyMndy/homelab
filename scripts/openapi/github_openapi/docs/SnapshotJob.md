# SnapshotJob


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The external ID of the job. | 
**correlator** | **str** | Correlator provides a key that is used to group snapshots submitted over time. Only the \&quot;latest\&quot; submitted snapshot for a given combination of &#x60;job.correlator&#x60; and &#x60;detector.name&#x60; will be considered when calculating a repository&#39;s current dependencies. Correlator should be as unique as it takes to distinguish all detection runs for a given \&quot;wave\&quot; of CI workflow you run. If you&#39;re using GitHub Actions, a good default value for this could be the environment variables GITHUB_WORKFLOW and GITHUB_JOB concatenated together. If you&#39;re using a build matrix, then you&#39;ll also need to add additional key(s) to distinguish between each submission inside a matrix variation. | 
**html_url** | **str** | The url for the job. | [optional] 

## Example

```python
from github_openapi.models.snapshot_job import SnapshotJob

# TODO update the JSON string below
json = "{}"
# create an instance of SnapshotJob from a JSON string
snapshot_job_instance = SnapshotJob.from_json(json)
# print the JSON string representation of the object
print(SnapshotJob.to_json())

# convert the object into a dict
snapshot_job_dict = snapshot_job_instance.to_dict()
# create an instance of SnapshotJob from a dict
snapshot_job_from_dict = SnapshotJob.from_dict(snapshot_job_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


