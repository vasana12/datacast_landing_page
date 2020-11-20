$(document).ready(function() {
	$('button').keydown(function(e) {
		if (e.which == 13)
		{
			$('form').submit();
		}
	});
});

function login() {
	if (!$('#username').val())
	{
		alert("아이디를 입력해 주시기 바랍니다.");
		alert("씨발");

	}
	if (!$('#password').val()) {
		alert("비밀번호를 입력해 주시기 바랍니다.");
	}

	$('#login_form').submit();
}