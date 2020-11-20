$(document).ready(function() {
    // $('table.display').DataTable();
    $('#analysis_list').DataTable(
        {
        "info": false,
            select: {
            style: 'single',

        },
    });

    $('#analysis_list tbody').on('click','tr',function(){
        var td = $(this).children('.status');
        var status = td.text()
        var url = $(this).attr('data-url')
        if (status==='분석요청' || status==='분석중'){
            alert('분석이 완료될까지 잠시만 기다려 주세요')
            return false
        }
        if (status==='분석불가'){
            alert('분석 키워드를 다시 설정해 주세요')
            return false
        }
        else
            {
            location.href=url.toString()
        }

    });

    $('#analysis_list_period').DataTable({
        "info":false,
        select: {
            style: 'single',
        }
    });

    $('#analysis_list_period tbody').on('click','tr',function(){
        var td = $(this).children('.status');
        var status = td.text()
        var url = $(this).attr('data-url')
        if (status==='분석요청' || status==='분석중'){
            alert('분석이 완료될까지 잠시만 기다려 주세요')
            return false
        }
        if (status==='분석불가'){
            alert('분석 키워드를 다시 설정해 주세요')
            return false
        }
        else
            {
            location.href=url.toString()
        }

    });



    // $('#frm_analysis_result').submit(function(e){
    //     url = $(this).attr('action');
    //     var result_url = "{% url 'landing:boards_result'}"
    //     var dataTableRows = table.rows({selected:true}).data().toArray();
    //     var arrTableSelectedRowsRendered = [];
    //     if (dataTableRows.length==0){
    //         //분석완료된것만 볼 수 있게 해줘야함. 분석 중, 분석요청은 기다려야함
    //         alert('분석 대상을 1개 이상 선택해주세요')
    //         return false;
    //     }
    //     else{
    //     for (var i = 0; i < dataTableRows.length; i++) {
    //         dataTableRows[i] = dataTableRows[i].slice(1, dataTableRows[i].length);
    //         arrTableSelectedRowsRendered.push(dataTableRows[i].slice(0, dataTableRows[i].length))
    //         // alert(dataTableRows.split(',').reverse()[0])
    //     }
    //     dataTableRows_id = String(dataTableRows[0]).split(',').reverse()[0]
    //
    //     // alert('rows_selected:',rows_selected)
    //
    //     jQuery.ajaxSettings.traditional = true;
    //     $.ajax({
    //         url : url,
    //         method : 'POST',
    //         data:{
    //             'obj_id_list[]' : arrTableSelectedRowsRendered,
    //             'is_ajax':true,
    //         },
    //
    //     }).done(function(data){
    //         alert('신청이 완료되었습니다.');
    //         location.href= result_url
    //     });
    //     return false
    //     }
    // });
});
