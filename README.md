
# Table of Contents

1.  [Local Setup](#orgf67e601)
    1.  [Endpoints](#orgbafda0f)
        1.  [Frontend - Nuxt](#orgb652995)
        2.  [Backend - Admin](#org86f9a4b)
        3.  [GraphQL - GraphiQL](#orgf16ebc8)
        4.  [Static Files - MinIO](#orgc5ea081)
        5.  [DB - Pgadmin](#org76c5504)
    2.  [Credentials](#org7542166)
        1.  [DB - Postgre](#org5660282)
        2.  [DB - Pgadmin](#orgf22fb3a)
        3.  [Backend - Admin](#org6527aaf)
        4.  [Static Files - MinIO](#org191faa8)
2.  [Traefik](#org714c97f)



<a id="orgf67e601"></a>

# Local Setup

Follow these steps to set everything up locally on your machine

1.  Clone repo
    
        git clone https://gitlab.com/devs-group/base-wagtail.git && cd base-wagtail

2.  Copy [.env.dist](.env.dist) to .env
    
        cp .env.dist .env

3.  Start Containers with docker-compose
    
        docker-compose up -d


<a id="orgbafda0f"></a>

## Endpoints

As soon as everything is up and running visit these addresses to interact with
the provided APIs, where necessary use [Credentials](#org7542166).


<a id="orgb652995"></a>

### Frontend - Nuxt

<http:localhost:3000>


<a id="org86f9a4b"></a>

### Backend - Admin

<http:localhost:8000/admin>


<a id="orgf16ebc8"></a>

### GraphQL - GraphiQL

<http:localhost:8000/api/graphiql>


<a id="orgc5ea081"></a>

### Static Files - MinIO

<http:localhost:9000>


<a id="org76c5504"></a>

### DB - Pgadmin

<http:localhost:5050>


<a id="org7542166"></a>

## Credentials

Credentials for the dev setup containing only insensitive test data.


<a id="org5660282"></a>

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


<a id="orgf22fb3a"></a>

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


<a id="org6527aaf"></a>

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


<a id="org191faa8"></a>

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


<a id="org714c97f"></a>

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

