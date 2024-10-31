# Introduction
* Project Name : IPS (ISP Plan Selector)
* Project Type : Web site
* Project Started : 26 October 2024
# Aim
Finding the optimal plan from Internet service providers (ISPs) depending on consumer needs is the goal of the IPS project.
# Requirements
Before using the project, make sure you have every single thing listed :
* PC / Laptop (1366 x 768 is reccomended)
* [Windows Operating System](https://www.microsoft.com/en-us/software-download/windows11)
* [WAMP Server](https://sourceforge.net/projects/wampserver/)
* [Browser](https://www.google.com/chrome/?brand=OZZY&ds_kid=43700080794581053&gad_source=1&gclid=Cj0KCQjwsoe5BhDiARIsAOXVoUsSnWCosJSkOCiJUmZ1CYBarTHHK5Zrci4wtEgUcSCNyhGgj3ooRjkaAuKPEALw_wcB&gclsrc=aw.ds) (Google Chrome is reccomended)
# Languages Used
* HTML
* CSS
* JAVA SCRIPT
* PHP
* PYTHON
# Procedure
1. Open browser
2. Download the zip file from the git hub
3. Extract the zip file
4. Download and Install Wamp software
5. Copy the folder after the extraction of zip file
6. Locate the folder www in the wamp folder
7. Paste the copied folder
8. Open wamp folder again
9. Double click on wampmanager.exe
10. After the loading is completed, click on show hidden icons at the right side of the task bar
11. Left click on the icon : ![wamp server icon](https://i.ytimg.com/vi/68pbesbrV4U/mqdefault.jpg)
12. Then make sure that the colour of the icon is green as given.
13. Click on the link : http://localhost/IPS/
13. Finally the browser will be opened and web site will be displayed
# Working
1. User will access the website using the [link](http://localhost/IPS/)
2. Select the Service Provider used by the user
3. Choose the option that the user prior on choosing their plan. The user choices can be :
    * Expiry
    * Cost
    * Call
    * Data
    * sms
    * Special Benifits
4. Click on Find Plan button
5. A request will be send to the server with user need and ISP name
6. First server will check the name of ISP
7. Then the server check whether the time for refreshing the ISP official page
8. If the time reaches or exceeds for refreshing time, then :
    1. Take the link of the official site of ISP from the DB (Database)
    2. Server start to execute the application refresh.exe by passing ISP link
    3. Then the application connect to the official site of ISP
    4. Take html code from the web site
    5. Convert the html code to the required datas
    6. Then these required datas will be compared with datas in the DB. <br/>The comparison have 3 conditions :
        1. If there is no DB table for comparing with the received data then,(First time the web site is taking the data from the ISP)
            1. Create new table for the ISP
            2. Directly insert the received data to the DB
        2. If the data in the ISP table is not matching with received data
            1. Update the table of the ISP in the DB
        3. If the data in the ISP table is matching with the received data
            1. Ignore it
    7. Stop the execution of refresh.exe
9. Then the server take the refreshed data from DB
10. Calculate the unit requirement of the user from every plan
11. Display the optimal plan to the user through the web site
# Output
Output will be available only after the completion of version 1.0.0
## Known Issues
* The refresh rate of ISP's web site and this project web site is low
* Error may occur when the ISPs changes their html code
## Found Bug
While executing the code, please inform when you find any bug and also submit your feedback though [Email](mailto:devaharsh14@gmail.com) , [Linked in](https://www.linkedin.com/in/devaharshr)
### Current Version : 1.0.0
#### Credit : [Devaharsh R](https://www.linkedin.com/in/devaharshr) , [Anakha Prasad T](https://www.linkedin.com/in/anakha-prasad-t-491388258/)
