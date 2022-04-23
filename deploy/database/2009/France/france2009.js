import { initializeApp } from 'https://www.gstatic.com/firebasejs/9.6.10/firebase-app.js'
// Import the functions you need from the SDKs you need
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

/*
var firebaseRef2 = firebase.database().ref("English2009")
firebaseRef2.on("value" , function(snapshot){
    snapshot.forEach(function(element){
        document.querySelector('#QID').innerHTML += `
        <div>${element.val()}</div>
                      `
    });
})
*/