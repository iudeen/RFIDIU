import pyrebase


config = {
  "apiKey": "AIzaSyBnHCRXLdDQgAAstsDPwhyCRgKqkphD5s8",
  "authDomain": "rfidiudeen.firebaseapp.com",
  "databaseURL": "https://rfidiudeen.firebaseio.com",
  "storageBucket": "rfidiudeen.appspot.com"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

    
def getdata(name):
    
    n = db.child(name).child("Name").get()
    amnt = db.child(name).child("amnt").get()
    nm = db.child(name).child("Number").get()
    if(n.val() == None):
        
        print("No such data Found")
        erract()
            
            
    else:
        return n.val(),amnt.val(), nm.val()


def edtdata(name, amnt):
    db = firebase.database()
    db.child(name).update({"amnt":amnt})

def dispdata(id1):
    myname, myamnt, mynum = getdata(id1)
    print("Name: ",myname)
    print("Amount: ",myamnt)
    print("Number: ",mynum)    

def calltoll(id1):
    myname, myamnt, mynum = getdata(id1)
    ##        print(myamnt)
    dispdata(id1)
    newamnt = myamnt - 10
    edtdata(id1, newamnt)
    print("After Editing Data",'\n')
    dispdata(id1)
    return "ok"
    
            

def erract():
    print("Please Try again")
    
    


    
