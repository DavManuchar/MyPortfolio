button = false

function ValidateEmail() {
  code = document.getElementById('code').value


  if (code.length == 6 ) {
    button = true
  }

}
$("#btn").click(function () {
  if(button == true){
    code = document.getElementById('code').value

    $.ajax({
      url: '../exom/regist_ex.php',
      method: 'POST',
      data: {action: 'code_ex', code: code},
      success: function (data) {
        data = JSON.parse(data)
        if (data.success == false){
          $('#nname').html(`<span class="error">Wrong code</span>`)
        }
        else{
          document.location = '../index.php'
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