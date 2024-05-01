# 📌 API
### Accounts
1. 회원가입
  - Endpoint : '/api/accounts/'
  - Method : POST
  - required Field : username, password, email, name, nickname, birth
<br>

2. 회원탈퇴
  - Endpoint : `/api/accounts/`
  - Method : DELETE
  - required Field : password
<br>

3. 로그인
  - Endpoint : `/api/accounts/login/`
  - Method : POST
  - required Field : username, password
<br>

4. 로그아웃
  - Endpoint : `/api/accounts/logout/`
  - Method : POST
  - required Field : refresh
<br>

5. 본인 정보 수정
  - Endpoint : `/api/accounts/<username>/`
  - Method : POST
<br>

6. 비밀번호 수정
  - Endpoint : `/api/accounts/password/`
  - Method : POST
  - required Field : old_password, new_password, confirm_password
<br>

7. token_refresh
  - Endpoint : `/api/accounts/token/refresh/`
  - Method : POST
  - required Field : refresh
<br>

### Products
1. 상품 목록 조회
  - Endpoint : `/api/products/`
  - Method : GET
<br>

2. 상품 등록
  - Endpoint : `/api/products/`
  - Method : POST
  - required Field : title, content
<br>

3. 상품 정보 수정
  - Endpoint : `/api/products/<product_id>`
  - Method : PUT 
<br>

4. 상품 삭제
  - Endpoint : `/api/products/<product_id>`
  - Method : DELETE
<br>
