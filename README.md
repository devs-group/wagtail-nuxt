
# Table of Contents

1.  [Setup](#org62d9d25)
2.  [Endpoints](#org1f07007)
    1.  [GraphQl - GraphiQl](#org91cf433)
    2.  [Backend - Admin](#org6973f56)
    3.  [Frontend - Nuxt](#orgc6c0ff5)
    4.  [Static Files - MinIO](#org36966ea)
    5.  [DB - Pgadmin](#orgb58cb72)
3.  [Traefik](#orgf0c848e)
4.  [Credentials](#orgcc279cd)
    1.  [DB - Postgre](#orga02664a)
    2.  [DB - Pgadmin](#orgc56748e)
    3.  [Static Files - MinIO](#orgb0e1e50)


<a id="org62d9d25"></a>

# Setup

1.  Copy [.env.dist](.env.dist) to [.env](.env)


<a id="org1f07007"></a>

# Endpoints


<a id="org91cf433"></a>

## GraphQl - GraphiQl

<http:localhost:8000/api/graphiql>


<a id="org6973f56"></a>

## Backend - Admin

<http:localhost:8000/admin>


<a id="orgc6c0ff5"></a>

## Frontend - Nuxt

<http:localhost:3000>


<a id="org36966ea"></a>

## Static Files - MinIO

<http:127.0.0.1:9000>


<a id="orgb58cb72"></a>

## DB - Pgadmin

<http:localhost:5050>


<a id="orgf0c848e"></a>

# Traefik

-   host: base-wagtail.devs-group.de
-   cms-host: cms.base-wagtail.devs-group.de
-   frontend: base-wagtail.devs-group.de


<a id="orgcc279cd"></a>

# Credentials


<a id="orga02664a"></a>

## DB - Postgre

-   database: cms
-   user: root
-   password: root


<a id="orgc56748e"></a>

## DB - Pgadmin

-   email: info@devs-group.com
-   password: root


<a id="orgb0e1e50"></a>

## Static Files - MinIO

-   access-key: root
-   secret-key: root1234

