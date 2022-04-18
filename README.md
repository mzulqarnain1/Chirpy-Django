Chirpy-Django
=======================================================================

Chirpy is a platform where users can post their thoughts and others can comment and have a discussion.

[![codecov](https://codecov.io/gh/mzulqarnain1/Chirpy-Django/branch/main/graph/badge.svg?token=0WECZ1XF9G)](https://codecov.io/gh/mzulqarnain1/Chirpy-Django)

## Prerequisites
~~~~~~~~~~~~~
You will need to have the following installed:
- Python 3.8+
- Docker
- Docker Compose
~~~~~~~~~~~~~

## Instructions to run the app

To get started using this app right away:

* `cd` into project root directory
* Build the docker images using `docker-compose build`
* Run the docker app using `docker-compose up`
* Visit http://0.0.0.0:8000/ in your browser


## Features & bonus work

1) You can sign-up & log-in 
2) You can share your thoughts via a post
3) You will see posts submitted by all users on your home feed
4) You can open any post and leave a comment
5) You will get a notification count in navigation bar if people leave a comment on your post.
6) You can open the notifications page by clicking on notifications button on navigation bar.
7) You can mark unread notifications as read on notifications page.

## Others

1) Dependencies are being managed using [Poetry](https://python-poetry.org/)
2) Tests are added for all modules and sub-modules
3) Github Actions CI is running tests with 100% coverage.
4) Code and imports are formatted using `black` & `isort`.
5) A superuser is already created for you with the app (Use admin/admin as username/password)

