 //https://www.youtube.com/watch?v=KnAsYNhI_CY
        //javascript part to fill in the table

        var QID = 0;
        var tbody = document.getElementById('tbody1');

        function AddItemToTable(english, foreign) {
            let trow = document.createElement("tr");
            let td1 = document.createElement('td');
            let td2 = document.createElement('td');
            let td3 = document.createElement('td');

            td1.innerHTML= ++QID;
            td2.innerHTML= english;
            td3.innerHTML= foreign;


            trow.appendChild(td1);
            trow.appendChild(td2);
            trow.appendChild(td3);

            tbody.appendChild(trow);
           // body.appendChild(trow);
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
        import { getDatabase, ref, child, onValue, get }
        from "https://www.gstatic.com/firebasejs/9.6.11/firebase-database.js";
        const db = getDatabase();

         //adding items to the table, this function is fine
        function AddAllItemsToTable(Question){    
            QID =0;
            tbody.innerHTML="";
            Question.forEach(element => {
                AddItemToTable(element.english, element.estonian)
            });
        }
        //working on everything else below here

        //getting data once
        function GetAllDataOnce() {
            const dbRef = ref(db);

            get(child(dbRef, "Estonia_2009"))
            .then((snapshot)=>{
                var questions =[];
                
                snapshot.forEach(childSnapshot => {
                    questions.push(childSnapshot.val());
                });
                AddAllItemsToTable(questions);
            });
        }


        window.onload = GetAllDataOnce;