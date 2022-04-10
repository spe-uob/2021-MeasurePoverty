// 回到顶部
$(window).scroll(function () {
    if ($(window).scrollTop() > 200) {
        $("#goTop").fadeIn(200);
    } else {
        $("#goTop").fadeOut(200);
    }
});
//当点击回到顶部后，回到页面顶部位置
$("#goTop").click(function () {
    $('body,html').animate({
            scrollTop: 0
        },
        500);
    return false;
});