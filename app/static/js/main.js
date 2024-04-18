
const d = new Date();
let year = d.getFullYear();
fid= 0;
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

$( ".searchABtn" ).on( "click", function() {
    fid = this.value
} );
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
    parent = "#" + fid;
    actor = fid;
    name = $(this).html();
    html = "<p><label>" + actor + " Name: </label><br>" +
        name +
        " <a href='' data-bs-toggle=\"modal\" data-bs-target=\"#searchModal\">Edit</a></p>"
    switch(actor) {
        case 'Judge':
            $('#judgeId').val(id);
            $("#judge_name").show();
            $("#judge_name").html('');
            $("#judge_name").append(html);
            break;
        case 'ba1':
                html = "<p><label>Offender Name: </label><br>" +
        name +
        " <a href='' data-bs-toggle=\"modal\" data-bs-target=\"#searchModal\">Edit</a></p>"
            $(parent + " #badActorId").val(id);
            $(parent + " #off_name").show();
            $(parent + " #off_name").html('');
            $(parent +" #off_name").append(html);
            $(parent +" #searchActorBtn").hide()
            $(parent +" #off_role").show();
            break;
        case 'AFC':
            $('#afcId').val(id);
            $("#afc_name").show();
            $("#afc_name").html('');
            $("#afc_name").append(html);
            break;
        case 'Evaluator':
            $('#evalId').val(id);
            $("#eval_name").show();
            $("#eval_name").html('');
            $("#eval_name").append(html);
            break;
        case 'Opposing Lawyer':
            $('#opLawyerId').val(id);
            $("#opLawyer_name").show();
            $("#opLawyer_name").html('');
            $("#opLawyer_name").append(html);
            break;
        case 'Effected Person Lawyer':
            $('#effectedLawyerId').val(id);
            $("#ePersonLawyer_name").show();
            $("#ePersonLawyer_name").html('');
            $("#ePersonLawyer_name").append(html);
            break;
        default:
    }
    $('#searchModal').modal('hide');
    $('.searchVal').val('');
    $("#searchResults").html('');
    fid= 0;
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