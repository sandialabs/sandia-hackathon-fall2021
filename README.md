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
- To run SQL autobuild, run the following command in the project directory. Doing so will create the default database, all the tables, and prepopulate the tables with test data.
...
mysql -u [username] -p[passwordhere] < fitnessServer/autobuild.sql
...
- To drop all tables, run:
...
mysql -u [username] -p[passwordhere] < fitnessServer/cleanup.sql
...