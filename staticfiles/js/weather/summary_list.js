// Summary delete 
$(document).ready(function () {
    /* Functions */
    var loadForm = function () {
        var btn = $(this);
        $.ajax({
            url: btn.attr("data-url"),
            type: 'get',
            dataType: 'json',
            beforeSend: function () {
                $("#modal-summary").modal("show");
            },
            success: function (data) {
                $("#modal-summary .modal-content").html(data.html_form);
            }
        });
    };

    var saveForm = function () {
        var form = $(this);
        $.ajax({
            url: form.attr("action"),
            data: form.serialize(),
            type: form.attr("method"),
            dataType: 'json',
            success: function (data) {
                if (data.form_is_valid) {
                    $("#summary-table tbody").html(data.html_summary_list);
                    $("#modal-summary").modal("hide");
                }
                else {
                    $("#modal-summary .modal-content").html(data.html_form);
                }
            }
        });
        return false;
    };
    /* Binding */

    // Delete summary
    $("#summary-table").on("click", ".js-delete-summary", loadForm);
    $("#modal-summary").on("submit", ".js-summary-delete-form", saveForm);
});
