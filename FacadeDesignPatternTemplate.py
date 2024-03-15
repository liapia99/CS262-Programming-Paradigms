class Venue_Booking:
    """
    Creating a subsystem responsible for handling venue bookings.
    """
    # forcing to return a str so that anything else would be an error
    def book_venue(self, date: str) -> str:
        return f"Venue Booked for {date}"

class Catering_Service:
    """
    Subsystem for handling catering orders.
    """
    def arrange_catering(self, menu: str) -> str:
        return f"Catering order for {menu}"

class Band_Service:
    """
    Subsystem for handling music played at event.
    """
    def arrange_band(self, music: str) -> str:
        return f"Music planned is {music}"

class Notification_System:
    """
    Subsystem for handling notifications.
    """
    def send_notification(self)->str:
        return "Invitation Sent."

class Event_Manager:
    """
    Facade class which simplifies the interaction with the various management systems.
    """
    def __init__(self)-> None:
        self.venue_booking = Venue_Booking()
        self.catering_service = Catering_Service()
        self.notification_system = Notification_System()
        self.band_service = Band_Service()

    def organize_event(self,date:str, menu:str, music:str)->str:
        """
        A method to organize the entire event between different services.
        :param date:
        :param menu:
        :return:
        """
        results = []
        results.append(self.venue_booking.book_venue(date))
        results.append(self.catering_service.arrange_catering(menu))
        results.append(self.band_service.arrange_band(music))
        results.append(self.notification_system.send_notification())
        return "\n".join(results)

def client_code(event_manager: Event_Manager)-> None:
    """
    The client code that uses the facade to simplify the process of organizing our event.
    :param event_manager:
    :return:
    """
    print(event_manager.organize_event("2024-03-15", "Carivore, Gluten-Free","U2"))

if __name__ == "__main__":
    event_manager = Event_Manager()
    client_code(event_manager)
