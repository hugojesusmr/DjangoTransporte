const uploadForm = document.getElementById('upload_form')
const input_file = document.getElementById('id')
const alertBox = document.getElementById('alert-box')
const progressBox = document.getElementById('progress-box')
const cancelBox = document.getElementById('cancel-box')
const cancelBtn = document.getElementById('cancel-btn')

const csrf = document.getElementsByName('csrfmiddlewaretoken')

    input_file.addEventListener('change', ()=>{
    progressBox.classList.remove('not-visible')
    cancelBox.classList.remove('not-visible')

    const file_data = input_file.files[0]
    console.log(file_data)

    const fd = new FormData();
    fd.append('csrfmiddlewaretoken', csrf[0].value)
    fd.append('file', file_data)

    $.ajax({
        type: 'POST',
        url: '/',
        enctype: "multipart/form-data",
        data: fd,
        beforeSend: function(){
            console.log("Before")
            alertBox.innerHTML=""
        },
        xhr: function(){
            const xhr = new window.XMLHttpRequest();
            xhr.upload.addEventListener('progress', e =>{
                if(e.lengthComputable){
                    const percentProgress = (e.loaded/e.total)*100;
                    console.log(percentProgress)
                    progressBox.innerHTML= `<div class="progress">
                    <div class="progress-bar" role="progressbar" style="width: ${percentProgress}%" aria-valuenow="${percentProgress}" aria-valuemin="0" aria-valuemax="100"></div>
                    </div>
                    <p>${percentProgress.toFixed(1)}%</p>`
                }
            });
            cancelBtn.addEventListener('click', ()=>{
                xhr.abort();
                setTimeout(()=>{
                    uploadForm.reset()
                    progressBox.innerHTML=""
                    cancelBox.classList.add('not-visible')
                    alertBox.classList.add('no-visible')
                },2000)
                
            })
            return xhr
        },
        success: function(response){
            console.log("exito",response)
            alertBox.innerHTML = `<div class="alert alert-success" role="alert">
                El Archivo Se subio Exitosamente
            </div>`
            cancelBox.classList.add('not-visible')
        },
        error: function(err){
            console.log(err)
            alertBox.innerHTML=`<div class="alert alert-success" role="alert">
            Error al Cargar el Archivo
        </div>`
        },
        cache: false,
        contentType: false,
        processData: false,
    });




});


    