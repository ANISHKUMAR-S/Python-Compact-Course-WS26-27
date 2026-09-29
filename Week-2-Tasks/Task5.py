events = {
    "Warm Up mit Dennis Streichert und Maxim Diagilew": {
        "date": "2026-09-19",
        "start": "20:00",
        "end": "22:00",
        "location": "Friedensplatz 1, 44135 Dortmund"
    },

    "Marquess Open-Air-Konzert": {
        "date": "2026-09-19",
        "start": "22:15",
        "end": "23:45",
        "location": "Friedensplatz 1, 44135 Dortmund"
    },

    "Musikfeuerwerk": {
        "date": "2026-09-19",
        "start": "23:45",
        "end": "00:00",
        "location": "Friedensplatz 1, 44135 Dortmund"
    },

    "Abfüllen und Etikettieren wie vor 100 Jahren": {
        "date": "2026-09-19",
        "start": "17:00",
        "end": "21:00",
        "location": "Brauerei-Museum Dortmund, Steigerstraße 16, Dortmund"
    },

    "Schnupperführungen": {
        "date": "2026-09-19",
        "start": "16:00",
        "end": "22:30",
        "location": "Apotheken-Museum, Wißstraße 11, Dortmund"
    },

    "Connected Digitale Kultur im Ruhrgebiet": {
        "date": "2026-09-19",
        "start": "18:00",
        "end": "23:00",
        "location": "Phoenix des Lumières, Phoenixplatz 4, Dortmund"
    }
}

night_date = "2026-09-19"

print("\nEvents running during the Night of Museums in Dortmund on 19 September 2026:")

for event, details in events.items():
    if details["date"] == night_date:
        print(f"\nEvent: {event}")
        print(f"Date: {details['date']}")
        print(f"Start Time: {details['start']}")
        print(f"End Time: {details['end']}")
        print(f"Location: {details['location']}")