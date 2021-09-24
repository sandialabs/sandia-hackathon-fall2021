# Install android studio
https://developer.android.com/studio

# install python 
https://www.python.org/downloads/

# Install flutter   
https://flutter.dev/docs/get-started/install/windows

# Install Mysql
https://dev.mysql.com/downloads/windows/installer/8.0.html

# install git 
https://git-scm.com/download/win

# install visual code or favorite ide
https://code.visualstudio.com/

# Clone Project
```
py -m pip install -r requirments.txt
```
- To run SQL autobuild, run the following command in the project directory. Doing so will create the default database, all the tables, and prepopulate the tables with test data.
```
# windows
mysqlsh --password <password> --uri=root@localhost  -f fitnessServer/autobuild.sql
# mac/linux
mysql -u [username] -p < fitnessServer/autobuild.sql
(or try 'sudo mysql -u [username] -p < fitnessServer/autobuild.sql')
```
- To drop all tables, run:
```
# windows 
mysqlsh --password <password> --uri=root@localhost  -f fitnessServer/cleanup.sql
# mac/linux 
mysql -u [username] -p < fitnessServer/cleanup.sql
```
