from website import create_app

app = create_app()

if __name__ == '__main__': # make sures the execution is when we want it by forcing it with an if statement
    app.run(debug=True) # everytime we make a change it will automatically restarts the web server