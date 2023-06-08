from flask import Flask, url_for, render_template, request

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    return render_template('home.html')

@app.route("/response", methods=['GET', 'POST'])
def render_response():
    if request.method == 'POST': 
        hotel = request.form['hotel'] 
        if hotel == 'BeachHotel':
            reply1 = "A great Beachside hotel is the Hilton Santa Barbara Beachfront Resort."
        if hotel == 'DowntownHotel':
            reply1 = "A great downtown hotel is Hotel Californian."
        if hotel == 'GoletaHotel':
            reply1 = "A great Goleta hotel is the Ritz-Carlton Bacara."
        if hotel == 'MontecitoHotel':
            reply1 = "A great Montecito hotel is the Rosewood Mirmar Beach"
        
        
        restaurant = request.form['restaurant'] 
        if restaurant == 'Italian':
            reply2 = "A great Italian restaurant is Ca' Dario."
        if restaurant == 'Japanese':
            reply2 = "A great Japanese restaurant is Ichiban."
        if restaurant == 'Mexican':
            reply2 = "A great Mexican Restaurant is Los Agaves."
        if restaurant == 'Seafood':
            reply2 = "A great Seafood Restraunt is The Boathouse."
            
        activity = request.form['activity'] 
        if activity == 'Exercise':
            reply3 = "A great place to exercise in Sana Barbara is the track at Santa Barbara City College."
        if activity == 'Historical':
            reply3 = "A great historical activity to do in Santa Barbara is go to the Santa Barbara Historical Museum."
        if activity == 'Artsy':
            reply3 = "A great activity in Santa Barbara if you are into art is"
        if activity == 'Nature':
            reply3 = "A great activity to do in nature in Santa Barbara is go to the Botanic Gardens."
            
    
        return render_template('response.html', response1 = reply1, response2 = reply2, response3 = reply3)
    
if __name__=="__main__":
    app.run(debug=False)
