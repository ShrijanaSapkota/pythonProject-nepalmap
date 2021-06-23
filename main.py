import turtle
import pandas
screen = turtle.Screen()
screen.title("Nepal Zone Game")
image = "nepal_divisions_blank.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("data.csv")
all_zones=data.zone.to_list()
guess_zones =[]
while len(guess_zones)<14:
    answer_zone = screen.textinput(title=f"{len(guess_zones)}/14 Zones correct", prompt=" What's another name?").title()

    if answer_zone == "Exit":
        missing_zones =[zone for zone in all_zones if zone not in guess_zones]
        # for zone in all_zones:
        #     if zone not in guess_zones:
        #         missing_zones.append(zone)
        new_data = pandas.DataFrame(missing_zones)
        new_data.to_csv("zones_to_learn.csv")
        break
    if answer_zone in all_zones:
        guess_zones.append(answer_zone)
        t=turtle.Turtle()
        t.hideturtle()
        t.penup()
        zone_data = data[data.zone == answer_zone]
        t.goto(int(zone_data.x), int(zone_data.y))
        t.write(answer_zone)

screen.exitonclick()