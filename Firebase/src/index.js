// import (som på python)
import {initializeApp} from "firebase/app"
import { 
    getFirestore, collection, getDocs,
    addDoc, deleteDoc, doc
} from "firebase/firestore"


// som nyckel till firebase
const firebaseConfig = {
    apiKey: "AIzaSyCbnXjnCHp3LFdjTC24OrAKFmYKZCPKyeA",
    authDomain: "fir-first-tutorial-f69d2.firebaseapp.com",
    projectId: "fir-first-tutorial-f69d2",
    storageBucket: "fir-first-tutorial-f69d2.appspot.com",
    messagingSenderId: "903508611279",
    appId: "1:903508611279:web:965aa1aa27c97c0c1be7ba"
  };


 // en app liknande vue som öppnar dörren till firebase
 // kallas för init firebase app
  initializeApp(firebaseConfig)

  // db för database och är en representation av firebase sidan
  // init services
const db = getFirestore()


  // importar books från db med collection func
  // collection ref
const colRef = collection(db, 'books')
  
  // hämtar innehåll i books
  // get collection data
getDocs(colRef).then((snapshot) => {
    let books = []
    snapshot.docs.forEach((doc) => {
      books.push({...doc.data(), id:doc.id })
    });
    console.log(books)
})
.catch(err => {
  console.log(err.messagingSenderId)
})

// adding documents
const addBookForm = document.querySelector(".add") 
addBookForm.addEventListener("submit", (e) => { 
  e.preventDefault()

  addDoc(colRef, {
    title: addBookForm.title.value, 
    author: addBookForm.author.value,
  })
  .then(() => {
    addBookForm.reset()  
  })

})

const deleteBookForm = document.querySelector(".delete")
deleteBookForm.addEventListener("submit", (e) => {
  e.preventDefault()

  const docRef = doc(db, "books", deleteBookForm.id.value)

  deleteDoc(docRef)
  .then(() => {
   deleteBookForm.reset() 
    
  }) 
})