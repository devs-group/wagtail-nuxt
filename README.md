
# Table of Contents

1.  [Setup - Local](#orgd1daac8)
2.  [Endpoints - Local](#org5b75216)
    1.  [Frontend - Nuxt](#org4eebcf3)
    2.  [Backend - Admin](#org75246ad)
    3.  [GraphQL - GraphiQL](#orge439014)
    4.  [Static Files - MinIO](#orgf242aac)
    5.  [DB - Pgadmin](#org3dbd061)
3.  [Credentials](#org7322316)
    1.  [DB - Postgre](#org662991c)
    2.  [DB - Pgadmin](#orgb518a83)
    3.  [Backend - Admin](#orgb939310)
    4.  [Static Files - MinIO](#org83b538f)
4.  [Traefik](#org530c6c9)



<a id="orgd1daac8"></a>

# Setup - Local

Follow these steps to set everything up locally on your machine

1.  Clone repo
    
        git clone https://gitlab.com/devs-group/base-wagtail.git && cd base-wagtail

2.  Start Containers with docker-compose
    
        docker-compose up -d

3.  Copy [.env.dist](.env.dist) to .env


<a id="org5b75216"></a>

# Endpoints - Local

As soon as everything is up and running visit these addresses to interact with
the provided APIs, where necessary use [Credentials](#org7322316).


<a id="org4eebcf3"></a>

## Frontend - Nuxt

<http:localhost:3000>


<a id="org75246ad"></a>

## Backend - Admin

<http:localhost:8000/admin>


<a id="orge439014"></a>

## GraphQL - GraphiQL

<http:localhost:8000/api/graphiql>


<a id="orgf242aac"></a>

## Static Files - MinIO

<http:localhost:9000>


<a id="org3dbd061"></a>

## DB - Pgadmin

<http:localhost:5050>


<a id="org7322316"></a>

# Credentials

Credentials for the dev setup containing only insensitive test data.


<a id="org662991c"></a>

## DB - Postgre

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


<a id="orgb518a83"></a>

## DB - Pgadmin

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


<a id="orgb939310"></a>

## Backend - Admin

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


<a id="org83b538f"></a>

## Static Files - MinIO

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


<a id="org530c6c9"></a>

# Traefik

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

