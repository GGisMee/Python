pass
import requests


# Define the request body
body = {
    "request": {
        "divWidth": 500,
        "divHeight": 500,
        "headerEnabled": False,
        "selectedPeriod": None,
        "selectedWeek": 34,  # Example week
        "selectedTeacher": None,
        "selectedGroup": None,
        "selectedClass": {
            "guid": "your_group_guid",  # Replace with your group GUID
            "isClass": True
        },
        "selectedRoom": None,
        "selectedStudent": None,
        "selectedCourse": None,
        "selectedSubject": None,
        "selectedSchool": {
            "guid": "your_school_guid",  # Replace with your school GUID
            "settings": {
                "activateViewer": True
            }
        },
        "selectedSignatures": None,
        "domain": "your_domain"  # Replace with the domain
    }
}

# Define headers
headers = {
    "Accept": "application/json",
    "Content-Type": "application/json; charset=UTF-8"
}

# Make the POST request
response = requests.post('https://web.skola24.se/timetable/timetable-viewer/data/render', json=body, headers=headers)

# Parse the JSON response
data = response.json()

# Now `data` contains the schedule information retrieved from the Skola24 API
print(data)