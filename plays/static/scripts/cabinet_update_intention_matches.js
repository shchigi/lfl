
$(window).unload(function(){

    var inputs = $('.onoffswitch-checkbox');
    var values = [];
    var values2 = {};

    console.log(values);

    inputs.each(function() {
            values.push($(this).prop("checked"));
            values2[$(this).attr('id')] = $(this).prop("checked");
        }
    );

    console.log(values);
    console.log(values2);

    $.ajax({
        type: 'POST',
        url: 'https://y2g6enni1422.runscope.net',
        async: false,
        data: values2
    });
    

});