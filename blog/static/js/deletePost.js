$(function() {
// Delete the post
$(".delete-post").on("click", function() {
    const id = $(this).attr("data-id");
    console. log(id);
    $.ajax({
        type: 'post',
        url: '/delete',
        data: {
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
            id: id
        },
        success: function(result) {
            if(result.deleted) {
                alert("Post Deleted");
                window.location = "/";
            }
            else{
                alert("Post failed to Delete");
            }
        }
    });
});
});