from flask import Flask,request
#create app with Flask
app=Flask(__name__)

#use python app decorator to create api route
# '\api' specifies the end point and methods specify that it will be used for 
# POST requests
@app.route('/api',methods={'POST'})

def say_hello():
    #data sent as json so we use get_json to extract input
    data=request.get_json(force=True)
    #extract name variable from data 
    name=data['name']
    return "hello {0}".format(name)
#main block i.e Entry point of script
if __name__=='__main__':
    # run function used to start Flask app at port 10001 and debug= True to get stacktrace
    app.run(port=10001,debug=True)