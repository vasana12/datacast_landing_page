$(document).ready(function() {
    $('#keyword_view_table').dataTable( {
          "columnDefs": [
            { "width": "5%", "targets": 0 }
          ],
        'info': false,
        scrollY:    '600px',
        paging:     false,
        colReorder: true,
        dom:'frtipB',
            buttons: [
        {
            extend: 'excel',
            text: '엑셀출력',
            filename: 'keyword_buzz',
            title: 'keyword_buzz',

        },
        {
            extend: 'copy',
            text: '클립보드 복사',
            title: 'keyword_buzz',

        },
        {
            extend: 'csv',
            text: 'csv출력',
            filename: 'keyword_buzz',
            title: 'keyword_buzz',

        }
    ]
    } );

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

} );
