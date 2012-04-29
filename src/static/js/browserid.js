$(function() {
  $('#browserid').click(function() {
    navigator.id.get(gotAssertion);
    return false;  
  });
});

function gotAssertion(assertion) {
  // got an assertion, now send it up to the server for verification
  if (assertion !== null) {
    $.ajax({
      type: 'POST',
      url: '/complete/browserid/',
      data: { assertion: assertion },
      success: function(res, status, xhr) {
        if (res === null) {}//loggedOut();
          else loggedIn(res);
        },
      error: function(res, status, xhr) {
        alert("login failure" + res);
      }
    });
  } else {
    //loggedOut();
  }
}
