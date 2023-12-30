document.getElementById("upload").addEventListener("submit", submitForm);

function submitForm(event){
    event.preventDefault();
    var split_name = window.location.href.split('/').slice(-1)

    var dark_corner = document.getElementById("dark_corner").checked
    var hair = document.getElementById("hair").checked
    var gel_border = document.getElementById("gel_border").checked
    var bubble = document.getElementById("bubble").checked
    var ruler = document.getElementById("ruler").checked
    var ink = document.getElementById("ink").checked
    var patches = document.getElementById("patches").checked

    var formData = new FormData();
    formData.append("dark_corner", dark_corner);
    formData.append("hair", hair);
    formData.append("gel_border", gel_border);
    formData.append("bubble", bubble);
    formData.append("ruler", ruler);
    formData.append("ink", ink);
    formData.append("patches", patches);


    formData.append("age", imgInfo.age);
    formData.append("dataset", imgInfo.dataset);
    formData.append("dx", imgInfo.dx);
    formData.append("dx_type", imgInfo.dx_type);
    formData.append("image_id", imgInfo.image_id);
    formData.append("lesion_id", imgInfo.lesion_id);
    formData.append("localization", imgInfo.localization);
    formData.append("sex", imgInfo.sex);

    $.ajax({
        type: "POST", 
        url: "/save_info/"+split_name, 
        cache: false,
        data: formData,
        contentType: false,
        processData: false, 
        beforeSend: null,
        success: function(data){
            console.log("submitted")
            window.location.reload(true);
        },
        error: function (request, status, error) {
            console.log("Error : ", error)
        },
    });
}
