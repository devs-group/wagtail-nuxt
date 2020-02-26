
# Table of Contents

1.  [Local Setup](#org82a8a3c)
    1.  [Endpoints](#org9252b1b)
    2.  [Credentials](#org4b9c3fd)
        1.  [DB - Postgre](#org0deb995)
        2.  [DB - Pgadmin](#orgacc1a99)
        3.  [Backend - Admin](#org2b4bbfa)
        4.  [Static Files - MinIO](#org595f708)
2.  [Traefik](#orgd9a3a7d)



<a id="org82a8a3c"></a>

# Local Setup

Follow these steps to set everything up locally on your machine

1.  Clone repo
    
        git clone https://gitlab.com/devs-group/base-wagtail.git && cd base-wagtail

2.  Start Containers with docker-compose
    
        docker-compose up -d

3.  Copy [.env.dist](.env.dist) to .env


<a id="org9252b1b"></a>

## Endpoints

As soon as everything is up and running visit these addresses to interact with
the provided APIs, where necessary use [Credentials](#org4b9c3fd).

<table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">


<colgroup>
<col  class="org-left" />

<col  class="org-left" />
</colgroup>
<tbody>
<tr>
<td class="org-left">Frontend - Nuxt</td>
<td class="org-left"><http:localhost:3000></td>
</tr>


<tr>
<td class="org-left">Backend - Admin</td>
<td class="org-left"><http:localhost:8000/admin></td>
</tr>


<tr>
<td class="org-left">GraphQL - GraphiQL</td>
<td class="org-left"><http:localhost:8000/api/graphiql></td>
</tr>


<tr>
<td class="org-left">Static Files - MinIO</td>
<td class="org-left"><http:localhost:9000></td>
</tr>


<tr>
<td class="org-left">DB - Pgadmin</td>
<td class="org-left"><http:localhost:5050></td>
</tr>
</tbody>
</table>


<a id="org4b9c3fd"></a>

## Credentials

Credentials for the dev setup containing only insensitive test data.


<a id="org0deb995"></a>

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


<a id="orgacc1a99"></a>

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


<a id="org2b4bbfa"></a>

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


<a id="org595f708"></a>

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


<a id="orgd9a3a7d"></a>

# Traefik

The subdomains where to find the

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

