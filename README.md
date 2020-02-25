
# Table of Contents

1.  [Setup - Local](#org64bf3b0)
2.  [Endpoints](#orgbccf9d1)
    1.  [GraphQl - GraphiQl](#org226cdc0)
    2.  [Backend - Admin](#org26d6774)
    3.  [Frontend - Nuxt](#org3864aee)
    4.  [Static Files - MinIO](#org07cfddc)
    5.  [DB - Pgadmin](#org11a913a)
3.  [Traefik](#orge395a68)
4.  [Credentials](#org2e7fdfa)
    1.  [Overview](#org986e3df)
    2.  [DB - Postgre](#org7f6eafb)
    3.  [DB - Pgadmin](#org3d920da)
    4.  [Backend - Admin](#org1b7f25e)
    5.  [Static Files - MinIO](#org8b7ab71)


<a id="org64bf3b0"></a>

# Setup - Local

1.  Copy [.env.dist](.env.dist) to [.env](.env)


<a id="orgbccf9d1"></a>

# Endpoints


<a id="org226cdc0"></a>

## GraphQl - GraphiQl

<http:localhost:8000/api/graphiql>


<a id="org26d6774"></a>

## Backend - Admin

<http:localhost:8000/admin>


<a id="org3864aee"></a>

## Frontend - Nuxt

<http:localhost:3000>


<a id="org07cfddc"></a>

## Static Files - MinIO

<http:127.0.0.1:9000>


<a id="org11a913a"></a>

## DB - Pgadmin

<http:localhost:5050>


<a id="orge395a68"></a>

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


<a id="org2e7fdfa"></a>

# Credentials


<a id="org986e3df"></a>

## Overview

<table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">


<colgroup>
<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />
</colgroup>
<thead>
<tr>
<th scope="col" class="org-left">&#xa0;</th>
<th scope="col" class="org-left">Postgre</th>
<th scope="col" class="org-left">Pgadmin</th>
<th scope="col" class="org-left">Admin</th>
<th scope="col" class="org-left">MinIO</th>
</tr>
</thead>

<tbody>
<tr>
<td class="org-left">ID</td>
<td class="org-left">root</td>
<td class="org-left">info@devs-group.com</td>
<td class="org-left">Admin</td>
<td class="org-left">root</td>
</tr>


<tr>
<td class="org-left">PW</td>
<td class="org-left">root</td>
<td class="org-left">root</td>
<td class="org-left">Admin123</td>
<td class="org-left">root1234</td>
</tr>
</tbody>
</table>


<a id="org7f6eafb"></a>

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


<a id="org3d920da"></a>

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


<a id="org1b7f25e"></a>

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


<a id="org8b7ab71"></a>

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

