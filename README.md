<<<<<<< HEAD
Flask on OpenShift
==================

This git repository helps you get up and running quickly w/ a Flask installation
on OpenShift.


Running on OpenShift
----------------------------

Create an account at http://openshift.redhat.com/

Create a python application

    rhc app create flask python-2.6

Add this upstream flask repo

    cd flask
    git remote add upstream -m master https://github.com/openshift/flask-example.git
    git pull -s recursive -X theirs upstream master
    
Then push the repo upstream

    git push

That's it, you can now checkout your application at:

    http://flask-$yournamespace.rhcloud.com

------------------------------

To get more log messages in your openshift logs please add the following line to your code

app.config['PROPAGATE_EXCEPTIONS'] = True  

To read more about logging in Flask please see this email

http://flask.pocoo.org/mailinglist/archive/2012/1/27/catching-exceptions-from-flask/

=======
dataninja
=========

Dataninja is a tool to fetch data from multiple sources via web services.
>>>>>>> 6ed6314e3b089f63308808808e3d13b904116e36
