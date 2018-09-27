# Assignment1 - Django 2 by Example Blog Tutorial

## Overview and Directions
In order to learn the basics of Python you will need to develop web applications. You will develop a blog described in Chapters 1 and 2 of the **Django 2 by Example** textbook we are using for this class. The authors have also provided the [Django 2 by Example Code in GitHub](https://github.com/PacktPublishing/Django-2-by-Example).

## Step 1
Before you jump into the tutorial, you should consider doing the following:
1. Installing python (version 3.7 or version 3.6.1). You can download this for your Windows or Mac laptops at the [Python Software Foundation](https://www.python.org/psf). Windows comes with no version of python installed so the install should be straightforward. Please note the Mac comes with an older version of python installed (typically 2.7) which is **NOT** compatible with the tutorials or the version of Django we will be using. You will need to upgrade to the newer version for this class. Please see me if that is an issue. Once Python 3.7 or 3.6 is installed you need to refer to python on the Mac and python3. Using python only will bring up python 2.7.
2. You will need an editor or, even better, an integrated development environment to work with the python code. As a student you can download a great one for free called PyCharm. Here is a link to sign up for free access to PyCharm and other JetBrains tools as a student: [Click here to signup](https://www.jetbrains.com/student).
3. If you want to simply use a good editor, consider [Sublime Text](https://www.sublimetext.com) or [Atom](https://atom.io).
4. Once you have downloaded and installed python and acquired an IDE or editor, it is time to begin your introduction to python and Django. In the directory where you have or are planning to manage all your python projects create a directory called dbeblog You can do this with file explorer or with the command line tool using this command: `mkdir dbeblog` 
5. Create a virtual environment and activate the virtual environment using these commands:
Run the following commands:
```shell
# On Windows
python -m venv c:\path\to\myvenv
# On MAC
python3 -m virtualenv myvenv
```
Next **we must activate the virtual environment** with 
* On Windows go to scripts directory and type `activate`
* On Mac go to bin inside venv and issue the command `source activate`

In Windows this will look like this:
![win-venv-activate](https://github.com/uno-isqa-4900/assignment1/blob/master/images/assign1-windows-venv-activate.png)

In a Mac it should look like this
![mac-venv-activate](https://github.com/uno-isqa-4900/assignment1/blob/master/images/assign1-mac-venv-activate.png)

As it mentions, any time you want to exit the virtual environment you can type `deactivate`.

6.	Now we will install django into the virtual environment using this command:
```Python
pip install django==2.0.5 
```
Follow the directions in the book. When you are asked to edit the settings.py file to add the blog app you should consider editing these lines in settings.py so times look correct and to prepare for deployment.
```bash
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'America/Chicago'
ALLOWED_HOSTS = ['*']
```
## Step 2
Complete all activities in Chapter 1 and Chapter 2 up to page 54 of the **Django 2 by Example Book**. You do not need to complete other portions of the Chapter 2 for full credit. We are using Django 2 to stay current and since it is actually easier than previous versions of Django. 
 
When you are done you will have a blog where blog posts can be created and you can also share these blog posts with an email. When complete, you should be able to post blog entries in the Django Admin Panel like this
![django-admin-panel](https://github.com/uno-isqa-4900/assignment1/blob/master/images/assign1-django-admin-panel.png)

All views of the blog will see it like this:
![view-blog](https://github.com/uno-isqa-4900/assignment1/blob/master/images/assign1-view-blog.png)

If the user clicks on the post, they will see the detail of the speech as shown below.
![view-post](https://github.com/uno-isqa-4900/assignment1/blob/master/images/assign1-post.png)

If you click on **Share this post** you will see a webform come up to allow you to easily send a link to the post in an email.
![share-post](https://github.com/uno-isqa-4900/assignment1/blob/master/images/assign1-share-post.png)

If you set up your site with an SMTP relay such as a gmail account, you can send out a note. When you do, the website should respond with:  
![send-email-website-response](https://github.com/uno-isqa-4900/assignment1/blob/master/images/assign1-view-email.png)

The email will look like this:
![assign1-email](https://github.com/uno-isqa-4900/assignment1/blob/master/images/assign1-email.png)

Click here for Email Resources to connect to both Pythonanywhere or Heroku

## Step 3
If you have not already done git repository for your code. Click here for Git and Github Resources if you are new to Git. Also push your code to a GitHub repository.

## Step 4
Deploy your application to Heroku or Pythonanywhere. Go to the **Canvas Module** called **General Resources Used Throughout Class** and select **Deploy to Heroku** or **Deploy to Pythonanywhere**. Deploy your application to one of these hosting facilities and be sure to test it and make sure it has all the functions of the local application you developed. Add a few posts to demonstrate you have successfully deployed and tested the application.

