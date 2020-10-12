from flask import Flask,request,jsonify,redirect,render_template
import requests
webui=Flask(__name__)
@webui.route("/graph",methods=["GET","POST"])
def create():
    if request.method=="POST":
        if request.form["submit"]=="find_graph":
            response=requests.get("http://825cf6964a7d.ngrok.io/display")
            data=response.json()
            return render_template("results.html",list=data)
        elif request.form["submit"]=="create":
            name=request.form["name"]
            id=request.form["empid"]
            if(name=="" or id==""):
                return("Please enter the values for employee id or name")
            else:
             response=requests.get("http://825cf6964a7d.ngrok.io/create/"+name+"&"+id)
             return(response.text)



    
    else:
     return render_template("graph.html")

if __name__=="__main__":
    webui.run(port=5002)