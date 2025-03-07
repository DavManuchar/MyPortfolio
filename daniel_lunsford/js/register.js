var pasww = false
var mailww = false
var numm = false
var rpas = false
var button = false

var inputText = document.getElementById('email')
var n = document.getElementById('phone')
var pass = document.getElementById('password')

function ValidateEmail() {
  var rpass = document.getElementById('repeat_password')

  var mailformat = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
  var phone = /^[\+]?\d{2,}?[(]?\d{2,}[)]?[-\s\.]?\d{2,}?[-\s\.]?\d{2,}[-\s\.]?\d{0,9}$/im
  if (inputText.value.match(mailformat)) {
    inputText.style.border = '1px solid green'
    inputText.style.color = 'green'
    mailww = true
  }
  else {
    inputText.style.border = '1px solid red'
    inputText.style.color = 'red'
    mailww = false
  }
  if (n.value.match(phone)) {
    n.style.border = '1px solid green'
    n.style.color = 'green'
    numm = true
  }
  else {
    n.style.border = '1px solid red'
    n.style.color = 'red'
    numm = false
  }


  if (pass.value.length > 7 && pass.value.length < 16) {
    pass.style.border = '1px solid green'
    pass.style.color = 'green'
    pasww = true
  }
  else {
    pass.style.border = '1px solid red'
    pass.style.color = 'red'
    pasww = false
  }
  if (rpass.value == pass.value && rpass.value.length != 0) {
    rpass.style.border = '1px solid green'
    rpass.style.color = 'green'
    rpas = true
  }
  else {
    rpass.style.border = '1px solid red'
    rpass.style.color = 'red'
    rpas = false
  }

  if (mailww == true && numm == true && pasww == true && rpas == true) {
    button = true
  }
  
}

$("#btn").click(function () {
  if(button == true){
    $.ajax({
      url: '../exom/regist_ex.php',
      method: 'POST',
      data: { action: 'register', mail: inputText.value, phone: n.value, password: pass.value, out: true},
      success: function (data) {
        data = JSON.parse(data)
        if (data.success == false){
          inputText.style.border = '1px solid red'
          inputText.style.color = 'red'
          $('#nname').html(`<span class="error">Email taken</span>`)
        }
        else{
          document.location = '../exom/verif.php'
        }
      }
    });
  }else{
    ValidateEmail()
  }

}) 


$("input").on("change input", function () {
  ValidateEmail()
});