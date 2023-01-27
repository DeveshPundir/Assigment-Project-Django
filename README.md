
# Asgard project

This is a Django app with an HTML/JavaScript Front end and a database.


## API Reference




#### Get data for every button

```http
  GET /api/items/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `Geograpghy`      | `string` |The Geography of Asgard is dominated by huge mountains
| `History`      | `string` |The Geography of Asgard is dominated by huge mountains
| `Culture`      | `string` |The Geography of Asgard is dominated by huge mountains
| `Language`      | `string` |The Geography of Asgard is dominated by huge mountains

#### Display buttons

A Djnago app in which we Click on the button to see the related description




## Screenshots
Please use below links to see the Screenshots 
https://drive.google.com/file/d/1ys7OLA89R2p5VG3ZDB_vxV0yCouQHIBn/view?usp=sharing
https://drive.google.com/file/d/1nc1iMN12P7LXDykYCyryFMzqytb0yruY/view?usp=sharing









## Demo

Video link of project  
https://drive.google.com/file/d/1SO2aoEiAJvNw7r3L3LPSEVqiiMuc-lHu/view?usp=sharing


## Usage/Examples

#Models used
```
from django.db import models
class data(models.Model):
    
    name=models.CharField(max_length=122,default="")
    snippet=models.CharField(max_length=500,default="")



```
#views.py
```
from django.shortcuts import render
from .models import data
def index(request):
    data_all=data.objects.all()
    print(len(data_all))
   
    print(data_all[0].snippet)
    print(data_all[1].snippet)
    print(data_all[2].snippet)
    print(data_all[3].snippet)
    return render(request,'index.html',{'geo':data_all[0].snippet,'his':data_all[1].snippet,'cul':data_all[2].snippet,'lan':data_all[3].snippet})
```



## Tech Used

HTML,CSS,JAVASCRIPT

Framework Used-
Django



