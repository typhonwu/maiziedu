
function do_ajax(){
    var word=$('#word').val();
    if(word!=''){
            $.get('/search/',{'word':word},function(data){
                var str =''
                $.each($.parseJSON(data),function(k,v){
                     str +='<li id="this_li" onclick="fun(this)">'+v.fields.word_value+'<li>';
                });
                if(str!=''){
                    $('#drop_down').css('display','block');
                    $('#word_txt').html(str)
                }else{
                    $('#drop_down').css('display','none');
                }
            })
    }
}
function fun(obj){
    $("#word").val($(obj).html());
    $('#drop_down').css('display','none');
}