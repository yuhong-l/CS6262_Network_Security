function chan(arg) {
  if (arg.target.id == 'red') {
    chrome.tabs.executeScript(null, {
      code: 'var config="red";'
    }, function() {
        chrome.tabs.executeScript({
          file: 'content.js'
        });
    });
  } else if (arg.target.id == 'blue') {
    chrome.tabs.executeScript(null, {
      code: 'var config="blue";'
    }, function() {
        chrome.tabs.executeScript({
          file: 'content.js'
        });
    });
  } else if (arg.target.id == 'purple') {
    chrome.tabs.executeScript(null, {
      code: 'var config="purple";'
    }, function() {
        chrome.tabs.executeScript({
          file: 'content.js'
        });
    });
  } else if (arg.target.id == 'green') {
    chrome.tabs.executeScript(null, {
      code: 'var config="green";'
    }, function() {
        chrome.tabs.executeScript({
          file: 'content.js'
        });
    });
  }
}

document.addEventListener('DOMContentLoaded', function() {
  var butt = document.querySelectorAll('button');
  for (var j = 0; j < butt.length; j++) {
     butt[j].addEventListener('click', chan);
  }
});
