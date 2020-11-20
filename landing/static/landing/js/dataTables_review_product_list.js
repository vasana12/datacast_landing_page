$(document).ready(function() {


    var table = $('#reivew_product_list').DataTable( {
          "lengthMenu": [[5, 10,25,50,-1], [5,10, 25, 50, "All"]],
          "columnDefs": [
              {orderable: false,
                  className : 'select-checkbox',
                  targets:0
              },
          { "width": "5%", "targets": 1},
              {"sortable":false, "targets":1}
          ],
        select:{
              style: 'multi',
            selector : 'td:first-child'
        },
        "order":[[2,"asc"]],//column indexes is zero based
        'info': false,
        colReorder: true,
        dom:'<"top"B>rt<"bottom"ip>',
            buttons: [
                'pageLength',
        {
            extend: 'excel',
            text: '엑셀출력',
            filename: 'review_list',
            title: 'review_list',


        },
        {
            extend: 'copy',
            text: '클립보드 복사',
            title: 'review_list',

        },
        {
            extend: 'csv',
            text: 'csv출력',
            filename: 'review_list',
            title: 'review_list',

        }
    ]
    });

    // let review_product_table_id;
    // $('#reivew_product_list tbody tr').on('click',function(){
    //     review_product_table_id = String($(this).attr('itemid'))
    //
    // })

    $('#reviewRequestCreateForm').submit(function(e){
        //preventDefault 로 페이지 이동 못하도록 설정
        e.preventDefault()
        //데이터 전달할 열의 데이터의 id를 저장할 리스트 초기화 설정
        var obj_dict_list = [];

        //form의 action=""에 있는 경로를 url 이라는 변수로 저장
        var url = $(this).attr('action');

        var url_to_move = $(this).attr('data-url')
        var csrf_token = $('input[name="csrfmiddlewaretoken"]').val()
        //선택된 데이터의 값을 가져오기
        var dataTableRows = table.rows({selected:true}).data().toArray();
        for (var i = 0; i < dataTableRows.length; i++) {
            dataTableRows[i] = dataTableRows[i].slice(1, dataTableRows[i].length);
            // var review_product_table_id = String(dataTableRows[i]).split(',').reverse()[2]
            var productID = String(dataTableRows[i]).split(',').reverse()[1]
            var productLink = String(dataTableRows[i]).split(',').reverse()[0]

                obj_dict_list.push(JSON.stringify({productID: productID, productLink:productLink}))
        }

        jQuery.ajaxSettings.traditional = true;
        if(obj_dict_list.length>=9999)
        {
                    $.ajax({
                        url : url,
                        method : 'POST',
                        dataType : 'json',
                        data: {
                        //    리스트 형태로 보낼 때는 변수 뒤에 '[]' 입력
                            'obj_dict_list[]': obj_dict_list,
                            'csrfmiddlewaretoken':csrf_token,
                            'is_ajax': true,
                        },
                    //    서버쪽으로 데이터 전달 및 수신 성공 시, html 단에서 실행할 코드 입력
                            }).done(function(data){
                                if(data.works){
                                    alert('수집 요청 완료되었습니다.');
                                    var move = confirm('결과보기 페이지로 이동하겠습니까?')
                                    if(move === true){
                                    //    사용자가 결과보기 페이지로 이동 희망 시, 특정 url 경로로 이동
                                    window.location.href = url_to_move.toString()
                                    }
                                //사용자가 결과보기 페이지 이동 미희망 시, 해당 페이지 새로고침
                                else{
                                    location.reload()
                                    }
                                }
                            });
        }
        else{
            alert('서비스 준비중 입니다.');
        }
        return false;
    });
});


    //체크확인 버튼 눌렀을 때의 이벤트

    // $(".dt-button").click(function(){
    // $('<table>')
    // .append(
    //      $("#keyword_view_table thead").html()
    //  )
    //  .append(
    //     $("#keyword_view_table").DataTable().$('tr').clone()
    //  )
    //  .table2excel({
    //     exclude: "",
    //     name: "casting",
    //     filename: "keyword_buzz.xls"
    //  });
    // });
