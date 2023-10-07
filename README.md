# Pre-Requisites
Install the following tools in order to start the programming challenge

## Install Python 
https://www.python.org/downloads/

## Install Mysql
https://dev.mysql.com/downloads/mysql/

- When Installing MySQL, ensure that you setup a legacy password and set it to `NSU2023Hack!`

## Install Git 
https://git-scm.com/download/win

## Install Visual Studio code or favorite ide
https://code.visualstudio.com/

## Install NodeJS runtime environment
https://nodejs.org/en/download

# Setup
After installing the previous tools, you are now ready to run the app. The following steps detail how to install all of the dependencies and get the server and FitnessApp up and running!

## Open VSCode
Create a new folder and open it inside VSCode. In the top toolbar select `Terminal` -> `New Terminal`

## Clone Project
In the new terminal that was just opened, clone the source code for the app using the following commands:
```
git clone https://github.com/sandialabs/sandia-hackathon-fall2021.git
cd sandia-hackathon-fall2021
```
## Setup Database
- To run SQL autobuild, run the following command in the project directory. Doing so will create the default database, all the tables, and prepopulate the tables with test data.
```
# windows
mysqlsh --password <password> --uri=root@localhost  -f Server/src/autobuild.sql
# mac/linux
mysql -u [username] -p < Server/src/autobuild.sql
```

## Setup Server
In order to install the corresponding Python Dependencies, run the following command
```
py -m pip install -r Server/requirements.txt
```
- In order to run the Flask server, open another terminal window. If you need to terminate the server at any time, Ctrl+C will shut it down. 
```
cd sandia-hackathon-fall2021/Server/src
flask run
```

## Setup Angular App
In order to run the Angular app, we first need to install the angular CLI. In a new terminal, run the following command.

```
npm install -g @angular/cli
```

After installation, we need to navigate to the Angular App Source code and install all dependencies
```
cd sandia-hackathon-fall2021/FitnessApp/src/app
npm install
```
After the dependencies are done installing, we can now build our Angular App
```
ng serve
```
The app should now be running on http://localhost:4200

# Resources
Here are walkthroughs or links on how to modify the app
## How to add an image to your app.
1. Find an image you want to add
2. Save it to the `FitnessApp/src/assests` folder. <br />
![Screenshot](https://github.com/sandialabs/sandia-hackathon-fall2021/blob/master/resources/image2.PNG)
3. Create an `img` tag in the component in which you wish to add the image to. Set the `src` attribute of that image tag to the relative path of where you saved the image ![Screenshot](https://github.com/sandialabs/sandia-hackathon-fall2021/blob/master/resources/image1.PNG)

## HTML Documentation
https://www.w3schools.com/html/html_examples.asp
## CSS Documentation
https://welearncode.com/beginners-guide-css/
