$(document).ready(function () {
    $('form input').tooltip({
      placement: 'top',
      trigger: 'focus',
      title: function (){
        return $(this).attr('placeholder');
      }
    });
});