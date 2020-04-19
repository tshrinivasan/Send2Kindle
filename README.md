# Send2Kindle
A Python mailer specifically crafted for [FreeTamilEbooks.com](http://freetamilebooks.com) to add ebooks directly to kindle device.

#### Send to Kindle by E-mail
**Send documents to your Kindle as an email attachment**
You and your approved contacts can send documents to your registered Kindle devices, free Kindle reading applications, and your Kindle Library in the Amazon Cloud by e-mailing them to your Send-to-Kindle e-mail address ([name]@kindle.com). Your Send-to-Kindle e-mail address is a unique e-mail address assigned to each of your Kindle devices and free Kindle reading applications upon registration.

To know how to add a contact to approved list see [here](https://www.amazon.com/gp/help/customer/display.html?nodeId=201974240)

### Tech

Send2Kindle uses a number of python in-built and opensource projects to work properly:

* [Flask](http://flask.pocoo.org/) - microframework for Python
*  [Twitter Bootstrap](http://twitter.github.com/bootstrap/) - great UI boilerplate for modern web apps
* [jQuery](http://jquery.com)- duh

### Installation

You need Python 2.*, its dependency packages, flask installed globally:

```sh
$ https://github.com/Dineshkarthik/Send2Kindle.git
$ cd Send2Kindle
$ pip install -r requirements.txt
$ python mailer.py
```

   By default the script runs in `port 5000`, this can be changed to any port of required port using `-p or --port` option.
   

    python mailer.py -p 8000


### Configurations

 - URL should have 2 parameters
	 - fileurl - Url of the file to be mailed.
	 - filename - Name of the file to be mailed.
	 - ex: http://localhost:5000/?fileurl=http://freetamilebooks.com/download/%e0%ae%89%e0%ae%b2%e0%ae%95-%e0%ae%b5%e0%ae%b0%e0%ae%b2%e0%ae%be%e0%ae%b1%e0%af%8d%e0%ae%b1%e0%ae%bf%e0%ae%b2%e0%af%8d-%e0%ae%b5%e0%ae%bf%e0%ae%9f%e0%af%81%e0%ae%a4%e0%ae%b2%e0%af%88-%e0%ae%b5-2/
	 https://35.166.185.40/send2kindle?fileurl=http://freetamilebooks.com/download/%e0%ae%89%e0%ae%b2%e0%ae%95-%e0%ae%b5%e0%ae%b0%e0%ae%b2%e0%ae%be%e0%ae%b1%e0%af%8d%e0%ae%b1%e0%ae%bf%e0%ae%b2%e0%af%8d-%e0%ae%b5%e0%ae%bf%e0%ae%9f%e0%af%81%e0%ae%a4%e0%ae%b2%e0%af%88-%e0%ae%b5-2/&filename=ulaga_varalatril_viduthalai_veerargal.mobi
License
----

MIT


**Free Software, Hell Yeah!**