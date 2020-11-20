$(document).ready(function() {
    $('.tab_menu_btn').on('click', function () {
        //버튼 색 제거,추가
        $('.tab_menu_btn').removeClass('on');
        $('.alert').hide();
        $(this).addClass('on')

        //컨텐츠 제거 후 인덱스에 맞는 컨텐츠 노출
        var idx = $('.tab_menu_btn').index(this);

        $('.tab_box').hide();
        $('.tab_box').eq(idx).show();
    });

    $(function () {
      $("#datepicker").datepicker();
    });

//     $(function () {
//     $('#keywordCompareForm').submit(function () {
//         alert('수집을 시작합니다 분석결과는 결과보기에서 확인해주세요')
//
//     });
// });
});
