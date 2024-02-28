$('#example3').DataTable({
  paging: true,
  pageLength: 12,
  lengthChange: true,
  searching: true,
  select: false,
  info: false,         
  lengthChange:true,
  language: {
    paginate: {
      next: '<i class="fa fa-angle-double-right" aria-hidden="true"></i>',
      previous: '<i class="fa fa-angle-double-left" aria-hidden="true"></i>' 
    }
    }
});