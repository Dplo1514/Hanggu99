function save_member() {
    let name = $('#name_input').val();
    let id = $('#id_input').val();
    let b = $('#b_input').val();

    if ($('#name_input').val() == '') {
        alert('이름을 입력해주세요.')
        return;
        }else if ($('#id_input').val() ==''){
            alert('ID를 입력해주세요')
            return;
        }else if ($('#b_input').val() ==''){
            alert('비밀번호를 입력해주세요')
            return;
        }

    $.ajax({
        type: 'POST',
        url: '/save_member',
        data: {name_give : name ,id_give : id , b_give : b},
        success: function (response) {
            alert(response['msg'])
            window.location.reload;
        }
    });
}

function login() {
    let id = $('#login_id').val();
    let b = $('#login_b').val();

    if ($('#login_id').val() ==''){
        alert('ID를 입력해주세요')
        return;
    }else if ($('#login_b').val() ==''){
        alert('비밀번호를 입력해주세요')
        return;
    }

    $.ajax({
        type: 'POST',
        url: '/login',
        data: {id_give : id , b_give : b},
        success: function (response) {
            alert("회원가입 완료!")
        }
    });
}