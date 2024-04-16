# RESTful API Design Guidelines

## 1. Use HTTP Methods Appropriately
- **GET**: Retrieve resources.
- **POST**: Create new resources.
- **PUT/PATCH**: Update existing resources. Use `PUT` for full replacements and `PATCH` for partial updates.
- **DELETE**: Remove resources.

## 2. Resource Naming
- Use nouns to represent resources (e.g., `users`, `orders`).
- Use plural names for collections (`users`) and singular for individual elements (`users/{id}`).
- URLs should be simple and predictable.

## 3. Use Sub-resources for Relations
- For hierarchical or related resources, use nested routes, e.g., `/users/{userId}/orders`.

## 4. Use HTTP Status Codes to Indicate API Responses
- **200 OK**: Successful read operations.
- **201 Created**: Successful creation of a resource.
- **204 No Content**: Successful request with no return body (like DELETE).
- **400 Bad Request**: Invalid user input.
- **401 Unauthorized**: Access errors.
- **403 Forbidden**: Authorization errors.
- **404 Not Found**: Resource does not exist.
- **500 Internal Server Error**: Server errors.

## 5. Version Your API
- Include a version number in the URL (e.g., `/v1/users`) to manage changes over time.

## 6. Include Metadata in Responses
- Provide metadata (pagination, links, etc.) in API responses to enhance usability.

## 7. Use Query Parameters for Optional Features
- Filter, sort, and paginate collections using query parameters, like `/users?role=admin&page=2`.

## 8. Secure the API
- Use HTTPS to encrypt data in transit.
- Implement authentication and authorization to protect resources.

## 9. Provide Meaningful Documentation
- Document endpoints, parameters, request/response examples, status codes, and errors to facilitate easy integration.


---------

## 1. HTTP 메소드 적절하게 사용하기
- **GET**: 리소스 검색.
- **POST**: 새로운 리소스 생성.
- **PUT/PATCH**: 기존 리소스 업데이트. `PUT`은 전체 교체용, `PATCH`는 부분 업데이트용.
- **DELETE**: 리소스 제거.

## 2. 리소스 명명
- 리소스를 표현하기 위해 명사 사용 (예: `users`, `orders`).
- 집합체에는 복수형 이름 사용 (`users`), 개별 요소에는 단수형 이름 사용 (`users/{id}`).
- URL은 단순하고 예측 가능해야 함.

## 3. 관계에 대한 하위 리소스 사용
- 계층적이거나 관련된 리소스에 대해서는 중첩된 라우트 사용, 예: `/users/{userId}/orders`.

## 4. HTTP 상태 코드를 사용하여 API 응답 표시
- **200 OK**: 성공적인 읽기 작업.
- **201 Created**: 리소스 생성 성공.
- **204 No Content**: 본문 반환 없이 성공적인 요청 (예: DELETE).
- **400 Bad Request**: 사용자 입력이 잘못됨.
- **401 Unauthorized**: 접근 오류.
- **403 Forbidden**: 권한 오류.
- **404 Not Found**: 리소스가 존재하지 않음.
- **500 Internal Server Error**: 서버 오류.

## 5. API 버전 관리
- URL에 버전 번호 포함 (예: `/v1/users`) 시간이 지나도 변경 관리 가능.

## 6. 응답에 메타데이터 포함
- 사용성 향상을 위해 API 응답에 메타데이터 (페이지네이션, 링크 등) 제공.

## 7. 선택적 기능에 대한 쿼리 파라미터 사용
- 쿼리 파라미터를 사용하여 컬렉션 필터링, 정렬 및 페이지네이션, 예: `/users?role=admin&page=2`.

## 8. API 보안 유지
- HTTPS를 사용하여 전송 중인 데이터 암호화.
- 리소스 보호를 위한 인증 및 권한 부여 구현.

## 9. 의미 있는 문서 제공
- 쉬운 통합을 위해 엔드포인트, 파라미터, 요청/응답 예시, 상태 코드 및 오류 문서화.

