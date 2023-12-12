from model import RealEstateModel
from view import RealEstateView

class RealEstateController:
    def __init__(self):
        self.model = RealEstateModel()
        self.view = RealEstateView(self)

        # Attach event handlers and other setup as needed

        self.update_views()

    def update_views(self):
        apartments_data = self.model.get_apartments()
        clients_data = self.model.get_clients()
        applications_data = self.model.get_applications()

        self.view.update_apartments_tree(apartments_data)
        self.view.update_clients_tree(clients_data)
        self.view.update_applications_tree(applications_data)

    # Add methods for handling user actions and updating the model and view accordingly

if __name__ == "__main__":
    app = RealEstateController()
    app.view.mainloop()
