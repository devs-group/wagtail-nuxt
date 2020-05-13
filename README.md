
# Table of Contents

1.  [Requirements](#org98at330)
2.  [Local Setup](#org57856e7)
    1.  [Endpoints](#org809e937)
        1.  [Frontend - Nuxt](#orgc37a804)
        2.  [Backend - Admin](#org211c10f)
        3.  [GraphQL - GraphiQL](#orgc70d5b5)
        4.  [Static Files - MinIO](#org8110bc6)
    2.  [Credentials](#org749259c)
        1.  [DB - Postgre](#orgc6c10a9)
        2.  [Backend - Admin](#orge1ac287)
        3.  [Static Files - MinIO](#orgc1fcbcb)
3.  [Branding](#org13fa485)        
4.  [Frontend](#orgc473881)
5.  [Administration](#orgbf9c4d0)
    1.  [Delete all Wagtail Images](#orgf36cc02)
    2.  [Migrate Changes](#org2525778)
    3.  [Persist Data](#org0ac7a34)




<a id="org98at330"></a>

# Requirements

You need to have [docker](https://docs.docker.com/get-docker/) and preferely docker-compose installed on your system.


<a id="org57856e7"></a>

# Local Setup

Follow these steps to set everything up locally on your machine

1.  Clone repo
    
        git clone https://gitlab.com/devs-group/base-wagtail.git && cd base-wagtail

2.  Copy [.env.dist](.env.dist) to .env
    
        cp .env.dist .env
        
3.  Install node modules

        cd web_frontend
        yarn install

4.  Start Containers with docker-compose
    
        docker-compose up -d


<a id="org809e937"></a>

## Endpoints

As soon as everything is up and running visit these addresses to interact with
the provided APIs, where necessary use [Credentials](#org749259c).


<a id="orgc37a804"></a>

### Frontend - Nuxt

<http:localhost:3000>


<a id="org211c10f"></a>

### Backend - Admin

<http:localhost:8000/admin>


<a id="orgc70d5b5"></a>

### GraphQL - GraphiQL

<http:localhost:8000/api/graphiql>

<a id="org8110bc6"></a>

### Static Files - MinIO

<http:localhost:9000>


<a id="org749259c"></a>

## Credentials

Default Credentials for the dev setup containing only insensitive test data.
It is advised to change these in the .env.dist and .env files. 


<a id="orgc6c10a9"></a>

### DB - Postgre

<table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">


<colgroup>
<col  class="org-left" />

<col  class="org-left" />
</colgroup>
<tbody>
<tr>
<td class="org-left">database</td>
<td class="org-left">cms</td>
</tr>


<tr>
<td class="org-left">user</td>
<td class="org-left">root</td>
</tr>


<tr>
<td class="org-left">password</td>
<td class="org-left">root</td>
</tr>
</tbody>
</table>


<a id="orgee65cfb"></a>

### Backend - Admin

<table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">


<colgroup>
<col  class="org-left" />

<col  class="org-left" />
</colgroup>
<tbody>
<tr>
<td class="org-left">user</td>
<td class="org-left">root</td>
</tr>


<tr>
<td class="org-left">password</td>
<td class="org-left">root</td>
</tr>
</tbody>
</table>


<a id="orgc1fcbcb"></a>

### Static Files - MinIO

<table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">


<colgroup>
<col  class="org-left" />

<col  class="org-left" />
</colgroup>
<tbody>
<tr>
<td class="org-left">access-key</td>
<td class="org-left">root</td>
</tr>


<tr>
<td class="org-left">secret-key</td>
<td class="org-left">root</td>
</tr>
</tbody>
</table>


<a id="org13fa485"></a>

# Branding

Search the project for strings starting with "PLACEHOLDER_" and exchange to enable custom branding of the admin panel and more.


<a id="orgc473881"></a>

# Frontend

Details concerning the nuxt instance serving the frontend can be found in its own [README](web_frontend/README.md)


<a id="orgbf9c4d0"></a>

# Administration

To interface with the containers, a Makefile is provided which provides additional
management commands to the [default django-admin commands](https://docs.djangoproject.com/en/3.0/ref/django-admin/).


<a id="orgf36cc02"></a>

## Delete all Wagtail Images

If there is a `key not found` error due to a dead reference, wagtail images might be the problem.
It usually helps to delete all instances of the `wagtail.images.Image` class.
This make command shortens the procedure:

    make deletewagtailimages


<a id="org2525778"></a>

## Migrate Changes

To shorten the migration process after a database relevant change was made use:

    make migrate

This will execute inside the container the commands `./manage.py makemigrations` and `./manage.py migrate`


<a id="org0ac7a34"></a>

## Persist Data

To be able to work with data from a different docker volume, fixtures can be created with:

    make backup

To load the fixtures us:

    make load


<a id="org3a8cc49"></a>
