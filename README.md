# CinemaTicket System

Introduction
a cinema ticket reservation system, focusing on OOP concepts in Python.
The system facilitates the reservation and purchase of tickets for movies, providing a user-friendly interface for customers. It includes features such as seat selection, payment processing, and order management.

### Features  
User Management: Allows users to create accounts, log in, and manage their profiles.  
Movie Selection: Displays a list of available movies for users to choose from.  
Seat Reservation: Enables users to select their preferred seats for a chosen movie.  
BankAccount Application: Facilitates secure payment transactions using CVV2 and ensures user data confidentiality.  
Discount Options: Applies discounts based on specified criteria, enhancing the user experience.  
Order History: Maintains a record of users' order history for reference.  


it is being done in collaboration with these following developers:  
**_Hesel Gharehbaei_** [@HeselGharehbaei](https://github.com/HeselGharehbaei)  
**_Mahsa Rahimimanesh_** [@MahsaRahimimanesh](https://github.com/MahsaRah99)  

---
### the prototypes of **_CinemaTicket_** project:

![prototype](<Screenshot from 2024-03-29 21-56-30.png>)
![prototype](<Screenshot from 2024-03-29 21-58-46.png>)
![prototype](<Screenshot from 2024-03-29 21-52-00.png>)
---

#### all project options:

![options](<Screenshot from 2024-03-29 22-13-06.png>)

### Installation
Clone the repository:  
Visit [**GitHub Repository**](https://github.com/MahsaRah99/CinemaTicket)  
or  
Copy the [**_SSH Key_**](git@github.com:MahsaRah99/CinemaTicket.git)  

---
## Usage
### 1) Create a virtual environment and activate it:  
> ## for linux:
> **1. create:**  
>
>        python3 -m venv env  
> **2. activate:**
>
>        source env/bin/activate

> ## for windows:
> **1. create:**   
>
>     python -m venv env
>    
>
> **2. activate:**
>
>     env/Scripts/activate       
>
---

### 2) Inserting movie and cinema data: 

#### run script files with arguman in terminal:
> **1. create manager:**
>
>        ppython scripts/create_managers.py (argumans) 
>

> **2. create movie:**
>
>        python scripts/create_movie.py (argumans) 
>

> **3. create cinema:**
>
>        python scripts/create_cinema.py (argumans) 
>

> **4. create reservation:**
>
>        python scripts/create_reservations.py (argumans) 
>


### 3) Run main menu and use the platform: 
>
>        python main.py 
>

---