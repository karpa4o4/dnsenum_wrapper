# dnsenum_wrapper

#### API methods

* Start scan
  ```
  curl -d "domain=google.com" -X POST http://0.0.0.0:8000/api/scans/start_scan/
  ```
* Get scan status
  ```
  curl http://0.0.0.0:8000/api/scans/<pk>/get_status/
  ```
* Get scan result
  ```
  curl http://0.0.0.0:8000/api/scans/<pk>/get_result/
  ```