# Veprof

## Application cycle

Fill out `app.demo.env` in folder - **docker** with your `Firebase credentials` and **rename** it to `app.env` 

Build

```shell
docker-compose -f .\docker\docker-compose.yml -p veprof build
```

Start 

```shell
docker-compose -f .\docker\docker-compose.yml -p veprof up -d
```

## Credentials

```
username: john-doe
email: admin@example.com
password: admin123
```

## API

### /firebase/sign-in/

Request
```
curl --location --request POST '127.0.0.1:8000/fb_auth/sign-in/' \
--header 'Content-Type: application/json' \
--header 'Cookie: csrftoken=KmVt7v9nk34BZwU6Js4mXlySfxcOUgpOqT7uia2EuwAJq6dVjZgAMBX1SmWVPlEQ' \
--data-raw '{
    "email": "admin@example.com",
    "password": "admin123"
}'
```

Response
```
{
    "token": "eyJhbGciOiJSUzI1NiIsImtpZCI6IjUyZmEwZjE2NmJmZjZiODU5N2FjMGFlMDRlNTllZmYxOTk1N2MyYmIiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL3NlY3VyZXRva2VuLmdvb2dsZS5jb20vdmVwcm9mLTcxY2JjIiwiYXVkIjoidmVwcm9mLTcxY2JjIiwiYXV0aF90aW1lIjoxNjYxNzczOTY0LCJ1c2VyX2lkIjoiMFJKWEkxa0pTOWRBZ3dDam15NUhaTTZoZnFvMSIsInN1YiI6IjBSSlhJMWtKUzlkQWd3Q2pteTVIWk02aGZxbzEiLCJpYXQiOjE2NjE3NzM5NjQsImV4cCI6MTY2MTc3NzU2NCwiZW1haWwiOiJhZG1pbkBleGFtcGxlLmNvbSIsImVtYWlsX3ZlcmlmaWVkIjpmYWxzZSwiZmlyZWJhc2UiOnsiaWRlbnRpdGllcyI6eyJlbWFpbCI6WyJhZG1pbkBleGFtcGxlLmNvbSJdfSwic2lnbl9pbl9wcm92aWRlciI6InBhc3N3b3JkIn19.a0ebxx9z5y1L9Qd0mMOfUhM2i0nEeqRTKTAiAgrB2HxVXWod3kBkXXzZETay0TumbAzi27GDBQsGw_31tk38-5gqOHY6jpTgSyjGORAs-XrLGtjMJUyfB8IyppGFiEL37c2nBWAARq6zQlkav_Ou_00p5fDErnZ05VYT79pMvc4c-FpHxqWjZZGwlAZ_QDWOzk4P66Jqe5LV-sfrQDtvO6ZMo9YLVfs_UBOF0G53iZ9Z5CIdIZkxafC3NbT1bV4TBH5kEitRLpIbd8H_K0JF5zV7WVX69BTSKJMcToMWF6KCFiNNGqh49xftUFlL8ZpksI3ICpYWz8FKsz7XCThx3w"
}
```

Errors:

`Status 404`
```
```

### /firebase/dj-users/

Request
```
curl --location --request GET '127.0.0.1:8000/fb_auth/' \
--header 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IjUyZmEwZjE2NmJmZjZiODU5N2FjMGFlMDRlNTllZmYxOTk1N2MyYmIiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL3NlY3VyZXRva2VuLmdvb2dsZS5jb20vdmVwcm9mLTcxY2JjIiwiYXVkIjoidmVwcm9mLTcxY2JjIiwiYXV0aF90aW1lIjoxNjYxNzcxMzAyLCJ1c2VyX2lkIjoiMFJKWEkxa0pTOWRBZ3dDam15NUhaTTZoZnFvMSIsInN1YiI6IjBSSlhJMWtKUzlkQWd3Q2pteTVIWk02aGZxbzEiLCJpYXQiOjE2NjE3NzEzMDIsImV4cCI6MTY2MTc3NDkwMiwiZW1haWwiOiJhZG1pbkBleGFtcGxlLmNvbSIsImVtYWlsX3ZlcmlmaWVkIjpmYWxzZSwiZmlyZWJhc2UiOnsiaWRlbnRpdGllcyI6eyJlbWFpbCI6WyJhZG1pbkBleGFtcGxlLmNvbSJdfSwic2lnbl9pbl9wcm92aWRlciI6InBhc3N3b3JkIn19.TOKdyaVOBYjozVvlv4E9Tc1mqlSsa20_SgSKc5PUpEc_3C2c2vE26qrCiQIZuvwMD1athkj6xAmX-5NfBw9B1S_JzDwh0xgouuEb0li1P9SehVQl8SyOYMi0VcxlZDdW-qwRW4bGjtdq6mCT0SEqMyGoTuJUujAqIWfPrKyp_lLSRSvXJOAoVK8FEvzeOP3aSyqdR5_ojHy_ptr01_jTOOOZkFQVrB_ouCd4wA8L036UG_d7u40RRMI6WNxGZFW__BFAvhToratY4om11Sdz-i26l7HhP-_nw2fWZrkV-lw_w7qnPjjnUe4ob0t4T7K9dvUYdWUOQDcex0H34-cLqg' \
--header 'Cookie: csrftoken=KmVt7v9nk34BZwU6Js4mXlySfxcOUgpOqT7uia2EuwAJq6dVjZgAMBX1SmWVPlEQ' \
--data-raw ''
```

Response
```
[
    {
        "username": "john-doe",
        "email": "admin@example.com"
    }
]
```

Errors:

`Status 401`
```
{
    "detail": "Incorrect authentication credentials."
}
```
