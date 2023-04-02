from flask import Flask,render_template, request, session, url_for,redirect
import sqlite3



app=Flask(__name__)
app.secret_key="12345"

@app.route("/",methods=['GET','POST'])
def Home():
      if request.method =='POST':
         search=request.form['search']
         conn=sqlite3.connect("D://Python//SQLite//Image_store.db")
         cur=conn.cursor()
         cur.execute("SELECT * FROM dietRecord where name=?",[search])
         conn.row_factory=sqlite3.Row
         res=cur.fetchone()
         conn.commit()
         conn.close()
         if res:
           session['protein']=res[2]
           session['carbo']=res[3]
           session['fat']=res[4]
           session['vitamins']=res[5]
           session['bp']=res[6]
           session['calories']=res[7]
           session['testrone']=res[8]
           session['detail']=res[10]
           with open("D://Python//Flask-Projects//Flask in Dietry system//static//empty.jpg",'wb') as f:
             f.write(res[9])
      return render_template("FitOne.html")

@app.route('/insert',methods=['GET','POST'])
def insert():
     if request.method == 'POST':
        pid=request.form['id']
        pname=request.form['name']
        protein=request.form['protein']
        carbo=request.form['carbo']
        fat=request.form['fat']
        vitamin=request.form['vitamin']
        bp=request.form['bp']
        calories=request.form['calories']
        testrone=request.form['testrone']
        detail=request.form['detail']
        filename=request.form['image']
        filename=f"C://fakepath//{filename}"  
        photo_img=0
        with open(filename,'rb') as file:
          photo_img=file.read()
         


        conn=sqlite3.connect("D://Python//SQLite//Image_store.db")
        cur=conn.cursor()
        cur.execute("INSERT INTO dietRecord VALUES(?,?,?,?,?,?,?,?,?,?,?)",(pid,pname,protein,carbo,fat,vitamin,bp,calories,testrone,photo_img,detail))
        conn.commit()
        conn.close()
        return redirect(url_for("Home"));

     return render_template('index.html')
        

if __name__ == "__main__":
    app.run(debug=True)