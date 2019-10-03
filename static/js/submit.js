var submit = function() {
    var url = "/data/";
    var comment = document.getElementById("input").value;
    var params = "comment="+comment;
    ajax(url, params, basicDump);
}
