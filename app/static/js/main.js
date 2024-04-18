
const d = new Date();
let year = d.getFullYear();
$( ".year" ).html(year);

//report offender form hide/show certain fields
//$( ".nyoptions" ).hide();
$("#off_name").hide();
$("#off_role").hide();

$('.searchVal').keyup(function() {
    val = $(".searchVal").val();
    url= "/api/searchactors/" + val;
    $.getJSON(url, function(result){
        searchResults(result);
    });
});


function searchResults(data) {
    data = data;
    let items ="";
   for (key in data) {
       items += "<li class='list-group-item list-group-item-action list-group-item-light' value=" + data[key].id + ">" + data[key].fName + " " + data[key].lName + "</li>";
   }
    $("#searchResults").html(items);
}

$('#searchResults').on('click','li',function() {
    id = this.value
    test = this.id
    name = $(this).html();
    html = "<p><label>Offender Name: </label><br>" +
        name +
        " <a href='' data-bs-toggle=\"modal\" data-bs-target=\"#searchModal\">Edit</a></p>"
    $("#badActorId").val(id);
    $("#off_name").show();
    $("#off_name").html('');
    $("#off_name").append(html);
    $("#searchActorBtn").hide()
    $("#off_role").show();
    $('#searchModal').modal('hide');
    $('#searchVal').val('');
    $("#searchResults").html('');
});


$("#states").change(function(){
    var selected = $('#states').find(":selected").val();
    if (selected == "NY") {
        $( ".nyoptions" ).toggle();
    }
})


$("#violations").children('li').addClass("list-group-item");

//$("li").addClass( "list-group-item" );

$('#saveNext').click(function(){
    $(".accordion-collapse").addClass("collapse show");
});