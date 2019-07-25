# Dnsenum wrapper

#### API methods

* Start scan
  ```
  curl -d "domain=google.com" -X POST http://0.0.0.0:8000/api/scans/start_scan/
  ```
* Get scan status
  ```
  curl http://0.0.0.0:8000/api/scans/get_status/<pk>/
  ```
* Get scan result
  ```
  curl http://0.0.0.0:8000/api/scans/get_result/<pk>/
  ```