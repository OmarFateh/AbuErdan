# AbuErdan
> AbuErdan app made with django framework, Ajax, and django templates.

## Table of contents
* [Technologies](#technologies)
* [Live](#live)
* [DB Schema](#db-schema)
* [Features](#features)
* [User Credentials](#user-credentials)


## Technologies
* Python 3.9
* Django 2.2.19
* Ajax
* JQuery
* Css
* Html

## Live
https://abuerdan-grid.herokuapp.com/weather/list/  
https://abuerdan-grid.herokuapp.com/weather/add/  
https://abuerdan-grid.herokuapp.com/weather/summary/list/  

## DB Schema
![Alt text](https://github.com/OmarFateh/AbuErdan-grid/blob/main/DB%20Schema.png?raw=true)

## Features
* Weather:  
      - add weather record  
      - validate temperature values (from 19 to 28)  
      - validate humidity values (from 35 to 65)
      - view all weather records ( date - time - temperature - humidity)      

* Summary:  
      - view all summary records    
      - add the 10th record inside the weather record should directly create a new summary record    
      - new summary record inlcudes ( avg temp - avg humidiy - start date - end date)  
      - delete a summary record     
      - Deleting a record in the summary data should automatically delete all related record in the weather data (the 10 records related).     

* No Foreign keys are used  
* CSS grid is used in templates  

## User Credentials
* username--> omar  - password-->admin1600  
