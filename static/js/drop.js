Dropzone.autoDiscover = false; 

const myDropzone = new Dropzone("#MyDropZone", {
  
  clickable: true,
  maxFiles:1,
  maxFilesize:100000,
  acceptedFiles:'.xlsx',
  addRemoveLinks: true,



  
})

