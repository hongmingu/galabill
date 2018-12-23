$(function () {
    $('#nav_li_a_menu').click(function (e) {
        e.preventDefault();
        $('#modal_menu').modal('show')
    });
    var width = $(window).width();
    if (!(width >= 768)) {
        //작으면
        if (!$("#nav_div_ul_li_search").length) {
            $("#nav_div_ul_li_bsearch").after('<li id="nav_div_ul_li_search"><a class="padding_15_i" href="#" id="nav_div_ul_li_a_search"><i class="glyphicon glyphicon-search"></i></a></li>')
            $("#nav_div_ul_li_a_search").click(function () {
                if ($("#nav_search").length) {
                    $("#nav_search").remove();
                }
                else {
                    var appender = $('<nav class="navbar navbar-default navbar-fixed-top navbar_search_base top_50" id="nav_search">' +
                        '<div class="container-fluid padding_right_0 padding_left_0 desktop_display_none">' +
                        '<form class="navbar-form navbar_search_form_base width_100_i margin_auto">' +
                        '<div class="input-group input-group-sm">' +
                        '<input class="form-control" placeholder="Search" id="search_mobile_input" type="text">' +
                        '<div class="input-group-btn">' +
                        '<i class="btn btn-default" id="search_mobile_btn"><i class="glyphicon glyphicon-search"></i>' +
                        '</i>' +
                        '</div>' +
                        '</div>' +
                        '</form>' +
                        '</div>' +
                        '</nav>')
                    appender.on('keypress', function (e) {
                        if (e.keyCode === 13) {
                            var passed_value = $('#search_mobile_input').val()
                            if (passed_value.trim() === '') {
                                return false;
                            }
                            //need ajax
                            var path = '/search/all/?q=' + passed_value
                            location.href = path
                            return false;
                        }
                    })
                    appender.find('#search_mobile_btn').on('click', function (e) {
                        e.preventDefault()
                        var passed_value = $('#search_mobile_input').val()
                        if (passed_value.trim() === '') {
                            return false;
                        }
                        //need ajax
                        var path = '/search/all/?q=' + passed_value
                        location.href = path
                    })

                    $('body').append(appender)
                }
            });
        }
    }

    $(window).on('resize', function () {
        if ($(this).width() != width) {
            width = $(this).width();
            console.log(width);
            if (width >= 768) {
                if ($("#nav_search").length) {
                    $("#nav_search").remove()
                }
                if ($("#nav_div_ul_li_search").length) {
                    $("#nav_div_ul_li_search").remove()
                }
            }
            else {
                if (!$("#nav_div_ul_li_search").length) {
                    $("#nav_div_ul_li_bsearch").after('<li id="nav_div_ul_li_search"><a class="padding_15_i" href="#" id="nav_div_ul_li_a_search"><i class="glyphicon glyphicon-search"></i></a></li>\n')
                    $("#nav_div_ul_li_a_search").click(function () {
                        if ($("#nav_search").length) {
                            $("#nav_search").remove();
                        }
                        else {
                            var appender = $('<nav class="navbar navbar-default navbar-fixed-top navbar_search_base top_50" id="nav_search">' +
                                '<div class="container-fluid padding_right_0 padding_left_0 desktop_display_none">' +
                                '<form class="navbar-form navbar_search_form_base width_100_i margin_auto">' +
                                '<div class="input-group input-group-sm">' +
                                '<input class="form-control" placeholder="Search" id="search_mobile_input" type="text">' +
                                '<div class="input-group-btn">' +
                                '<i class="btn btn-default" id="search_mobile_btn"><i class="glyphicon glyphicon-search"></i>' +
                                '</i>' +
                                '</div>' +
                                '</div>' +
                                '</form>' +
                                '</div>' +
                                '</nav>')
                            appender.on('keypress', function (e) {
                                if (e.keyCode === 13) {
                                    var passed_value = $('#search_mobile_input').val()
                                    if (passed_value.trim() === '') {
                                        return false;
                                    }
                                    //need locate
                                    var path = '/search/all/?q=' + passed_value
                                    location.href = path
                                    return false;
                                }
                            })
                            appender.find('#search_mobile_btn').on('click', function (e) {
                                e.preventDefault()
                                var passed_value = $('#search_mobile_input').val()
                                if (passed_value.trim() === '') {
                                    return false;
                                }
                                var path = '/search/all/?q=' + passed_value
                                location.href = path
                            })
                            $('body').append(appender)
                        }
                    });
                }
            }
        }
    });


    $('#search_desktop_input').on('keypress', function (e) {
        if (e.keyCode === 13) {
            var passed_value = $('#search_desktop_input').val()
            if (passed_value.trim() === '') {
                return false;
            }
            var path = '/search/all/?q=' + passed_value
            location.href = path
            //need ajax
            return false;
        }
    })
    $('#search_desktop_btn').on('click', function (e) {
        e.preventDefault()
        var passed_value = $('#search_desktop_input').val()
        if (passed_value.trim() === '') {
            return false;
        }
        var path = '/search/all/?q=' + passed_value
        location.href = path
        //need ajax

    })
    // do something here
    //$("#a_search_modal").click(function () {
    //    $("#div_modal_search").modal();
    //
    //});
});