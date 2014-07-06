// Add your JavaScript below!
$(document).ready(function(){
    $("#adate").datepicker();
    $("button").click(function(e){
        e.preventDefault();
        var adate = $('#adate').val();
        frm = document.forms['aform'];
        reqs = [];
        for(var i=0; i < frm.length; i++){
            if(frm[i].required && frm[i].value==""){
                reqs.push(frm[i].name);
            }
        }
        console.log(reqs);
        if (reqs.length > 0){
            alert('Please, fill all required fields: ' + reqs);
        } else alert('You data have been sent!');
    });
});
