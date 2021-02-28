from jsonparser import JSONParser
from traveladvisoryexample.travel_advisory_parser import TravelAdvisoryParser


class Menu:
    url = "https://www.travel-advisory.info/api"
    json_object = JSONParser(url)
    travel_object = TravelAdvisoryParser(json_object.data)

    def __init__(self):
        self.choices = {
                "1": self.show_travel_score,
                "2": self.show_travel_message,
                "3": self.quit
                }
    
    @staticmethod
    def display_menu():
        print("""
              1. Travel score
              2. Travel message
              3. Quit
              """)
        
    @staticmethod
    def show_travel_score():
        code = input("Enter country code or country name ")
        print(Menu.travel_object.get_travel_score(code))
        return True
        
    @staticmethod
    def show_travel_message():
        code = input("Enter country code or country name ")
        print(Menu.travel_object.get_travel_message(code))
        return True
        
    @staticmethod
    def quit():
        print("Quit")
        return False

    def run(self):
        while True:
            Menu.display_menu()
            choice = input("Enter an option ")
            action = self.choices.get(choice)
            if action:
                status = action()  # call necessary action
                if not status:
                    break
            else:
                print("Invalid choice")


if __name__ == "__main__":  # False when module is imported
    Menu().run()