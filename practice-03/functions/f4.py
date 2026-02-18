def show_data(*args, **kwargs):
    print("Positional:", args)
    print("Named:", kwargs)

show_data(1, 2, 3, name="Aidar", age=17)
