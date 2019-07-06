$(document).ready(function(){
    // Setting the preview.
    $(".adjust-content img").each(function(){
            $(this).addClass("img-fluid");
    });

    let contenttxt = $("#id_content");
    function setContent(value){
        let markedContent = marked(value);
        $("#preview-content").html(markedContent);
        $("#preview-content img").each(function(){
            $(this).addClass("img-fluid");
        });
    }

    contenttxt.keyup(function(){
        let newContent = $(this).val();
        setContent(newContent);
    });

    let titletxt = $("#id_title");
    function setTitle(value){
        $("#preview-title").text(value);
    }
    setTitle(titletxt.val())
    titletxt.keyup(function(){
        let newContent = $(this).val();
        setTitle(newContent);
    });

});
