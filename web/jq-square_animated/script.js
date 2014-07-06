$(document).ready(function() {
   $('div').mouseenter(function() {
       $(this).animate({
           height: '+=30px'
       });
   });
   $('div').mouseleave(function() {
       $(this).animate({
           height: '-=30px'
       }); 
   });
   $('div').click(function() {
       $(this).toggle(1000);
   }); 
});
