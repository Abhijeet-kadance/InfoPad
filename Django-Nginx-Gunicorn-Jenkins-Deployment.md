## CI-CD for Staging to Production Using Jenkins


### In this PipeLine we are going to  use NGINX as a Web/Proxy Server , Gunicorn as a Application Server and Jenkins as Pipeline Management.
---

### For Web Application backend we are using Django 

---

## Installation of Jenkins 

We first need to install jenkins into our Linux system. 

Update you VM (Ubuntu):

    sudo apt-get update -y

Upgrade Ubuntu :

    sudo apt-get upgrade -y 

Installing Openjdk-11-jre into the VM:

    sudo apt-get install openjdk-11-jre

    click 'y' to continue the installation 
---

## Setting Up Project Directory 

On github create a fresh repository for your Django application and CI-CD configuration.

Clone the repository into your local system can be (Windows/MAC-OS/ Linux)

Add required .gitignore for Djngo python app

Now add a basic README.ms file to the code and push the changes to check wheather you have correctly setup the github enviornment.

---

## Creating a virtual Enviornment for Django application 

This is a pre-requisite to Creating a django application 

We create a Virtual environment to install all the dependencies to a specific enviornment and work on the required modules according to the virtual env.

to create a virtual environment :

    Basically we use :

        python3 -m venv "Your enviornment Name"
        python -m venv "Your enviornment Name"

        for ex:
            
            python3 -m venv app_env

            python -m venv app_env

    This way you created a virtual environment of the name app_env.

---

## Creating a requirement.txt to install Django application dependencies

When inside virtual env we can use a pip freeze command to view all the installed dependencies that are installed installed in a particular virtual enviornment.

In our case our virtual env is app_env so once inside app_env we can use the pip freeze command to view all dependencies inside the virtual env 

***How to activate a virutal enviornment***

To do so :

    In windows simple use the command :

        app_env/Scripts/activate 

    In Linux :

        source app_env/bin/activate

This way you can activate a virtual enviornment 

To Deactivate a virtual enviornment you can use the command :

    deactivate

>***Note : Keep in mind that deactive will only work if you are already inside a virutalenv***

***Creating a requirement.txt file***

To create one simply use 

    # for python3
    pip3 freeze > requirements.txt

    # for python2
    pip freeze > requirements.txt

>***Note: Its a better pratice to use python3 for dveleopment***

---

