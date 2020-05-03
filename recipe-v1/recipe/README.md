**_Technologies_**

    - Python
    - Django

**_Installed Libraries_**

	- Django Rest Framwork

**_Setup Instructions_**

    - python manage.py migrate
    - python manage.py makemigrations 
    - python manage.py migrate
    - python manage.py runserver

**_Test REST APIs_**

    - Authentication Token
        - Get Authentication Token
            - http://localhost:8000/api/login
        
        - Add the Authentication Token into Request Header 
            - Authorization : Token <Token>
            
        - "ModHeader Extention" can be used to set "Authorization Header" when send reuqests from browser
        
        - Authorization Token only need for HTTP "POST" / "PUT" / "PATCH / "DELETE Requests

    - http://localhost:8000/api/profile
        - GET : List All Profiles
        - POST: Create new Profile  
        
    - http://localhost:8000/api/profile/<profile_id/>
        - GET: View Specific Profile
        - PUT: Update Specific Profile
        - PATCH: Update Specific Field in Specific Profile
        - DELETE: Delete Specific Profile
        
    - http://localhost:8000/api/feed/
        - GET : List All Feed Items
        - POST: Create new Feed Item  
        
    - http://localhost:8000/api/feed/<feed_item_id/>
        - GET: View Specific Feed Item
        - PUT: Update Specific Feed Item
        - PATCH: Update Specific Field in Specific Feed Item
        - DELETE: Delete Specific Feed Item