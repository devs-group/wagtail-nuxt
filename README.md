
# Table of Contents

1.  [Local Setup](#org57856e7)
    1.  [Endpoints](#org809e937)
        1.  [Frontend - Nuxt](#orgc37a804)
        2.  [Backend - Admin](#org211c10f)
        3.  [GraphQL - GraphiQL](#orgc70d5b5)
        4.  [Static Files - MinIO](#org8110bc6)
        5.  [DB - Pgadmin](#orgfa83a0a)
    2.  [Credentials](#org749259c)
        1.  [DB - Postgre](#orgc6c10a9)
        2.  [DB - Pgadmin](#orgee65cfb)
        3.  [Backend - Admin](#orge1ac287)
        4.  [Static Files - MinIO](#orgc1fcbcb)
2.  [Deployment](#org177a345)
3.  [Frontend](#orgc473881)
4.  [Administration](#orgbf9c4d0)
    1.  [Delete all Wagtail Images](#orgf36cc02)
    2.  [Migrate Changes](#org2525778)
    3.  [Persist Data](#org0ac7a34)
5.  [Traefik](#org3a8cc49)



<a id="org57856e7"></a>

# Local Setup

Follow these steps to set everything up locally on your machine

1.  Clone repo
    
        git clone https://gitlab.com/devs-group/base-wagtail.git && cd base-wagtail

2.  Copy [.env.dist](.env.dist) to .env
    
        cp .env.dist .env

3.  Start Containers with docker-compose
    
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


<a id="orgfa83a0a"></a>

### DB - Pgadmin

<http:localhost:5050>


<a id="org749259c"></a>

## Credentials

Credentials for the dev setup containing only insensitive test data.


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

### DB - Pgadmin

<table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">


<colgroup>
<col  class="org-left" />

<col  class="org-left" />
</colgroup>
<tbody>
<tr>
<td class="org-left">email</td>
<td class="org-left">info@devs-group.com</td>
</tr>


<tr>
<td class="org-left">password</td>
<td class="org-left">root</td>
</tr>
</tbody>
</table>


<a id="orge1ac287"></a>

### Backend - Admin

<table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">


<colgroup>
<col  class="org-left" />

<col  class="org-left" />
</colgroup>
<tbody>
<tr>
<td class="org-left">user</td>
<td class="org-left">Admin</td>
</tr>


<tr>
<td class="org-left">password</td>
<td class="org-left">Admin123</td>
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
<td class="org-left">root1234</td>
</tr>
</tbody>
</table>


<a id="org177a345"></a>

# Deployment

Details concerning the deployment can be found in its own [README](.deploy/README.md)


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

To be able to work with data in between container creation and deletion processes fixtures can be created with:

    make backup

To load the fixtures us:

    make load


<a id="org3a8cc49"></a>

# Traefik

Subdomains for the Traefik interface:

<table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">


<colgroup>
<col  class="org-left" />

<col  class="org-left" />
</colgroup>
<tbody>
<tr>
<td class="org-left">host</td>
<td class="org-left">base-wagtail.devs-group.de</td>
</tr>


<tr>
<td class="org-left">cms-host</td>
<td class="org-left">cms.base-wagtail.devs-group.de</td>
</tr>


<tr>
<td class="org-left">frontend</td>
<td class="org-left">base-wagtail.devs-group.de</td>
</tr>
</tbody>
</table>

