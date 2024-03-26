from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def generate_band_name():
    band_name = ""
    if request.method == 'POST':
        # Correctly extract form data for name and favorite place
        name = request.form['name']
        place = request.form['place']  # This is the correct way to access the "place" input
        
        # Generate a band name using the first two letters of each input
        name_part = name[:2] if len(name) >= 2 else name
        place_part = place[:3] if len(place) >= 3 else place
        
        # Combining the parts to form the band name
        band_name = name_part + place_part
        
        # Capitalize the first letter of the band name
        band_name = band_name.capitalize()
              
    return render_template('home.html', band_name=band_name)
if __name__ == '__main__':
    app.run(debug=True)
