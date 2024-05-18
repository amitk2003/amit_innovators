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
