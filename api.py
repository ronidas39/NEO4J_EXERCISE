from flask import Flask,request,jsonify,redirect,render_template
from neo4j import GraphDatabase
import csv

#establish the connection with bolt 
with open("cred.txt") as f1:
    data=csv.reader(f1,delimiter=",")
    for row in data:
        username=row[0]
        pwd=row[1]
        uri=row[2]
    f1.close()
driver=GraphDatabase.driver(uri=uri,auth=(username,pwd))
session=driver.session()
api=Flask(__name__)
@api.route("/create/<string:name>&<int:id>",methods=["GET","POST"])
def create_node(name,id):
    q1="""
    create (n:Employee{NAME:$emp_name,EMP_ID:$emp_id})
    """
    map={"emp_name":name,"emp_id":id}
    try:
     session.run(q1,map)
     return(f"Employee node created with NAME = {name} & EMPLOYEE ID = {id}")
    except Exception as e:
        return (f"Error occured with {str(e)}")

@api.route("/display",methods=["GET","POST"])
def display():
 q1="""
 match(n) return n.NAME as NAME , n.EMP_ID as EMP_ID
 """
 results=session.run(q1)
 data=results.data()
 

 return jsonify(data)






if __name__=="__main__":
    api.run(port=5000)

