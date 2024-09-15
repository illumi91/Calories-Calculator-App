from flask.views import MethodView
from wtforms import Form, StringField, SubmitField
from flask import Flask, render_template, request
from calories_app.calories_calculator import CaloriesCalculator
from calories_app.temperature import Temperature

app = Flask(__name__)


class HomePage(MethodView):
    
    def get(self):
        return render_template("index.html")


class CaloriesFormPage(MethodView):
    def get(self):
        calories_form = CaloriesForm()
        return render_template("calories_form_page.html", caloriesform=calories_form)
    
    def post(self):
        caloriesform = CaloriesForm(request.form)
        
        weight = float(caloriesform.weight.data)
        height = float(caloriesform.height.data)
        age = float(caloriesform.age.data)
        city = caloriesform.city.data
        country = caloriesform.country.data
        
        temperature = Temperature(country, city).get()
        calories_calculator = CaloriesCalculator(weight, height, age, temperature)

        return render_template(
            "calories_form_page.html",
            result=True,
            caloriesform=caloriesform,
            calories=calories_calculator.calculate(),
        )


class CaloriesForm(Form):
    weight = StringField("Insert your weight: ", default=70)
    height = StringField("Insert your height: ", default=175)
    age = StringField("Insert your age: ", default=25)
    city = StringField("Insert the city: ", default="Ancona")
    country = StringField("Insert the country: ", default="Italy")
    
    button = SubmitField("Calculate")


app.add_url_rule("/", view_func=HomePage.as_view("home_page"))
app.add_url_rule("/calories_form", view_func=CaloriesFormPage.as_view("calories_form_page"))

app.run(debug=True)