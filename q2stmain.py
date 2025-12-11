from pyscript import document, display
from pyodide.ffi import create_proxy

def show_club_info(event=None):

    #socsci club dictionary
    socsci_club = {
        "name": "Social Science Club",
        "description": "A club for students passionate about social sciences.",
        "schedule": "Tuesday & Thursday, 3:00-4:00 PM",
        "venue": "Room 409",
        "moderator": "Mr. Roberto Lim",
        "members": 22
    }

    #math club dictionary
    math_club = {  
        "name": "Mathematics Club",
        "description": "A club for students who love mathematics.",
        "schedule": "Monday, 2:30-3:00 PM",
        "venue": "Room 404",
        "moderator": "Mr. Nicole Gabuya",
        "members": 15
    }

    #basketball varsity dictionary
    basketball_varsity = {
        "name": "Basketball Varsity",
        "description": "The varsity for true hoopers.",
        "schedule": "Monday, 3:00-4:00 PM",
        "venue": "Quadrangle",
        "moderator": "Mr. Adrian Ruiz",
        "members": 16
    }

    #cocc dictionary
    cocc = {
        "name": "Cadet Officer Candidate Corps (COCC)",
        "description": "For students aspiring to be officers in the armed forces.",
        "schedule": "Wednesday, 2:30-4:30 PM",
        "venue": "Quadrangle or Teatro Preciosa",
        "moderator": "SSgt. Jemima David",
        "members": 15
    }

    #dance club dictionary
    dance_club = {
        "name": "Dance Club",
        "description": "A club for students who love dancing.",
        "schedule": "Tuesday, 3:00-5:00 PM",
        "venue": "Teatro Preciosa",
        "moderator": "Mr. Alfred Cases",
        "members": 27
    }

    #marching band dictionary
    marching_band = {
        "name": "Marching Band",
        "description": "A club for musically inclined students.",
        "schedule": "Tuesday & Wednesday, 3:00-4:30 PM",
        "venue": "Band Room",
        "moderator": "Mr. Emilio Alumno",
        "members": 35
    }   

    #get selected club from dropdown
    selected_club = document.getElementById("select_club").value
    
    #display corresponding club information
    if selected_club == "socsci":
        document.getElementById('club_info').innerText = "Club Name: " + socsci_club["name"] + "\n" + \
        "Description: " + socsci_club["description"] + "\n" + \
        "Schedule: " + socsci_club["schedule"] + "\n" + \
        "Venue: " + socsci_club["venue"] + "\n" + \
        "Moderator: " + socsci_club["moderator"] + "\n" + \
        "Number of Members: " + str(socsci_club["members"])
    elif selected_club == "math":
        document.getElementById('club_info').innerText = "Club Name: " + math_club["name"] + "\n" + \
        "Description: " + math_club["description"] + "\n" + \
        "Schedule: " + math_club["schedule"] + "\n" + \
        "Venue: " + math_club["venue"] + "\n" + \
        "Moderator: " + math_club["moderator"] + "\n" + \
        "Number of Members: " + str(math_club["members"])
    elif selected_club == "bball":
        document.getElementById('club_info').innerText = "Club Name: " + basketball_varsity["name"] + "\n" + \
        "Description: " + basketball_varsity["description"] + "\n" + \
        "Schedule: " + basketball_varsity["schedule"] + "\n" + \
        "Venue: " + basketball_varsity["venue"] + "\n" + \
        "Moderator: " + basketball_varsity["moderator"] + "\n" + \
        "Number of Members: " + str(basketball_varsity["members"])
    elif selected_club == "cocc":
        document.getElementById('club_info').innerText = "Club Name: " + cocc["name"] + "\n" + \
        "Description: " + cocc["description"] + "\n" + \
        "Schedule: " + cocc["schedule"] + "\n" + \
        "Venue: " + cocc["venue"] + "\n" + \
        "Moderator: " + cocc["moderator"] + "\n" + \
        "Number of Members: " + str(cocc["members"])
    elif selected_club == "dance":
        document.getElementById('club_info').innerText = "Club Name: " + dance_club["name"] + "\n" + \
        "Description: " + dance_club["description"] + "\n" + \
        "Schedule: " + dance_club["schedule"] + "\n" + \
        "Venue: " + dance_club["venue"] + "\n" + \
        "Moderator: " + dance_club["moderator"] + "\n" + \
        "Number of Members: " + str(dance_club["members"])
    elif selected_club == "band":
        document.getElementById('club_info').innerText = "Club Name: " + marching_band["name"] + "\n" + \
        "Description: " + marching_band["description"] + "\n" + \
        "Schedule: " + marching_band["schedule"] + "\n" + \
        "Venue: " + marching_band["venue"] + "\n" + \
        "Number of Members: " + str(marching_band["members"])

submit_button = document.getElementById('show_info')
submit_button.addEventListener('click', create_proxy(show_club_info))