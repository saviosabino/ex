$(document).ready(function() {
    $('input').focus();
    $('button').click(function(){
        var val = $('input').val();
        $('ul').append('<li class="item">'+val+'</li>');
        $('input').val('');
        $('input').focus();
    });
    $(document).on('click','.item', function(){
        $(this).remove();
    });
});
