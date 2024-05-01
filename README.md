# Sparta - Market
**Django**의 **DRF**를 배우고서 익숙해지기 위해 개인과제로서 수행

## 📑 ERD
![ERD4 drawio (1)](https://github.com/pkg0203/SpartaMarket_DRF/assets/141356379/e88cd6a2-754d-44d1-9c5d-c178e659ac3b)




## 🖥️ 프로젝트 소개
중고 게시판 사이트로 물품의 CRUD와 사이트를 DRF로 구현

https://teamsparta.notion.site/DRF-89e4241bfd504e2aaa4d715bf9055d19
<br>

## 🕰️ 개발 기간
* 24.04.29. - 24.05.02. / 4일

### 🧑‍🤝‍🧑 맴버구성 
* 박강균


### ⚙️ 개발 환경
- **Backend** 및 **API** : `Python`, `Postman`
- **Framework** : `Django 4.2v`, 'rest_framework'
- **Database** : `SQLite3`
<br>



## 📌 주요 기능
### < Accounts >
#### 회원가입 `api/accounts/` , `POST`
- `username` 과 `email`은 primary key로 table에 unique하게 존재
- 이 때 `password`는 encode 된 것을 보여주게 됨

![image](https://github.com/pkg0203/SpartaMarket_DRF/assets/141356379/e9d1eff8-31d9-4a2e-95dd-558d4d19fd69)

#### 로그인 `api/accounts/login` , 'POST'
- `JWT(Jason Web Token)`을 이용하여 구현
- `username` 과 `password`가 유효할 경우 `access token`과 `refresh token`을 부여받음

![image](https://github.com/pkg0203/SpartaMarket_DRF/assets/141356379/0b09f71e-6d83-43ce-8f32-65b6b40f3a79)

#### 로그아웃 `api/accounts/logout` , 'POST'
- 로그인 상태로, `refresh token`을 body에 담아서 요청 시
- `refresh token`은 blacklist에 올라가게 됨
-  `access token`이 만료되기 전이라면 기능을 사용할 수 있지만 그건 `FE`의 일임
  
![image](https://github.com/pkg0203/SpartaMarket_DRF/assets/141356379/7cb9a1dc-725f-449c-b37c-7eb91e9ce544)

#### 프로필 조회 `api/accounts/<username>/` , `GET`
- 로그인 상태로, 요청 시 해당 유저의 프로필을 조회할 수 있음
- password 를 제외한 값을 보게됨

![image](https://github.com/pkg0203/SpartaMarket_DRF/assets/141356379/f3dbd9b7-0b36-4402-9f6c-194e2f0f17e9)

#### 회원 탈퇴 `api/accounts/` , `DELETE`
- 로그인 상태로, body에 자신의 `password`를 담아 요청하면 된다.

![image](https://github.com/pkg0203/SpartaMarket_DRF/assets/141356379/ac4f0104-41c1-4ec9-be32-d78fc36793a8)

#### 본인 정보 수정 `api/accounts/<username>/` , `PUT`
- 로그인 상태로, 본인 정보만 수정할 수 있음
- 부분 수정도 가능
  
![image](https://github.com/pkg0203/SpartaMarket_DRF/assets/141356379/7c3e25e5-bb28-460a-baa3-bb0a673ecb4c)

#### 비밀번호 변경 `api/accounts/password/` , `PUT`
- 이전 비밀번호와 동일할 경우 **변경할 수 없음**

![image](https://github.com/pkg0203/SpartaMarket_DRF/assets/141356379/d2eafd13-82a6-436d-a9a3-446d84e9661a)
![image](https://github.com/pkg0203/SpartaMarket_DRF/assets/141356379/c6249c4e-a86d-4bbe-96a1-2867476aa7c9)

#### 팔로우 `api/accounts/<username>/follow` , `POST`
- 로그인 상태로, <username> 을 팔로우 하는 요청
  - 이미 팔로우 중이면, 언팔로우하게 됨
  - 그렇지 않으면 팔로우하게 됨 

![image](https://github.com/pkg0203/SpartaMarket_DRF/assets/141356379/992c93d8-44fa-4410-ab1d-a5000f80b0e2)

### < Products >

#### Product 생성 `api/products/` , `POST`
- 로그인 상태로, `title` , `content` , `image` 를 기입 가능
- **`image` field는 비울 수 없음**
  - 또한 **base64** 를 이용하여 encode한 것을 body에 채워야 함

  ![image](https://github.com/pkg0203/SpartaMarket_DRF/assets/141356379/41a1796b-d0ff-4111-80c7-bf935cc5f730)

- 업로드된 image는 `media` 폴더에서 확인 가능 

#### Product 조회 `api/products/` , `GET`
- 모든 Product를 조회할 수 있다.
- 로그인하지 않은 상태로 사용할 수 있는 유일한 기능

![image](https://github.com/pkg0203/SpartaMarket_DRF/assets/141356379/6e20348a-2910-461a-8ee4-dda755646f7f)

#### Product 삭제 `api/products/<product_id>` , `DELETE`
- 로그인 상태로, 본인 글만 삭제 가능

![image](https://github.com/pkg0203/SpartaMarket_DRF/assets/141356379/7795b107-095f-4c60-9f2a-03fd6e45131a)

#### Product 수정 `api/products/<products_id>` , `PUT`
- 로그인 상태로, 본인 글만 수정 가능
- 부분 수정 가능
  - 아래 글의 수정 전 글 상태는 `Product 조회` 에서 확인 할 수 있다.
  
  ![image](https://github.com/pkg0203/SpartaMarket_DRF/assets/141356379/7d16d391-d497-4c4e-82cb-dd253f26bd20)

#### Product 좋아요 `api/products/<proucts_id>/like/` , `POST`
- 로그인 상태에서만 사용 가능
- body는 빈 상태로 요청만 해도 된다
  - 팔로우와 마찬가지 로직을 가지고 있다.

 ![image](https://github.com/pkg0203/SpartaMarket_DRF/assets/141356379/113f774f-0632-4e87-afbb-20c26272c60d)
