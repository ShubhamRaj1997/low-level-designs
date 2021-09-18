import datetime


class FloorDisplay(object):
    def __init__(self):
        pass

    @staticmethod
    def display(display_data, floor_id):
        print(f"Updating Display for floor: {floor_id}....\n")
        s = f"Time : {datetime.datetime.now()}\n"
        for type_data, value_data in display_data.items():
            s += f"{type_data}:\n"
            for val_key, data in value_data.items():
                s += f"{val_key} = {data}\n"
            s += "\n"
        print(s)
