function displayFieldsSettingsSave() {

    var form = $('#settings_display_column').serialize(true);
    if ( !form ) {
        return false;
    }

    $.ajax({
        type: "POST",
        url: "/admin_display_fields_settings/change_form/",
        data: {
            "operation": "save_form",
            'form': form,
            "csrfmiddlewaretoken": getCookie('csrftoken')
        },
        success: function (response) {

            switch (response.success) {
                case false: {
                    break;
                }
                case true: {
                    window.location = window.location.href;
                    break;
                }
                default:
                    return;
            }
        },
        dataType: "json"
    });

    return false;
}

function displayFieldsSettingsForm() {
    $.ajax({
        type: "POST",
        url: "/admin_display_fields_settings/change_form/",
        data: {
            "operation": "get_form",
            "csrfmiddlewaretoken": getCookie('csrftoken')
        },
        success: function (response) {

            switch (response.success) {
                case false: {
                    break;
                }
                case true: {
                    if ( $(response.selector) ) {
                        if (response.insert_type == 'before') {
                            $(response.selector).before(response.form);
                        } else if (response.insert_type == 'append') {
                            $(response.selector).append(response.form);
                        } else if (response.insert_type == 'prepend') {
                            $(response.selector).prepend(response.form);
                        } else if (response.insert_type == 'inner') {
                            $(response.selector).innerHTML(response.form);
                        } else {
                            change_form_insert_default(response.form);
                        }
                    }
                    else {
                        change_form_insert_default(response.form);
                    }
                    break;
                }
                default:
                    return;
            }
        },
        dataType: "json"
    });
}

function change_form_insert_default(form) {
    var list_actions = $('#content-main ul.object-tools');
    if ( list_actions ) {
        $(list_actions).append('<li>' + form + '</li>');
    } else {
        $('#changelist').before(form);
    }
}

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

$( document ).ready(function() {
   displayFieldsSettingsForm();
});