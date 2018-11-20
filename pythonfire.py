from firebase import firebase

firebase = firebase.FirebaseApplication('https://okupyd.firebaseio.com/', None)
seats = 'seats'
buildingID = 'ChIJSXFbmjAJZ0gRtYltUXsp3YA'
roomID = 'A'
seatID = '1'
def updateDB(var):
    result = firebase.put(seats+'/'+buildingID+'/'+roomID+'/'+seatID,"occupied", var)
#print(result)
updateDB(0)
print("updatedDB")
