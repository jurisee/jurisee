
const d = new Date();
let year = d.getFullYear();
$( ".year" ).html(year);

$( ".nyoptions" ).hide();
$("#off_name").hide();

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
    alert(test)
    name = $(this).html();
    html = "<label>Offender Name: </label><br>" +
        name +
        "<a href='' data-bs-toggle=\"modal\" data-bs-target=\"#searchModal\">Edit</a>"
    $("#badActorId").val(id);
    $("#off_name").show();
    $("#off_name").html('');
    $("#off_name").append(html);
    $("#searchActorBtn").hide()
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

$('#saveNext').click(function(){
    $(".accordion-collapse").addClass("collapse show");
});