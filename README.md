
# Table of Contents

1.  [Setup - Local](#orgf55167d)
2.  [Endpoints](#org37815f0)
    1.  [GraphQl - GraphiQl](#org177d42e)
    2.  [Backend - Admin](#org1a4a842)
    3.  [Frontend - Nuxt](#org04cc71e)
    4.  [Static Files - MinIO](#orgf35284a)
    5.  [DB - Pgadmin](#orgc849483)
3.  [Traefik](#org703efef)
4.  [Credentials](#org930bc99)
    1.  [DB - Postgre](#org740b236)
    2.  [DB - Pgadmin](#org1c1cc7f)
    3.  [Backend - Admin](#org283983f)
    4.  [Static Files - MinIO](#orga0dce3c)


<a id="orgf55167d"></a>

# Setup - Local

1.  Copy [.env.dist](.env.dist) to [.env](.env)


<a id="org37815f0"></a>

# Endpoints


<a id="org177d42e"></a>

## GraphQl - GraphiQl

<http:localhost:8000/api/graphiql>


<a id="org1a4a842"></a>

## Backend - Admin

<http:localhost:8000/admin>


<a id="org04cc71e"></a>

## Frontend - Nuxt

<http:localhost:3000>


<a id="orgf35284a"></a>

## Static Files - MinIO

<http:127.0.0.1:9000>


<a id="orgc849483"></a>

## DB - Pgadmin

<http:localhost:5050>


<a id="org703efef"></a>

# Traefik

-   host: base-wagtail.devs-group.de
-   cms-host: cms.base-wagtail.devs-group.de
-   frontend: base-wagtail.devs-group.de


<a id="org930bc99"></a>

# Credentials

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


<a id="org740b236"></a>

## DB - Postgre

-   database: cms
-   user: root
-   password: root


<a id="org1c1cc7f"></a>

## DB - Pgadmin

-   email: info@devs-group.com
-   password: root


<a id="org283983f"></a>

## Backend - Admin

-   user: Admin
-   password: Admin123


<a id="orga0dce3c"></a>

## Static Files - MinIO

-   access-key: root
-   secret-key: root1234

