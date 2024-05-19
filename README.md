
# amit_innovators
This is event management system created by amit (me) and my ideal innovators(team_mates). The superuser of this website have rights to create and scale events.this is user_freindly applications. All data is stored in admin dashboard. by entering different routes he can go to different location.
website have rights to create and scale events.this is user_freindly applications. All data is stored in admin dashboard. by entering different routes he can go to different location.
-------how to ACCESS AND RUN PROJECT-----------------------
clone this project git clone` https://github.com/amitk2003/ideal_innovators.git`
go to project directory `cd am123-09qw` 
for first time user create a virtual environment `python3 -m venv env`
Activate Virtual Environment `source env/bin/activate` 
Install Requirements Package `pip install -r requirements.txt`
Migrate Database `python manage.py migrate`
Create Super User or admin of this project `python manage.py createsuperuser `
Finally Run The Project `python manage.py runserver`
-----inorder to access this website below urls is must strictly follow other wise huge error will encounterd-- 
after running in cli or powershell on this `python manage.py runserver` you will redirect to admin dashboard.
if you want to access admin log url should be` https://127.0.0.1:8000` here you will access to all login credentials, all superuser details. 
if you want to signup `https://127.0.0.1:8000/USER/signup/` after signup hello message will displayed
if you want to login with your signup details` https://127.0.0.1:8000/USER/login/` after login you will redirect to page that is for customer where user can get short disription of what event is about go to `https://127.0.0.1:8000/USER/event_booking/ `
*if want to know contact details of owner `https://127.0.0.1:8000/events/user-mark/contact_us.html` 
*if want to know about us details `https://127.0.0.1:8000/events/about_us.html`
----these are some of screenshots that will get idea of my project---
1.screenshot of dashboard:
![dashboard](https://github.com/amitk2003/amit_innovators/assets/125468413/01bdae3f-2057-4fd1-9fd3-37b2100726c2)
2.screenshot of add event_detais:

![Screenshot 2024-05-18 091403](https://github.com/amitk2003/amit_innovators/assets/125468413/d3712879-cef2-426c-9b8a-75b92ae354aa)
3.screen shot of admin login:
![Screenshot 2024-05-18 093134](https://github.com/amitk2003/amit_innovators/assets/125468413/08fdf808-0642-46f4-84dc-9635bb54155a)
4. screenshot of signup(by user):

![Screenshot 2024-05-18 091700](https://github.com/amitk2003/amit_innovators/assets/125468413/937e0a72-e7ca-4d1c-ad63-0f49614f4b7d)

5. screenshot of signup(confirmation message that displayed signup)
   
![Screenshot 2024-05-18 091808](https://github.com/amitk2003/amit_innovators/assets/125468413/da017d70-5579-4f90-b7e6-c24c78c0319c)
6. screenshot of all login details till now:
![Screenshot 2024-05-17 214744](https://github.com/amitk2003/amit_innovators/assets/125468413/7c5176c7-b3ad-4c07-b63a-e9c4fb96575a)
7. screenshot of contact details of owner:

![Screenshot 2024-05-18 085441](https://github.com/amitk2003/amit_innovators/assets/125468413/a7e77e6e-0946-4dbb-8e70-c00619e0f18d)
8.screenshot of about us section which display short review of project:

![Screenshot 2024-05-18 085247](https://github.com/amitk2003/amit_innovators/assets/125468413/7ea008da-b16b-4cbb-8a69-111095b2794f)
9.screenshot of booking_event

![Screenshot 2024-05-18 085727](https://github.com/amitk2003/amit_innovators/assets/125468413/206f3f78-f3e2-441d-ae3a-635a8b6a0248)
>>>>>>> origin/master
