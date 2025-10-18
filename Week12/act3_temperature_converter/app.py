from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def convert_temperature():
    result = None
    temp = None
    original_unit = None
    target_unit = None
    if request.method == 'POST':
        try:
            temp = float(request.form['temperature'])
            conversion = request.form['conversion_type']

            if conversion == 'C_to_F':
                result = f"{(temp * 9/5) + 32}"
                original_unit = "°C"
                target_unit = "°F"
            elif conversion == 'F_to_C':
                result = f"{(temp - 32) * 5/9}"
                original_unit = "°F"
                target_unit = "°C"
            elif conversion == 'C_to_K':
                result = f"{temp + 273.15}"
                original_unit = "°C"
                target_unit = "K"
            elif conversion == 'K_to_C':
                result = f"{temp - 273.15}"
                original_unit = "K"
                target_unit = "°C"
            elif conversion == 'F_to_K':
                result = f"{(temp - 32) * 5/9 + 273.15}"
                original_unit = "°F"
                target_unit = "K"
            elif conversion == 'K_to_F':
                result = f"{(temp - 273.15) * 9/5 + 32}"
                original_unit = "K"
                target_unit = "°F"
        except ValueError:
            result = "Invalid input. Please enter a numeric value."
    return render_template('index.html', result=result, original_unit=original_unit, target_unit=target_unit)

if __name__ == "__main__":
    app.run(debug=True)

