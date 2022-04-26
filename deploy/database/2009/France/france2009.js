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


// youtube link: https://www.youtube.com/watch?v=H8frPNjKSC8
// Initialize Firebase
firebase.initializeApp(firebaseConfig);
var firebaseRef = firebase.database().ref("QuestionIDs")
firebaseRef.on("value" , function(snapshot){
    snapshot.forEach(function(element){
        document.querySelector('#englishQuestions').innerHTML += `
               <div>${element.val()}</div>
               `
    });
})


var firebaseRef2 = firebase.database().ref("QuestionIDs")
firebaseRef2.on("value" , function(snapshot){
    snapshot.forEach(function(element){
        document.querySelector('#questionID').innerHTML += `
        <div>${element.key}</div>
                      `
    });
})

var firebaseRef3 = firebase.database().ref("France-2009")
firebaseRef3.on("value" , function(snapshot){
    snapshot.forEach(function(element){
        document.querySelector('#frenchQuestions').innerHTML += `
        <div>${element.val()}</div>
                      `
    });
})
//this point onwards is table
var stdNo = 0;
var tbody = document.getElementById('tbody1');


function AddItemToTable(hi, how, are, you) {
    let trow = document.createElement("trow");
    let td1 = document.createElement("td");
    let td2 = document.createElement("td");
    let td3 = document.createElement("td");
    let td4 = document.createElement("td");
    let td5 = document.createElement("td");

    td1.innerHTML= ++stdNo;
    td2.innerHTML= hi;
    td3.innerHTML= how;
    td4.innerHTML= are;
    td5.innerHTML= you;

    trow.appendChild(td1);
    trow.appendChild(td2 );
    trow.appendChild(td3);
    trow.appendChild(td4);
    trow.appendChild(td5);
}

function AddAllItemsToTable(QuestionIDs) {
    stdNo=0;
    tbody.innerHTML="";
    QuestionIDs.forEach(element => {
        AddItemToTable(element.var())
    });
}

// getting all data

function GetAllDataOnce() {
    const dbRef = ref(db);
    get(child(dbRef, "QuestionIDs"))
    .then((snapshot)=> {
        var hi =[];
        snapshot.forEach(childSnapshot => {
            students.push(childSnapshot.val())  ;
        });
        AddAllItemsToTable(hi)
    });
}

window.onload = GetAllDataOnce