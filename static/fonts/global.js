// logout event
document.querySelector('.logout').addEventListener('click', showLogout);

function showLogout(e){
  e.preventDefault();

  swal({
    title: "Are you sure?",
    text: "You will be logged out!",
    icon: "warning",
    buttons: {
      cancel: true,
      confirm: "confirm",
    },
    dangerMode: true,
  })
  .then((willDelete) => {
    if (willDelete) {
      swal("You have been successfully logged out, see you soon!", {
        icon: "success",
      });
      setTimeout(function(){
        window.location = '/accounts/logout/';
      }, 3000);
    } else {
      // swal("Your imaginary file is safe!");
    }
  });
}
// end logout function
