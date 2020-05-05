**_Technologies_**

    - Python
    - Django
    - Postgres DB
    - TDD

**_Installed Libraries_**

	- Django Rest Framwork
	- Psycopg2
	- Pillow

**_Setup Instructions_**

    - Create 'recipe' DB in Postgres DB Server
    - python manage.py makemigrations
    - python manage.py migrate
    - python manage.py createsuperuser
    - docker-compose up

**_Run TDD Unit Tests Manually_**

    - python manage.py test

**_Test REST APIs_**  

    - Authentication Token
        - Get Authentication Token
            - http://localhost:8000/api/user/token
        
        - Add the Authentication Token into Request Header 
            - Authorization : Token <Token>
            
        - "ModHeader Extention" can be used to set "Authorization Header" when send reuqests from browser
        
        - Authorization Token only need for HTTP "POST" / "PUT" / "PATCH" / "DELETE" Requests

    - http://localhost:8000/api/user/create        
        - POST: Create new User
        
    - http://localhost:8000/api/user/me
        - GET : Current User 
    
    - http://localhost:8000/api/recipe/tags/
        - GET : Get List of Tags
        - POST : Create new Tag
        
    - http://localhost:8000/api/recipe/ingredients/
        - GET : Get List of Ingredients
        - POST : Create new Ingredient
        
    - http://localhost:8000/api/recipe/recipes/
        - GET : Get List of Recipes
        - POST : Create new Recipe 
    
    - http://localhost:8000/api/recipe/recipes/<id>
        - GET : Get Spicific Recipe
        
    - http://localhost:8000/api/recipe/recipes/<id>/upload-image
        - POST : Upload an image to the Recipe
        
    - http://localhost:8000/api/recipe/recipes/?ingredients=<id>
        - GET : Filter by Ingredients
        
    - http://localhost:8000/api/recipe/recipes/?tagss=<id>
        - GET : Filter by Tags
        
    - http://localhost:8000/api/recipe/ingredients/?assigned_only=1
        - GET : Filter by Ingredients which only used  in Recipes
        
    - http://localhost:8000/api/recipe/tags/?assigned_only=1
        - GET : Filter by Tags which only used in Recipes