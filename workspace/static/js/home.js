$('#removeModal').on('show.bs.modal', function (event) {
    var button = $(event.relatedTarget) // Button that triggered the modal
    var content = button.data('whatever') // Extract info from data-* attributes
    var modal = $(this)
    modal.find('.modal-title').text('確認刪除'+content)
  });
  
    $(function () {
      $('#myList a:first-child').tab('show')
    });
  
  
  // Example starter JavaScript for disabling form submissions if there are invalid fields
  (function() {
    'use strict';
    window.addEventListener('load', function() {
      // Fetch all the forms we want to apply custom Bootstrap validation styles to
      var forms = document.getElementsByClassName('needs-validation');
      // Loop over them and prevent submission
      var validation = Array.prototype.filter.call(forms, function(form) {
        form.addEventListener('submit', function(event) {
          if (form.checkValidity() === false) {
            event.preventDefault();
            event.stopPropagation();
          }
          form.classList.add('was-validated');
        }, false);
      });
    }, false);
  })();
  
  $(function(){
    var $win = $(window);
    var $backToTop = $('.js-back-to-top');
    
    $win.scroll(function(){
      if($win.scrollTop() > 200){
        $backToTop.show();  
      } else {
        $backToTop.hide(); 
      }
    });
    $backToTop.click(function(){
      $('html, body').animate({scrollTop: 0}, 1000);
    });
  });
  
  