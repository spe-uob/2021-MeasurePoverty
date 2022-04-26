
var stdNo = 0;
var tbody = document.getElementById('tbody1');


function AddItemToTable(name, roll, sec, gen) {
    let trow = document.createElement("tr");
    let td1 = document.createElement('td');
    let td2 = document.createElement('td');
    let td3 = document.createElement('td');
    let td4 = document.createElement('td');
    let td5 = document.createElement('td');

    td1.innerHTML= ++stdNo;
    td2.innerHTML= name;
    td3.innerHTML= how;
    td4.innerHTML= are;
    td5.innerHTML= you;

    trow.appendChild(td1);
    trow.appendChild(td2);
    trow.appendChild(td3);
    trow.appendChild(td4);
    trow.appendChild(td5);

    tbody.appendChild(trow);
}

function AddAllItemsToTable(QuestionIDs) {
    stdNo=0;
    tbody.innerHTML="";
    QuestionIDs.forEach(element => {
        AddItemToTable(element.QuestionIDs);
    });
}
import { initializeApp } from "https://www.gstatic.com/firebasejs/9.6.11/firebase-app.js";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
const firebaseConfig = {
  apiKey: "AIzaSyASZ59fobXr6ovy8QQUX2mogFso22v5nQM",
  authDomain: "measuredb.firebaseapp.com",
  databaseURL: "https://measuredb-default-rtdb.firebaseio.com",
  projectId: "measuredb",
  storageBucket: "measuredb.appspot.com",
  messagingSenderId: "298611251603",
  appId: "1:298611251603:web:0d236cfa7d1926a552f066"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);  
import {getDatabase, ref, child, onValue, get}
from "https://www.gstatic.com/firebasejs/9.1.1/firebase-database.js";
//getting all data

function GetAllDataOnce() {
    const dbRef = ref(db);
    get(child(dbRef, "QuestionIDs"))
        .then((snapshot)=> {
            
            var students =[];
            
            snapshot.forEach(childSnapshot => {
                students.push(childSnapshot.val());
            });
            AddAllItemsToTable(students);
        })
}

function GetAllDataRealTime() {
    const dbRef = ref(db);

    onValue(dbRef, (snapshot)=>{
        var students =[];
            
            snapshot.forEach(childSnapshot => {
                students.push(childSnapshot.val());
            });
            AddAllItemsToTable(students);
    });
    
}


window.onload = GetAllDataOnce;