# aws-serverless-url-redirector

AWS API Gateway + Lambda service to redirect a web request to another location.  Useful for handling redirects from _https://example.com -> https://www.example.com_.

## Usage
Set the following variables when deploying this service

* **SLS_SERVICE_LOCATION:** The DNS name this service will be handling requests for.
* **SLS_SERVICE_DOMAIN:** Domain name of service's location. (Will use SLS_SERVICE_LOCATION if not set.)
* **SLS_REDIRECT_LOCATION:** Domain to redirect requests to.

```
SLS_SERVICE_LOCATION=serverlessops.io SLS_REDIRECT_LOCATION=www.serverlessops.io sls deploy -v
```

_NOTE: This service creates a Certificate Manager certificate and deploy will hold until the certificate is approved._

