
# Table of Contents

1.  [Local Setup](#org9604ff9)
    1.  [Endpoints](#org6126c90)
        1.  [Frontend - Nuxt](#org47b6a45)
        2.  [Backend - Admin](#org023e4be)
        3.  [GraphQL - GraphiQL](#org6241c6d)
        4.  [Static Files - MinIO](#org681d4f5)
        5.  [DB - Pgadmin](#orgc17c042)
    2.  [Credentials](#orgb1b6bf6)
        1.  [DB - Postgre](#org8b9ac5c)
        2.  [DB - Pgadmin](#org1983b41)
        3.  [Backend - Admin](#org1649605)
        4.  [Static Files - MinIO](#org9b4d67b)
2.  [Traefik](#orgc146614)
3.  [Deployment](#org8e7a96c)
4.  [Frontend](#org5f8dc76)



<a id="org9604ff9"></a>

# Local Setup

Follow these steps to set everything up locally on your machine

1.  Clone repo
    
        git clone https://gitlab.com/devs-group/base-wagtail.git && cd base-wagtail

2.  Copy [.env.dist](.env.dist) to .env
    
        cp .env.dist .env

3.  Start Containers with docker-compose
    
        docker-compose up -d


<a id="org6126c90"></a>

## Endpoints

As soon as everything is up and running visit these addresses to interact with
the provided APIs, where necessary use [Credentials](#orgb1b6bf6).


<a id="org47b6a45"></a>

### Frontend - Nuxt

<http:localhost:3000>


<a id="org023e4be"></a>

### Backend - Admin

<http:localhost:8000/admin>


<a id="org6241c6d"></a>

### GraphQL - GraphiQL

<http:localhost:8000/api/graphiql>


<a id="org681d4f5"></a>

### Static Files - MinIO

<http:localhost:9000>


<a id="orgc17c042"></a>

### DB - Pgadmin

<http:localhost:5050>


<a id="orgb1b6bf6"></a>

## Credentials

Credentials for the dev setup containing only insensitive test data.


<a id="org8b9ac5c"></a>

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


<a id="org1983b41"></a>

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


<a id="org1649605"></a>

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


<a id="org9b4d67b"></a>

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


<a id="orgc146614"></a>

# Traefik

Subdomains for the

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


<a id="org8e7a96c"></a>

# Deployment

Details concerning the deployment can be found in its own [README](.deploy/README.md)


<a id="org5f8dc76"></a>

# Frontend

Details concerning the nuxt instance serving the frontend can be found in its own [README](web_frontend/README.md)

