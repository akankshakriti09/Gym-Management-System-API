### Gym-Management-System-API
## Endpoints


* GET Gym List http://127.0.0.1:8000/gyms/ - gets the list of all gyms

* POST Gym  http://127.0.0.1:8000/gyms/ - post new gyms in list
    Body:
        {
            "Name": "cult.fit",
            "Address": "HSR Layout, Bangalore"
        }

* GET Trainer List http://127.0.0.1:8000/trainers/  - gets the list of all Trainers

* POST Trainer http://127.0.0.1:8000/trainers/ - post new trainers in list
    Body:
        {
            "Name": "Mahesh Kumar",
            "Specialization": "Fat Loss",
            "Gym": 12
        }

* GET Client List http://127.0.0.1:8000/clients/ - gets the list of all Clients

* POST Client http://127.0.0.1:8000/clients/ - post new clients in list
    Body:
        {
            "Name": "Ayisha",
            "Age": 23
        }

* GET Workout Session List http://127.0.0.1:8000/workouts/ - gets the list of all Workouts Session

* POST Workout Session http://127.0.0.1:8000/workouts/ - post new workout session in list
    Body:
        {
            "Client": 12,
            "Trainer": 7,
            "Date": "2023-10-22",
            "Duration": 32
        }

