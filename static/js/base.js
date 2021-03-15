/**
 * While document loads, show loader
 * original code idea: 
 * https://stackoverflow.com/questions/3623890/jquery-onload-function
 */
$(document).ready(function () {
  $('.loader-overlay-wrapper').fadeOut(1200);
})
// loads tooltips 
$(function () {
  $('[data-toggle="tooltip"]').tooltip()
})