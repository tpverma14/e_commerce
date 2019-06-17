function save(isLiked, callback) {
  // Pretend this is an AJAX call.
  return Promise.delay(!isLiked, 2000);
}

$('.js-like-button').on('click', function(evt) {
  evt.preventDefault();
  var $btn = $(this);
  var liked = ($btn.text().match('Unlike') === null);
  $btn.html('<img class="like-btn__spinner" src="http://jxnblk.com/loading/loading-bars.svg" alt="loading"/> Saving');
  save(liked).then(function(isLiked) {
    if (liked) {
      $btn.html('☹&nbsp; Unlike');
    } else {
      $btn.html('♥︎&nbsp; Like');
    }
  });
});