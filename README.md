django-settings-template
========================

Rational
--------

Everyone who uses Django eventually runs into the problem of 
having multiple configurations for different deployments as 
well as different configurations for each developer on a project.

There are many proposed solutions, but I wasn't really satisfied
with any of them. So I decided to modify one I liked to suit my 
needs. 

Use
---

To use this template simply checkout this repo. Then copy the
settings files to your app, making sure to create a backup of 
the original files if necessary.

    cp /path/to/django-settings-template/django-settings-template/settings* /path/to/your/awesome-project/awesome-project/

Then you need to find all instances of {{your_project}} and replace them with the name of your project.

    cd /path/to/your/awesome-project/awesome-project/
    find . -name "settings*" -print | xargs sed -i 's/\{\{your_project\}\}/awesome-project/g'

Next edit settings_map.py to change {{your_computer_name}} to 
the name of the computer where you doing development and change 
{{production_computer_name}} to the name of the production server
as reported by

    uname -a

You can now add all the standard settings your deployments have in common to 
settings_common.py, your development specific settings in settings_dev.py,
and your production specific settings in settings_prod.py.

You can also add arbitrary settings files simply by adding key value pairs to
settings_map.py where the key is the computer name and the value is the file to 
load. This has been tested under wsgi and shouldn't require any special setup
for any other deployment.

Acknowledgment
--------------

Paul J. Warner, for the original idea http://ruffyen.blogspot.com/2012/02/django-and-version-control-for-multiple.html

FunkyBob from #django on freenode, for help figuring out how to include the files properly
