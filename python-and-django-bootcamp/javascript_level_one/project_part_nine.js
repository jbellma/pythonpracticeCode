var firstName = prompt("Hello and Welcome. Please enter your Fisrt Name:");
var secondName = prompt("Please enter your Second Name :");
var age = prompt("How old are you?");
var height = prompt("How tall are you?")
var petName = prompt("Please enter your Pet's Name :");
alert("Thank you so much for the information.");

if(firstName[0] === "J"){
  if (secondName[0] === "J"){
    if (age > 20 && age < 30){
      if(height >= 170){
          if (petName[petName.length -1] === "y"){
            console.log("Welcome Secret Agent.");
          }
      }
    }
  }
}
