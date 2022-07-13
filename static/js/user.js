function is_nickname(asValue) {
    var regExp = /^(?=.*[a-zA-Z])[-a-zA-Z0-9_.]{2,10}$/; //정규표현식. 컴퓨터에게 규칙을 알려줌
    return regExp.test(asValue);
}

function is_password(asValue) {
    var regExp = /^(?=.*\d)(?=.*[a-zA-Z])[0-9a-zA-Z!@#$%^&*]{8,20}$/;
    return regExp.test(asValue);
}

function sign_in() {
    let username = $("#input-email").val()
    let password = $("#input-password").val()
    console.log(username, password)

    if (username == "") {
        $("#help-id-login").text("아이디를 입력해주세요.")
        $("#input-email").focus()
        return;
    } else {
        $("#help-id-login").text("")
    }

    if (password == "") {
        $("#help-password-login").text("비밀번호를 입력해주세요.")
        $("#input-password").focus()
        return;
    } else {
        $("#help-password-login").text("")
    }
    $.ajax({
        type: "POST",
        url: "/sign_in",
        data: {
            username_give: username,
            password_give: password
        },
        success: function (response) {
            if (response['result'] == 'success') {
                $.cookie('mytoken', response['token'], {path: '/'}); // 서버로부터 받은 토큰을 쿠키에 저장
                alert("로그인 되었습니다!")
                window.location.replace("/")
            } else {
                alert(response['msg'])
            }
        }
    });
}


function sign_up() {
    let password = $("#input-password").val()
    let password2 = $("#input-password2").val()
    let address = $("#address_kakao").val()
    let username = $("#input-name").val()
    let email = $("#input-email").val()

    if (password == "") {
        $("#help-password").text("비밀번호를 입력해주세요.").removeClass("is-safe").addClass("is-danger")
        $("#input-password").focus()
        return;
    } else if (!is_password(password)) {
        $("#help-password").text("비밀번호의 형식을 확인해주세요. 영문과 숫자 필수 포함, 특수문자(!@#$%^&*) 사용가능 8-20자").removeClass("is-safe").addClass("is-danger")
        $("#input-password").focus()
        return
    } else {
        $("#help-password").text("사용할 수 있는 비밀번호입니다.").removeClass("is-danger").addClass("is-success")
    }
    if (password2 == "") {
        $("#help-password2").text("비밀번호를 입력해주세요.").removeClass("is-safe").addClass("is-danger")
        $("#input-password2").focus()
        return;
    } else if (password2 != password) {
        $("#help-password2").text("비밀번호가 일치하지 않습니다.").removeClass("is-safe").addClass("is-danger")
        $("#input-password2").focus()
        return;
    } else {
        $("#help-password2").text("비밀번호가 일치합니다.").removeClass("is-danger").addClass("is-success")
    }
    $.ajax({
        type: "POST",
        url: "/sign_up",
        data: {
            username_give: username,
            password_give: password,
            email_give: email,
            address_give: address
        },
        success: function (response) {
            alert("회원가입을 축하드립니다!")
            window.location.replace("/login")
        }
    });

}

function sign_out() {
    // user의 token을 지우면 로그아웃! jquery에서 쿠키를 삭제하는 함수.
    $.removeCookie('mytoken', {path: '/'});
    alert('로그아웃!')
    // 로그아웃 후 login 페이지로 보내준다.
    window.location.href = "/login"
}

function getUserInfo(execute) {

    $.ajax({
        type: "GET",
        url: "/getUserInfo",
        data: {},
        success: function (response) {
            execute(response)
        }
    });
}

function postUserAddr() {
    let address =  $("#address_kakao").val()
    console.log(address)
    $.ajax({
        type: "POST",
        url: "/updateAddr",
        data: {
            address_receive: address
        },
        success: function (response) {
            console.log(response)
        }
    });
}

