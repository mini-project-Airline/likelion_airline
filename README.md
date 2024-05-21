## likelion_Airline 핵심기능

**User**
1. 회원가입 (Sign Up)
   - Endpoint: `POST /signup`
   - Description: 새로운 사용자 등록
   - Payload: Includes firstName, lastName, email, and password.
   - Response: Success message and user details. 
2. 로그인 (Login)
   - Endpoint: `POST /login`
   - Description: 사용자가 로그인하고 JWT 토큰 발급
   - Payload: User email and password.
   - Response: Success message, JWT token, and user details.
3. 사용자 삭제 (Delete User)
   - Endpoint: `DELETE /delete/{user_id}`
   - Description: 사용자 삭제
   - Authentication: Requires JWT token.
   - Response: Confirmation message.

**Ticket**
1. 티켓 목록 조회 (Get Tickets)
   - Endpoint: `GET /tickets`
   - Description: 현재 사용자의 모든 티켓 조회
   - Authentication: Requires JWT token.
   - Parameters: Pagination options (`page`, `limit`).
   - Response: List of tickets and pagination details.
2. 티켓 구매 (Purchase Ticket)
   - Endpoint: `POST /purchase/{ticket_id}`
   - Description: 사용자가 티켓 구매
   - Authentication: Requires JWT token.
   - Payload: `flightId` of the ticket to purchase and userId.
   - Response: Purchase details.
3. 티켓 환불 (Refund Ticket)
   - Endpoint: `DELETE /tickets/{ticket_id}/refund`
   - Description: 사용자가 특정 티켓 환불
   - Authentication: Requires JWT token.
   - Response: Confirmation message.

**Password**
1. 비밀번호 변경 (Change Password)
   - Endpoint: `POST /change-password`
   - Description: 사용자가 비밀번호 변경
   - Authentication: Requires JWT token.
   - Payload: oldPassword and newPassword.
   - Response: Confirmation message.

**Flight**
1. 항공편 조회 (Get Flights)
   - Endpoint: `GET /flights`
   - Description: 항공편 목록 조회
   - Parameters: Filter options such as `departures`, `arrivals`, `departure_date`, `arrival_date`, `flightClass`, `airline`, and pagination (`page`, `limit`).
   - Response: List of flights matching the criteria.



## Database ERD

To view the **`Database ERD`**, please click [here](https://www.erdcloud.com/p/rxBGYRpi8yz5r5LEm).

## How To Use

To clone and run this application, you'll need [Git](https://git-scm.com), [Python](https://www.python.org/downloads/) and [Node.js](https://nodejs.org/) installed on your computer. From your command line:

```bash
# Go into the repository
$ cd backend

# Install dependencies
$ pip install -r requirements.txt
```

> ### Backend

After setting up the database, please use the `makemigrations` and `migrate` commands.

```bash
# Run the app
$ python manage.py runserver
```

> ### Frontend

```bash
# Go into the repository
$ cd frontend

# Install dependencies
$ npm install

# Run the app
$ npm run dev
```


## Credits

This software uses the following open source packages:

- [Python](https://www.python.org/)
- [DRF : Django REST Framework](https://www.django-rest-framework.org/)
- [React](https://react.dev/)

## Related

- [Axios](https://axios-http.com/kr/docs/intro)
- [Swagger](https://swagger.io/)

