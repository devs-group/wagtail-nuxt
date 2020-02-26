
# Table of Contents

1.  [Local Setup](#org9ac8da9)
    1.  [Endpoints](#org70811f9)
        1.  [Frontend - Nuxt](#orge5d919b)
        2.  [Backend - Admin](#org938272b)
        3.  [GraphQL - GraphiQL](#orgd08e351)
        4.  [Static Files - MinIO](#org1a33a21)
        5.  [DB - Pgadmin](#org89b69d9)
    2.  [Credentials](#org8c083bf)
        1.  [DB - Postgre](#org4d0eed7)
        2.  [DB - Pgadmin](#org8787931)
        3.  [Backend - Admin](#org4a24599)
        4.  [Static Files - MinIO](#org995d14f)
2.  [Deployment](#orgcdbd8d2)
3.  [Frontend](#org5e9d3b4)
4.  [Administration](#orge2deb06)
    1.  [Delete all Wagtail Images](#org52a919b)
    2.  [Migrate Changes](#org267acf6)
    3.  [Persist Data](#orgc8759a7)
5.  [Traefik](#org56255ff)



<a id="org9ac8da9"></a>

# Local Setup

Follow these steps to set everything up locally on your machine

1.  Clone repo
    
        git clone https://gitlab.com/devs-group/base-wagtail.git && cd base-wagtail

2.  Copy [.env.dist](.env.dist) to .env
    
        cp .env.dist .env

3.  Start Containers with docker-compose
    
        docker-compose up -d


<a id="org70811f9"></a>

## Endpoints

As soon as everything is up and running visit these addresses to interact with
the provided APIs, where necessary use [Credentials](#org8c083bf).


<a id="orge5d919b"></a>

### Frontend - Nuxt

<http:localhost:3000>


<a id="org938272b"></a>

### Backend - Admin

<http:localhost:8000/admin>


<a id="orgd08e351"></a>

### GraphQL - GraphiQL

<http:localhost:8000/api/graphiql>


<a id="org1a33a21"></a>

### Static Files - MinIO

<http:localhost:9000>


<a id="org89b69d9"></a>

### DB - Pgadmin

<http:localhost:5050>


<a id="org8c083bf"></a>

## Credentials

Credentials for the dev setup containing only insensitive test data.


<a id="org4d0eed7"></a>

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


<a id="org8787931"></a>

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


<a id="org4a24599"></a>

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


<a id="org995d14f"></a>

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


<a id="orgcdbd8d2"></a>

# Deployment

Details concerning the deployment can be found in its own [README](.deploy/README.md)


<a id="org5e9d3b4"></a>

# Frontend

Details concerning the nuxt instance serving the frontend can be found in its own [README](web_frontend/README.md)


<a id="orge2deb06"></a>

# Administration

To interface with the containers, a Makefile is provided which provides additional
management commands to the [default django-admin commands](https://docs.djangoproject.com/en/3.0/ref/django-admin/).


<a id="org52a919b"></a>

## Delete all Wagtail Images

If there is a `key not found` error due to a dead reference, wagtail images might be the problem.
It usually helps to delete all instances of the `wagtail.images.Image` class.
This make command shortens the procedure:

    make deletewagtailimages


<a id="org267acf6"></a>

## Migrate Changes

To shorten the migration process after a database relevant change was made use:

    make migrate

This will execute inside the container the commands `./manage.py makemigrations` and `./manag.py migrate`


<a id="orgc8759a7"></a>

## Persist Data

To be able to work with data in between container creation and deletion processes fixtures can be created with:

    make backup

To load the fixtures us:

    make load


<a id="org56255ff"></a>

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

