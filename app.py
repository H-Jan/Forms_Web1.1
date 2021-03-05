from flask import Flask, request, render_template
import random

app = Flask(__name__)

def sort_letters(message):
    """A helper method to sort the characters of a string in alphabetical order
    and return the new string."""
    return ''.join(sorted(list(message)))


@app.route('/')
def homepage():
    """A homepage with handy links for your convenience."""
    return render_template('home.html')

@app.route('/froyo')
def choose_froyo():
    """Shows a form to collect the user's Fro-Yo order."""
    return render_template('froyo_form.html')

@app.route('/froyo_results')
def show_froyo_results():
    users_froyo_flavor = request.args.get('flavor')
    users_toppings = request.args.get('toppings')

    #Refactoring with context dictionary

    context = {
        'users_froyo_flavor': users_froyo_flavor,
        'users_froyo_toppings': users_froyo_toppings
    }

    return render_template('froyo_results.html', **context)
    #Treated as **kwargs
    #Used Request.args because the method is a get method rather than a Post method


    
@app.route('/favorites')
def favorites():
    return """
    <form action="/favorites_results" method="GET">
        What is your favorite color?
        <input type="text" name="color"> <br/>
        What is your favorite animal?
        <input type="text" name="animal"> <br/>
        What is your favorite city?
        <input type="text" name="city"> <br/>
        <input type="submit" value="Submit!">
    </form>
    """



@app.route('/favorites_results')
def favorites_results():
    users_favorite_color = request.args.get('color')
    users_favorite_animal = request.args.get('animal')
    users_favorite_city = request.args.get('city')
    return f'Wow, I didn\'t know {users_favorite_color} {users_favorite_animal} lived in {users_favorite_animal} '




@app.route('/secret_message')
def secret_message():
    return """
    <form action="/message_results" method="POST">
        Type your secret message here
        <input type="text" name="message"> <br/>
        <input type="submit" value="Submit!">
    </form>

    """

@app.route('/message_results', methods=['POST'])
def message_results():
    user_secret_message = request.form['message']
    print (f'Here\'s your secret message!')
    return sort_letters(user_secret_message)






@app.route('/calculator')
def calculator():
    return render_template('calculator_form.html')

@app.route('/calculator_results')
def calculator_results():
    operation = request.args.get('operation')
    #Gets operation
    number1 = request.args.get('operand1')
    number2 = request.args.get('operand2')
    #Gets numbers
    if operation == "add":
        result = (int(number1) + int(number2))
    elif operation == "subtract": 
        result = (int(number1) - int(number2))
    elif operation == "multiply":
        result = (int(number1) * int(number2))
    else:
        result = (int(number1) / int(number2))

    #Refactoring with context dictionary 

    context = {
        'operation': operation,
        'number1': number1,
        'number2': number2,
        'result': result
    }

    return render_template('calculator_results.html', **context)












HOROSCOPE_PERSONALITIES = {
    'aries': 'Adventurous and energetic',
    'taurus': 'Patient and reliable',
    'gemini': 'Adaptable and versatile',
    'cancer': 'Emotional and loving',
    'leo': 'Generous and warmhearted',
    'virgo': 'Modest and shy',
    'libra': 'Easygoing and sociable',
    'scorpio': 'Determined and forceful',
    'sagittarius': 'Intellectual and philosophical',
    'capricorn': 'Practical and prudent',
    'aquarius': 'Friendly and humanitarian',
    'pisces': 'Imaginative and sensitive'
}






@app.route('/horoscope')
def horoscope_form():
    """Shows the user a form to fill out to select their horoscope."""
    return render_template('horoscope_form.html')





@app.route('/horoscope_results')
def horoscope_results():
    """Shows the user the result for their chosen horoscope."""

    # TODO: Get the sign the user entered in the form, based on their birthday
    horoscope_sign = request.args.get('horoscope_sign')

    # TODO: Look up the user's personality in the HOROSCOPE_PERSONALITIES
    # dictionary based on what the user entered
    users_personality = HOROSCOPE_PERSONALITIES[horoscope_sign]

    # TODO: Generate a random number from 1 to 99
    lucky_number = random.randint(1, 99)

    #Should have been a ToDo for Usersname
    users_name = request.args.get('users_name')

    context = {
        'users_name': users_name,
        'horoscope_sign': horoscope_sign,
        'personality': users_personality, 
        'lucky_number': lucky_number
    }

    return render_template('horoscope_results.html', **context)

if __name__ == '__main__':
    app.config['ENV'] = 'development'
    app.run(debug=True)
