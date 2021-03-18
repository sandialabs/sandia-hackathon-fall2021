### build the docker image
-  if on the SRN, copy the following into ~/.docker/config.json
```
{
 "proxies":
 {
   "default":
   {
     "httpProxy": "http://proxy.sandia.gov:80/",
     "httpsProxy": "http://proxy.sandia.gov:80/",
     "noProxy": "localhost,127.0.0.1,gitlab.sandia.gov,cee-gitlab.sandia.gov,*.sandia.gov,sandia.gov,192.168.*, 172.16.*, 10.*"
   }
 }
}
```