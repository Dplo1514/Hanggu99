
function hey() {
    $.ajax({
        type: "GET",
        url: "/test?title_give=봄날은간다",
        data: {},
        success: function (response) {
            alert(response)
        }
    })
}

function hey2() {
    $.ajax({
        type: "POST",
        url: "/test",
        data: {
            title_give: '봄날은간다'
        },
        success: function (response) {
            alert(response)
        }
    })
}
