console.log("Hello World");

const submitButton = document.getElementById('submit-button');

submitButton.addEventListener('click', event => {
  if (filled === 3) 
  alert("Thanks for sharing " + input2.value + "!")
});

let filled = 0; 

//check if there is email

const input = document.getElementById('email');

 input.onblur = function() {
  if (!input.value.includes('@')) { // not email
    input.classList.add('invalid');
    error.innerHTML = 'Please enter a correct email.'
  } else {
  filled ++;
}
};

input.onfocus = function() {
  if (this.classList.contains('invalid')) {
    input.classList.remove('invalid');
    error.innerHTML = "";
  } 
};


//Check if there is a name

const input2 = document.getElementById('yourname');

input2.onblur = function() {
  if (input2.value == "") { // not name
    input2.classList.add('invalid');
    error2.innerHTML = 'Please enter a name.'
  } else 
  {   
    filled ++; 
  }
};

input2.onfocus = function() {
  if (this.classList.contains('invalid')) {
    this.classList.remove('invalid');
    error2.innerHTML = "";
  }
};


//Check if there is a message 

const input3 = document.getElementById('query');


input3.onblur = function() {
  if (input3.value == "") { // not message
    input3.classList.add('invalid');
    error3.innerHTML = 'Please enter a message.'
  } else {
      filled ++;
     }
};

input3.onfocus = function() {
  if (this.classList.contains('invalid')) {
    this.classList.remove('invalid');
    error3.innerHTML = "";
  }
};