from channel_client_api import ClientHandgun
import os

if __name__=="__main__":
    # create client's socket
    # client = ClientHandgun("127.0.0.1", 8888)
    client = ClientHandgun(os.getenv("ip"), 8888)

    # load the set of data (e.g., images)
    client.load_bullets("resources/images/angry/")
    # client.refit_gun(preprocessed_function)
    client.round_shoot()
    # next(client.shoot())
    client.drop_gun()
